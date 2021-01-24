from src.Parser import Parser
from src.Polynom import Polynom
import argparse
import ctypes


kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

if __name__ == "__main__":
	parser_arg = argparse.ArgumentParser(description="Polynom decision")
	parser_arg.add_argument('polynom', type=str, help='Input polynom')
	args = parser_arg.parse_args()
	try:
		parser = Parser(args.polynom)
		Polynom(parser)
	except (Exception, BaseException) as e:
		print(e)
		exit(1)
