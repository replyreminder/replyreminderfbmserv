# stdlib imports
import os

# other imports
import requests

# project imports

# setup variables

PAGE_ACCESS_TOKEN = os.environ['PAGE_ACCESS_TOKEN']

# functions

"""
Content-Type: application/json" -d ''

"""
def getReminders():
    r = requests.get("https://replyreminder.herokuapp.com/reminders/")
    if r.status_code == 200:
        return r.json()

    return []


def sendReminder(reminder):
    data = {
            "recipient": {
                "id": "<PSID>"
            },
            "message": {
                "text": "hello, world!"
            }
           }
    r = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token="+PAGE_ACCESS_TOKEN, data)
    pass


def markReminderSent(reminderID):
    pass


def main():
    pass

if __name__ == "__main__":
    main()
