import time
import datetime
from datetime import timezone
from zoneinfo import ZoneInfo
#Make a function to check the word amount in a file, and then use a more basic
def word_time_checker(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        #Use split to count the amount of words using whitespace
        word_count = len(content.split())
        zone_info = ZoneInfo('US/Mountain')
        current_time = datetime.datetime.now(zone_info)
        #using datetime print out the day, weekday, month, year, hour, and minute
        date_formatted = current_time.strftime("%d, %A, %B %Y, at %I:%M %p")
        print(f"Word count: {word_count}\nDate: {date_formatted}")
        return word_count, date_formatted
word_time_checker("word counter project/file.txt")