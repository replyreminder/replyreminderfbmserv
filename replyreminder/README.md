# Server Endpoints
- `/`
    - test enpoint. REturns 200 if server is up

- `/user/` [POST]
    - create user endpoint
    - expects: `{userid: int, email:string, first_name:string, last_name:string, timezone:datetime, updated_time:datetime}`
    - returns:
        - 200: user exists, or was created correctly
        - 500: unknown server error (DB)

- `/reminder/` [POST]
    - create reminder endpoint
    - expects:
    - returns: