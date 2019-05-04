from fsm import *
from SLU import *
class TASK(FiniteStateMachine):
	initial_state = '0'
	transitions = [
	('0', '1'),
	('1', '1'),
	('1', '2'),
	('2', '3')
	]
	def __init__(self, *args, **kwargs):
		super(TASK, self).__init__(*args, **kwargs)
		self.cnt = 0
		self.pay_state = False
	def on_message(self, message):
		slu = SLU()
		intent = slu.analyze(message)
		print message
		if self.__state__ == '0':
			if intent == 'buy fruit':
				buy_intent = intent
				print 'Please show your fruit information, including type, weight and unit price.'
				self.transition(to='1', event=message)
		elif self.__state__ == '1':
			if intent == 'pay':
				self.pay_state = True
				print 'Please pay.'
				self.transition(to='2', event=message)
			elif True:
				self.cnt += 1
				print 'Please input corretly.'
				self.transition(to='1', event=message)
		elif self.__state__ == '2':
			if self.pay_state == False:
				
				print 'Your order failed. Thanks for your application.'
				self.transition(to='3', event=message)
			elif self.pay_state == True:
				
				print 'Your order completed. Thanks for your application.'
				self.transition(to='3', event=message)
dm = TASK()
f = open("input.txt", "r")
for line in f:
	input_line = line[:-1]
	dm.on_message(input_line)
