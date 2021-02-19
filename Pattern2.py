def main():
 print("Enter Number:")
 no=int(input())
 
 for i in range(no,0,-1):
  print("\n")
  for j in range(0,i,1):
   print("*",end=" ")
 

if __name__=="__main__":
 main()
