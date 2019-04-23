import json

result = 'from fsm import *\n' + 'def contain(s1, s2):\n' + '\treturn (s1 in s2)\n' + 'def equal(x1, x2):\n' + '\treturn x1 == x2\n'
main_part = ''
initial_state_part = ''
declaration_part = ''
transitions = []
transitions_part = ''
middle_part = ''

f = open("json.json", 'r')
input = json.load(f)

def DeclareVariable(dict_variable, num_tab):
    declare = ""
    for key in dict_variable:
        right_part = dict_variable[key]
        if isinstance(dict_variable[key], unicode):
            right_part = "'" + right_part + "'"
        cur_declare_variable = ''
        for i in range(num_tab):
            cur_declare_variable += '\t'
        cur_declare_variable = cur_declare_variable + 'self.' + str(key) + ' = ' + str(right_part) + '\n'
        declare += cur_declare_variable
    return declare

def logic_analyzing(begin_str, logic, num_tab):
    condition_str = ''
    for i in range(num_tab):
        condition_str += '\t'
    condition_str += begin_str
    list_condition = logic["condition"]
    k = 0
    for dict_condition in list_condition:
        for key in dict_condition:
            cur_condition_str = ''
            k += 1
            if k != 1:
                cur_condition_str += ' and '
            else:
                cur_condition_str += ' '
            if key == 'contain':
                cur_condition_str += 'contain(\''+dict_condition[key]+'\', message)'
            elif key == 'equal':
                cur_condition_str += 'equal'+dict_condition[key]
            condition_str += cur_condition_str
    condition_str += ":\n"
    content_str = ''
    list_operation = logic["operation"]
    for dict_operation in list_operation:
        for key in dict_operation:
            if key == 'assign':
                for i in range(num_tab + 1):
                    content_str += '\t'
                tuple = dict_operation[key]
                assign_left = tuple[tuple.find('(') + 1:tuple.find(',')]
                assign_right = tuple[tuple.find(',') + 1:tuple.find(')')]
                content_str += assign_left+' = '+assign_right
                content_str += '\n'
    #output
    for i in range(num_tab + 1):
        content_str += '\t'
    content_str += 'print' + logic["output"] + '\n'
    #next_state
    for i in range(num_tab + 1):
        content_str += '\t'
    content_str += 'self.transition(to=\''+logic["nextState"]+'\', event=message)\n'
    return condition_str + content_str

general_environment = False
num_state = 0
for dict in input:

    if (not general_environment):
        general_environment = True
        task = dict["task"]
        dict_variable = dict["Variable"]
        declaration_part +=  '\tdef __init__(self, *args, **kwargs):\n\t\tsuper('+ str(dict["task"]) + ', self).__init__(*args, **kwargs)\n'
        declaration_part += DeclareVariable(dict_variable, 2)
        name = 'class ' + str(dict["task"]) + '(FiniteStateMachine):\n'
        result += name
        main_part += ('dm = ' + str(dict["task"]) + '()\n')
        main_part += 'f = open("input.txt", "r")\nfor line in f:\n\tinput_line = line[:-1]\n\tdm.on_message(input_line)\n'
        middle_part += '\tdef on_message(self, message):\n\t\tprint(self.__state__)\n'
    else:
        num_state += 1
        small_part = ''
        cur_type = dict["type"]
        cur_state = dict["name"]
        if cur_type == 'atom-start':
            initial_state_part = '\tinitial_state = \'' + cur_state + '\'\n'
        logics = dict["logic"]
        num_logics = len(logics)
        for i in range(num_logics):
            small_dict = logics[i]
            next_state = small_dict["nextState"]
            transitions.append((cur_state, next_state))
            if i == 0:
                small_part += logic_analyzing('if', small_dict, 3)
            else:
                small_part += logic_analyzing('elif', small_dict, 3)
        if num_state == 1:
            middle_part += '\t\tif self.__state__ == \'' + cur_state + '\':\n'
        else:
            middle_part += '\t\telif self.__state__ == \'' + cur_state + '\':\n'
        if small_part == '':
            small_part = '\t\t\tpass\n'
        middle_part += small_part

    # print(dict)

transitions = set(transitions)
transitions_part += '\ttransitions = [\n'
k = len(transitions)
mk = 0
for (xx, yy) in transitions:
    transitions_part += '\t(\''+xx+'\', \''+yy+'\')'
    mk += 1
    if mk != k:
        transitions_part += ','
    transitions_part +='\n'
transitions_part += '\t]\n'

result += initial_state_part
result += transitions_part
result += declaration_part
result += middle_part
result += main_part
f = open("result.py", "w")
f.write(result)