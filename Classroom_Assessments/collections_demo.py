'''from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0) # Add to left
dq.append(4) # Add to right
print(dq)
dq.pop() # Remove from right
dq.popleft()'''

'''from collections import Counter
data = ['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C']
counter = Counter(data)
print(counter)
print(counter.most_common(2))
print(list(counter.elements()))'''

'''from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
print(od)'''

'''from collections import defaultdict
dd = defaultdict(int) # Default value is 0
dd['a'] += 1
print(dd['a'])
print(dd['b'])'''

from collections import ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
cm = ChainMap(dict1, dict2)
print(cm)
print(cm['b'])