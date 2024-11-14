import runner_and_tournament as test
import unittest


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner_1 = test.Runner('Усэйн', 10)
        self.runner_2 = test.Runner('Андрей', 9)
        self.runner_3 = test.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print(show_result)

    def test_1(self):
        self.tournament = test.Tournament(90, self.runner_1, self.runner_3)
        self.all_results = self.tournament.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == self.runner_3.name)
        TournamentTest.all_results[1] = self.all_results

    def test_2(self):
        self.tournament = test.Tournament(90, self.runner_2, self.runner_3)
        self.all_results = self.tournament.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == self.runner_3.name)
        TournamentTest.all_results[2] = self.all_results

    def test_3(self):
        self.tournament = test.Tournament(90, self.runner_1, self.runner_2,  self.runner_3)
        self.all_results = self.tournament.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == self.runner_3.name)
        TournamentTest.all_results[3] = self.all_results

if __name__ == '__main__':
    unittest.main()