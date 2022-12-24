import inspect
import logging


def customLogger():
    # This is used to get the class/method name from where this custom logger is called
    logName = inspect.stack()[1][3]

    # To Create the logging pbject and pass the logName in it
    logger = logging.getLogger(logName)

    # Set log level
    logger.setLevel(logging.INFO)

    # Create file handler to save the log in the file
    fileHandler = logging.FileHandler('{0}.log'.format(logName), mode='a')
    #fileHandler = logging.FileHandler('../LogReport/CustomLog.log', mode='a')


    # ../ LogReport /

    # set log level for file handler
    fileHandler.setLevel(logging.DEBUG)

    # create the formatter
    formatter = logging.Formatter('%(asctime)s :%(levelname)s :%(message)s',
                                  datefmt='%d/%m/%y %I:%M:%S %p %A')

    # set the formatter to file handler
    fileHandler.setFormatter(formatter)

    # Add file handler to logging
    logger.addHandler(fileHandler)

    return logger