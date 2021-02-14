#types of function definations

#accepts nothing return nothing
def fun():
 print("inside fun")	

 #accepts parameter and return nothing
def gun(value):
 print("inside gun",value) 

 #accepts parameter and return the value
def sun(value):
 value=value+1
 print("inside sun")	
 return value


def main():
  fun()
  gun(11)
  ret=sun(10)
  print(ret)
 

if __name__=="__main__":
  main() 
