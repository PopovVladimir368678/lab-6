class Book: # класс - описание книги

    def __init__(self, number_of_pages, reading_time_per_page, number_of_pictures): # заполняю метод инит, хорактеристики книги.
        self.number_of_pages = number_of_pages
        self.reading_time_per_page = reading_time_per_page
        self.number_of_pictures = number_of_pictures

    def reading_time(self):
        return self.number_of_pages * self.reading_time_per_page  # метод считающий время чтения.

    def __add__(self, other):
        number_of_pages = self.number_of_pages + other.number_of_pages
        reading_time_per_page = (self.reading_time_per_page * self.number_of_pages +
                                 other.reading_time_per_page * other.number_of_pages)/(self.number_of_pages +
                                                                                       other.number_of_pages)
        number_of_pictures = self.number_of_pictures + other.number_of_pictures
        return f'Сумма страниц - {number_of_pages}\n' \
               f'Средняя скорость чтения страници в обеих книгах - {round(reading_time_per_page, 2)}\n' \
               f'Сумма картинок - {number_of_pictures}'

     # обобщает две книги, например первую часть и её продолжение

class Encyclopedia(Book): # энциклопедия

    def __init__(self, number_of_pages, reading_time_per_page, number_of_pictures, article_length):
        super().__init__(number_of_pages, reading_time_per_page, number_of_pictures)
        self.article_length = article_length

    def number_of_articles(self):
        return int(self.number_of_pages) // int(self.article_length)


class Phonebook(Book):  #телефонный справочник

    def __init__(self, number_of_pages, reading_time_per_page, number_of_pictures, number_of_rooms):
        super().__init__(number_of_pages, reading_time_per_page, number_of_pictures)
        self.number_of_rooms = number_of_rooms

    def numbers_per_page(self):
        return int(self.number_of_rooms) // int(self.number_of_pages)

a = Book(123, 3, 45)
print(a.reading_time())
q = Book(1223, 2, 95)
print(a.reading_time())

z = q + a
print(z)

s = Phonebook(234, 3, 34, 12311.4)
print(s.numbers_per_page())
e = Encyclopedia(234, 3, 3, 12)
print(e.number_of_articles())

