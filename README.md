# Mass mailing CLI app
Mass email sending with template message filling


## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Usage](#usage)
* [Technologies](#technologies)


## General info
Simple app to send personalized e-mails to our mailing list.



## Setup
* Make sure you have Python 3.7+ installed. (I developed it with Python 3.7)
* Some Python modules are required which are contained in requirements.txt and will be installed below.

#### 1. Requirements
In the email-sender folder, run:

`python -m pip install -r requirements.txt`

Adapt the command to your operating system if needed.

#### 2. Setup mailing list
Open mailing-list.xlsx file with excel or similar software. 
Put e-mail addresses in the A column.
If you would like to use e-mails personalization, put the corresponding data in next columns.
**Remember to name the column in the first row (this name will be used in message templating)**

#### 3. Setup message template
Open email-sender/message_templates.py in any editor. Change the SUBJECT variable to dired message subject.
Fill both text and html templates. 

Notice that you can use data from mailing-list file. Use it with leading $ sign. For example, for column named "name": `$name` 

## Usage
Go to email_sender folder and run:

`python main.py`

On the first use app will ask for email login data and will store it in local file.

If one wants to use other address to send emails, one has to delete login-data.yaml file


## Technologies
Project is created with:
* Python 3.7
* PyYAML 5.4.1
* pandas 0.25.1
* pytest 6.2.1

## [License](https://github.com/retip94/email-sender/blob/master/LICENSE.md)

MIT © [Piotr Piekielny](https://github.com/retip94)

