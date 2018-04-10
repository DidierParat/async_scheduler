import logging
import threading
import time

from task import Task


class AsyncScheduler(object):
    def __init__(self, timer=None):
        """
        Timer is an optional parameter that represents the amount of time in seconds
        that the scheduler should run.
        """
        self.__timer = timer
        self.__log = logging.getLogger('AsyncScheduler')
        self.__tasks = []
        self.__start_time = None

    def schedule(self, frequency, method):
        """ Schedule a call to a method every 'frequency'. Where frequency is in seconds """
        task = Task(frequency, method)
        self.__tasks.append(task)

    def run(self):
        """ Runs the scheduler """
        self.__start_time = time.time()
        next_wake_up = time.time()
        while not self.__timer_expired():
            next_wake_up += 1
            for task in self.__tasks:
                if task.decrement_tick_counter():
                    threading.Timer(0, task.run).start()
                    task.reset_tick_counter()
            """ TODO: add warning if active threads > 10 """
            self.__log.debug("Active threads: %d", threading.active_count())
            sleeping_time = next_wake_up - time.time()
            self.__log.debug("Sleep now, starting a new thread in %f", sleeping_time)
            time.sleep(sleeping_time)

    def __timer_expired(self):
        if self.__timer is None:
            return False
        return time.time() >= (self.__timer + self.__start_time)
