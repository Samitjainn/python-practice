#wap to count the digit upto n ..........

n=int (input("enter a number "))
count=0
while(n>0):
    n=n//10
    count+=1
print("total digits",count) 
