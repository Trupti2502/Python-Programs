
#accept n numbers from user and return the addition of n numbers
def addition2(List):
 print("INSIDE WHILE LOOP")
 sum=0
 i=0
 while i<len(List):
  sum=sum+(List[i])
  i=i+1
 return sum


def addition(List):
 print("INSIDE FOR LOOP")
 sum=0
 icnt=0
 for icnt in range(len(List)):
  sum=sum+(List[icnt])
 return sum

def xyz():
 arr=[]
 print("enter how many array elements you want")
 no=int(input())

 print("enter the elements")
 for i in range(no):
  print("enter element no:",i+1)
  value=int(input())
  arr.append(value)
 print("accepted data is:",arr)
 ret1=addition(arr)
 print("sum of {} is={}".format(arr,ret1))
 
 ret2=addition2(arr)
 print("sum of {} is={}".format(arr,ret2))

if __name__=="__main__":
  xyz()