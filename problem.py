import logging 

def basicLogger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formate = logging.Formatter('%(asctime)s : %(process)s : %(levelname)s : %(message)s ')
    sh = logging.StreamHandler()
    sh.setFormatter(formate)
    logger.addHandler(sh)
    return (logger)


logger = basicLogger()

logger.info("this is test")
