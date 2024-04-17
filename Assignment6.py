#Write a Python function to calculate the factorial of a number (a non-negative integer). 
#The function accepts the number as an argument.



num=int(input("Enter the number: "))

if(num<0):
    print("Enter valid positive number")
    

def fact(num):
        i=1
        fact=1
        while(i<=num):
             fact=fact*i
             i=i+1
        return fact

Fact = fact(num)
print(f"Fact = {Fact}") 
            



