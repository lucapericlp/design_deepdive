'''
Factory Method: creation through inheritance. Prototype: creation through delegation.
'''
import copy 

class Prototype(object):
	pass

def main():
	proto = Prototype()
	proto2 = copy.deepcopy(proto)

if __name__ == "__main__":
	main()
