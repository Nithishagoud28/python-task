# # i.	Write a program to check if a given number is positive,  negative, or zero. 
# num=int(input("enter a number"))
# if num > 0:
#     print("positive number")
# elif num==0:
#     print("equal")
# else:
#     print("negative number")

# # ii.	Determine if a number is odd or even.
# num1=int(input("enter a number"))
# if num1 % 2==0:
#     print("num1 is even number")
# else:
#     print("num1 is a odd number")

# #   iii. 	 Check if a person is eligible to vote (age >= 18).
# num=int(input("enter a number"))
# if num >=18:
#     print("num is eligible for the vote")
# else:
#     print("num is not eligible for the vote")

# #  iv. 	 Write a program to find the greatest of two numbers. 
# num=int(input("enter a number"))
# num1=int(input("enter a number"))
# if num > num1:
#     print("num is greater")
# else:
#     print("num1 is greater")

# # v.Print "Pass" if a student scores more than 40 marks;  otherwise, print "Fail." 
# num =int(input("enter a number"))
# if num > 40:
#     print("student is pass")
# else:
#     print("student is fail")

# # vi.	Write a program to display the day of the week based on a  number input (1 for Monday, 2 for Tuesday, etc.). 
# num=int(input("enter a number of (1-5)"))
# if num == 1:
#     print("num is monday")
# elif num == 2:
#     print("num is tuesday")
# elif num == 3:
#     print("num is wednesday")
# elif num ==4:
#     print("num is thursday")
# elif num==5:
#     print("num is friday")
# else:
#     print("please enter a valid number")


# # vii.	Implement a simple calculator to perform addition,  subtraction, multiplication, and division. 
# opt=input("enter a operation perform")
# opd1=int(input("enter a first number"))
# opd2=int(input("enter a second number"))
# if opt=="add":
#     print(opd1 + opd2)
# elif opt=="sub":
#     print(opd1-opd2)
# elif opt == "mul":
#     ptint(opd1 * opd2)
# elif opt =="div":
#     str1="Division by zero not possible" if opd2==0 else opd1/opd2
#     print(str1)
# else:
#     print("invalid operator")
 
# # viii.	Write a program to display the name of a month based on  the month number (1 for January, 2 for February, etc.).
# num=int(input("enter a number of (1-6)"))
# if num ==1:
#     print(" num is january") 
# elif num ==2:
#     print("num is february")
# elif num ==3:
#     print("num is march")
# elif num ==4:
#     print("num is april")
# elif num ==5:
#     print("num is may")
# elif num ==6:
#     print("num is june")
# else:
#     print("please enter a valid number")

#  b.  Medium Questions: 
# i.	Write a program to find the greatest of three numbers. 
# num1=int(input("entera first number"))
# num2=int(input("enter second number"))
# num3=int(input("enter third number"))
# str1="num1 is greater" if num1 > num2 and num1 > num3 else "num2 is greater" if num2 > num3 else "num3 is greater"
# print(str1)

# ii.	Check if a year is a leap year. 
# Non century years should be divisible by 4
# century years should be divisible by 400
# year=int(input("enter a number"))
# if (year %100!=0 and year % 4==0) or year % 400==0:
#     print("leap year")
# else:
#     print("year is not a leap year")

# str1="leap year" if (year % 100 !=0 and year % 4==0) or year %4 00==0 else "not a leap year"
# print(str1)

# iii. write a program check the vowels consonants or neither
# str1=input("Enter a single character").lower()
# if len(str1) > 1 or len(str1) ==0:
#     print("i wont run code")
# else:
#     if str1 in "aeiou":
#        print("vowels")
#     elif str1.isalpha():
#         print("consonants")
#     else:
#       print("Neither")  #numbers

# if str1 in "aeiou":
#    print("vowels")
# else:
#     print("consonants")

# if str1 in ['a','e','i','o','u']:
#    print("vowels")
# else:
#     print("consonants")





# iv.	Calculate the grade of a student based on the marks they  score: 
# 1.	90-100  : Grade A 
# 2.	80-89  : Grade B 
# 3.	70-79  : Grade C 
# 4.	<70  : Fail. 
# num=int(input("enter a number"))
# if num >=90:
#     print("Grade A")
# elif num >=80:
#     print("Grade B")
# elif num >=70:
#     print("Grade C")
# else:
#     print("fail")

# v. write a program  to check if three sides length form a valid triangle.
# side1=int(input("side 1"))
# side2=int(input("side 2"))
# side3=int(input("side 3"))
# print("Triangle possible" if ((side1 + side2 > side3) and (side3 + side1 >  side2) and (side3 + side2 > side1)) else "invalid triangle")


# loop
# a.  Easy Questions: 
# # i.	Print all numbers from 1 to 100 using a  for  loop. 
# for i in range(1,101):
#     print(i)

# assignment
# ii.	Write a program to print the sum of the first  n  natural  numbers. (n*n+1/ 2) 
num=int(input("enter a nummber"))
print(int(num*(num+1)/2))

# write a program print all even numbers 1 to 50 using a while loop
n=1
while n<=50:
    if n %2==0:
        print(n)
    n+=1

# iv.	Write a program to display the multiplication table of a given  number. First 20 
for i in range(1,21):
    for j in range(1,21):
        print(i,"x",j,"=",i * j)
    

# ii.	Check if a given number is a prime number using a  for  loop. 
num=int(input("enter a number"))
for i in range(1,num + 1):
    if num % i ==0:
        print("prime")
    else:
        print("not a prime")


# iii.	Write a program to calculate the factorial of a number using  a  while  loop.  

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    result = 1
    while n > 0:
        result *= n
        n -= 1
    
    return result

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")





#  Print all numbers from 1 to 100 that are divisible by 3 and 5  using a  for  loop. 
num=int(input("enter a number"))
for num in range(1,101):
    if num % 3==0 and num % 5==0:
        print(num)
        


# # nearest prime number
# year=int(input("enter a year"))
# while True:
#     year +=1
#     if year % 4 == 0 and year % 100 !=0 and year % 400 == 0:
#         print("year")
#         break

# present number
# num = 5
# sum = 0  

# for i in range(1, num):  
#     if num % i == 0:  
#         sum += i  

# if sum == num:  
#     print(f"{num} is a perfect number.")  
# else:  

#     print(f"{num} is not a perfect number.")  


# find all armstrong number in a given range
# for three digits numbers
# num1 = int(input("enter a number"))
# num2 =int(input("enter a number"))
# for i in range(num1 ,num2 + 1):
#     temp = i

#     sum =0
#     while temp > 0:
#         rem = temp % 10
#         # print(rem)
#         sum+= rem **3
#         temp = temp //10
#     if i == sum:
#         print(i,"armstrong")



#three and four digits
lower_range=100
upper_range=10000
for i in range(lower_range,upper_range + 1):
    temp = i

    temp_str =len(str(i))
    sum =0
    while temp > 0:
        rem = temp % 10
        sum+=rem ** temp_str
        temp =temp // 10
    if i == sum:
        print(i,"armstrong")
