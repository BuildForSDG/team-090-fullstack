""" This populates City table with cities.
"""
import csv
from fullstack.models import MyCity


def string_or_number(data):
    if len(data) > 0:
        return data
    else:
        return 0


def enter_data(data, count):

    MyCity.objects.create(
        id=count, city=data[0], city_ascii=data[1],
        latitude=float(data[2]),
        longitude=float(data[3]), country=data[4],
        iso2=data[5], iso3=data[6],
        admin_name=data[7], capital=data[8],
        population=float(string_or_number(data[9])),
        city_id=float(string_or_number(data[10])))
    print(data)
    print('Entered row: {}'.format(count))


with open('data/worldcities.csv', encoding='utf8') as f:
    res = csv.reader(f)
    res = list(res)
    count = 0
    for data in res[1:]:
        enter_data(data, count)
        count += 1
