import logging

class Log:

    def getLoggerInstance(self):

        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger(__name__)

        handler = logging.FileHandler('application.log')

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        return logger
