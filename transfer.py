import json

f = open("json.json", 'r')
input = json.load(f)

general_environment = False
for dict in input:

    if (not general_environment):
        general_environment = True
        task = dict["task"]
        dict_variable = dict["Variable"]
        print("task = ", task)
        print("dict_variable = ", dict_variable)
    else:
        pass

    print(dict)

