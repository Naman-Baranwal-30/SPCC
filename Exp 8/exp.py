def cg(code):              #code = ['A=B+C', 'B=A-D', 'C=B+C', 'D=B']
    c=code[0]         #c = 'A=B+C'
    d={}                    #d = {'A':'R1', 'B':'R1', 'C':'R1', 'D':'R1'}
    c1=c.split("=")   #c1 = ['A','B+C']
    op={'+':'ADD','-':'SUB'}
    j=1
    curr_operator=""

    for i in c1[1]:       #'B+C'
        if i in op.keys():
            curr_operator=i
            continue
        print("MOV"+ " " + "R"+str(j) + "," + i)
        j=j+1
    print(op[curr_operator]+" "+"R1"+","+"R2")
    d[c1[0]]="R1"

    for w in code[1:]:
        r=[]
        r=w.split("=")
        if len(r[1])==1:
            print("MOV"+" "+r[1]+","+d[r[1]])
        else:
          for t in r[1]:
            if(t in op.keys()):
                curr_operator=t
                continue
            if(t in d.keys()):
                if(r[1].index(t)==0):
                  ind=2
                else:
                  ind=0
                print("MOV"+" "+" "+"R2"+","+r[1][ind])
                m=d[t]
          print(op[curr_operator]+" "+m+","+"R2")
        d[r[0]]="R1" 
code=[]
n=int(input("ENTER NUMBER OF LINES:"))
for y in range(n):
    cc=input('ENTER LINE:')
    code.append(cc)
cg(code)

# ENTER NUMBER OF LINES:4
# ENTER LINE:A=B+C
# ENTER LINE:B=A-D
# ENTER LINE:C=B+C
# ENTER LINE:D=B


