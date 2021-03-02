def Check(List,N):
 icnt=0
 for i in range(0,len(List)):
  if List[i]==N:
   icnt=icnt+1
 return icnt




def main():
 
 arr=[]
 print("\nEnter Number of Elements:");
 size=int(input());
 print("\n\n")
 for i in range(size):
  print("Enter element number",i+1)
  no=int(input())
  arr.append(no)
 
 print("Element To Search:")
 no=int(input())
 
 freq=Check(arr,no)
  
 print("\n\n{} occurs {} times".format(no,freq))


if __name__=="__main__":
 main()
 
 
 """output:-
 user@user-Lenovo-G50-80:~/Desktop/PYTHON/Assignment/Assignment 3$ python3 Assignment3_4.py

Enter Number of Elements:
11



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
5
Enter element number 8
34
Enter element number 9
2
Enter element number 10
5
Enter element number 11
65
Element To Search:
5


5 occurs 3 times

"""
 

