#positional argument
def Student(name,rno,address,marks):
 print("name is:",name)	
 print("roll no is:",rno)
 print("address is:",address)
 print("marks is:",marks)



#keyword argument
def Computer(RAM,Processor,HDD):
 print("RAM size is is:",RAM)	
 print("processor is:",Processor)
 print("size of hard disk is:",HDD)



#defualt value(should be from right to left order)
def CircleArea(r,pi=3.14):
 print("value of pi is:",pi)
 return pi*r*r



#variable no of arguments
def fun(*value):
 print(type(value))	
 print("numnber of arguments are:",len(value))
 


def main():
 
 Student("Trupti",6,"pune",73) #POSITONAL PARAMETRES

 Computer(Processor="i5",RAM=8,HDD="1TB") #KEYWORD ARGUMENT
 Computer(RAM=16,Processor="i7",HDD="5GB")
 
 CircleArea(10.5)  #DEFULT ARGUMENT
 CircleArea(10.5,23)
 CircleArea(r=10.5,pi=23)#POSITIONAL WITH DEFAULT
 CircleArea(pi=23,r=10.5)#KEYWORD WITH DEFAULT

 fun()  #VARIABLE NUMBER OF ARGUMENTS
 fun(11,12,32)
 fun(12,43,32,66,75,88)


if __name__=="__main__":
 main() 	