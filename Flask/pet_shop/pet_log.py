import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("pet_log.log")
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s %(name)s %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.info("log file created")

def do_something():
    logging.info('Doing something')

def log_info():
    f=open('pet_log.log','r')
    log = f.read()
    log = log.split('\n')
    return log

