def Display(List):
 sum=0
 icnt=0
 for icnt in range(len(List)):
	 sum=sum+(List[icnt])
 return sum

def main():
 Arr=[10,20,30,40,50]
 ans=Display(Arr)
 print("sum of {} is={}".format(Arr,ans))

if __name__=="__main__":
  main()