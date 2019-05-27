'''
Understanding the nature of metaclasses within Python3 is key. __call__ is the first method to be invoked upon class instantiation which does not trigger a Singleton init call unless object hasn't been created yet
'''
class Singleton(type):
	def __init__(cls,name, bases, attrs, **kwargs):
		super().__init__(name,bases,attrs)
		cls._instance = None
		print("Inited")

	def __call__(cls, *args, **kwargs):
		print("Called")
		if cls._instance is None:
			cls._instance = super().__call__(*args, **kwargs)
		return cls._instance

class ArbitraryClass(metaclass=Singleton):
	pass

def main():
	ex1 = ArbitraryClass()
	#ex2 = "Something" 
	ex2 = ArbitraryClass()
	print("{} vs {}".format(hex(id(ex1)),hex(id(ex2))))
	assert ex1 is ex2
	return True	

if __name__ == "__main__":
	main() 
