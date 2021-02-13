#defination of addition function
def Addition(no1,no2):
	ans=no1+no2
	return ans

#defination of addition function
def Substraction(no1,no2):
	ans=no1-no2
	return ans

#entry point function
def main():
 print("Enter first number:")
 value1=int(input())

 print("Enter first number:")
 value2=int(input())

 ret1=Addition(value1,value2)
 ret2=Substraction(value1,value2)

 print("Addition is:",ret1)
 print("Substraction is:",ret2)

#code stater
if __name__=="__main__":
 main()

