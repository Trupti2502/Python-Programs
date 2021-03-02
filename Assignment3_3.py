def Min(List):
 min=List[0]
 for i in range(1,len(List)):
  if List[i]<min:
   min=List[i]
 return min




def main():
 
 arr=[]
 print("\nEnter Number Of Elements");
 size=int(input());
 print("\n\n")
 for i in range(size):
  print("Enter element number",i+1)
  no=int(input())
  arr.append(no)
 
 min=Min(arr)
  
 print("\n\nMinimum number is",min)


if __name__=="__main__":
 main()
 
 
 """OUTPUT:-
 user@user-Lenovo-G50-80:~/Desktop/PYTHON/Assignment/Assignment 3$ python3 Assignment3_3.py

Enter Number Of Elements
4



Enter element number 1
13
Enter element number 2
5
Enter element number 3
45
Enter element number 4
7


Minimum number is 5

"""
 
