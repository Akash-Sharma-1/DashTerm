import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import datetime

# If modifying these scopes, delete the file token.pickle.

CREDENTIALS_FILE = 'credentials.json'

def get_calendar_service():
    creds = None
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token-cal.pickle'):
        with open('token-cal.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token-cal.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service


def get_task_service():
    creds = None
    SCOPES = ['https://www.googleapis.com/auth/tasks']
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token-task.pickle'):
        with open('token-task.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token-task.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('tasks', 'v1', credentials=creds)
    return service

def get_keep_service():
    creds = None
    SCOPES = ['https://www.googleapis.com/auth/keep']
    
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token-keep.pickle'):
        with open('token-keep.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token-keep.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('keep', 'v1', credentials=creds)
    return service

def cal_events():
    returnString=""
    service = get_calendar_service()
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        return 'No upcoming events found.'
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        returnString += str(start) + " ," + str(event['summary']) + "\n"

    return returnString


def tasks_lists(option, taskIndex=0):
    service = get_task_service()
    # Call the Calendar API
    results = service.tasklists().list(maxResults=10).execute()
    items = results.get('items', [])

    if not items:
        return 'No task lists found.'

    if(option== "tasklists"):
        returnString="Task lists:" + "\n" 
        for item in items: 
            returnString += (str(item['title'])+" <-> "+str(item['id'])+ "\n")
            # print(u'{0} ({1})'.format(item['title'], item['id']))
        return returnString
    else :
        returnString = "Tasks :" + "\n" 
        tasks = service.tasks().list(tasklist=items[taskIndex]['id']).execute()
        for task in tasks['items']:
            returnString+=(str(task['title']) + '\n')
            # print(task['title'])
        return returnString

def keep_lists():
    service = get_keep_service()
    # Call the Calendar API
    results = service.notes().list().execute()
    print(results)
    items = results.get('items', [])

    print(items)


# if __name__ == '__main__':
    # print("Calendar events ---------------------")
    # print(cal_events())
    # print("Todos ---------------------")
    # print(tasks_lists("tasks", 0))
    # keep_lists()