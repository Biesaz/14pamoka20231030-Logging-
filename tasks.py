# 1
# Create a simple program that would log all inputs from the terminal. 
# Configs must show all additional data (time, date, level etc.)

# import logging

# logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='w')

# list_of_ten_integers = []
# print("Enter 10 numbers: ")
# for numbers in range(10):
#     entered_numbers = int(input())
#     list_of_ten_integers.append(entered_numbers)
# sum_of_ten_integers = sum(list_of_ten_integers)
# average_of_ten_integers = sum_of_ten_integers / len(list_of_ten_integers)
# print("The sum of the entered 10 numbers is:", sum_of_ten_integers)
# print("The average of the entered 10 numbers is:", average_of_ten_integers)

# logging.info(f"Entered numbers is {list_of_ten_integers}, their sum is {sum_of_ten_integers} and average is {average_of_ten_integers}. All logged successfully !!")

# 2
# Write a function that moves all elements of one type to the end of the list:
# move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.
# Log out inputs and results in a file.

# import logging

# logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='w')

# def move_to_end(list, element):
#     # Filter the elements to move to the end
#     elements_to_move = [x for x in list if x == element]
    
#     # Remove the elements from the original list
#     list = [x for x in list if x != element]
    
#     # Append the filtered elements to the end of the list
#     list.extend(elements_to_move)
    
#     return list

# # Test the function with your example
# input_list = [1, 3, 2, 4, 4, 1]
# element_to_move = 1
# result = move_to_end(input_list, element_to_move)
# print(result)

# logging.info(f" Entered list is {input_list}, and moved list is {result}. All logged successfully !!")

