def IsPrime(value):
 cnt=0
 for i in range(2,value):
  if value%i==0:
   cnt=cnt+1
   return cnt>0


def main():
 print("\nEnter Number:")
 no=int(input())
 
 ret=IsPrime(no)
 
 if ret==True:
  print("{} is not prime number\n\n".format(no))
  
 else:
  print("{} is prime number\n\n".format(no))

if __name__=="__main__":
 main()
 
