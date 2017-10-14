# Server Side Design

## Heroku Rest Server
- `/reminders/` [get]
- `/reminder/` [post]
    - user id
    - the person to follow up withs user name
    - time and date to follow up
    - *some god forsaken timestamp format*
    - `{'userid': 1234567, 'followupUser': 'John Smith', 'time': 152343543}`

## Heroku Scheduler Server
- set schedule
- call send FBM message
- 

## Database Postgres
- Tables
    - users
        - userid (fb)
        - email
        - first_name
        - last_name
        - timezone
        - updated_time
        
    - reminders
        - userid
        - followupUsername
        - reminderTime
        - notes