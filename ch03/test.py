i = input()
j = input()
def is_integer(n):
    if n[0] == ('-', '+'):
        return n[1:].isdigit()
    else:
        return n.isdigit()
        
def add(a, b):
    if is_integer(a) == True and is_integer(b) == True:
        n = int(a) + int(b)
    else:
        n = a + b
    return n
print(add(i,j))