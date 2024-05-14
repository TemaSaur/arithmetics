import random


def get_random_base():
	return random.randint(2, 10)


SIGN = {
	True: '',
	False: '-'
}

def to_base(x, b):
	result = []
	sign = x >= 0
	x = abs(x)
	while x > 0:
		result.append(str(x % b))
		x = x // b
	return SIGN[sign] + ''.join(reversed(result))


def get_random_number(base):
	length = random.randint(1, 3)
	options = list(range(base))
	digits = [str(random.choice(options)) for _ in range(length)]

	number = ''.join(digits).lstrip('0')
	sign = random.choice(['', '-'])
	return (sign + number) if number else '0'


def get_problem():
	base1 = get_random_base()
	number1 = get_random_number(base1)

	actual_number1 = int(str(number1), base1)

	base2 = get_random_base()
	number2 = get_random_number(base2)

	actual_number2 = int(str(number2), base2)

	return (
		f'({number1})<sub>{base1}</sub> + ({number2})<sub>{base2}</sub> =',
		actual_number1 + actual_number2
	)


class Answer:
	def __init__(self, number, answer, actual_answer, result):
		self.number = number
		self.answer = answer
		self.actual_answer = actual_answer
		self.result = result

	def to_dict(self):
		return {
			'number': self.number,
			'answer': self.answer,
			'actual_answer': self.actual_answer,
			'result': int(self.result)
		}


class User:
	def __init__(self, name, tries):
		self.name = name
		self.tries = int(tries)
		self.problem, self.answer = get_problem()

		self.user_answers = []

		self.answer_base = get_random_base()
		self.counter = 0

	def check_answer(self, answer):
		actual_answer = to_base(self.answer, self.answer_base)
		self.counter += 1
		self.user_answers.append(
			Answer(
				self.counter,
				answer,
				actual_answer,
				answer == actual_answer
			)
		)
		return answer == actual_answer

	def get_results(self):
		for answer in self.user_answers:
			yield answer.to_dict()

	def done(self):
		return self.counter >= self.tries