#import mysql.connector as connector

#mycursor = database.cursor()
from datetime import timedelta, datetime
from django.utils import timezone

def norm_time(datetimeobj):
    return datetimeobj.strftime(("%d/%m/%Y, %H:%M:%S"))

def norm(string):
    if ',' in string: # if time/date given manually then;
        task, timedetails = string.split(',')
        # in order to set dd/mm/year instead of stupid format.
        task, timedetails = task.strip(), timedetails.replace(',', '').strip()

        format = ["%d/%m/%y %H:%M:%S", "%d/%m/%y %H:%M:%S %p"]
        length = len(timedetails.split(' '))

        if length == 1:
            temporal = datetime.strptime(timedetails, format[0])

        else:
            temporal = datetime.strptime(timedetails, format[0])

    else: # default. set time/date split = 1;
        task = string
        temporal = str(timezone.now() + timedelta(days=1))


    return task.strip(), temporal


def filter_(list, element):
    return [item for item in list if item != element]

class clsmemory:
    def __init__(self):
        self.list = []
