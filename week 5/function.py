import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


# 2
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

/3
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


# 4
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

# 5
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# 6
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

# 7
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# 8
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
