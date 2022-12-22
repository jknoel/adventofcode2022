import numpy as np

# recursive function to solve for the monkey's value!
def getValue(dic: dict, monkey: str) -> float:
    if not dic[monkey]['known']:
        first = getValue(dic,dic[monkey]['monkey1'])
        second = getValue(dic,dic[monkey]['monkey2'])
        if dic[monkey]['operation'] == '+':
            return first+second
        elif dic[monkey]['operation'] == '-':
            return first-second
        elif dic[monkey]['operation'] == '/':
            return first/second
        elif dic[monkey]['operation'] == '*':
            return first*second
        else:
            raise Exception(f"bad operation! {dic[monkey]['operation']}")
    else:
        return dic[monkey]['value']

dic = {}
with open("input") as file:
    for line in file:
        data = line.strip().replace(':','').split(' ')
        if len(data) < 3:
            dic[data[0]] = {'known': True, 'value': float(data[1])}
        else:
            dic[data[0]] = {'known': False, 'value': None, 'monkey1': data[1], 'monkey2': data[3], 'operation': data[2]}

print(int(getValue(dic,'root')))
