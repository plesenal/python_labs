from collections import deque

class Stack:
    def __init__(self,data :list):
        if data:
            self._data = list(data)
        else:
            self._data = []

    def __len__(self) -> int:
        try :
            return len(self._data)
        except TypeError:
            return 0
    def push(self, item):
        # корректно: добавление в конец списка O(1) амортизированно
        self._data.append(item)


    def pop(self):

        try:
            return self._data.pop()
        except IndexError:
            return print("Стек пуст")

    def peek(self):

        try :
            return self._data[-1]
        except IndexError:
            return None

    def is_empty(self) -> bool:
        # TODO: улучшить реализацию
        if  self._data:
            return False
        else:
            return True



class Queue:
    def __init__(self, data:deque):

        if data:
            self._data = deque(data)
        else:
            self._data = deque()
    def __len__(self) -> int:
        return len(self._data)

    def enqueue(self, item):

        self._data.append(item)

    def dequeue(self):

        try:
            return self._data.popleft()
        except IndexError:
            print("Пусто")


    def peek(self):

        try:
            return self._data[0]
        except IndexError:
            print("Пусто")

    def is_empty(self) -> bool:
        if self._data:
            return False
        else:
            return True

def main ():

    # s = Stack([])
    # s.push(4)
    # print(s.peek())
    # print(s.is_empty())
    # print(s.pop())
    # print(s.is_empty())
    #s = Stack([1,2,3,4,5])
    #print(s.is_empty())
    #print(s.peek())

    #queue = deque([1, 2, 3, 4, 5])

    q = Queue([])
    print(q.is_empty())
    #q.enqueue(5)
    #q.enqueue(6)
    q.dequeue()
    print(q.is_empty())
    print(q.peek())

if __name__ == '__main__':
    main()