import time
import datetime
#Make a function to check the word amount in a file, and then use a more basic
def word_time_checker(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        word_count = len(file.split())
        current_time = datetime.now()
        #using datetime print out the day, weekday, month, year, hour, and minute
        date_formatted = current_time.strftime("%d, %A, %B %Y, at %I:%M %p")
        print(f"Word count: {word_count}\n")