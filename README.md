# Fast-Food-Fast-api


[![Build Status](https://travis-ci.com/actlikewill/fast-food-fast.svg?branch=api%2Fv1)](https://travis-ci.com/actlikewill/fast-food-fast) [![Maintainability](https://api.codeclimate.com/v1/badges/e2cd1d58017013479dbe/maintainability)](https://codeclimate.com/github/actlikewill/fast-food-fast/maintainability) [![Coverage Status](https://coveralls.io/repos/github/actlikewill/fast-food-fast/badge.svg?branch=api%2Fv1)](https://coveralls.io/github/actlikewill/fast-food-fast?branch=api%2Fv1) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/5e56bbfcb29341d185ae034e743654da)](https://www.codacy.com/app/actlikewill/fast-food-fast?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=actlikewill/fast-food-fast&amp;utm_campaign=Badge_Grade)

This is an Version two of the api for Fastfood Fast ordering app. You can use it to place orders create new menu items.
This version implements a postgreql database for storage.

<hr>

The following endpoints for the api are available.


| Endpoint  | Description |
| ------------- | ------------- |
|`POST /auth/users`| To create new users |
|`GET /auth/users`| To get a list of all users|
| `GET /api/v2/orders` | To get a list of orders |
| `GET /api/v2/orders/<orderId>`|To fetch a specific order using the order Id |
| `POST /api/v2/orders` | To place an order  |
| `PUT /api/v2/orders/<order_id>`| To update the status of an order  |
|`GET /api/v2/menu`| To view to menu items |
|`POST /api/v2/menu` | To add new menu items |
|`GET /api/v2/menu/<menu_id>`| To view a single menu item details |
|`PUT /api/menu/<menu_id>`| To edit a single menu item using the id|

## Getting Started

Create a folder and clone the repository using the following command:

     git clone https://github.com/actlikewill/fast-food-fast.git
     
Switch to the api branch using:

     git checkout ft-api-v2-160814187
     
### Prerequisites

The api uses the python flask framework. You will need to have python 3 installed to test it locally. 
You also might want to install Postman to make the requests in Json format, though you can also use curl on your terminal
Here are the links:

[Download Python 3.7](https://www.python.org/downloads/)

[Download Postman](https://www.getpostman.com/)

### Installing

Create a virtual environment using the following command on your terminal:

     python -m venv venv

Activate the environment using:
    
    source venv/scripts/activate

You will need to install the dependencies from the requirements file. 
In the active virtual environment use the following command:

    pip install -r requirements.txt

To launch the api use the command:

    python manage.py runserver

The api will run at your localhost on port:5000

    http://localhost:5000/api/v2
    
    http://localhost:5000/auth/users


An example request to login a user  using curl commands would be:

     curl --request POST \
       --url http://localhost:5000/auth/login \
       --header ': ' \
       --header 'Content-Type: application/json' \
       --data '{
          "username":"Admin",
          "password":"adminpassword"
     }'

To add a food item you can use:

     curl --request POST \
       --url http://localhost:5000/api/v2/menu \
       --header 'Authorization: Bearer <your-token-here> \
       --header 'Content-Type: application/json' \
       --data '{
          "menu_item": "Hotdog",
          "description": "Spicy pork hotdog slathered in mustard",
          "price": 300
     }'
     
To place an order you can use:

     curl --request POST \
       --url http://localhost:5000/api/v2/orders \
       --header 'Authorization: Bearer <your-token-here> \
       --header 'Content-Type: application/json' \
       --data '
     {"Sandwich":2, "Burger": 3, "Hotdog":5}


The full documentation on how to you form your requests can be found at this link published using Postman.

[Fast Food Fast -Api Documentation](https://documenter.getpostman.com/view/5281813/RWgm525d)

 The api is also hosted on Heroku at:
 
 [https://actlikewill-fastfoodfast.herokuapp.com/auth/users](https://actlikewill-fastfoodfast.herokuapp.com/auth/users)
 
 ## Running the tests
 
 The tests are written using pytest and can be run using the terminal command:
 
     pytest
     
  The tests are found in the test_api.py file. And cover the full functionality of the app.
  
## Deployment

The easiest way to deploy this on a live server is to use a platform such as heroku and use the command:

     git push heroku:master
     
 You need to create and account and a new application on their platform. The app contains scripts the can run the installation automatically.
 
[Here is a link to Heroku.com](http://heroku.com/)


## Built With
[Python 3.7](https://www.python.org/downloads/)

[Flask](http://flask.pocoo.org/)

[Postman](https://www.getpostman.com/)

## Authors

Wilson Gaturu in collaboration with Andela Developers


## Acknowledgments

Big thanks to the team at Andela for making this possible and May the code be with you! :)
