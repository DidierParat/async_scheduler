import logging

from async_scheduler import AsyncScheduler

foo1_call_counter = 0
foo2_call_counter = 0
foo3_call_counter = 0


def foo1():
    global foo1_call_counter
    foo1_call_counter += 1


def foo2():
    global foo2_call_counter
    foo2_call_counter += 1


def foo3():
    global foo3_call_counter
    foo3_call_counter += 1
    raise


def main():
    """ starting point
    """
    logging.basicConfig(
        filename='test.log',
        filemode='w',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s')
    async_scheduler = AsyncScheduler(11)
    async_scheduler.schedule(2, foo1)
    async_scheduler.schedule(3, foo2)
    async_scheduler.schedule(7, foo3)
    async_scheduler.run()
    test_fail = False
    if foo1_call_counter != 5:
        print "Unexpected number of calls for foo1!"
        print "Expected 5, got {0}".format(foo1_call_counter)
        test_fail = True
    if foo2_call_counter != 3:
        print "Unexpected number of calls for foo2!"
        print "Expected 5, got {0}".format(foo2_call_counter)
        test_fail = True
    if foo3_call_counter != 1:
        print "Unexpected number of calls for foo3!"
        print "Expected 5, got {0}".format(foo3_call_counter)
        test_fail = True
    if not test_fail:
        print "All tests passed !"

if __name__ == '__main__':
    main()
