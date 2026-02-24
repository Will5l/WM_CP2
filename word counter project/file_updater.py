#Make a function that edits the file content, and one that views it
def view_file(file):
    with open(file, 'r') as f:
        content = f.read()
        print(content)

def edit_file(file):
    with open(file, 'a') as f:
        print("Type what you want to add to the file, press enter twice in a row to exit and save changes.")
        lines = []
        while True:
            line = input()
            if line == '':
                if line == '' and lines[-1] == '\n':
                    lines.pop(-1)
                    x=0
                    while x<len(lines):
                        f.write(lines[x])
                        x+=1
                    return
                else:
                    lines.append(line+'\n')
            else:
                lines.append(line+'\n')