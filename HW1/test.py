import util

a = util.PriorityQueue()

b = (1,2,3)
a.push(b, 0)
c,d,e,f = a.pop()
print(c,d,e)