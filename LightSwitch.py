from fsm import *

class LightSwitch(FiniteStateMachine):
  # Initial state.
  # initial_state = 'off'

  # Possible transitions.
  transitions = [
    ('off', 'on'),
    ('on', 'off'),
    ('off', 'broken'),
    ('on', 'broken')
  ]

  # Initialize the FSM.
  def __init__(self, *args, **kwargs):
    super(LightSwitch, self).__init__(*args, **kwargs)
    self.electricity = True
    self.indicator = 'dim'

  # Handle incoming events.
  def on_message(self, message):
    print 'message =', message
    if message == 'turn on':
      self.transition(to = 'on', event = message)
    elif message == 'turn off':
      self.transition(to = 'off', event = message)
    elif message == 'break':
      self.transition(to = 'broken', event = message)
    print 'State =', self.__state__

  # Attach a guard to the FSM that protects transitions into
  # the on state. The guard is a predicate that returns True
  # or False based on the availability of electricity to the
  # socket.
  @Guard(state = 'on')
  def check_electricity(self):
    return self.electricity

  # Attach an action to the FSM that will execute anytime
  # the off state is entered.
  @Action(state = 'off')
  def turn_off(self, message):
    print "The light is",
    self.indicator = 'dim'
    print self.indicator + '.'

  # Attach an action to the FSM that will execute anytime
  # the on state is entered.
  @Action(state = 'on')
  def turn_on(self, message):
    print "The light is",
    self.indicator = 'lit'
    print self.indicator + '.'

  # Attach an action to the FSM that will execute anytime
  # the broken state is entered.
  @Action(state = 'broken')
  def smash(self, message):
    print "The light is",
    self.indicator = 'broken'
    self.electricity = False
    print self.indicator + '.'

# Instantiate an FSM and send it events to process.
light_switch = LightSwitch()
f = open("input.txt", "r")
for line in f:
  input_line = line[:-1]
  light_switch.on_message(input_line)
