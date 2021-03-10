import unittest
import calculator

class test_plus(unittest.TestCase):
	def test1(self):
		self.assertEqual(calculator.plus(1, 1), 2);
	def test2(self):
		self.assertEqual(calculator.plus(-1, 1), 0);
	def test3(self):
		self.assertEqual(calculator.plus(1, -1), 0);
	def test4(self):
		self.assertEqual(calculator.plus(-1, -1), -2);
	def test5(self):
		self.assertEqual(calculator.plus(1.1, 1.1), 2.2);

class test_minus(unittest.TestCase):
	def test1(self):
		self.assertEqual(calculator.minus(1, 1), 0);
	def test2(self):
		self.assertEqual(calculator.minus(-1, 1), -2);
	def test3(self):
		self.assertEqual(calculator.minus(1, -1), 2);
	def test4(self):
		self.assertEqual(calculator.minus(-1, -1), 0);
	def test5(self):
		self.assertEqual(calculator.minus(1.1, 1.1), 0);

class test_times(unittest.TestCase):
	def test1(self):
		self.assertEqual(calculator.times(1, 1), 1);
	def test2(self):
		self.assertEqual(calculator.times(-1, 1), -1);
	def test3(self):
		self.assertEqual(calculator.times(1, -1), -1);
	def test4(self):
		self.assertEqual(calculator.times(-1, -1), 1);
	def test5(self):
		self.assertEqual(calculator.times(1, 1.1), 1.1);

class test_divide(unittest.TestCase):
	def test1(self):
		self.assertEqual(calculator.divide(1, 1), 1);
	def test2(self):
		self.assertEqual(calculator.divide(-1, 1), -1);
	def test3(self):
		self.assertEqual(calculator.divide(1, -1), -1);
	def test4(self):
		self.assertEqual(calculator.divide(-1, -1), 1);
	def test5(self):
		self.assertEqual(calculator.divide(2, .5), 4);
	def test6(self):
		with self.assertRaises(ZeroDivisionError):
			calculator.divide(1, 0);

if __name__ == '__main__':
	unittest.main()
