# stdlib imports
import os
import time
import json

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


def sendLoginButton(psid):
    print(psid)
    
    data = {
                "recipient": {
                    "id": psid
                },
                "message": {
                    "attachment": {
                        "type": "template",
                        "payload": {
                            "template_type": "button",
                            "text": "login with Facebook to get started",
                            "buttons": [{
                                "type": "account_link",
                                "url": "http://replyreminder.com/login/"
                            }]
                        }
                    }
                }
            }

    r = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token="+PAGE_ACCESS_TOKEN, json.dumps(data), headers={'Content-Type': 'application/json'})
    print(r.status_code)
    print(r.text)
    return True


def sendReminder(reminder):
    data = {
            "recipient": {
                "id": reminder['userid']
            },
            "message": {
                "text": str(reminder['followupUsername']) + '\n' + str(reminder['notes'])
            }
           }

    r = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token="+PAGE_ACCESS_TOKEN, json.dumps(data), headers={'Content-Type': 'application/json'})
    return True


def markReminderSent(reminderID):
    r = requests.post("https://replyreminder.herokuapp.com/reminder/sent/", {'reminderid': reminderID})
    print(r.status_code)
    if r.status_code == 200:
        return True

    return False


def main():
    for each in getReminders():
        if sendReminder(each):
            markReminderSent(each['id'])

if __name__ == "__main__":
    main()
