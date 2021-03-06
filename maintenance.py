#!/usr/bin/env python

import requests
import json

# Update to match your API key
API_KEY = '2XzFnenkzU4SsWKbc-os'

# Update to match your email address
EMAIL = 'hk.satyawali@gmail.com'
TIME_ZONE = 'UTC'
# set the delay and duration of maintenance windows
maintenance_start_delay_in_minutes = 0
maintenance_duration_in_minutes = 10

# This gets the timezone of your local server - for UTC, use datetime.datetime.utcnow()
import datetime
current_time = datetime.datetime.utcnow()
start_time = str(current_time + datetime.timedelta(minutes = maintenance_start_delay_in_minutes))
end_time = str(current_time + datetime.timedelta(minutes = maintenance_start_delay_in_minutes + maintenance_duration_in_minutes))

# You can also specify a start or end date here instead (Date format: '2018-09-30T14:00:00')
start = start_time
end = end_time
START_TIME = (start[0:10] + 'T' + start[11:19])
END_TIME = (end[0:10] + 'T' + end[11:19])
DESCRIPTION = 'Enter your maintenance window description here'
SERVICES = [{
    'id': 'P436PNG',
    'type': 'service_reference'
}]
TEAMS = []
TYPE = 'maintenance_window'


	with open('TZ.txt') as file1:
	data = json.load(file)
        SERVICES = []
        return SERVICES
    #print(r.json())
    #data = json.loads(r.text)
    total_services = data['total']
    print('Creating maintenance window on {total_services} services...'.format(total_services=total_services))
    SERVICES = data['services']
    return SERVICES
def create_maintenance_window():
    url = 'https://sapient-3.pagerduty.com/api/v1/maintenance_windows'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY),
        'Content-type': 'application/json',
        'From': EMAIL
    }
    payload = {
        'maintenance_window': {
            'start_time': START_TIME,
            'end_time': END_TIME,
            'description': DESCRIPTION,
            'services': SERVICES,
            'teams': TEAMS,
            'type': TYPE
        }
    }
  r = requests.post(url, headers=headers, data=json.dumps(payload))
    print('\tStatus code: {code}'.format(code=str(r.status_code)))
    if r.status_code >= 200 and r.status_code < 204:
        print("Maintenance window successfully created:")
        print("\tStart: ", START_TIME)
        print("\tEnd: ", END_TIME)
        print("\tServices: ")
        for service in range(int(len(SERVICES))):
            print("\t\t", SERVICES[service]['id'])
    else:
        print("\tThere was an error creating this maintenance window.")
        print("\tPlease ensure that the login email and v2 REST API key in this script have proper permissions")

if __name__ == '__main__':
    create_maintenance_window()
