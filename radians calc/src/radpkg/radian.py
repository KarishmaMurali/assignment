'''degree to radians'''
import math
import logging
def rad(degree):
    '''calculate radians'''
    logging.basicConfig(filename="configfile.log", level=logging.ERROR,
                        format='%(asctime)s:%(levelname)s:%(message)s',
                        filemode='w')

    try:
        degree = float(degree)
        constpi = math.pi
        radian = degree * (constpi / 180)
        return radian
    except ValueError as ex:
        logging.error(ex.message)
        return "Enter a number"
