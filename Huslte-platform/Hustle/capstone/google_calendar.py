from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta

# Path to your credentials JSON file
CREDENTIALS_FILE = "capstone/google_credentials.json"

def get_google_calendar_service():
    """Authenticate with Google Calendar API and return a service object."""
    creds = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE,
        scopes=["https://www.googleapis.com/auth/calendar"]
    )
    return build("calendar", "v3", credentials=creds)

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

    event = service.events().insert(calendarId="primary", body=event).execute()
    return event.get("htmlLink")
