fieldnames = ['username', 'color']
    reader = csv.reader(csvfile)
    for line in reader:
        print(f'{fieldnames[0]}, {line[0]}, favorite color {line[1]}')