import logging

class Log:

    def initLog(self):

        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger(__name__)

        # create a file handler
        handler = logging.FileHandler('Test_Log.log')

        # create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # add the handlers to the logger
        logger.addHandler(handler)
        return logger
