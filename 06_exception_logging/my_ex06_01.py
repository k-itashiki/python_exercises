from logging import basicConfig, getLogger, DEBUG


def create_logger(name, log_level):
    """create logger"""
    basicConfig(level=log_level)
    logger = getLogger(name if name else __file__)
    return logger





def main():
    """show how to handle and log the exception"""

    logger = create_logger("my_logger", DEBUG)
    
    try:
        with open("ex_not_exist_file1.py") as f:
            lines = f.readlines()

    except IOError as ex:
        logger.info("Now try to open file that does not exist!")
        logger.critical("You faced Exception! {}".format(ex))

if __name__ == "__main__":
    main()
