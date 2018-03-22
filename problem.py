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

logger.info("Pleae go to that link and start working with some basic problems ")
print "\t https://www.hackerrank.com/domains/python/py-basic-data-types \n"
