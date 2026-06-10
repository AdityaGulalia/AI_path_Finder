import logging 

def setup_logger(filename):
    logging.basicConfig(filename=f"logs/{filename}.log", level = logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')