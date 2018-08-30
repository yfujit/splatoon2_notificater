import json
import os
import time
import datetime
import urllib.request
import sys
import requests

def format_message(data):
    data = json.loads(data)
    notify_data = {}
    now_datetime_str = datetime.datetime.now().strftime("%Y/%m/%d %H")
    now_datetime_formated = datetime.datetime.strptime(now_datetime_str,"%Y/%m/%d %H")
    start_time = int(time.mktime(now_datetime_formated.timetuple()))
    end_time = start_time - 7200 #2h unixtime
    print(datetime.datetime.fromtimestamp(start_time))

    for match_data in data['league']:
        if match_data['start_time'] == start_time:
            notify_data = match_data

    payload = {
        'username': 'Splatoon Stage Notificater',
        'icon_emoji': ':splatoon_icon:',
        'text': 'Splatoon Event Notification',
        'attachments': [
            {
                'fallback': 'Detailed information on Splatoon Stage.',
                'color': 'good',
                'title': 'Stage Information at Ranked Battle from {} to {}'.format(datetime.datetime.fromtimestamp(notify_data['start_time']+3600*9).strftime("%H:%M"), datetime.datetime.fromtimestamp(notify_data['end_time']+3600*9).strftime("%H:%M")),
                'fields': [
                    {
                        'title': 'Game Mode',
                        'value': notify_data['game_mode']['name'],
                        'short': False
                    },
                    {
                        'title': 'Rule',
                        'value': notify_data['rule']['name'],
                        'short': False
                    },
                    {
                        'title': 'Stage A',
                        'value': notify_data['stage_a']['name'],
                        'short': True
                    },
                    {
                        'title': 'Stage B',
                        'value': notify_data['stage_b']['name'],
                        'short': True
                    }
                ]
            }
        ]
    }
    return payload

def notify_slack(url, payload):
    data = json.dumps(payload).encode('utf-8')
    method = 'POST'
    headers = {'Content-Type': 'application/json'}

    request = urllib.request.Request(url, data = data, method = method, headers = headers)
    with urllib.request.urlopen(request) as response:
        return response.read().decode('utf-8')

def get_splatoon_information(url,iksm_session):
    cookies = dict(iksm_session=iksm_session)
    r = requests.get(url, cookies=cookies)
    if r.status_code == 200:
        return r.json()
    else:
        print(r.status_code)
        sys.exit(1)

def lambda_handler(event, context):
    webhook_url = os.environ['WEBHOOK_URL']
    iksm_session = os.environ['IKSM_SESSION']
    splatoon_information = get_splatoon_information("https://app.splatoon2.nintendo.net/api/schedules",iksm_session)
    payload = format_message(json.dumps(splatoon_information))
    response = notify_slack(webhook_url, payload)
    return response
