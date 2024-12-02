# Werken met queue
from queue import Queue # hoofdletter!
q = Queue(maxsize=4)
print("Aantal elementen: ", q.qsize())
q.put("a")
q.put("b")
q.put("c")
q.put_nowait("d")
# q.put_nowait("d") # element teveel
print("Type: ", type(q))
for item in q.queue:
    print(item)
print("Queue getoond")
print(q.get(2)) # Index geven heeft geen zin
print(q.get())
print(q.get())

# Werken met LIFO-queue
from queue import LifoQueue # hoofdletters!
Max_size = 4
lq = LifoQueue(maxsize=Max_size)
print("Aantal elementen: ", lq.qsize())
lq.put("a")
lq.put("b")
lq.put("c")
lq.put_nowait("d")
# q.put_nowait("d") # element teveel
print("Type: ", type(lq))
print("# elementen in LifoQueue :", lq.qsize())
for item in lq.queue:
    print(item)
print("Queue getoond")
print(lq.get(2)) # Index geven heeft geen zin
print(lq.get())
print(lq.get())




