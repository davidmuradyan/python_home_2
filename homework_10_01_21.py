# #Exercise 1
# class Person():

# 	def __init__(self, first_name, last_name, gender, nationality):
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.gender = gender
# 		self.nationality = nationality


# 	def presenting(self):
# 		print(F"The whole information is\nfirst name: {self.first_name}\nlast name: {self.last_name}\ngender: {self.gender}\nnationality: {self.nationality}")


# 	def drive(self):
# 		print(F"{self.first_name} drives a car!")


# 	def sing(self):
# 		print(F"{self.first_name} also sings very well!")


# 	def work(self, workplace):
# 		self.workplace = workplace
# 		print(F"{self.first_name} works at {self.workplace}!")


# gago = Person("Gago", "Gagikyan", "male", "armenian")
# gago.presenting()
# gago.drive()
# gago.sing()
# gago.work("Factory")
# print("\n")

# class Student(Person):

# 	def __init__(self, first_name, last_name, gender, nationality):
# 		super().__init__(first_name, last_name, gender, nationality)


# 	def work(self):
# 		print(F"{self.first_name} does not work anywhere!")


# 	def study(self, university):
# 		self.university = university
# 		print(F"{self.first_name} studies in {self.university}!")

# vagho = Student("Vagho", "Vaghikyan", "male", "armenian")
# vagho.presenting()
# vagho.drive()
# vagho.sing()
# vagho.study("YSU")
# vagho.work()


# #Exercise 2
# class Country():

# 	def __init__(self, country_name, continent):
# 		self.country_name = country_name
# 		self.continent = continent

# 	def countryPresentation(self):
# 		return F"The country name is {self.country_name} and it is in {self.continent} continent!"




# class Brand():

# 	def __init__(self, brand_name, start_date):
# 		self.brand_name = brand_name
# 		self.start_date = start_date

# 	def brandPresentation(self):
# 		return F"The brand's name is {self.brand_name}, and its start date is {self.start_date}!"




# class Season():

# 	def __init__(self, season_name, average_temperature):
# 		self.season_name = season_name
# 		self.average_temperature = average_temperature

# 	def seasonPresentation(self):
# 		return F"The season name is {self.season_name}, and its average temperature is {self.average_temperature} celsius!"




# class Product(Country, Brand, Season):

# 	def __init__(self, product_name, product_type, product_price, product_quantity, country_name, continent):
# 		self.product_name = product_name
# 		self.product_type = product_type
# 		self.product_price = product_price
# 		self.product_quantity = product_quantity
# 		self.percent = 0
# 		# self.country_name = Country.country_name
# 		# self.continent = Country.continent
# 		# Country().__init__(self, country_name, continent)
		
# 	def productPresentation(self):
# 		return F"Product name: {self.product_name}\nProduct type: {self.product_type}\nProduct price: {self.product_price}\nProduct quantity: {self.product_quantity}"

# 	def discount(self, percent):
# 		self.percent = percent
# 		self.product_price -= self.product_price * self.percent / 100
# 		return F"The product price has been discounted by {self.percent} percents!"

# 	def increaseQuantity(self, add_quantity):
# 		# increases the quantity with given quantity "add_quantity"
# 		self.add_quantity = add_quantity
# 		self.product_quantity += self.add_quantity
# 		return F"The product quantity was added up to {self.product_quantity}!"



# banana = Product("Banana", "Fruit", 100, 50)

# print(banana.discount(10))
# print(banana.increaseQuantity(2))




# spain = Country("Spain", "Europe")
# print(spain.countryPresentation())

# dole = Brand("Dole", "01.03.2021")
# print(dole.brandPresentation())

# spring = Season("Spring", 10)
# print(spring.seasonPresentation())