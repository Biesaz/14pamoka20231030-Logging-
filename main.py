# Lesson 14: Logging ######################################
# There are five ways we can display a log message in python with setting log levels: DEBUG, INFO, WARNING, ERROR, and CRITICAL.

# The Five Levels of Logging (The severity level)
# 10 DEBUG:          It is used for diagnosing the problem. It gives a piece of detailed information about the problem.
# 20 INFO:           It gives the confirmation message of the successful execution of the program.
# 30 WARNING:        The message is for when an unexpected situation occurs.
# 40 ERROR:          It is due to a more serious problem than a warning. 
#                    It can be due to some inbuilt error Like syntax or logical error.
# 50 CRITICAL:       It occurs when the program execution stops and it can not run itself anymore.

# import logging

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')
# -------------------OUTPUT---------------------
# WARNING:root:This is a warning message
# ERROR:root:This is an error message
# CRITICAL:root:This is a critical message

# basicConfig #########################################################
# level:      To change the root logger to a specified severity level.
# filename:   Filename where the logs going to be stored.
# filemode:   If a filename is given then this specifies the file mode in which the file will open. default is append (a )
# format:     This is the format of the log message.
# datefmt:    It specified the date and time format.

# import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
# logging.debug('This is Debug Message')
# logging.info('This is an info message')
# -------------------------CONSOLE OUTPUT------------------
# 12/05/2021 20:46:41 - root - DEBUG - This is Debug Message
# 12/05/2021 20:46:41 - root - INFO - This is an info message

# Logging to file ##########################################################################################
# Similarly, for logging the result** in a file** you can add filename and file mode to basicConfig:
# logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='w')

# import logging
# logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
# name = input("Enter Your Name:\n")
# logging.info(f"{name} has logged in successfully !!")

# Logging Exception ##################################
# import logging
# a = 10
# b = 0
# try:
#   c = a / b
# except Exception as e:
#   logging.error("Exception Occurred", exc_info=True)  ## At default it is True
  
#  ----------------------------------CONSOLE OUTPUT------------------------
# ERROR:root:Exception Occurred        ## If exc_info=False then only this message will print
# Traceback (most recent call last):
#   File "C:\Users\minde\Desktop\ds\python\advance_concepts\logging_code.py", line 5, in <module>
#     c = a / b
# ZeroDivisionError: division by zero