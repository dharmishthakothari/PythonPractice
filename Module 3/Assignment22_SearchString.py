# W.A.P to search a word from the string using Search()  
import re
str = "This is first string program"
s=re.search('first',str)
print(f"String starts at {s.start()} and end at {s.end()}")