from src.Parser import Parser
from src.Polynom import Polynom


def test_one_solution1():
	equation = "2 * X^0 + 4 * X^1 + 2 * X^2 = 0 * X^0"
	parser = Parser(equation)
	polynom = Polynom(parser)
	assert polynom.answer[0] == -1


def test_one_solution2():
	equation = "1 * X^0 + 2 * X^1 + 1 * X^2 = 0 * X^0"
	parser = Parser(equation)
	polynom = Polynom(parser)
	assert polynom.answer[0] == -1.0


def test_one_solution3():
	equation = "1 * X^0 - 2 * X^1 + 1 * X^2 = 0 * X^0"
	parser = Parser(equation)
	polynom = Polynom(parser)
	assert polynom.answer[0] == 1.0


def test_one_solution4():
	equation = "-1 * X^0 - 2 * X^1 - 1 * X^2 = 0 * X^0"
	parser = Parser(equation)
	polynom = Polynom(parser)
	assert polynom.answer[0] == -1.0


def test_one_solution5():
	equation = "6 * X^0 + 11 * X^1 + 5 * X^2 = 1 * X^0 + X"
	parser = Parser(equation)
	polynom = Polynom(parser)
	assert polynom.answer[0] == -1


def test_two_solutions1():
	equation = "4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0 * X^0"
	parser = Parser(equation)
	polynom = Polynom(parser)
	assert polynom.answer[0] == -0.47513146387096705
	assert polynom.answer[1] == 0.9052389907526873


def test_two_solutions2():
	equation = "5 * X^0 + 13 * X^1 + 3 * X^2 = 1 * X^0 + 1 * X^1"
	parser = Parser(equation)
	polynom = Polynom(parser)
	assert polynom.answer[0] == -0.3670068381666696
	assert polynom.answer[1] == -3.63299316183333


def test_two_solutions3():
	equation = "-5 * X^0 + 13 * X^1 + 3 * X^2 = 1 * X^0 + 1 * X^1"
	parser = Parser(equation)
	polynom = Polynom(parser)
	assert polynom.answer[0] == 0.44948974266666425
	assert polynom.answer[1] == -4.449489742666664


def test_two_solutions4():
	equation = "X ^ 2 = 4"
	parser = Parser(equation)
	polynom = Polynom(parser)
	assert polynom.answer[0] == 2
	assert polynom.answer[1] == -2


def test_two_solutions5():
	equation = "x ^ 2 = 0.0001"
	parser = Parser(equation)
	polynom = Polynom(parser)
	assert polynom.answer[0] == 0.01
	assert polynom.answer[1] == -0.01


def test_two_solutions6():
	equation = "6 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
	parser = Parser(equation)
	polynom = Polynom(parser)
	assert polynom.answer[0] == -0.5490683012365587
	assert polynom.answer[1] == 0.979175828118279


def test_two_solutions7():
	equation = "7 * X^0 + 13 * X^1 + 3 * X^2 = 1 * X^0 + 1 * X^1"
	parser = Parser(equation)
	polynom = Polynom(parser)
	assert polynom.answer[0] == -0.5857864376666676
	assert polynom.answer[1] == -3.4142135623333325


def test_two_complex_solutions1():
	equation = "5 * X^0 + 3 * X^1 + 3 * X^2 = 1 * X^0 + 0 * X^1"
	parser = Parser(equation)
	polynom = Polynom(parser)
	assert polynom.answer[0] == f'-0.5 + 1.0408329996666663 * i'
	assert polynom.answer[1] == f'-0.5 - 1.0408329996666663 * i'


def test_two_complex_solutions2():
	equation = "4 * X^0 + 3 * X^1 + X^2 = 0"
	parser = Parser(equation)
	polynom = Polynom(parser)
	assert polynom.answer[0] == f'-1.5 + 1.3228756555000003 * i'
	assert polynom.answer[1] == f'-1.5 - 1.3228756555000003 * i'


def test_two_complex_solutions3():
	equation = "6 * X^0 + 4.2 * X^2 = 1 * X^0"
	parser = Parser(equation)
	polynom = Polynom(parser)
	assert polynom.answer[0] == f'1.0910894509999998 * i'
	assert polynom.answer[1] == f'-1.0910894509999998 * i'


def test_degree1_solution1():
	equation = "5 * X^0 + 4 + 7 * X^1 + 8 * X = 0"
	parser = Parser(equation)
	polynom = Polynom(parser)
	assert polynom.answer[0] == -0.6


def test_degree1_solution2():
	equation = "5X^0 + 4X^1 - 0 * X^2 = 1 * X^0"
	parser = Parser(equation)
	polynom = Polynom(parser)
	assert polynom.answer[0] == -1


def test_infinitive_solutions1():
	equation = "5 * X^2 = 5 * X^2"
	try:
		parser = Parser(equation)
		polynom = Polynom(parser)
	except:
		pass


def test_no_solutions1():
	equation = "6 * X^0 + 0 * X^2 = 1 * X^0"
	try:
		parser = Parser(equation)
		polynom = Polynom(parser)
	except:
		pass


def test_no_solutions2():
	equation = "5 * X^0 = 8 * X^0"
	try:
		parser = Parser(equation)
		polynom = Polynom(parser)
	except:
		pass


def test_big_degree1():
	equation = "4 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^3"
	try:
		parser = Parser(equation)
		Polynom(parser)
	except:
		pass


def test_big_degree2():
	equation = "4 * X^0 + 4 * X^4 - 9.3 * X^2 = 0 * X^2"
	try:
		parser = Parser(equation)
		Polynom(parser)
	except:
		pass


def test_big_degree3():
	equation = "1 * X^5 = 0 * X^0"
	try:
		parser = Parser(equation)
		Polynom(parser)
	except:
		pass


def test_big_degree4():
	equation = "6 * X^0 + 4 * X^18 - 9.3 * X^3 = 1 * X^0"
	try:
		parser = Parser(equation)
		polynom = Polynom(parser)
	except:
		pass


def test_error_negative():
	equation = "6 * X^0 + -4 * X^2 = 1 * X^0"
	try:
		parser = Parser(equation)
		polynom = Polynom(parser)
	except:
		pass


def test_error_characters():
	equation = "5glezjjngv = 1 * X^0"
	try:
		parser = Parser(equation)
		polynom = Polynom(parser)
	except:
		pass


def test_error_equal():
	equation = "5 * X = 1 * X^0 = 3 * X"
	try:
		parser = Parser(equation)
		polynom = Polynom(parser)
	except:
		pass


def test_error_equal1():
	equation = "5 * X + 3 * X"
	try:
		parser = Parser(equation)
		polynom = Polynom(parser)
	except:
		pass
