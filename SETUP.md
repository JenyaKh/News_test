To install the application on your local computer, you need Python 3.9 or higher.

- Download the application to your computer by selecting "download source code" and the required archive format for your OS. 
Unpack the archive into a folder of your choice.
(If you are using git, you can clone the project using the command: `git clone git@gitlab.com:lms.hillel/vehicles.git` )

- In the console go to the folder 'vehicles-main', wwhich contains the file manage.py

- Create a virtual environment for the project:
  `python -m venv venv`

- Activate virtual environment:
  `venv\Scripts\activate.bat` (for Windows)
  `source venv/bin/activate` (for Linux)
  Make sure the viral environment is active: the console displays (venv)

- To install the required packages:
  `pip install -r requirements.txt`

- To create the database and run the project, run:
  `python manage.py migrate`
  and then 
  `python manage.py runserver`

If you see a link to your local server - the application is running! Use a browser to navigate to endpoints
