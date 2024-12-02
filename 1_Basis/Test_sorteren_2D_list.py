List = [["a","b"], ["c","d"], ["e", "f"]]
print(List)
sorted = sorted(List, key=lambda x: str(x[1]), reverse=True)
print(sorted)
print("")


List = [["a","b", "c"], ["d","e", "f"], ["g","h", "i"]]
print(List)
Sorted = sorted(List, key=lambda x: str(x[1]), reverse=True)
print(Sorted)
print("")
"""
List = [["a","a", "c"], ["c","h", "e"], ["e", "a", "h"]]
print(List)
Sorted = sorted(List, key=lambda x: str(x[1]), reverse=True)
print(Sorted)
"""
