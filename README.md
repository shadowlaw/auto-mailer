# Auto Mailer
A python script that sends a predefined email once a file has been created in a specified location.
This script is aimed at reducing human involvement in sending mundane emails with attachments. 

## Usage
### Step 1: Installation
a) Navigate to desired folder and clone the master branch using `git clone https://github.com/shadowlaw/auto-mailer.git`.   

b) Create and start virtual environment using python's virtualenv (optional)

c) Install requirements from requirements.txt file using `pip install -r requirements.txt` 

### Step 2: Configuration
Two configuration files are available to be edited: user_conf.yaml and system_conf.yaml. Each file and its fields
attached to them are described below.

The `app/config/user_conf.yaml` file needs  to be edited to allow this script to function properly. The following table 
shows the fields to be edited and describes how they are used.

|  Field |  Type |  Description |
|---|---|---|
|  EVENT_GROUPS |  array |  An array of object for grouping event. |
|  WATCH_EXTS | array  |  An array of regular expressions that describe the file that the event group should be triggered by. All regular expressions should be prefixed with `.*`  |
|  WATCH_PATH |  string |  The full path to the folder that the script should watch for the event group. |
|  DEFAULT_OBSERVER_TYPE  |  string  |  The default observer type for all watched folders. Set to polling or native. This options will default to native if not set.  See [Watch Folder Content Detection](https://github.com/shadowlaw/auto-mailer/wiki/Watch-Folder-Content-Detection) page for more details  |
|  MAIL_DATA_PATH |  string |  The full path to the email template file. |
|  SMTP_SERVER |  string |  URL or IP address of the SMTP server for your email address. |
|  SMTP_PORT |  integer |  The SMTP server port number. |
|  EMAIL_ADDRESS |  string |  The sending email address or username. |
|  PASSWORD |  string |  Password for logging into the email address provided. |

Note. This script currently only supports SMTP via SSL.

The `app/config/system_conf.yaml` file contains fields that modify the scripts behavior and does not have to be edited 
for the script to be used. The following table shows the fields that can be edited.

|  Field |  Type |  Description |
|---|---|---|
|  LOG_LOCATION |  string |  The full path to the script log file resides (should include the logfile name and extension). |
|  DEFAULT_LOG_LEVEL |  string |  The scripts default log level. Corresponds to the Python logging module log levels.|
 
#### Email Configuration
1. Set up your log-in information which consist of your email address and password. To configure, go to `app/config/user_conf.yaml` and set fields: `EMAIL_ADDRESS` and `PASSWORD`.
2. Configure the mail server you plan to use. To configure, go to `app/config/user_conf.yaml` and set fields: `SMTP_SERVER` and `SMTP_PORT`. Note that currently only SMTP SSL is supported. 
3. Set the location of your email template. A default email template is defined in `app/message_data/email/email.json`. Note that the location of the template can be changed.  

### Predefined Email Template Setup
The default email template provided in `app/message_data/email/email.json` requires the basic fields for an email.

|  Field |  Type |  Description |
|---|---|---|
|  to |  array |  Email address that of the intended recipient(s). |
|  from |  string |  Email address of the sender. |
|  subject |  string |  Subject of the email. |
|  body |  string |  Body of the email.|

example email template.
```json
{
    "to": ["example@example.com", "example1@example.com"],
    "from": "sender@example.com",
    "subject": "Example Email Template",
    "body": "This is an example email template. The email body supports escape sequences such as \n"
}
```


#### Event Group Configuration
1. Set up an Event Group in `app/config/user_conf.yaml`. A default group has been setup but it is advised that you change the attribute values under `EVENT_GROUPS`.  
Note: `WATCH_EXTS` is a list of regular expressions that should match the name of the files you want the application should be triggered by. 
### Step 3: Run the application
a) Navigate to the application root folder `auto-mailer` and run the application using `python run.py`

## Install and Run with Docker
See wiki for docker [installation](https://github.com/shadowlaw/auto-mailer/wiki/Installation#docker)

## Docker Configuration
See wiki for docker [config](https://github.com/shadowlaw/auto-mailer/wiki/Configuration#docekr-configuration)