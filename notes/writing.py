
with open("notes/reading.txt", 'w') as file:
    file.write("stop")

print("Code end")

with open("notes/writing.txt", 'a') as file:
    file.write("\nThis is more on my file!")

print("Code end")


import csv

with open("notes/Class CSV sample - Sheet1.csv", 'r+', newline='') as csvfile:
    fieldnames = ['username', 'color']
    reader = csv.reader(csvfile)
    for line in reader:
        print(f'{fieldnames[0]}, {line[0]}, favorite color {line[1]}')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #writer.writeheader()
    writer.writerow({'username': 'aUser', 
                     'color': 'pink'})
    writer.writerow({'username': 'aUser2', 
                     'color': 'darkpink'})
    writer.writerow({'username': 'aUser3', 
                     'color': 'darkerpink'})
    writer.writerow({'username': 'aUser4', 
                     'color': 'darkestpink'})
    writer.writerow({'username': 'aUser5', 
                     'color': 'notevenpinkanymore'})
    writer.writerow({'username': 'aUser6', 
                     'color': 'blackpink'})
    writer.writerow({'username': 'aUser7', 
                     'color': 'literallyjustblack'})


print("Code is done")