#Write a Python function to find the maximum of three numbers.



def max(num1,num2,num3):
 if(num1==num2==num3):
    print("All values are equal")
 elif(num1>num2 & num1>num3):
    return num1
 elif(num2>num1 & num2>num3):
    return num2
 else:
    return num3

Max=max(10,20,30)  
print(f"Max={Max}")          

