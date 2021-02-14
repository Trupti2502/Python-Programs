import sys

def Addition(no1,no2):
 return no1+no2

def main():
 if len(sys.argv)<3 or len(sys.argv)>3:
  print("INSUFFICIENT ARGUMENTS")
  return

 ret=Addition(int(sys.argv[1]),int(sys.argv[2]))
 print("Addition of{} and {} is:{}".format(sys.argv[1],sys.argv[2],ret))

if __name__=="__main__":
 main() 	