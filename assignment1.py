2#mirror dimension
sake= input("enter the input ")
print(sake[::-1])
3#odd n even numbers seies
sake =input("enter the series").split(',')
count=0
count1=0
for i in sake:
   if int(i)%2==0:
      count+=1
   else :
      count1+=1
print(count," count of even number")
print(count1,"count of odd number")
1# The Fibonacci Sequence
fib=0
n1=0
n2=1
for i in range(0,50):
    fib=n1+n2
    n1=n2
    n2=fib
    print(n1)
