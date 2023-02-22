<h1 align="center">Football API</h1>

<img src="https://github.com/gurupratap-matharu/midware/blob/master/staticfiles/img/hero.jpg" alt="drawing" width="1920"/>

## Development setup 🛠

Steps to locally setup development after cloning the project.

`make build`

This single command should

- Install all your dependencies
- Make and apply all DB migrations
- Spin up a server running on port 8000

## Browsable API

The application features a full featured browsable api for quick verification.
Once you have the local server running simply head on to

http://localhost:8000/api/v1/

At this moment the database would be empty. We can populate it by running the sample
requests below. The terminal running the app should give detailed logging messages about
how the data is being pulled.

## Sample Requests

```
### Import League
POST http://localhost:8000/api/v1/import-league/AU/


### Players filtered by league
GET http://localhost:8000/api/v1/players/PL/


### Players filtered by league is case insensitive
GET http://localhost:8000/api/v1/players/pl/


### Players filtered by INVALID league - throws http 404
GET http://localhost:8000/api/v1/players/PLA/


### Players filtered by league and team
GET http://localhost:8000/api/v1/players/PL/BOU/


### Players filtered by valid league and invalid team - throws http 404
GET http://localhost:8000/api/v1/players/PL/BOA/

### If you request for players by valid league and valid team but
### team is not part of the league then you'd get an empty response


### Teams Detail view
GET http://localhost:8000/api/v1/teams/ARS/


### Teams Detail view is case insensitive
GET http://localhost:8000/api/v1/teams/ars/


### Teams Detail view show players as well
GET http://localhost:8000/api/v1/teams/ARS/?players=true

### You can also access a team with all its players like this
GET http://localhost:8000/api/v1/teams/ARS/players/

```

## Train of thought 🤔

### 1. Why chose django and django rest framework for such a project? 🐍

    Django is a batteries included framework based on python and battle tested with many
    big companies using it for large projects. Building rapid prototypes is very fast in
    Django and it helps in removing a lot of boiler plate code.

    Django also plays really well with relational databases especially Postgres. Although we
    should note that django is purely synchronous (with limited async support being introduced)
    as python itself runs synchronously unlike javascript and nodejs which run purely async.

### 2. Why use sqlite as a db as its not a production Db? 📀

    Sqlite is a file based DB and not recommended for large scale heavy traffic production
    applications. Having said that, switching from sqlite to postgres in this project would
    need minimal effort. Django by default provides sqlite as a db backend.

    For the purpose of this code challenge using postgres as the backend would demand other users to either spin
    up the service locally on their system with all the correct configuration or use a docker based alternative which would be
    an overkill for this challenge. So sqlite has been used for its simplicity.

### 3. How did you design the data modelling? 🖋️

    After studying the Football API we understand that the three main resources we are dealing
    with are `Competition (League)`, `Team` and `Player`. My understanding about their relation is

    - Competition can have many teams <-> Team can participate in many competitions
    - Team can have many players <-> A player can participate in many teams

    Both these scenarios are Many To Many relationships in the world of Django models.

    Other models are Coach and Area where the relation looks like

    - An area can have many competitions
    - An area can have many teams
    - A team can have many coaches

### 4. Testing 🧪

    We use the classic unit test framework to run django tests testing each endpoint
    The broad approach is to create mock data for each test with setup and check specific
    test case. Although in production scenario you would add integration or End to end testing.

### 5. App structure 🏛️

    Personally I'm fond of modular approach and clean code with smaller methods and classes
    that are easy to maintain and understand.

    The idea during development has been to compartmentalize everything in its domain like
    views, serializers, urls, models, tests which is the recommended approach in django and python
    projects. Docstrings, comments and flake8 linting suggestions have been incorporated as
    much as possible

### 6. What about rate limiting to prevent abuse? ✋

    We use throttling limits to prevent users to send loads of requests rapidly and clog our
    server down. For the sake of challenge this has been set in settings to

    - `100 requests/day` for anonymous users 🦹‍♂️
    - `1000 requests/day` for authenticated users 👨🏼‍💼

    You can test this for example by running this code snippet in your shell

    `make shell`

    ```python
    for _ in range(5000):
        response = requests.get('http://localhost:8000/api/v1/')
    ```

## Admin Interface 👩‍💼

For convenience we have access to an admin interface provided by django.

All data models are hooked up to the admin interface to verify if data has been correctly
populated in the database.

But to access the admin you would need to create a super user by running the following

```
make superuser
```

Provide a username, password, email and then you can access admin at http://localhost:8000/admin/

## Features ✨

- Uses logging module quite frequently for easy debugging
- Unit tests to verify functionality as per requirements
- Versioning of api possible easily. for eg: `/api/v1/`
- Fast response time
- Easily customizable with Login | Logout | reset password features and rest-token authentication
- Make file for faster setup and reusability
- Throttling limits in place
  - `100 requests/day` for anonymous users
  - `1000 requests/day` for authenticated users
