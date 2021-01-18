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
#### Email Configuration
1. Set up your log in information which consist of your email address and password. To configure, go to `app/config/user_conf.yaml` and set fields: `EMAIL_ADDRESS` and `PASSWORD`.
2. Configure the mail server you plan to use. To configure, go to `app/config/user_conf.yaml` and set fields: `SMTP_SERVER` and `SMTP_PORT`. Note that currently only SMTP SSL is supported. 
3. Set the location of your email template. A default email template is defined in `app/message_data/email/email.json`. Note that the location of the template can be changed.  

#### Event Group Configuration
1. Set up an Event Group in `app/config/user_conf.yaml`. A default group has been setup but it is advised that you change the attribute values under `EVENT_GROUPS`.  
Note: `WATCH_EXTS` is a list of regular expressions that should match the name of the files you want the application should be triggered by. 
### Step 3: Run the application
a) Navigate to the application root folder `auto-mailer` and run the application using `python run.py`

