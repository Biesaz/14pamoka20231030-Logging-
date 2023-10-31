# 1
# Create a simple program that would log all inputs from the terminal. 
# Configs must show all additional data (time, date, level etc.)

import logging
logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

list_of_ten_integers = []
print("Enter 10 numbers: ")
for numbers in range(10):
    entered_numbers = int(input())
    list_of_ten_integers.append(entered_numbers)
sum_of_ten_integers = sum(list_of_ten_integers)
average_of_ten_integers = sum_of_ten_integers / len(list_of_ten_integers)
print("The sum of the entered 10 numbers is:", sum_of_ten_integers)
print("The average of the entered 10 numbers is:", average_of_ten_integers)

# logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

# import logging

# logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
# name = input("Enter Your Name:\n")
logging.info(f"{sum_of_ten_integers} has logged {list_of_ten_integers} successfully !!{average_of_ten_integers}")


# 4
# Create a program that takes 4 data types/structures: strings, numbers, list, dict. 
# Iterate 10 times with inputs and log what data type/structure and how many times was entered. 
# Handle all possible errors and log it.

