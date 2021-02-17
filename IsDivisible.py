def IsDivisible(x):
 if x%5==0:
  return True
 else:
  return False


def main():
 print("Enter Number")
 no=int(input())
 ret=IsDivisible(no)
 if ret==True:
  print("True")
 else:
  print("False")
 #print("{} is divisible by 5".format(no))
 #print("{} is not divisible by 5".format(no))

if __name__=="__main__":
 main()
