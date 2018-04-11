import time
import unittest

from async_scheduler import AsyncScheduler
from mock import MagicMock


class TestAsyncScheduler(unittest.TestCase):

    def test_run(self):
        async_scheduler = AsyncScheduler(2)
        start_time = time.time()
        async_scheduler.run()
        end_time = time.time()
        run_time = end_time - start_time
        self.assertAlmostEqual(run_time, 2, 2)

    def test_function_without_parameter(self):
        async_scheduler = AsyncScheduler(1)
        foo = MagicMock()
        async_scheduler.schedule(1, foo)
        async_scheduler.run()
        foo.assert_called_once()

    def test_function_with_one_parameter(self):
        async_scheduler = AsyncScheduler(1)
        foo = MagicMock()
        foo_param = 'param'
        async_scheduler.schedule(1, foo, foo_param)
        async_scheduler.run()
        foo.assert_called_once()
        foo.assert_called_with(foo_param)

    def test_function_with_several_parameters(self):
        async_scheduler = AsyncScheduler(1)
        foo = MagicMock()
        foo_param1 = 'param1'
        foo_param2 = 'param2'
        async_scheduler.schedule(1, foo, foo_param1, foo_param2)
        async_scheduler.run()
        foo.assert_called_once()
        foo.assert_called_with(foo_param1, foo_param2)

    def test_several_functions_scheduled(self):
        async_scheduler = AsyncScheduler(1)
        foo1 = MagicMock()
        foo2 = MagicMock()
        async_scheduler.schedule(1, foo1)
        async_scheduler.schedule(1, foo2)
        async_scheduler.run()
        foo1.assert_called_once()
        foo2.assert_called_once()

if __name__ == '__main__':
    unittest.main()
