# flake8: noqa
"""
Test for Swedish Personal identity number
"""

import unittest

from stdnum.se import personalid as ssn
from stdnum.exceptions import ValidationError


VALID_SSN = ['880320-0016', '880320-0057', '8803200073', '8803200099', '8803200420',
             '8803200115', '8803200131', '8803200156', '8803200172', '8803200198']


class TestSwedenSSN(unittest.TestCase):
    """
    Test for Swedish Personal identity number
    """
    def test_non_digit(self):
        try:
            ssn.validate('a' * 10)
            self.assertTrue(False, 'Should throw ValidationError')
        except ValidationError:
            self.assertTrue(True, 'Should throw ValidationError')

    def test_valid(self):
        for number in VALID_SSN:
            ssn.validate(number)
            self.assertTrue(ssn.is_valid(number))

    def test_invalid_checksum(self):
        for num in VALID_SSN:
            checksum = int(num[-1:])

            for n in range(0, 10):
                if n == checksum:
                    continue
                number = num[:-1] + str(n)
                self.assertFalse(ssn.is_valid(number))
                try:
                    ssn.validate(number)
                    self.assertTrue(False, 'Should throw ValidationError')
                except ValidationError:
                    self.assertTrue(True, 'Should throw ValidationError')
