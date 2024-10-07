import logging
import unittest
#import rt_with_exceptions as runner
import UnitTest
import runner_and_tournament as r_and_t

LOG_FILENAME = 'py.log'
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.INFO, filemode="w", encoding='UTF-8',
    format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipUnless(is_frozen != True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            first = UnitTest.Runner("First", -100)
            for i in range(10):
                first.walk()
            logging.info("'test_walk' выполнен успешно")
            self.assertEqual(first.distance, 50)
            return first.distance
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)
            self.assertEqual(first.distance, 50)
            return first.distance


    @unittest.skipUnless(is_frozen != True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            second = UnitTest.Runner(2, 10)
            for i in range(10):
                second.run()
            self.assertEqual(second.distance, 100)
            logging.info("'test_run' выполнен успешно")
            return second.run().distance
        except:
            logging.warning("Неверный тип данных для Runner", exc_info=True)
            self.assertEqual(second.distance, 100)
            return second.distance


    @unittest.skipUnless(is_frozen != True, 'Тесты в этом кейсе заморожены')
    def test_chellenge(self):
        self.third = UnitTest.Runner(name="Third")
        self.fourth = UnitTest.Runner(name="Fourth")
        for i in range(10):
            self.third.run()
            self.fourth.walk()
        self.assertNotEqual(self.third.run, self.fourth.walk)



class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):

        del cls.all_results


    def setUp(self):
        self.run_1 = r_and_t.Runner('Усейн', 10)
        self.run_2 = r_and_t.Runner('Андрей', 9)
        self.run_3 = r_and_t.Runner('Ник', 3)
        self.results = {}

    def tearDown(self):

        self.all_results = self.results
        for key in self.all_results:
            print(key, self.all_results[key])
        print('___ ' * 20)
        super().tearDown()

    @unittest.skipUnless(is_frozen != True, 'Тесты в этом кейсе заморожены')
    def test_start1(self):
        distance = r_and_t.Tournament(90, self.run_1, self.run_3)
        distance1 = distance.start()
        self.results = distance1
        self.assertTrue(self.results[2] == 'Ник')

    @unittest.skipUnless(is_frozen != True, 'Тесты в этом кейсе заморожены')
    def test_start2(self):
        distance = r_and_t.Tournament(90, self.run_2, self.run_3)
        distance2 = distance.start()
        self.results = distance2
        self.assertTrue(self.results[2] == 'Ник')

    @unittest.skipUnless(is_frozen != True, 'Тесты в этом кейсе заморожены')
    def test_start3(self):
        distance = r_and_t.Tournament(90,  self.run_3, self.run_1, self.run_2)
        distance3 = distance.start()
        self.results = distance3
        self.assertTrue(self.results[3] == 'Ник')

    @unittest.skipUnless(is_frozen != True, 'Тесты в этом кейсе заморожены')
    def test_start4(self):
        """Введен дополнительно """
        distance = r_and_t.Tournament(90,  self.run_2, self.run_1, self.run_3)
        distance4 = distance.start()
        self.results = distance4
        self.assertTrue(self.results[2] == 'Андрей', 'Наличие логической ошибки в методе start')


if __name__ == '__main__':
    unittest.main()
