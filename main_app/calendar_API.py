from decouple import config
from google.oauth2 import service_account
import googleapiclient.discovery
import datetime

CAL_ID = config('CAL_ID')
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = './google-credentials.json'


def test_calender():
    print("RUNNING TEST_CALENDAR()")

    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    # CREATE A NEW EVENT
    new_event = {
    'summary': "Demo Assignment",
    'location': 'India',
    'description': 'Internshala Assignment',
    'start': {
        'date': f"{datetime.date.today()}",
        'timeZone': 'America/New_York',
    },
    'end': {
        'date': f"{datetime.date.today() + datetime.timedelta(days=3)}",
        'timeZone': 'America/New_York',
    },
    }
    service.events().insert(calendarId=CAL_ID, body=new_event).execute()
    print('Event created')

 # GET ALL EXISTING EVENTS
    events_result = service.events().list(calendarId=CAL_ID, maxResults=2500).execute()
    events = events_result.get('items', [])

    # LOG THEM ALL OUT IN DEV TOOLS CONSOLE
    for e in events:

        print(e)




    return events

    
