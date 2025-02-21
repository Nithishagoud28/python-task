# Sum of elements in a List.
# list1=[2,4,6,8,9,10,15]
# sum=0
# for i in list1:
#     sum+=i
# print(sum)

# Finding the k Element which is present in a List.
num=[10,11,13,15,20,25]
k=2
for i in range(len(num)):
    if i == k:
        print(num[i])
        break


# Wap to print duplicates and unique numbers in an array/List.
my_list=[1,2,3,4,5,2,7,1,8,8,9,5,3,4,9,2]
duplicates=[]
unique=[]
for num in my_list:
    if my_list.count(num) > 1 and num not in  duplicates:
        duplicates.append(num)
    elif my_list.count == 1:
        unique.append(num)
print(duplicates)
print(unique)

# ) Count Occurrences of Each Digit
# input: 2788
# output: 2=> 1
# 7=> 1
# 8=> 2

def count_digits(num):
    num_str = str(num)
    digit_count = {}

    for digit in num_str:
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1

    for digit, count in digit_count.items():
        print(f"{digit} => {count}")

# Example usage
count_digits(2788)

# Reverse an Array.
num=12345  #reverse
rev_num=0
while num >0:
    rem= num % 10
    rev_num = rev_num * 10 + rem
    num = (num // 10)
print(rev_num)

# wap to check the digits of each number in an list are in increasing order returing true or false
def increasing_order(num):
    num_str=str(num)
    for i in range(len(num_str)-1):
        if num_str[i] >= num_str[i + 1]: 
            return False
    return True
numbers = [568, 89, 112, 88, 571]
res=[increasing_order(num) for num in numbers]
print(res)
# Find Unique and Duplicate Digits and If only one digit is duplicated,
#                      output: Duplicate is X.
#     If multiple digits are duplicated, output: Duplicates are X, Y, ....
#                      input :1214
#          output: 2,4
#         output: duplicate is 1
# duplicates= set()
# unique = set()
# num=input("enter a number")
# for digit in num:
#     if digit in unique:
#         duplicates.add(digit)
#         unique.remove(digit)
#     elif digit not in duplicates:
#         unique.add(digit)
# print(",".join(unique))
# print(",".join(duplicates))

# Wap to check if the digits of each number in an list are in decreasing order and return an array of true otherwise false.Decreasing order -true
def decreasing_order(num):
    num_str=str(num)
    for i in range(len(num_str)-1):
        if num_str[i] <= num_str[i + 1]: 
            return False
    return True
numbers = [538,111,200,652,]       
res=[decreasing_order(num) for num in numbers]
print(res)

# 17) Finding the frequency of elements in an array.
    # arr = [10, 30, 10, 20, 10, 20, 30, 10]  O/p: 10=> 4 30 =>2  20=> 2
arr = [10, 30, 10, 20, 10, 20, 30, 10]
frequency = {}
for num in arr:
    if num in frequency:
        frequency[num] += 1 
    else:
        frequency[num] = 1  
for num, count in frequency.items():
    print(f"{num} => {count}")


# 19) check if array is subset of another array or not .if the arr2 contains elements which are there in arr1 then it is a subset of an array.
# arr1=[1,3,4,5,2]
# arr2=[2,4,3,1,7.5.15]
# output: arr1 is subset of arr2
# Print arr2 is subset or not subset of arr1
# let arr1=[2,21,5,7,3,5,7,3,1,6,14,44];
# let arr2=[7,3,1];
arr1=[1,3,4,5,2]
arr2=[2,4,3,1,7.5,15]

set_arr1=set(arr1)
set_arr2=set(arr2)
if set_arr2.issubset(set_arr1):
    print("arr2 is a subset of arr1")
else:
    print("arr2 is not a subset of arra1")


arr1=[2,21,5,7,3,5,7,3,1,6,14,44]
arr2=[7,3,1]
set_arr1 = set(arr1)
set_arr2 = set(arr2)
if set_arr2.issubset(set_arr1):
    print("arr2 is a subset of arr1")
else:
    print("arr2 is not a subset of arr1")


# 20) Wap to print the number of pairs formed by the array of elements
#  Input: 10 20 10 30 20 20	  Output: 2 pairs
#  Input: 30 50 30 50 20 50 50 20 50 50    Output : 5 pairs
arr = [10, 20, 10, 30, 20, 20]
# arr1= [30, 50 ,30, 50 ,20 ,50 ,50, 20 ,50 ,50]
frequency = {}
for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
pairs = 0
for count in frequency.values():
    pairs += count // 2  
print(f"{pairs} pairs")



# 3)read a matrix 
# input : 
# 2 3 4 
# 3 9 2 
# 3 4 1 
# find the sum of numbers 2+9+1+4+3=?
list1=[
    [2, 3, 4],
    [3, 9, 2],
    [3, 4, 1]
]
sum = 0
for i in range(len(list1)):
    for j in range(len(list1[i])):
        if i == j or i + j == len(list1) - 1:  # Main & secondary diagonals
            sum += list1[i][j]
print(sum)




matrix = [
    [2, 3, 4],
    [3, 9, 2],
    [3, 4, 1]
]
target_numbers = {2, 9, 1, 4, 3} 
total_sum = 0
for i in matrix:
    for num in i:
        if num in target_numbers:
            total_sum += num
print(total_sum)

# matrix = [
#     [2, 3, 4],
#     [3, 9, 2],
#     [3, 4, 1]
# ]
sum_diagonals = [2,9,1,4,3]
total_sum = sum(sum_diagonals)
print(total_sum)


# 2) read a matrix 
# input : 
# 2 3 4 
# 3 9 2 
# 3 4 1 
# find the sum of outer layers 
# 2+3+4+3+3+3+4+1+2= ?

list = [[2,3,4],[3,9,2],[3,4,1]]
sum = 0
for i in range(len(list)):
    for j in range(len(list[i])):
        if i == 0 or j == 0 or i == len(list) -1 or j == len(list[i]) - 1:
             sum +=list[i][j]
print(sum)


# 4) print the outer number in a matrix
# input: 
# 1 2  3
# 5  4  1
# 3  6  1
# Out:
# 1 2 3 
# 5    1
# 3 6 1

list = [[1,2,3],[5,4,1],[3,6,1]]

for i in range(len(list)):
    for j in range(len(list[i])):
         if i == 0 or j == 0 or i == len(list) - 1 or j == len(list) - 1:
           print(list[i][j], end = " ")
         else:
             print(" ",end = " ")
    print()  




# Another Question:
# input:
# 8  1  3 
# 4   2  9 
# 3   1  5

# output
# 8   3 
#    2   
#  3   5

list = [[8,1,3],[4,2,9],[3,1,5]]
for i in range(len(list)):
    for j in range(len(list[i])):
        if i == 0 or i + j == len(list) -1:
            print(i,end= " ")

# 5) 1 2 3
#     4 5 3
#     2 5 3
# Print the outer layer elements side by side
# Outer layer elements: 1 2 3 4 3 2 5 3

ismatrix = [[1,2,3],[4,5,3],[2,5,3]]
sum = []
for i in range(len(ismatrix)):
    for j in range(len(ismatrix[i])):
        if i == 0 or i == len(ismatrix)-1:
          sum.append(ismatrix[i][j])
        else:
          if j == 0 or j == len(ismatrix)-1:
               sum.append(ismatrix[i][j])
print(sum)

# 5) 1 2 3
#     4 5 3
#     2 5 3
# Output: print the diagonal elements side by side:
# Diagonal elements are :1 5 3 3 5 2

 
list =[[1,2,3],[4,5,3],[2,5,3]]
sum = []
for i in range(len(list)):
   for j in range(len(list[i])):
      if i == j or i + j == len(list) - 1:
         sum.append(list[i][j])
         if i == j and i  + j == len(list) - 1:
             sum.append(list[i][j])
print(sum)
