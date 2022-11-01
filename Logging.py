import logging

logger = logging.getLogger("Calculate")
error_logger = logging.getLogger("Error")
formatter = logging.Formatter("'%(asctime)s - %(message)s'")

Arithmetic_handler = logging.FileHandler("Calculate.log")
Arithmetic_handler.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(Arithmetic_handler)

Error_handler = logging.FileHandler("Error.log")
Error_handler.setFormatter(formatter)
error_logger.setLevel(logging.WARNING)
error_logger.addHandler(Error_handler)

def DivByZero():
    message = "Error: Divide by Zero"
    error_logger.warning(message)

def InvalidInput():
    message = "Error: Invaild Choice Input - Out of Range(1~4)"
    error_logger.warning(message)

def Arithmetic_Add(message):
    logger.info(message)

def Arithmetic_Sub(message):
    logger.info(message)

def Arithmetic_Mul(message):
    logger.info(message)

def Arithmetic_Div(message):
    logger.info(message)