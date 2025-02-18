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
