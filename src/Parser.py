from .Color import Color
import re
import collections

MAPP = {'^0': '⁰', '^1': '¹', '^2': '²', '^3': '³', '^4': '⁴', '^5': '⁵', '^6': '⁶', '^7': '⁷', '^8': '⁸', '^9': '⁹', '*': '·'}


class Parser:
	def __init__(self, polynom):
		self.raw_polynom = polynom
		self.polynom = polynom.lower()
		self.pow_coef = {}
		self.left = None
		self.right = None
		self.degree = 0
		self.reduce_form1 = ''
		self.reduce_form2 = ''
		self.reduce_form3 = ''
		self.get_power_and_coef()
		self.get_reduce_forms()

	def get_power_and_coef(self):
		try:
			self.left, self.right = self.polynom.split('=')
		except Exception as e:
			raise BaseException(f'{Color.WARNING}ERROR: There is should be equal "=" in expression: "{self.raw_polynom}"{Color.END}')
		left_token = self.get_coef(self.left)
		right_tokens = self.get_coef(self.right)
		left_token.update({key: left_token[key] - right_tokens[key] for key in right_tokens.keys() if key in left_token.keys()})
		left_token.update({key: -right_tokens[key] for key in right_tokens.keys() if key not in left_token.keys()})
		self.pow_coef = dict(collections.OrderedDict(sorted(left_token.items())))
		self.pow_coef = list(filter(lambda x: x[1] != 0.0, self.pow_coef.items()))
		pass

	def get_coef(self, left_or_right: str):
		left_or_right = left_or_right.replace(" ", "")
		tokens = {}
		pattern_expression = re.compile(r'[+-]?[^+-]*')
		patterns_term = [re.compile(r'^((?P<sign>[+-]?)(?P<coef>(\d+\.)?\d+)(\*?(?P<X>x)(\^(?P<power>\d+))?)?)$'),
						re.compile(r'^((?P<sign>[+-]?)(?P<X>x)(\^(?P<power>\d+))?(\*?(?P<coef>(\d+\.)?\d+))?)$'),
						 None]
		for term1 in list(filter(None, pattern_expression.findall(left_or_right))):
			for pattern in patterns_term:
				if pattern is None:
					raise BaseException(f'{Color.WARNING}ERROR: expression "{self.raw_polynom}" has bad format{Color.END}')
				term = pattern.match(term1)
				if term is not None:
					sign = term.group('sign')
					coef = float(term.group('coef') or 1)
					x = term.group('X')
					power = float(term.group('power') or 1 if x else 0)
					coef = -coef if sign == '-' else coef
					if not tokens.get(power):
						tokens[power] = coef
					else:
						tokens[power] += coef
					break
		return tokens

	def get_reduce_forms(self):
		if self.pow_coef:
			self.degree = int(self.pow_coef[-1][0])
			for power, coef in self.pow_coef:
				if coef < 0 and power == 0:
					self.reduce_form1 += '-'
					self.reduce_form2 += '-'
					coef = -coef
				elif coef < 0:
					self.reduce_form1 += ' - '
					self.reduce_form2 += ' - '
					coef = -coef
				elif power > 0:
					self.reduce_form1 += " + "
					self.reduce_form2 += " + "
				coef = self.preprocess_coef(coef)
				self.reduce_form1 += f'{coef} * X^{int(power)}'
				if power == 0:
					self.reduce_form2 += f'{coef}'
				elif power == 1:
					self.reduce_form2 += f'{coef} * X'
				else:
					self.reduce_form2 += f'{coef} * X^{int(power)}'
		else:
			self.reduce_form1 += "0"
			self.reduce_form2 += "0"
		self.reduce_form1 += " = 0"
		self.reduce_form2 += " = 0"
		print("Reduced form 1:", self.reduce_form1)
		print("Reduced form 2:", self.reduce_form2)

		regex = re.compile("(%s)" % "|".join(map(re.escape, MAPP.keys())))
		self.reduce_form3 = regex.sub(lambda mo: MAPP[mo.string[mo.start():mo.end()]], self.reduce_form2)
		print("Reduced form 3:", self.reduce_form3)

		print("Polynomial degree:", self.degree)

	@staticmethod
	def preprocess_coef(coef: float):
		coef_int = int(coef)
		if coef - coef_int == 0.0:
			coef = coef_int
		return str(coef)
