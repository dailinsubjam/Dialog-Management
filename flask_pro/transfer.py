import json
from tool import *



def DeclareVariable(dict_variable, num_tab):
    declare = ""
    for key in dict_variable:
        right_part = dict_variable[key]
        # if isinstance(dict_variable[key], unicode):
        if isinstance(dict_variable[key], str):
            right_part = right_part
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
    if logic["condition"] == "":
        condition_str += ' True'
    else:
        condition_str += ' ' + logic["condition"]
    condition_str += ":\n"
    content_str = ''
    str_operation = normalize(num_tab + 1, logic["operation"])
    # for i in range(num_tab + 1):
    #     content_str += '\t'
    content_str += str_operation + '\n'
    '''
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
    '''
    #output
    
    #TODO
    # output_str = logic["output"]
    # swap_position = re.finditer('\'', output_str)
    
    #next_state
    for i in range(num_tab + 1):
        content_str += '\t'
    content_str += 'self.transition(to=\''+logic["nextState"]+'\', event=message)\n'
    for i in range(num_tab + 1):
        content_str += '\t'
    content_str += "return " + logic['output'] + "\n"
    return condition_str + content_str



def Compile():
    result = 'from fsm import *\nfrom tool import *\n'
    main_part = ''
    initial_state_part = ''
    declaration_part = ''
    transitions = []
    transitions_part = ''
    middle_part = ''

    f = open("mid_result.json", 'r')
    input = json.load(f)


    general_environment = False
    num_state = 0
    for dict in input:

        if (not general_environment):
            general_environment = True
            task = 'TASK'
            dict_variable = dict["Variable"]
            declaration_part +=  '\tdef __init__(self, *args, **kwargs):\n\t\tsuper('+ task + ', self).__init__(*args, **kwargs)\n'
            declaration_part += DeclareVariable(dict_variable, 2)
            name = 'class ' + task + '(FiniteStateMachine):\n'
            result += name
            main_part += ('dm = ' + task + '()\n')
            main_part += 'def reply(IN):\n\treturn dm.on_message(IN)\n'
            middle_part += '\tdef on_message(self, message):\n\t\tintent,slot = parse(message)\n'
        else:
            num_state += 1
            small_part = ''
            cur_type = dict["type"]
            cur_state = dict["name"]
            cur_id = dict["ID"]
            if cur_type == 'Start':
                initial_state_part = '\tinitial_state = \'' + str(cur_id) + '\'\n'
            logics = dict["logic"]
            num_logics = len(logics)
            for i in range(num_logics):
                small_dict = logics[i]
                next_state = small_dict["nextState"]
                transitions.append((str(cur_id), next_state))
                if i == 0:
                    small_part += logic_analyzing('if', small_dict, 3)
                else:
                    small_part += logic_analyzing('elif', small_dict, 3)
            if num_state == 1:
                middle_part += '\t\tif self.__state__ == \'' + str(cur_id) + '\':\n'
            else:
                middle_part += '\t\telif self.__state__ == \'' + str(cur_id) + '\':\n'
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


