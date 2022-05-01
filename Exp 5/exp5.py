keywords = ["int", "void", "float", "double", "char", "if", "else",
            "for", "while", "long", "return", "switch", "break", "continue"]
symbols = ["(", ")", "{", "}", "=", ",", ";", ":", "!=",
           "==", ">=", "<=", "<", ">", "+", "-", "*", "/", "%"]

fileObj = open("exp5.c", "r")
codeLines = fileObj.read().splitlines()
codeLines = list(map(str.strip, codeLines))

for codeLine in codeLines:
    tokenList1 = []
    if codeLine[0:2] == "//":
        continue
    elif codeLine[0:6] == "printf":
            tokenList1.append("printf")             
            tokenList1.append("(")
            tokenList1.append(codeLine[7:-2])
            tokenList1.append(")")
            tokenList1.append(";")
    else:    
        tokenList = codeLine.split(" ")
        for token in tokenList:
            if token[-1] == ";":
                splittedToken = token.split(";")[0]
                if splittedToken[-2:] == "()":
                    splittedToken2 = splittedToken.split("()")[0]
                    tokenList1.append(splittedToken2)
                    tokenList1.append("(")
                    tokenList1.append(")")
                else:
                    tokenList1.append(splittedToken)

                tokenList1.append(";")         
            else:
                tokenList1.append(token)

    for token in tokenList1:
        if token[0] == "#":
            print(token, "\tPreprocessor Directive")
        elif token[0] == "<" and len(token) > 1:
            print(token, "\tHeaderFile")
        elif token[0] == '"':
            msg = token[1:-1]
            msg = msg.replace("\\n","")
            msg = msg.replace("\\t","")
            print(msg, "\tMessage")
        elif token.isnumeric():
            print(token, "\tNumber")
        elif token in keywords:
            print(token, "\tKeyword")
        elif token in symbols:
            print(token, "\tSymbol")
        else:
            if token[-1] == ";":
                print(";", "\tSymbol")
            if len(token) > 2 and token[-2:] == "()":
                print(token[:-2], "\tIdentifier")
                print("(\tSymbol")
                print(")\tSymbol")
            else:
                print(token, "\tIndentifier")
