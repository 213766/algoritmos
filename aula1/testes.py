import sys

print(sys.version)

# comentario de uma linha

"""
    COMENTARIO
    DE
    VARIAS
    LINHAS
"""

var1 = int(input("coloq um numero para var 1:"))
var2 = int(input("coloq um numero para var 2:"))

for _ in range(5):
    if var1 > var2:
        print("var1 maior")
        break
    else:
        print("var2 maior ou igual")
        var1 += 1