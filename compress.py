import sys,getopt,os

def compressFile(file:str):
    with open(file,'r+') as f:
        final = ''
        for line in f.readlines():
            if line != '\n':
                addLine = False
                newLine = ''
                inString = False
                for char in line:
                    if char == '\'' or char == '"':
                        if inString:
                            inString = False
                        else:
                            inString = True
                            
                    if char == "#" and not inString:
                        newLine = newLine.rstrip()
                        newLine += '\n'
                        break
                    elif char not in ' \n':
                        addLine = True
                    newLine += char
                if addLine:
                    newLine = newLine.rstrip()
                    final+=newLine+'\n'
        f.seek(0)
        f.write(final.strip())
        f.truncate()

def greatFilter(items):
    for item in items:
        if '.' in item:
            compressFile(item)
        else:
            greatFilter(sorted([os.path.join(item,file) for file in os.listdir(item)], key=os.path.getctime))

options,args = getopt.getopt(sys.argv[1:],"s:t:h")

greatFilter(args)