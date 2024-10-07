# обложить тестами UnitTest
import unittest
import UnitTest


class RunnerTest(unittest.TestCase):

# test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
# Далее вызовите метод walk у этого объекта 10 раз. После чего методом assertEqual
# сравните distance этого объекта со значением 50

    def test_walk(self):
        first = UnitTest.Runner("First")
        for i in range(10):
            first.walk()
        self.assertEqual(first.distance, 50)

# test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
# Далее вызовите метод run у этого объекта 10 раз. После чего методом assertEqual
# сравните distance этого объекта со значением 100

    def test_run(self):
        second = UnitTest.Runner("Second")
        for i in range(10):
            second.run()
        self.assertEqual(second.distance, 100)

# test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
# Далее 10 раз у объектов вызываются методы run и walk соответственно.
# Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.

    def test_chellenge(self):
        self.third = UnitTest.Runner(name="Third")
        self.fourth = UnitTest.Runner(name="Fourth")
        for i in range(10):
            self.third.run()
            self.fourth.walk()
        self.assertNotEqual(self.third.run, self.fourth.walk)

if __name__ == '__main__':
    unittest.main()

            

