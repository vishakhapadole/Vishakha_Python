km=5
print(f"{km} kilometers is equal to {5*0.621371} miles.")


c=int(input("Enter the temperature in celcius "))
print("Temperature in Fahrenheueit is ",(c*9/5)+32)


n=5
if n>0:
    print(f"{n} is a positive number.")
elif n<0:
    print(f"{n} is a negative number.")
else:
    print(f"{n} is a zero.")


if n%2==0:
    print(f"{n} is even number.")
else:
    print(f"{n} is odd number.")


y=2020
if (y%4==0 and y%100!=0)or(y%400==0):
    print(f"{y} is a leap year")
else:
    print(f"{y} is not a leap year")


a=10
b=18
c=12
if (a>=b and a>=c):
    print(f"{a} is a largest.")
elif (b>=a and b>=c):
    print(f"{b} is a largest.")
else:
    print(f"{c} is a largest.")


n=29
if n>1:
  for i in range(2,n):
    if(n%i==0):
       print(f"{n} is not a prime number.")
       break
    else:
        print(f"{n} is a prime number.")
        break
else:
    print(f"{n} is not a prime number.")


#Simple interest
p=int(input("Enter the principal "))
r=int(input("Enter the rate "))
t=int(input("Enter the time "))
print("Simple interest is ",(p*r*t)/100)

# Swap without using third variable
a=10
b=20
print("Before swapping\na=",a,"\tb=",b)
a=a+b
b=a-b
a=a-b
print("After swapping\na=",a,"\tb=",b)


s="Happy to see you"
print(s)
print(type(s))
print(s.upper())
print(s.lower())
print(dir(s))
print(s.capitalize())
print(s.title())
print(s.find("to"))
print(s.count("e"))
print(s.index("p"))
print(s.swapcase())

