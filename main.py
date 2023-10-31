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

# import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
# logging.debug('This is Debug Message')
# logging.info('This is an info message')
# -------------------------CONSOLE OUTPUT------------------
# 12/05/2021 20:46:41 - root - DEBUG - This is Debug Message
# 12/05/2021 20:46:41 - root - INFO - This is an info message

import logging
logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
name = input("Enter Your Name:\n")
logging.info(f"{name} has logged in successfully !!")
