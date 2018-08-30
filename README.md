[![Build Status](https://travis-ci.org/evamaina/StackOverflow-lite.svg?branch=master)](https://travis-ci.org/evamaina/StackOverflow-lite)
[![Coverage Status](https://coveralls.io/repos/github/evamaina/StackOverflow-lite/badge.svg?branch=Develop)](https://coveralls.io/github/evamaina/StackOverflow-lite?branch=Develop)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/hyperium/hyper/master/LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

## StackOverflow-lite
StackOverflow-lite is a platform where people can ask questions and provide answers
## Challenge 3 Endpoints

| Endpoint       | Description          |   HTTP-verb  |
| ------------- |:-------------:| -----:| 
| /api/v2/signup | Register new user | POST |
| /api/v2/login  | Login the user using this endpoint      | POST   |
| /api/v2/logout | Logout the user from the system      | POST   |
| /api/v2/questions | Fetch all questions |  GET |
| /api/v2/question | Post a question | POST|
| /api/v2/question/id | Fetch a question by id | GET |
| /api/v2/question/question_id | Delete a question | DELETE |
| /api/v1/answer/questionId | Post an answer | POST|
| /api/v2/users/question/user_id | Fetch all questions for a user | POST|
| /api/v2/question/question_id/answers/answer_id | Mark answer as accepted or update answer | PUT |

## Screenshots
#### SignUp user 
![signup](https://image.ibb.co/cnboa9/user_sign.png)
#### Login user
![login](https://image.ibb.co/cypKyU/login_user.png)
#### Logout user
![logout](https://image.ibb.co/gnsNJU/logout.png)
#### Post question
![post-quest](https://image.ibb.co/b6VCk9/post_quest.png)
#### Post answer to a question
![answer-quest](https://image.ibb.co/htf6Cp/post_answer.png)
#### Delete a question
![delete-quest](https://image.ibb.co/eHhBTU/delete.png)
#### Fetch all questions
![fetch-all-quest](https://image.ibb.co/jaBck9/fetch_all_quest.png)
#### Fetch a single question
![fetch-a-quest](https://image.ibb.co/dbBosp/fetch_a_quest.png)
#### Update an answer
![update-answer](https://image.ibb.co/cNwKyU/update.png)
#### Mark answer as accepted
![accept-answer](https://image.ibb.co/mKoJQ9/accept.png)





## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
A few requirements to install, run and test this project.

cd path/to/directory-your-directory
- git clone https://github.com/evamaina/StackOverflow-lite
 -Install virtual environment 
- cd to ride-my-way-api and execute the following commands:
    
    - $ virtualenv venv --python=python3
    - $ source venv/bin/activate
    - $ pip install -r requirements.txt
    - $ pip install pytest
    
- To run tests, do:

    - $ pytests

- Then run the app by executing:
    - $ python run.py
    
- Install and open postman to test the various endpoints

## Testing
Manually open the index.html file in your preferred browser. Navigate through the pages with the links provided.

## Built With
* HTML
* CSS
* JavaScript
* python

## Authors
Eva Maina



