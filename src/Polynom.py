from .Color import Color


class Polynom:
	def __init__(self, parser):
		self.degree = parser.degree
		self.pow_coef = parser.pow_coef
		self.answer = {}
		self.solve()
		self.print_answer()

	def solve(self):
		if self.degree > 2:
			raise BaseException(f"{Color.RED}ERROR: The polynomial degree is strictly greater than 2, I can't solve.{Color.END}")
		elif self.degree == 2:
			self.square_equation()
		elif self.degree == 1:
			self.simple_equation()
		else:
			self.not_equation()

	def square_equation(self):
		count_coefs = len(list(zip(*self.pow_coef))[1])
		if count_coefs == 3:
			c, b, a = list(zip(*self.pow_coef))[1]
			discriminant = b**2 - 4 * a * c
			if discriminant > 0:
				print("Discriminant is strictly positive, the two solutions are:")
				self.answer[0] = (-b + self._sqrt(discriminant)) / (2. * a)
				self.answer[1] = (-b - self._sqrt(discriminant)) / (2. * a)
			elif discriminant == 0:
				print("Discriminant is zero, the solutions is:")
				self.answer[0] = (-b + self._sqrt(discriminant)) / (2. * a)
			else:
				print(f"{Color.WARNING}Discriminant < 0: the two complex solutions are{Color.END}")
				b = -b / (2. * a)
				d = self._sqrt(-discriminant) / (2. * a)
				self.answer[0] = f'{b} + {d} * i'
				self.answer[1] = f'{b} - {d} * i'
		elif count_coefs == 2:
			if self.pow_coef[0][0] == 0:
				c, a = list(zip(*self.pow_coef))[1]
				if c > 0 and a > 0:
					print(f"{Color.WARNING}Complex solution{Color.END}")
					self.answer[0] = f'{self._sqrt(abs(-c/a))} * i'
					self.answer[1] = f'{-self._sqrt(abs(-c/a))} * i'
				elif c < 0 and a < 0:
					print(f"{Color.WARNING}Complex solution{Color.END}")
					self.answer[0] = f'{self._sqrt(abs(-c/a))} * i'
					self.answer[1] = f'{-self._sqrt(abs(-c/a))} * i'
				else:
					self.answer[0] = self._sqrt(-c/a)
					self.answer[1] = -self._sqrt(-c/a)
			else:
				b, a = list(zip(*self.pow_coef))[1]
				self.answer[0] = 0
				self.answer[1] = -b/a
		else:
			self.answer[0] = 0

	def simple_equation(self):
		if self.pow_coef[0][0] != 0.0:
			self.answer[0] = 0
			print("The solution is:")
		else:
			a, b = list(zip(*self.pow_coef))[1]
			self.answer[0] = -a / b
			print("The solution is:")

	def not_equation(self):
		if not self.pow_coef:
			raise BaseException(f"{Color.WARNING}Any real number is a solution{Color.END}")
		a = self.pow_coef[0][1]
		if a == 0:
			raise BaseException(f"{Color.WARNING}Any real number is a solution{Color.END}")
		else:
			raise BaseException(f"{Color.WARNING}No solutions{Color.END}")

	def print_answer(self):
		for key, answer in self.answer.items():
			print(f"{Color.GREEN}x{key+1}: {answer}{Color.END}")

	@staticmethod
	def _sqrt(num):
		res = 0
		inc = 1.0
		for _ in range(10):
			if res * res == num:
				return res
			while (res + inc) * (res + inc) <= num:
				res += inc
			inc /= 10
		return res
