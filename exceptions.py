import sys
sys.stdin = open("C:/Users/xoxlo/Desktop/tester.txt",'r')
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
#print(family)

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
excepts = [input().strip() for i in range(q)]
#print(excepts)
last_ex = ''
for i in range(q):
    son = excepts[i]
    #print('i=',i,sep='')
    t = i
    for t1 in range(t):
        #print('t1=', t1, sep='')
        parent = excepts[t1]
        #print(parent,'!current')
        if fnd_parent(parent, son) == 'Yes' and parent != son and last_ex != son:
            print(son)
            last_ex = son

