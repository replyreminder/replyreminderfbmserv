# replyreminderfbmserv
ReplyReminder for Facebook Messenger server

# Server Endpoints
- `/`
    - test endpoint. Returns 200 if server is up

- `/user/` [POST]
    - create user endpoint
    - expects: `{userid: int, email:string, first_name:string, last_name:string, timezone:datetime, updated_time:datetime}`
    - returns:
        - 200: user exists, or was created correctly
        - 400: malformed json input
        - 500: unknown server error (DB)

- `/reminder/` [POST]
    - create reminder endpoint
    - expects: `{userid: int, followupUsername: string, reminderTime: datetime, notes: string(optional)}`
    - returns:
        - 200: reminder was successfully added
        - 400: malformed json
        - 500: unknown server error (DB)
    
## Notes
- using flask postgresql and heroku
    - http://blog.y3xz.com/blog/2012/08/16/flask-and-postgresql-on-heroku
