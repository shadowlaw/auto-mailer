#Auto Mailer
A python script that sends a predefined email once a file has been added to a specified location.

## How to use
There are a few things that you as the user will need to do before using this application.
These will be listed bellow in steps.  

### Step 1: Installation
a) Navigate to desired folder and clone the master branch using `git clone https://github.com/shadowlaw/auto-mailer.git`.   

b) Create and start virtual environment using python's virtualenv

c) Install requirements from requirements.txt file using `pip install -r requirements.txt` 

### Step 2: Configuration
a) You would need to set up your log in information which consist of your
email address and password. 

To configure go to `app/config/user_conf.yaml` and set fields: `EMAIL_ADDRESS` and `PASSWORD`.

b) You would need to set up your mailing file, which consist of the recipient
email address, your email address, the subject and the message you would like
to go with the email.

To configure go to `app > message_data > email > email.json` and set 
fields: `to`, `from`, `subject`, and `body`.  
Note: the from field can be specified in two ways: `email address` or `name <email address>`.

c) You would have to set up the files that you would be looking for, which
is basically setting regular expressions to find the files that you would
want the program to find.

To configure go to `app/config/user_conf.yaml` and set the field: `WATCH_EXTS`.

d)You would have to set the folder path that you want to be watched.

To configure go to `app/config/user_conf.yaml` and set the field: `WATCH_PATH`.  

### Step 3: Run the application
a) Navigate to the application root folder `auto-mailer` and run the application using `python run.py`