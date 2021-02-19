def CountDigit(n):
 icnt=0
 while(n>0):
  ret=n%10
  n=int(n/10)
  icnt=icnt+1
 return icnt



def main():
 print("\n\nEnter Number:")
 no=int(input())
 cnt=CountDigit(no)
 print("{} digits present in {} \n\n".format(cnt,no))
 
 
if __name__=="__main__":
 main()
