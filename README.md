# BFE Django
This is a quick Django application to run the Library of Congress's 
[BFE](https://github.com/lcnetdev/bfe), a standalone editor for  
BIBFRAME. This application allows JSON-LD entities to be created and
saved as JSON-LD on the Filesystem. *NOTE:* This application is strictly for 
demostration purposes and has not been tested or used in an production
environment.


## Installation
Clone this repository:

`git clone https://github.com/jermnelson/bfe_django`

## Running
Before running the application the first time, make a top-level static 
directory `bfe_django/static` and then run `python manage.py collectstatic`
command.

To run the application using the development server, run the following 
command, `python manage.py runserver.py 0.0.0.0:8000` to run on locally
on port 8000. 

