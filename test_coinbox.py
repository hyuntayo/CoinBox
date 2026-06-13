# test_coinbox.py
"""
Tests for CoinBox module.
"""

import unittest
from coinbox import CoinBox

class TestCoinBox(unittest.TestCase):
    """Test cases for CoinBox class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoinBox()
        self.assertIsInstance(instance, CoinBox)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoinBox()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
