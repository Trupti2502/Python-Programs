def main():
 mult=1
 print("\n\nEnter Number:")
 no=int(input())
 for i in range(1,no+1):
  mult=mult*i
 print("Factorial of {} is: {}\n\n".format(no,mult))
 
if __name__=="__main__":
 main()
 
 """O/P-
 user@user-Lenovo-G50-80:~/Desktop/PYTHON/Assignment/Assignment2$ python3 Assignment2_3.py


Enter Number:
4
Factorial of 4 is: 24

"""
