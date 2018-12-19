# The Gram

## Author
### *Gloria Givondo* (14/12/2018)

## Description 

A clone of the popular app Instagram.

You can view the live link on: https://.herokuapp.com/

## User Stories
These are the behaviours that the application implenents for use by a user.

As a user, I would like to: 
* Sign in to the application to start using.
* Upload my pictures to the application.
* See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like a picture and leave a comment on it.

## Setup / Installation Requirements
* Web browser
* Virtual environment
* Django
* Python version 3.6


### Cloning the Repo
* In your terminal run:

        $ git clone https://github.com/GeGe-K/theGram.git
        $ cd theGram

## Running the Application 
* Create the virtual environment

        $ sudo apt-get install python3.6 -venv 
        $ python3.6 -m venv virtual

* Activate virtual environment

        $ source virtual/bin/activate

* Download the latest version of pip

        $ curl https:/bootstrap.pypa.io/get-pip.py | python

* Install application dependancies and other Modules

        $ pip install -r requirements.txt

* Create the database

        $ psql
        
        CREATE DATABASE instagram;

* Create a .env file and add the following

        - SECRET_KEY = `<secret_key>`
        - DB_NAME = `instagram`
        - DB_USER = `<Username>`
        - DB_PASSWORD = `your db password`
        - DEBUG = `True`


* Run initial migration

        $ python3.6 manage.py makemigrations <name of app>
        $ python3.6 manage.py migrate

* Run the application in your terminal:

        $ python3.6 manage.py runserver

## Testing the Application 
* To run the tests for the class files and check if they function well:

        $ python3.6 manage.py tests

## Technologies Used
* Virtual environment
* Python version 3.6.7(Django framework)
* Bootstrap4 & 3
* Postgresql
* HTML5
* CSS
* Heroku
* Visual Studio Editor

## Known Bugs
There are no known bugs. Contact gloriagivondo@gmail.com in-case of any bugs.

## License
The content of this site is license under the MIT license
Copyright (c) 2018 **Gloria**

