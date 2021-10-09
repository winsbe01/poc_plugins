import utils

def enter(argv):
	print("greetings from plug 2")
	print(f"received {len(argv)} arguments")
	print("calling a shared function, returning the result")
	num = utils.get_random_integer()
	return num

	
