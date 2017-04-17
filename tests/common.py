import unittest
import stats.common as cm

import numpy as np


class TestAcvar(unittest.TestCase):

    def test_trivial_case(self):

        """ Auto-covariance of a constant list should be 0 """

        # generating sample
        sample_length = 1000
        sample = [1.]*sample_length

        # expected output
        n_legs = 5
        expected_output = [0.]*(n_legs+1)

        # actual output
        actual_output = cm.acvar(sample, n_legs)

        self.assertEqual(expected_output, actual_output)
