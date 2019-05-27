'''
Factory Method: creation through inheritance. Prototype: creation through delegation.
'''
from timeit import default_timer as timer
import copy 

class Prototype(object):
	pass

def main():
	start = timer()
	proto = Prototype()
	for i in range(0,1000):
		proto2 = copy.deepcopy(proto)
	end = timer()
	proto_result = end-start
	print("Using prototypes: {}".format(proto_result))

	start = timer()	
	for i in range(0,1000):
		proto3 = Prototype()
	end = timer()
	vanilla_result = end-start
	print("Using vanilla new operator: {}".format(vanilla_result))

if __name__ == "__main__":
	main()
