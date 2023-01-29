import random

def split_list(input_list):
    # Use the sample method to randomly select elements from the input list
    list1 = random.sample(input_list, len(input_list)//2)
    list2 = [item for item in input_list if item not in list1]
    return list1, list2

my_list = [1, 2, 3, 4, 5, 6]
list1, list2 = split_list(my_list)
print(list1)
print(list2)
