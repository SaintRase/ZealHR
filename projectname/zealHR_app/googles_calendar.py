from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/calendar']

SERVICE_ACCOUNT_FILE = 'C:/Users/user-pc/Downloads/sapient-logic-379408-046b5e6749b4.json'

def create_calendar_event(event_title, start_time, end_time):
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('calendar', 'v3', credentials=credentials)

    event = {
        'summary': event_title,
        'start': {
            'dateTime': start_time,
            'timeZone': 'Africa/Johannesburg',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Africa/Johannesburg',
        },
    }

    try:
        event = service.events().insert(calendarId='zealhrfakecompany@gmail.com', body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))
        print(event['id'])
        return event.get('htmlLink')
    except HttpError as error:
        print('An error occurred: %s' % error)
        return None
