def Max(List):
 max=List[0]
 for i in range(1,len(List)):
  if List[i]>max:
   max=List[i]
 return max




def main():
 
 arr=[]
 print("\nEnter Number Of Elements\n\n");
 size=int(input());
 
 for i in range(size):
  print("Enter element number",i+1)
  no=int(input())
  arr.append(no)
 
 max=Max(arr)
  
 print("\n\nMaximum number is",max)


if __name__=="__main__":
 main()
 
 
"""OUTPUT:-

user@user-Lenovo-G50-80:~/Desktop/PYTHON/Assignment/Assignment 3$ python3 Assignment3_2.py

Enter Number Of Elements


7
Enter element number 1
13
Enter element number 2
5
Enter element number 3
45
Enter element number 4
7
Enter element number 5
4
Enter element number 6
56
Enter element number 7
34


Maximum number is 56

"""
