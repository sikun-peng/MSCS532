import unittest
from RecommendationSystem import RecommendationSystem

class TestRecSys(unittest.TestCase):
    def test_add_and_predict(self):
        r = RecommendationSystem()
        r.add_interaction("u1", "i1", 4)
        self.assertAlmostEqual(r.predict_score("u1", "i1"), 4)

    def test_global_avg(self):
        r = RecommendationSystem()
        r.add_interaction("u1", "i1", 4)
        r.add_interaction("u2", "i2", 2)
        self.assertAlmostEqual(r.global_avg, 3.0)

if __name__ == '__main__':
    unittest.main()