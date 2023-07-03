import logging
import datetime

# C_LOG_PATH_FILE_NAME = "/home/myproject/logs/myproject"
C_LOG_PATH_FILE_NAME = 'C:/Users/marcelo.miotto/OneDrive/Documents/Python/easyPlub/backend/flask/logs/myproject'
C_LOG_DATE_MASK = '{:%Y-%m-%d}'

def log(msg):
    logging.basicConfig(filename=C_LOG_PATH_FILE_NAME+"_" + C_LOG_DATE_MASK.format(datetime.datetime.now()) + ".log",
                        format='%(asctime)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S',
                        level=logging.INFO)
    logging.log(level=logging.INFO, msg=msg)


