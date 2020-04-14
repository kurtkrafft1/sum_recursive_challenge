numbers  = [1,4,5,3,2,5]
##### sum with for loop

total = 0

# for number in numbers:
#     new_total = total + number
#     total = new_total
#     print(total)


####### sum with while loop 

# counter = 0
# total = 0
# while counter < len(numbers):
#     new = numbers[counter] + total
#     total = new
#     print (new)
#     counter += 1

###### Recursive function

def recursive_test(num):
    if num == (len(numbers)-1):
        return numbers[num]
    else:
        return(numbers[num] + recursive_test(num+1))

print(recursive_test(0))

