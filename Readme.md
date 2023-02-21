<h1 align="center">Football API</h1>

<img src="https://github.com/gurupratap-matharu/midware/blob/master/staticfiles/img/hero.jpg" alt="drawing" width="1920"/>

### Development setup 🛠

Steps to locally setup development after cloning the project.

`docker-compose up -d --build`
or simple
`make build` ;)

Make sure you rename .env.example to .env and declare the environment variables in root folder for docker to pickup!

### Browsable API

The application features a full featured browsable api for quick verification.
Once you have the local server running simply head on to

http://localhost:8000/api/v1/

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

### You can alos access a team with all its players like this
GET http://localhost:8000/api/v1/teams/ARS/players/

```

### Admin Interface

For convenience we have access to an admin interface provided by django.

All data models are hooked up to the admin interface to verify if data has been correctly
populated in the database.

But to access the admin you would need to create a super user by running the following

```
make superuser
```

Provide a username, password, email and then you can access admin at http://localhost:8000/admin/

The interface should look like this
<img src="https://github.com/gurupratap-matharu/midware/blob/master/staticfiles/img/admin.png" alt="drawing" width="1920"/>

### Features ✨

- Development with docker for easy setup and scaling on cloud
- Uses logging module quite frequently for easy debugging
- Unit tests to verify functionality as per requirements
- Versioning of api possible easily. for eg: `/api/v1/`
- Fast response time
- Easily customizable with Login | Logout | reset password features and rest-token authentication
- Make file for faster setup and reusability
- Throttling limits in place
  - `100 requests/day` for anonymous users
  - `1000 requests/day` for authenticated users
