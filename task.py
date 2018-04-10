import logging
import time


class Task(object):
    def __init__(self, frequency, method):
        self.__frequency = frequency
        self.__method = method
        self.__tick_counter = frequency
        self.__log = logging.getLogger('AsyncScheduler')

    def decrement_tick_counter(self):
        self.__tick_counter -= 1
        return self.__tick_counter == 0

    def reset_tick_counter(self):
        self.__tick_counter = self.__frequency

    def run(self):
        start = time.time()
        try:
            self.__method()
        except:
            self.__log.exception('%s threw an exception: ', self.__method.func_name)
        finally:
            execution_time = time.time() - start
            self.__log.info('%s took %f seconds', self.__method.func_name, execution_time)
