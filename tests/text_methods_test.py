from main import get_extractable_char, compare
import unittest


class TestStringMethods(unittest.TestCase):
	
	def test_is_extractable(self):
		test_data = (
			('|test|', 'test', '|'),
			('|test|', 'test', '|'),
			('|XYZ|', 'test', None),
			('|XYZ"', 'XYZ', None),
			('"XYZ"', 'XYZ', '"'),
			('"XYZ', 'XYZ', None),
			('XYZ', 'XYZ', None)
		)
		for data in test_data:
			res = get_extractable_char(data[0], data[1])
			with self.subTest(text=data[0], test_for=data[1], result=res, expected_result=data[2]):
				self.assertEqual(res, data[2])
	
	def test_compare(self):
		test_data = (
			('test', 'test', 100),
			('ABC', 'ABCDEFGHIJ', 30),
			('test ABCDE', 'ABCDE', 50),
			('abcdefghij', 'hij', 30)
		)
		for data in test_data:
			result = int(compare(data[0], data[1]))
			with self.subTest(src=data[0], text=data[1], result=result, expected_result=data[2]):
				self.assertEqual(result, data[2])


if __name__ == '__main__':
	TestStringMethods().run()
