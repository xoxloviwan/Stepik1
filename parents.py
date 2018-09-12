n = int(input())
family = dict()
for i in range(n):
    text = input()
    if ':' in text:
        name, parents = text.split(' : ')
        parents = list(parents.split())
    else:
        name = text.strip()
        parents = ['Godfather']
    family.update({name: parents})
# print(family)

def fnd_parent(parent, son):
    if son not in family.keys():
        return 'No' 
    if (parent == son or
    	parent in family.get(son) ):
        return 'Yes'
    for sub in family.get(son):
        res = fnd_parent(parent, sub)
        if res == 'Yes':
            return res
    return 'No'
    
           
q = int(input())
for i in range(q):
    parent, name = input().split()
    # A D
    #print(parent, name)
    res = fnd_parent(parent, name)
    
         
    print(res)
# print(family)

#{'A': ['Godfather'], 'C': ['A'], 'B': ['A'], 'D': ['B', 'C']}
