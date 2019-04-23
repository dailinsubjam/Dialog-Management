from fsm import *
def contain(s1, s2):
	return (s1 in s2)
def equal(x1, x2):
	return x1 == x2
class LightSwitch(FiniteStateMachine):
	initial_state = 'off'
	transitions = [
	('off', 'off'),
	('off', 'broken'),
	('on', 'broken'),
	('on', 'off'),
	('broken', 'broken'),
	('off', 'on'),
	('on', 'on')
	]
	def __init__(self, *args, **kwargs):
		super(LightSwitch, self).__init__(*args, **kwargs)
		self.electricity = True
		self.indicator = 'off'
	def on_message(self, message):
		print(self.__state__)
		if self.__state__ == 'off':
			if contain('turn on', message) and equal(self.electricity, True):
				self.indicator =  'lit'
				print 'The light is  ' + self.indicator
				self.transition(to='on', event=message)
			elif contain('turn off', message):
				self.indicator =  'dim'
				print 'The light is  ' + self.indicator
				self.transition(to='off', event=message)
			elif contain('broken', message):
				self.indicator =  'broken'
				self.electricity =  False
				print 'The light is  ' + self.indicator
				self.transition(to='broken', event=message)
		elif self.__state__ == 'on':
			if contain('turn on', message) and equal(self.electricity, True):
				self.indicator =  'lit'
				print 'The light is  ' + self.indicator
				self.transition(to='on', event=message)
			elif contain('turn off', message):
				self.indicator =  'dim'
				print 'The light is  ' + self.indicator
				self.transition(to='off', event=message)
			elif contain('broken', message):
				self.indicator =  'broken'
				self.electricity =  False
				print 'The light is  ' + self.indicator
				self.transition(to='broken', event=message)
		elif self.__state__ == 'broken':
			if contain('turn on', message):
				print 'The light is  ' + self.indicator
				self.transition(to='broken', event=message)
			elif contain('turn off', message):
				print 'The light is  ' + self.indicator
				self.transition(to='broken', event=message)
			elif contain('broken', message):
				self.indicator =  'broken'
				self.electricity =  False
				print 'The light is  ' + self.indicator
				self.transition(to='broken', event=message)
dm = LightSwitch()
f = open("input.txt", "r")
for line in f:
	input_line = line[:-1]
	dm.on_message(input_line)
