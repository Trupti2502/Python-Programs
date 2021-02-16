import Arithmatic #importing module Arithmatic
import Arithmatic as A #renaming to module Arithmatic and in further code we can write A insted of writing Arithmatic
from  Arithmatic import Multiplication #we can import only one function from mudule
from Arithmatic import* #we can import all functions from modul Arithmatic

def main():
 print("**ADDITION,SUSTRACTION,MULTIPLICATION,DIVISION OF 2 NUMBERS BY USING USER DEFINED MODULE**")
 print("Enter First Number")
 no1=int(input())
 print("Enter Second Number")
 no2=int(input())
 
 ret1=Arithmatic.Addition(no1,no2)
 print("Addition of {} and {} is:{}".format(no1,no2,ret1))

 ret2=A.Substraction(no1,no2)
 print("Substraction of {} and {} is:{}".format(no1,no2,ret2))

 ret3=Multiplication(no1,no2)
 print("Multiplication of {} and {} is:{}".format(no1,no2,ret3))

 ret4=A.Division(no1,no2)
 print("Division of {} and {} is:{}".format(no1,no2,ret4))

if __name__=="__main__":
 main()
