from datetime import date
from abc import ABC, abstractmethod
from typing import Callable, List, Dict, Any, Optional

class Workout:
    def __init__(self, athlete_name: str, exercise_type: str, duration_min: int, calories_burned: float, workout_date: date):
        if not isinstance(athlete_name, str) or not athlete_name.strip():
            raise ValueError("имя")
        self.__athlete_name = athlete_name.strip()

        if not isinstance(exercise_type, str) or not exercise_type.strip():
            raise ValueError("тип упражнения")
        self.__exercise_type = exercise_type.strip()

        if isinstance(duration_min, bool) or not isinstance(duration_min, int) or not (1 <= duration_min <= 600):
            raise ValueError("длительность")
        self.__duration_min = duration_min

        if isinstance(calories_burned, bool) or not isinstance(calories_burned, (int, float)) or calories_burned <= 0:
            raise ValueError("калории")
        self.__calories_burned = calories_burned

        if not isinstance(workout_date, date):
            raise ValueError("дата должна быть объектом datetime.date")
        if workout_date > date.today():
            raise ValueError("будущее")
        self.__date = workout_date

    @property
    def athlete_name(self): 
        return self.__athlete_name

    @property
    def exercise_type(self) : 
        return self.__exercise_type

    @property
    def duration_min(self): 
        return self.__duration_min

    @property
    def calories_burned(self) : 
        return self.__calories_burned

    @property
    def date(self): 
        return self.__date

    def intensity(self) -> float:
        return self.__calories_burned / self.__duration_min

    def is_intense(self) -> bool:
        return self.intensity() > 10


    def __str__(self) -> str:
        cal_str = f"{self.__calories_burned}"
        return f"{self.__athlete_name} — {self.__exercise_type}, {self.__duration_min} мин, {cal_str} ккал ({self.__date})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Workout):
            return NotImplemented
        return (self.__athlete_name == other.__athlete_name and self.__exercise_type == other.__exercise_type and self.__date == other.__date)

    def __lt__(self, other) -> bool:
        if not isinstance(other, Workout):
            return NotImplemented
        return self.__date < other.__date


class WorkoutJournal:
    def __init__(self, workouts: Optional[List[Workout]] = None):
        self.__workouts: List[Workout] = list(workouts) if workouts else []
        self.__strategy: Optional[AnalyticsStrategy] = None

    def add(self, workout: Workout) -> None:
        if not isinstance(workout, Workout):
            raise TypeError("Ожидается объект Workout")
        self.__workouts.append(workout)

    def __iter__(self):
        return iter(self.__workouts)

    def __len__(self) -> int:
        return len(self.__workouts)

    def filter_by(self, predicate: Callable[[Workout], bool]) -> 'WorkoutJournal':
        return WorkoutJournal(list(filter(predicate, self.__workouts)))

    def map_to(self, transform_func: Callable[[Workout], Any]) -> list:
        return list(map(transform_func, self.__workouts))

    def apply(self, func: Callable[[Workout], None]) -> 'WorkoutJournal':
        for w in self.__workouts:
            func(w)
        return WorkoutJournal(self.__workouts.copy())

    def set_analytics(self, strategy: AnalyticsStrategy) -> None:
        if not isinstance(strategy, AnalyticsStrategy):
            raise TypeError("Ожидается экземпляр AnalyticsStrategy")
        self.__strategy = strategy

    def get_report(self) -> dict:
        if self.__strategy is None:
            raise ValueError("Стратегия анализа не установлена. Вызовите set_analytics().")
        return self.__strategy.analyze(self.__workouts)

class AnalyticsStrategy(ABC):
    @abstractmethod
    def analyze(self, workouts: List[Workout]) -> dict:
        pass

class TotalStats(AnalyticsStrategy):
    def analyze(self, workouts: List[Workout]) -> dict:
        return {
            "total_workouts": len(workouts),
            "total_minutes": sum(w.duration_min for w in workouts),
            "total_calories": sum(w.calories_burned for w in workouts)
        }

class AverageStats(AnalyticsStrategy):
    def analyze(self, workouts: List[Workout]) -> dict:
        n = len(workouts)
        if n == 0:
            return {"avg_duration": 0.0, "avg_calories": 0.0, "avg_intensity": 0.0}
        return {
            "avg_duration": sum(w.duration_min for w in workouts) / n,
            "avg_calories": sum(w.calories_burned for w in workouts) / n,
            "avg_intensity": sum(w.intensity() for w in workouts) / n
        }

class ByExerciseStats(AnalyticsStrategy):
    def analyze(self, workouts: List[Workout]) -> dict:
        stats: Dict[str, Dict[str, int]] = {}
        for w in workouts:
            ex = w.exercise_type
            if ex not in stats:
                stats[ex] = {"count": 0, "total_calories": 0}
            stats[ex]["count"] += 1
            stats[ex]["total_calories"] += w.calories_burned
        return stats

def make_intensity_filter(min_intensity: float) -> Callable[[Workout], bool]:
    return lambda w: w.intensity() >= min_intensity

def make_date_range_filter(start_date: date, end_date: date) -> Callable[[Workout], bool]:
    return lambda w: start_date <= w.date <= end_date

def make_exercise_filter(exercise_type: str) -> Callable[[Workout], bool]:
    return lambda w: w.exercise_type == exercise_type

if __name__ == "__main__":
    j = WorkoutJournal()
    j.add(Workout('Иванов', 'бег', 30, 350, date(2025, 5, 15)))
    j.add(Workout('Иванов', 'присед.', 20, 150, date(2025, 5, 16)))
    j.add(Workout('Иванов', 'бег', 45, 500, date(2025, 5, 20)))

    # 1. TotalStats
    j.set_analytics(TotalStats())
    print(j.get_report())
    # {'total_workouts': 3, 'total_minutes': 95, 'total_calories': 1000}

    # 2. AverageStats
    j.set_analytics(AverageStats())
    print(j.get_report())
    # {'avg_duration': 31.666..., 'avg_calories': 333.333..., 'avg_intensity': 10.333...}

    # 3. ByExerciseStats
    j.set_analytics(ByExerciseStats())
    print(j.get_report())
    # {'бег': {'count': 2, 'total_calories': 850}, 'присед.': {'count': 1, 'total_calories': 150}}

    # 4. Фильтрация + map
    intense = j.filter_by(make_intensity_filter(10))
    print(len(intense))  # 2

    may_run = j.filter_by(make_exercise_filter('бег'))
    names = may_run.map_to(lambda w: w.athlete_name)
    print(names)         # ['Иванов', 'Иванов']