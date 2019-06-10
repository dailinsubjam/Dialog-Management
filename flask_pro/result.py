from fsm import *
from tool import *
class TASK(FiniteStateMachine):
	initial_state = '0'
	transitions = [
	('2', '3'),
	('1', '2'),
	('1', '3'),
	('0', '1'),
	('2', '4'),
	('1', '1')
	]
	def __init__(self, *args, **kwargs):
		super(TASK, self).__init__(*args, **kwargs)
		self.fruit_type = ''
		self.weight = 0
		self.unit_price = 0
		self.cnt = 0
	def on_message(self, message):
		intent,slot = parse(message)
		if self.__state__ == '0':
			if intent == 'buy' and 'fruit_type' in slot:
				

				self.transition(to='1', event=message)
				return 'Please show what fruit to buy.'
		elif self.__state__ == '1':
			if intent == 'buy' and 'fruit_type' in slot and 'weight' in slot and 'unit_price' in slot:
				self.fruit_type = slot['fruit_type']
				self.weight = slot['weight']
				self.unit_price = slot['unit_price']
				money = int(slot['unit_price']) * int(slot['weight'])

				self.transition(to='2', event=message)
				return 'This is your order: \n \n fruit: %s \n weight: %s \n unit_price: %s \n Total: %d \n Please pay.' %(slot['fruit_type'], slot['weight'], slot['unit_price'], money)
			elif self.cnt > 3:
				

				self.transition(to='3', event=message)
				return 'Too many times. Your order failed. Thanks for your application.'
			elif True:
				self.cnt += 1

				self.transition(to='1', event=message)
				return 'Wrong request.Please show your order again.'
		elif self.__state__ == '2':
			if intent == 'pay' and 'state' in slot and bool(slot['state']) == True:
				

				self.transition(to='4', event=message)
				return 'Successful! Thanks for your application.'
			elif True:
				

				self.transition(to='3', event=message)
				return 'No pay. Your order failed. Thanks for your application.'
dm = TASK()
def reply(IN):
	return dm.on_message(IN)
