
def IsEven(value):
	if value%2==0:
		return True
	

def main():
	no=int(input(("Enter number to check even or odd")))
	ret=IsEven(no)
	if ret==True:
		print("Given number is EVEN")
	else:
		print("Given number is ODD")

if __name__=="__main__":
	main()