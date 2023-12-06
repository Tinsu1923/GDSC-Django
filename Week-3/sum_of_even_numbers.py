numbers = [i for i in range(1,51)]
another_list = [] # Empty list
count = 0 # A count variable to store how many numbers are substituted by the words.
total_sum = 0 # We want to add the numbers not replaced by the words.
for i in numbers:
    if i % 3 == 0:
        another_list.append("Three")
        count += 1
    elif i % 5 == 0:
        another_list.append("Five")
        count += 1
    else:
        another_list.append(i)
        total_sum += i
print(another_list)
print(f"The numbers substituted with the words 'five' and 'three' are: {count} \nThe total sum of these numbers is {total_sum}")     
# First method to find the total sum of even numbers between 1 and 50
sums = 0
for i in range(1,51):
    if i % 2 == 0:
        sums += i
print(sums)
########################
# Second method.
sum2 = 0
for j in range(2,51, 2):
    sum2 += j
print(sum2)
    