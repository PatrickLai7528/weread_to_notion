# encoding:utf-8
from notion_client import Client
import json 
from datetime import timedelta, date

start_date = date(2022, 1, 1)
end_date = date(2022, 1, 7)

for i in range((end_date - start_date).days + 1):
    current_date = start_date + timedelta(days=i)
    print(current_date)

if __name__ == '__main__':
