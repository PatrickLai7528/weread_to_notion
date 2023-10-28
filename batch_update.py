# encoding:utf-8
from notion_client import Client
import json 
from datetime import datetime, date

if __name__ == '__main__':
    database_id = '065ab6d8c797439b98b89c3e85ae8aae'
    notion_token = 'secret_PhRDDpaaWlGpq5Rov1ZFPXzmAow6PTRIXqIPVYMawXi'

    client = Client(auth=notion_token)

    filter = {
        "and": [
            {
                "property": "日期",
                "date": {
                    "on_or_after": "2023-05-01"
                }
            },
            {
                "property": "日期",
                "date": {
                    "on_or_before": "2023-05-31"
                }
            }
        ]
    }

    response = client.databases.query(database_id=database_id, filter=filter)
    all_results = response.get('results')[:]

    next_cursor = response.get("next_cursor")


    while next_cursor:
        print(next_cursor)
        print({
            **filter,
            "start_cursor": next_cursor
        })
        response = client.databases.query(database_id=database_id, filter=filter, start_cursor=next_cursor)

        all_results.extend(response.get('results'))
        if response.get("has_more"):
            next_cursor = response.get("next_cursor");
        else:
            next_cursor = None

    print(all_results)
    counter = 0

    for entry in all_results:

        # has_quaters = len(entry.get('properties').get('Quarters')['relation']) > 0
        # has_months = len(entry.get('properties').get('Months')['relation']) > 0
        # has_weeks = len(entry.get('properties').get('Weeks')['relation']) > 0

        # if has_quaters and has_months and has_weeks:
        #     counter += 1
        #     print(counter, "skip", entry.get("id"))
        #     continue

        weeks = [
            '97efed5e-cda9-49ca-9062-a02d19f9bf66',
            '8431176e-6356-49c9-a5a6-d2e42957748a',
            'f2ae8265-69c1-4bbe-beb1-c0cce85dba1a',
            '5940d692-e9e8-41f6-af20-dc83b200fc6e',
            '40d5fcd0-200e-4e64-a3bc-58cf2494096d'
        ]

        date = datetime.strptime(entry.get('properties')["日期"]['date']['start'], '%Y-%m-%d')
        week_id = None

        if date <= datetime(2023, 5, 5):
            week_id = weeks[0]
        elif date <= datetime(2023, 5, 12):
            week_id = weeks[1]
        elif date <= datetime(2023, 5, 19):
            week_id = weeks[2]
        elif date <= datetime(2023, 5, 26):
            week_id = weeks[3]
        else:
            week_id = weeks[4]

        if len(entry.get('properties').get("Daily Tracking")['relation']) > 0:
            daily_tracking_filter = {
                'and': [
                    {
                        "property": "Date",
                        'date': {
                            'equals': date.isoformat()
                        }
                    }
                ]
            }
            daily_tracking_page = client.databases.query(database_id='0347ce5b6cac42c99b9c4b7c97a4f762', filter=daily_tracking_filter)
            print(daily_tracking_page is None)

        # properties = {
        #     "Quarters": {
        #         "relation": [
        #             {
        #                 'id': "831fab5d-36b7-475d-96aa-0ad8f7f95de1"
        #             }
        #         ]
        #     },
        #     "Months": {
        #         "relation": [
        #             {
        #                 "id": "453d8d9b-77ef-4566-9a67-070e15ff5e94"
        #             }
        #         ]
        #     },
        #     "Weeks": {
        #         'relation': [
        #             {
        #                 "id": week_id
        #             }
        #         ]
        #     }
        # }
        # response = client.pages.update(page_id=entry.get('id'), properties=properties)
        # print(counter, 'updated',entry.get("id"))
        # counter += 1