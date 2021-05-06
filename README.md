# Peach APP

## Description
Blogg is a web app developed using Python Flask, Postgressql and SQLAlchemy The app allows a user to create blogs for different categories, as well as comment and vote on them.The application incorporates an authentication system, ORM using SQLAlchemy, migrations and password hashing.

## Author

Josh Kimani
(https://gglob.herokuapp.com/)



# Installation

## Clone
    Place your secret key, mail_username, mail_password in the start.ps1
```bash
    git clone 
    
```
##  Create virtual environment
```bash
    python3.9 -m venv --without-pip
    
```
Activate virtual and install requirements.txt
```bash
   $ source virtual/bin/activate   or  $ virtual/scripts/activate.ps1 
   $ pip install - requirements.txt
    
```

## Run app
```bash
   $ ./start.ps1
    
```

## Test class

```bash
    $ python3.9 manage.py test
```
## Known Bugs
Flask_uploads version incompatible, making img file uploads unable to can. 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Technologies Used
    Python 3.7
    Flask 
    HTML
    SQL Database


## DB diagram
![image](https://user-images.githubusercontent.com/38456207/116395642-08d36b00-a82d-11eb-9e43-ea7485cba8e5.png)

## License
[LICENSE](LICENSE)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

