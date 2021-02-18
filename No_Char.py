def main():

 print("Enter Name:")
 name=input()
 
 test_str=name
 icnt=0
 
 for i in test_str:
  icnt=icnt+1
  
 print("No of characters present in {} are {}".format(name,icnt)) 
  
    
if __name__=="__main__":
 main()
