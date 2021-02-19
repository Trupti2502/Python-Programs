def DigitSum(n):
 sum=0
 while(n>0):
  rem=n%10
  sum=sum+rem
  n=int(n/10)
 return sum



def main():
 print("\nEnter Number:")
 no=int(input())
 
 sum=DigitSum(no)
 print("Sum of Digits in {} is {}\n".format(no,sum))


if __name__=="__main__":
 main()
