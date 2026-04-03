import unittest
import pycalc.pycalc as calculator

class PyCalcUnitTests(unittest.TestCase):
  def test_add(self):
    left = [5]
    right = [9]
    expected = [14]
    for i in range(len(left)):
      l = left[i]
      r = right[i]
      e = expected[i]
      with self.subTest(l=l, r=r, e=e):
        got = calculator.add(l, r)
        self.assertEqual(got, e)

  def test_multiply(self):
    left = [5]
    right = [9]
    excepted = [45]
    for i in range(len(left)):
      l = left[i]
      r = right[i]
      e = expected[i]
      with self.subTest(l=l, r=r, e=e):
        got = calculator.multiply(l,r)
        self.assertEqual(got, e)
        
if __name__ == '__main__':
  unittest.main()
