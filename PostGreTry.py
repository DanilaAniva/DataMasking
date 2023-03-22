import csv

from peewee import *
from secrets import *
from csv import *

def main():
    with open(r'C:\Users\ktota\Desktop\PostGreTry\PeopleData.csv') as f:
        order = ['Name', 'Gender', 'Country', 'Age of death']
        reader = csv.DictReader(f, fieldnames=order)
        for row in reader:
            print(row)
main()