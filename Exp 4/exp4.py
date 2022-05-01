import pandas as pd
import copy as cp

asm = {'.MODEL':[], '.STACK':[], '.DATA':[], '.CODE':[], '.STARTUP':[]}
with open("exp4.asm", 'r') as f:
    for line in f:
        temp = list(line.rstrip().split())
        if temp[0] in asm.keys(): key = temp[0]; continue
        asm[key].append(temp)
# print(asm)

mdt = {'Index':[], 'Card':[]}; mdtc = 1
mnt = {'Index':[], 'Macro Name':[], 'MDT Pointer':[]}; mntc = 1
ala = {}

flag = 0
for l in asm['.CODE']:
    if l[0] == 'MACRO':
        mnt['Index'].append(mntc)
        mnt['Macro Name'].append(l[1])
        mnt['MDT Pointer'].append(mdtc)
        ala[mntc] = list(l[2].split(','))
        mntc+=1; continue
    mdt['Index'].append(mdtc)
    if l[0] != 'ENDM':
        args = list(l[1].split(','))
        for arg in cp.deepcopy(args):
            if arg in ala[mntc-1]:
                x = args.index(arg); args.remove(arg)
                args.insert(x, f'#{ala[mntc-1].index(arg)+1}')
        mdt['Card'].append(' '.join([l[0], ','.join(args)]))
        mdtc+=1
    else:
        mdt['Card'].append(' '.join(l))
        mdtc+=1

print('MNT: ', pd.DataFrame(mnt).to_string(index=False), sep='\n')
for i, name in enumerate(mnt['Macro Name'],1):
    print(f"\nALA for Macro '{name}':",pd.DataFrame(ala[i], \
        index=range(1,len(ala[i])+1), columns=['Args']), sep='\n')
print('\nMDT: ',pd.DataFrame(mdt).to_string(index=False), sep='\n')

pass1_op = []
fg = 1
with open("exp4.asm", 'r') as f:
    for line in f:
        if '.STARTUP' == line.rstrip().split()[0]: fg = 1
        if '.CODE' == line.rstrip().split()[0]:
            pass1_op.append('.CODE\n'); fg = 0
        if fg: pass1_op.append(line)

pass1_op = ''.join(pass1_op)
# print('\nPass1 Output:', pass1_op, sep='\n')
print('-'*100)
with open('pass1_op.asm', 'w') as f:
    f.write(pass1_op)

asm2 = {'.MODEL':[], '.STACK':[], '.DATA':[], '.CODE':[], '.STARTUP':[]}
raw2 = []
with open('pass1_op.asm', 'r') as f:
    for line in f:
        raw2.append(line)
        temp = list(line.rstrip().split())
        if temp[0] in asm2.keys(): key = temp[0]; continue
        asm2[key].append(temp)
# print(asm2)
pass2_im = []
for z,l in enumerate(cp.deepcopy(asm2['.STARTUP'])):
    if l[0] in mnt['Macro Name']:
        subs = {}
        temp_exp = list()
        mi = mnt['Index'][mnt['Macro Name'].index(l[0])]
        mdtc = mnt['MDT Pointer'][mi-1]
        for c, arg in enumerate(l[1].split(','), 1):
            subs[f'#{c}'] = arg
        # print(subs)
        while mdt['Card'][mdtc-1] != 'ENDM':
            if '#' in mdt['Card'][mdtc-1]:
                temp = list(mdt['Card'][mdtc-1].split())
                temp[1] = list(temp[1].split(','))
                for c,i in enumerate(cp.deepcopy(temp[1])):
                    if '#' in i:
                        temp[1][c] = subs[i]
                temp[1] = ','.join(temp[1])
                temp_exp.append(' '.join(temp))
            else: temp_exp.append(mdt['Card'][mdtc-1])
            mdtc+=1
        pass2_im.append(temp_exp)
# print(pass2_im)

# print(raw2)
pass2_op = []
pass2c = 0
for l in raw2:
    temp = l
    if temp.rstrip().split()[0] in mnt['Macro Name']:
        temp = '\n'.join(pass2_im[pass2c])+'\n'; pass2c+=1
    pass2_op.append(temp)
# print(pass2_op)
pass2_op = ''.join(pass2_op)
# print('\nPass 2 Output: ' , pass2_op, sep='\n')

with open('pass2_op.asm', 'w') as f:
    f.write(pass2_op)
