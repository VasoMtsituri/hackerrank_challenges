import re

line = input()
m = re.search(r"(\w(?!_))\\1+", line)
print(m.group(1) if m else "-1")
