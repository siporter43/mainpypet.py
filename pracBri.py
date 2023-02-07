
def sean_func(variable):
    return variable

output = sean_func(5)

print(f"first output: {output}")



def sean_func(text, variable=10):
    return text, variable

text1 = "hi sean"

output = sean_func(text1)
print(f"second output: {output}")
output = sean_func(text1, 8)
print(f"third output: {output}")
