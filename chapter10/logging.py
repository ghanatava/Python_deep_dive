import logging

logging.basicConfig(filename='logs.log',level='DEBUG')

logging.error("An error has occured ")
logging.critical("System exited exit code 1")
logging.info("The System is up")
logging.debug("Line 10 syntax error")

#storing exxceptions

try:
    a=int(input('enter a number '))
    b=int(input('Enter another number '))
    c=a/b

except Exception as e:
    logging.exception(e)

else:
    print('the result of division: ',c)
