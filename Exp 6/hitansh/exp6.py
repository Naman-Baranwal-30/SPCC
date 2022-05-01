from rich.console import Console
from rich.table import Table
from rich import print as rprint
s = input()
Quadrupals = []
Pass = {0: ["*", "/"], 1: ["+", "-"]} 
temps = {}
passTemp = ""
tcount = 0
for p in range(2):
    idx = 0
    while idx < len(s):
        c = s[idx]
        if c in Pass[p]:
            temps[f"t{tcount}"] = s[idx-1:idx+2]
            passTemp = passTemp[:-1]
            passTemp += str(tcount)
            tcount += 1
            idx+=1
        else:
            passTemp += c
        idx += 1
    s = passTemp
for key, value in temps.items():
    arg1 = f"t{value[0]}" if value[0].isnumeric() else value[0]
    arg2 = f"t{value[2]}" if value[2].isnumeric() else value[2]
    Quadrupals.append((key[1:], value[1], arg1, arg2, key))
Quadrupals.append((str(len(Quadrupals)), "=", s.split("=")[0],"t"+str(len(Quadrupals)-1), " "))
table = Table(title="Quadrupals")
table.add_column("Index")
table.add_column("Operand")
table.add_column("Arg1")
table.add_column("Arg2")
table.add_column("Result")
for i in Quadrupals:
    table.add_row(*i)
    if i[1] == "=":
        rprint(f"{i[2]} {i[1]} {i[3]}")
    else:
        rprint(f"{i[-1]} = {i[2]} {i[1]} {i[3]}")
console = Console()
console.print(table)
table1 = Table(title="Triplate")
table1.add_column("Index")
table1.add_column("Operand")
table1.add_column("Arg1")
table1.add_column("Arg2")
for i in Quadrupals:
    table1.add_row(*i[:-1])
console.print(table1)

# a=b*c+d*c
