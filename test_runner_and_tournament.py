import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):

    # setUpClass - метод, где создаётся атрибут класса all_results.
    # Это словарь в который будут сохраняться результаты всех тестов.

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        del cls.all_results

    # setUp - метод, где создаются 3 объекта:
    # Бегун по имени Усэйн, со скоростью 10.
    # Бегун по имени Андрей, со скоростью 9.
    # Бегун по имени Ник, со скоростью 3.

    def setUp(self):
        self.run_1 = runner_and_tournament.Runner('Усейн', 10)
        self.run_2 = runner_and_tournament.Runner('Андрей', 9)
        self.run_3 = runner_and_tournament.Runner('Ник', 3)
        self.results = {}

    # tearDownClass - метод, где выводятся all_results по очереди в столбец.
    def tearDown(self):
        self.all_results = self.results
        print(self.all_results)
        for key in self.all_results:
            print(key, self.all_results[key])
        print('___ ' * 20)
        super().tearDown()

    # Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90.
    # У объекта класса Tournament запускается метод start, который возвращает словарь в переменную all_results.
    # В конце вызывается метод assertTrue, в котором сравниваются последний объект из all_results
    # (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
    # Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
    # Усэйн и Ник
    # Андрей и Ник
    # Усэйн, Андрей и Ник.
    # Как можно понять: Ник всегда должен быть последним.

    def test_start1(self):
        distance = runner_and_tournament.Tournament(90, self.run_1, self.run_3)
        distance1 = distance.start()
        self.results = distance1
        self.assertTrue(self.results[2] == 'Ник')

    def test_start2(self):
        distance = runner_and_tournament.Tournament(90, self.run_2, self.run_3)
        distance2 = distance.start()
        self.results = distance2
        self.assertTrue(self.results[2] == 'Ник')

    def test_start3(self):
        distance = runner_and_tournament.Tournament(90, self.run_3, self.run_1, self.run_2)
        distance3 = distance.start()
        self.results = distance3
        self.assertTrue(self.results[3] == 'Ник')

    # в методе start класса Tournament, допущена логическая ошибка.
    # В результате его работы бегун с меньшей скоростью может пробежать некоторые дистанции быстрее,
    # чем бегун с большей.
    # Попробуйте решить эту проблему и обложить дополнительными тестами.

    def test_start4(self):
        distance = runner_and_tournament.Tournament(90, self.run_2, self.run_1, self.run_3)
        distance4 = distance.start()
        self.results = distance4
        self.assertTrue(self.results[2] == 'Андрей', 'Наличие логической ошибки в методе start')


if __name__ == '__main__':
    unittest.main()
