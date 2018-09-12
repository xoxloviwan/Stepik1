import json


def fnd_parent(parent, son):
    if son not in family.keys():
        return False
    if parent == son or parent in family.get(son):
        return True
    for sub in family.get(son):
        res = fnd_parent(parent, sub)
        if res:
            return res
    return False

data = json.loads(input())
print(data)
family = dict()
for dct in data:
    if dct['parents']:
        family.update({dct['name']: dct['parents']})
    else:
        family.update({dct['name']: ['Godfather']})
print(family)
parents_dict = dict()
for par in family.keys():
    cnt = 0
    for son in family.keys():
        if fnd_parent(par, son):
            cnt += 1
    parents_dict.update({par: cnt})
lst = list()
for cls in parents_dict.keys():
    lst.append(cls)
lst.sort()
for cls in lst:
    print(cls, ':', parents_dict[cls])
