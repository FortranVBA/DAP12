# Application

This application is a back-end application to be executed locally in the context of OpenClassroom educational project. It allow registered users to manage other users, clients, contracts and events (permissions are according their staff department). This application has been developed with the Django rest framework, using a postgres.

## Installation and first launch

This locally-executable application can be installed and executed from [http://localhost:8000/](http://localhost:8000/) using the following steps.

1. Clone this repository using $ git clone `https://github.com/FortranVBA/DAP10.git` (you can also download the code using [as a zip file](https://github.com/FortranVBA/DAP10/archive/refs/heads/main.zip))
2. Move to the application root folder.
3. Create a virtual environment for the project with `$ py -m venv .venv` on windows or `$ python3 -m venv .venv` on macos or linux.
4. Activate the virtual environment with `$ .venv\Scripts\activate` on windows or `$ source .venv/bin/activate` on macos or linux.
5. Install project dependencies with `$ pip install -r requirements.txt`
6. Download and install PostgreSQL `https://www.postgresql.org/download/` (Follow instructions according your operating system).
7. Create the project Posgres database (named DAP12) with `$ createdb -O (your postgre username) DAP12`.
8. Configure the settings/settings.py file by putting your Postgres login in the variable called DATABASES (fields "USER" and "PASSWORD").
9. Run the postgres database with `$ postgres -D /usr/local/pgsql/data` (the command may depends on your operating system).
10. Run the django migration with `$ ./manage.py migrate`.
11. Import the status fixtures with the following commands: 
- `$ ./manage.py loaddata staffprofile_data.json`
- `$ ./manage.py loaddata clientstatut_data.json`
- `$ ./manage.py loaddata contractstatut_data.json`
- `$ ./manage.py loaddata eventstatut_data.json`
12. Import the data fixtures with the following commands:
- `$ ./manage.py loaddata staff_data.json` (compulsory to have default profiles to login with)
- `$ ./manage.py loaddata client_data.json` (optional if you want example data)
- `$ ./manage.py loaddata contract_data.json` (optional if you want example data)
- `$ ./manage.py loaddata event_data.json` (optional if you want example data)
13. Run the server with `$ python manage.py runserver`

When the server is running after step 13 of the procedure, the Soft Desk API can be requested from endpoints starting with the following base URL: http://localhost:8000/.
Since authentification is made with JWT (Json Web Token), the use of postman is recommanded for the API request.


## Usage after installation

For subsequent launches of the application, you only have to execute the following steps from the root folder of the project:
1. Activate the virtual environment with `$ .venv\Scripts\activate` on windows or `$ source .venv/bin/activate` on macos or linux.
2. Run the postgres database with `$ postgres -D /usr/local/pgsql/data` (the command may depends on your operating system).
3. Run the server with `$ python manage.py runserver`

Once you have launched the server, the application can be requested from endpoints starting with the following base URL [http://localhost:8000/](http://localhost:8000/).
Since authentification is made with JWT (Json Web Token), the use of postman is recommanded for the API request.

You can use already created users from management team (installation step 12) to register new ones:
-	Username: StaffManagementA ; Password: password
-	Username: StaffManagementB ; Password: password

The other registered users from sales team are:
-	Username: StaffSalesA ; Password: password
-	Username: StaffSalesB ; Password: password

The other registered users from support team are:
-	Username: StaffSupportA ; Password: password
-	Username: StaffSupportB ; Password: password


## Usage and detailed endpoint documentation

The list of allowed endpoints is the following:

| Description | Method |Endpoint |
| ----------- | ----------- | ----------- |
| User login | POST | /login/ |
| Add user | POST | /users/ |
| Update user | PATCH | /users/{id}/ |
| Delete user | DELETE | /users/{id}/ |
| List users | GET | /users/ |
| Retrieve user details | GET | /users/{id}/ |
| List clients | GET | /clients/ |
| Retrieve client details | GET | /clients/{id}/ |
| Add client | POST | /clients/ |
| Update client | PATCH | /clients/{id}/ |
| Change client status to actual | POST | clients/{id}/change_status/ |
| List contracts | GET | /contracts/ |
| Retrieve contract details | GET | /contracts/{id}/ |
| Add contract | POST | /contracts/ |
| Update contract | PATCH | /contracts/{id}/ |
| Change contract status to signed | POST | /contracts/{id}/change_status/ |
| List events related to contract | GET | /contracts/{id}/events/ |
| Retrieve event details | GET | /events/{id}/ |
| List events | GET | /events/ |
| Add event | POST | /events/ |
| Update event | PATCH | /events/{id}/ |


Please refer to the postman collection documentation (available at https://documenter.getpostman.com/view/9694290/U16nJPcS) for all endpoint description and expected parameters.

## Admin panel

Once you have launched the server, the Django default admin panel can be reached by visiting [http://localhost:8000/admin/](http://localhost:8000/admin/).

All management staff members have super user permissions to use the admin panel.
You can use already created users from management team (installation step 12):
-	Username: StaffManagementA ; Password: password
-	Username: StaffManagementB ; Password: password


## Testing commands

After running the server, the tests can be launched with the command `$ ./manage.py test`.

