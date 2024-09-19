import re
string = "Hi my name is Fernando Subido, 18 yrs old, my passion is Playing Basketball and my position is shooting guard."
# Creating separate lists using
# the re.findal() method
uppercase_characters = re.findall(r"[A-Z", string)
lowercase_characters = re.findall(r"[a-z]", string)
special_characters = re.findall(r"[=,.]", string)
