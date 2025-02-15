# Write a program to print numbers from -1 to -10
def numbers():
    for i in range(-1,-11,-1):
        print(i)
numbers()

for i in range(-1,-11,-1):
    print(i)

# sum of digits in a number and add when its is even
# def sum_of_digits(num):
#     sum=0
#     if num % 2 == 0:


# prime or not a prime
# def check_if_prime(num):
#     if num <=1:
#         return False
#     for i in range(2,num+1):
#         if num % i == 0:
#             return False
#     return True
# input=int(input("enter a number"))

# print (input,"prime number") if check_if_prime(input) else print(input,"not a prime number")



# range of numbers -check prime or not in certain range
def prime_range(num):
    if num <=1:
        return False
    for i in range(2, num + 1):
        return False
    return True

num1=int(input("enter a number"))
num2=int(input("enter a number"))
for num in range(num1,num2+1):
    print(num,"prime number") if prime_range(num) else print(num,"not a prime number")

# write a program to print sum of non-primes digits in a given number
def sum_nonprimes(n):
    primes={0,1,6,8,9,4}
    return 




# write a program to print max prime digit in a certain number









# compare first digit and last digit in a number (print equal if there are equal)
def compare_first_last_digit(n):
    n = str(n)  
    if n[0] == n[-1]:  
        return "Equal"
    else:
        return "Not Equal"

num = int(input("Enter a number: "))
print(compare_first_last_digit(num))


# print nth fibnocci number
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0  
    elif n == 2:
        return 1  
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter N: "))
print(f"{num}th Fibonacci number:", fibonacci(num))

# print non-fibnocci numbers in a given range (1 to 100)





# reverse a number in a negative numbers
def reverse_number(n):
    if n >= 0:
        return int(str(n)[::-1])
    else:
        return -int(str(n)[:0:-1])

num = int(input("Enter a number: "))
print("Reversed number:", reverse_number(num))






# write a program to check the index
def search_a_num(list, search_num):
    """Search for a number in the list and print its index."""
    index = 0  
    for num in list:
        if num == search_num:
            return index  
        index += 1  
    return -1  

list = [2, 4, 6, 8, 10, 0.2, -3]
search_num = float(input("Enter a number to search: "))  

index = search_a_num(list, search_num)
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")