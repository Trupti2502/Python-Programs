def main():
 print("\nBy Using While Loop\n")
 no=1
 while no<21:
  if no%2==0:
  	print(no,end=" ")
  no=no+1	
 
 print("\n\n\nBy Using For Loop\n")
 for no in range(2,21,2):
  print(no,end=" ")
 print("\n")



if __name__=="__main__":
 main()
 
