
def main():
 sum=0;
 print("\nEnter Number:")
 no=int(input())
 for i in range(1,no):
  if no%i==0:
   sum=sum+i
 print("\nsum of factors of {} is: {}\n\n".format(no,sum))
 
if __name__=="__main__":
 main()
 
