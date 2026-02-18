import csv


with open('/workspaces/WM_CP2/individual_projects/library.csv', mode = 'r') as csv_file:
            content = csv.reader(csv_file)
            headers = next(content)
            for line in content:
                print({headers[0]: line[0], headers[1]: line[1], headers[2]: line[2], headers[3]: line[3]})