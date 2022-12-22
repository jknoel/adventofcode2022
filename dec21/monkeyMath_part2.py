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

# do bisection search for intersection of
# root[monkey1]-root[monkey2] and 0
low = 1 #our lower bound guess for the solution (if less than 1 will never find it)
dic['humn'] = {'known': True, 'value': low}
left = getValue(dic,dic['root']['monkey1'])
right = getValue(dic,dic['root']['monkey2'])
diff = left - right
lastdiff = diff
lastlow = low
exp = 1
while abs(diff) > 0.001:
    if np.sign(lastdiff) != np.sign(diff):
        exp = exp * 0.9
        low = lastlow
    else:
        lastlow = low
        low = 2**exp * low
    dic['humn'] = {'known': True, 'value': low}
    left = getValue(dic,dic['root']['monkey1'])
    right = getValue(dic,dic['root']['monkey2'])
    diff = left - right

print(low)