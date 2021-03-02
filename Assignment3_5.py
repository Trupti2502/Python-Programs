def ChkPrime(n):
    s=0
    f=[]
    for i in range (0,len(n)):
        num=n[i]
        if num>1:
            f=[]
            for j in range (1,num+1):
                if num%j==0:
                    f=f+[j]
                if f==[1,num]:
                    s=s+num
    return(s) 

    


def ListPrime():

 arr=[]
 print("\nEnter Number of Elements");
 size=int(input());
 print("\n\n")
 for i in range(size):
  print("Enter element number",i+1)
  no=int(input())
  arr.append(no)


 sum=ChkPrime(arr)

 print("\n\nSum of prime numbers is",sum)


if __name__=="__main__":
 ListPrime()


"""
OUTPUT:-
user@user-Lenovo-G50-80:~/Desktop/PYTHON/Assignment/Assignment 3$ python3 Assignment3_5.py

Enter Number of Elements
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
10
Enter element number 8
34
Enter element number 9
2
Enter element number 10
5
Enter element number 11
8


Sum of prime numbers is 32


"""
