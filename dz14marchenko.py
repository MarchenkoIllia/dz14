# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. 
# Реализуйте  методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса
class Cars:
    def __init__(self, model, year, make, V, color, price):
        self.model = model
        self.year = year
        self.make = make
        self.V = V
        self.color = color
        self.price = price

    def auto(self):
        print(f"Model: {self.model}\nYear of manufacturing: {self.year}\nMake: {self.make}\nEngine volume: {self.V}\nColor: {self.color}\nPrice: {self.price}")

carbmw = Cars("M5","2018","BMW","4.4l","Deep Blue","102.000_USD")
# carbmw.auto()

# Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год выпуска, издателя, жанр, автора, цену. 
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса

class Books:
    def __init__(self,name,year,publisher,genre,author,price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price
    
    def book(self):
        print(f"Name: {self.name}\nYear: {self.year}\nPublisher: {self.publisher}\nGenre: {self.genre}\nAuthor: {self.author}\nPrice: {self.price}")

book1 = Books("Internationalism or Russification?", "1965", "Modernity(Сучасність)", "Anti-Soviet report", "Ivan Dziuba", "2_USD")
# book1.book()

# Реализуйте класс «Стадион». Необходимо хранить в полях класса: название стадиона, дату открытия, страну, город, вместимость. 
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса

class Stadiums:
    def __init__(self,name,year,country,city,capacity):
        self.name = name
        self.year = year
        self.country = country
        self.city = city
        self.capacity = capacity
    
    def stadium(self):
        print(f"Name: {self.name}\nYear: {self.year}\nCountry: {self.country}\nCity: {self.city}\nCapacity: {self.capacity}")

stadium1 = Stadiums("Donbas-Arena", "2009", "Ukraine", "Donetsk", "51 504")
stadium1.stadium()