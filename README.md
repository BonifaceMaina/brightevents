## Bright Events Application (Written in Flask, HTML5, Twitter Bootstrap, CSS and JavaScript)

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1764a0ff58f1440e8ad8f35a8932db93)](https://www.codacy.com/app/BonifaceMaina/brightevents?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BonifaceMaina/brightevents&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/BonifaceMaina/brightevents.svg?branch=master)](https://travis-ci.org/BonifaceMaina/brightevents)
[![Maintainability](https://api.codeclimate.com/v1/badges/033651583c868158e443/maintainability)](https://codeclimate.com/github/BonifaceMaina/brightevents/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/BonifaceMaina/brightevents/badge.svg)](https://coveralls.io/github/BonifaceMaina/brightevents)

This is an application that allows users to register, add events they want other users to attend as well as RSVP to other users' events.

## UI Templates

The UI templates for the project can be found at [Bright Events](https://bonifacemaina.github.io/brightevents/designs/UI/index.html)

## Local installation

The instructions below will guide you on how to set up the application and run it locally for testing.

## Project Prerequisites 

You will need the following on your machine:

Virtualenv
Python version 2.7
Postman

Install virtualenv:
```
pip install virtualenv
```
Navigate to your desired folder:
```
cd folder/
```
Create a virtualenvironment:
```
virtualenv myenv
```
Start the virtualenv:
```
source myenv/bin/activate
```
Clone the repo:
```
https://github.com/BonifaceMaina/brightevents.git
```
Install the requirements:
```
pip install -r requirements.txt
```
## Launching the project
Run ``` python run.py ``` from the project's root and use PostMan or cURL to test the endpoints

## Endpoints

| Resource URL | Methods | Description |
| -------- | ------------- | --------- |
| `/api/auth/register` | GET  | Creates a user account |
| `/api/auth/login/` | POST  | Logs in a user |
| `/api/auth/logout/` | POST  | Logs out a user |
|  `/api/auth/reset-password/` | POST | Password reset |
| `/api/events/` | POST  | Creates an event |
| `/api/events/` | GET  | Retrieves events |
| `/api/events/<eventId>` | PUT  | Updates an event |
| `/api/events/<eventId>/rsvp` | GET  | Allows a user to RSVP to an event |

## Testing

Run the tests using ```unittest```





## Author

Created by **Boniface Maina**

## Contributing

Any pull requests are welcome.

## Acknowledgements

[Andela Kenya](https://andela.com/)
