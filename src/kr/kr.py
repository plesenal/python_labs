class Book:
    def __init__(self, title: str, author: str, pages: int):
        self._title = title
        self._author = author
        self._pages = pages


    def get_info(self):
        return f"\"{self._title}\" — {self._author}, {self._pages} стр."


    def __str__(self):
        return self.get_info()


class Ebook(Book):
    def __init__(self, title, author, pages, format_type):
        super().__init__(title, author, pages)  # ошибка
        self._format = format_type


    def get_info(self):  
        return super().get_info() + f" [{self._format}]"  # ошибка
        

    def get_download_link(self):
        na =  self._title.lower().replace(' ','-')
        return f"https://books.com/{na}"
a = Ebook ('Война и мир','bddbeq',5,True)
print(a.get_download_link())
