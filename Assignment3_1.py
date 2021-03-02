def Sum(List):
 sum=0
 for i in range(0,len(List)):
  sum=sum+List[i]
 return sum




def main():
 
 arr=[]
 print("\nNumber Of Elements\n\n");
 size=int(input());
 
 for i in range(size):
  print("Enter element number",i+1)
  no=int(input())
  arr.append(no)
 
 sum=Sum(arr)
  
 print("\n\nAddition of {} numbers is {}\n".format(size,sum))


if __name__=="__main__":
 main()



"""OPTPUT:-
user@user-Lenovo-G50-80:~/Desktop/PYTHON/Assignment/Assignment 3$ python3 Assignment3_1.py

Number Of Elements


6
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


Addition of 6 numbers is 130


""" 
 

