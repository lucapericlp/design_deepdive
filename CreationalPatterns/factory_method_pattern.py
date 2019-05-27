'''
Factory Method requires subclassing, but doesn't require Initialize. Advantage of Factory Method is that it can return the same instance multiple times, or can return a subclass rather than an object of that exact type. New constructor is considered harmful. 
'''

import abc

class Creator(metaclass=abc.ABCMeta):
	def __init__(self,qty):
		self.products = []
		for i in range(0,qty):	
			print("Creating product...")
			self.products.append(self._factory_method())

	@abc.abstractmethod
	def _factory_method(self):
		pass

	def operation(self):
		for product in self.products:
			print("Following interface call made directly from Creator")
			product.interface()

class FirstConcreteCreator(Creator):
	def _factory_method(self):
		return FirstConcreteProduct()

class SecondConcreteCreator(Creator):
	def _factory_method(self):
		return SecondConcreteProduct()
	
class Product(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def interface(self):
		pass

class FirstConcreteProduct(Product):
	def interface(self):
		print("Interface of FirstConcreteProduct")

class SecondConcreteProduct(Product):
	def interface(self):
		print("Interface of SecondConcreteProduct")

def main():
	conc_creator = FirstConcreteCreator(5)
	for product in conc_creator.products:
		product.interface()
	conc_creator.operation()

if __name__ == "__main__":
	main()

