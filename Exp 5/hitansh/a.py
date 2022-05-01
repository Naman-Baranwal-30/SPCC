KEYWORDS = ["and","bool","break","case","char","continue","do","double","else","false","float","for","if","int","long","namespace","not","or","public","return","sizeof","static","switch","true","try","using","void","while"]

PREPROCESSORS = ['#define', '#include', '#if', '#else', '#elif', '#endif']

SYMBOLS = ['=', '+=', '/=', '*=', '-=', '==', '!=', '<', '<=', '>', '>=', '&', '&', '&&', '|', '||', '!', '>>', '>>>', '<<', '<<<' ,  ';', '{', '}', '[', ']', '(', ')']

# header files
# identifires
# keywords
# symbol
# preprocessor
# comments

code = []

with open('a.cpp') as f:
    code = f.readlines()

inlineComment = False
blockComment = False

output = []
for line in code:
    for word in line.split():
        if word == '//':
            break
        if word in KEYWORDS:
            output.append([word, "KEYWORD"])
        elif word in SYMBOLS:
            output.append([word, "SYMBOL"])
        elif word in PREPROCESSORS:
            output.append([word, "PREPROCESSOR"])
        elif word.isdigit():
            output.append([word, "CONSTANT"])
        elif word[0] == '<' and word[-1] == '>':
            output.append([word, "FILE DIRECTIVE"])
        elif word[0] == '"':
            output.append([word])
        else:
            output.append([word, "IDENTIFIER"]) 

for i in output:
    for j in i:
        print(j, end=" ")
    print()
    