from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta

<<<<<<< HEAD
# Path to your credentials JSON file
CREDENTIALS_FILE = "capstone/google_credentials.json"

def get_google_calendar_service():
    """Authenticate with Google Calendar API and return a service object."""
    creds = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE,
        scopes=["https://www.googleapis.com/auth/calendar"]
    )
    return build("calendar", "v3", credentials=creds)
=======
CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), '..', 'credentials.json')

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_google_calendar_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES, redirect_uri='http://localhost:8000/auth/google/callback/'
            )
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('calendar', 'v3', credentials=creds)
>>>>>>> 713f6a5628a791bc5df9044ccb476a7f1d877f22

def create_calendar_event(summary, description, start_time, end_time, attendees):
    """
    Create a Google Calendar event and return the event link.
    """
    service = get_google_calendar_service()

    event = {
        "summary": summary,
        "description": description,
        "start": {"dateTime": start_time, "timeZone": "UTC"},
        "end": {"dateTime": end_time, "timeZone": "UTC"},
        "attendees": [{"email": email} for email in attendees],
        "reminders": {
            "useDefault": False,
            "overrides": [
                {"method": "email", "minutes": 30},
                {"method": "popup", "minutes": 10},
            ],
        },
    }
<<<<<<< HEAD

    event = service.events().insert(calendarId="primary", body=event).execute()
    return event.get("htmlLink")
=======
    event = service.events().insert(calendarId='primary', body=event).execute()
    return event.get('htmlLink')
>>>>>>> 713f6a5628a791bc5df9044ccb476a7f1d877f22
