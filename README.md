# Fast-Food-Fast-api


[![Build Status](https://travis-ci.com/actlikewill/fast-food-fast.svg?branch=api%2Fv1)](https://travis-ci.com/actlikewill/fast-food-fast) [![Maintainability](https://api.codeclimate.com/v1/badges/e2cd1d58017013479dbe/maintainability)](https://codeclimate.com/github/actlikewill/fast-food-fast/maintainability) [![Coverage Status](https://coveralls.io/repos/github/actlikewill/fast-food-fast/badge.svg?branch=api%2Fv1)](https://coveralls.io/github/actlikewill/fast-food-fast?branch=api%2Fv1) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/5e56bbfcb29341d185ae034e743654da)](https://www.codacy.com/app/actlikewill/fast-food-fast?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=actlikewill/fast-food-fast&amp;utm_campaign=Badge_Grade)

This is an api for a fast food ordering app. You can use it to place orders create new menu items. It uses data structures as storage.

<hr>

Thisthe following endpoints for the api are available.


| Endpoint  | Description |
| ------------- | ------------- |
| `GET /api/v1/orders` | To get a list of orders |
| `GET /api/v1/orders/<orderId>`|To fetch a specific order using the order Id |
| `POST /api/v1/orders` | To place an order  |
| `PUT /api/v1/orders?status=<accepted> or <declined>`| To update the status of an order  |
|`GET /api/menu`| To view to menu items |
|`POST` /api/menu | To add new menu items |
|`GET /api/menu/<menu_id>`| To view a single menu item details |
|`PUT /api/menu/<menu_id>`| To edit a single menu item using the id|

## Getting Started

Create a folder and clone the repository using the following command:

     git clone https://github.com/actlikewill/fast-food-fast.git
     
Switch to the api branch using:

     git checkout api/v1
     
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

    http://localhost:5000/api/v1


An example request to place view the menu  using curl commands would be:

`curl --request GET \
 --url http://localhost:5000/api/v1/menu`
  
To add a food item you can use:

`curl --request POST \
  --url http://localhost:5000/api/v1/menu \
  --header 'Content-Type: application/json' \
  --data '{"menu_item":"Burger", "price": 400}'`

To place an order you can use:

`curl --request POST \
--url http://localhost:5000/api/v1/orders \
--header 'Content-Type: application/json' \
--data '{"Burger":3}'`


The full documentation on how to you form your requests can be found at this link published using Postman.

[Fast Food Fast -Api Documentation](https://documenter.getpostman.com/view/5281813/RWaRM5Ph)

 The api is also hosted on Heroku at:
 
 [https://actlikewill-fastfoodfast.herokuapp.com/api/v1/orders](https://actlikewill-fastfoodfast.herokuapp.com/api/v1/orders)
 
 ## Running the tests
 
 The tests are written using pytest and can be run using the terminal command:
 
     pytest
     
  The tests are found in the test_api.py file. And cover the full functionality of the app.
  
## Deployment

The easiest way to deploy this on a live server is to use a platform such as heroku and use the command:

     git push heroku api/v1:master
     
 You need to create and account and a new application on their platform. The app contains scripts the can run the installation automatically.
 
[Here is a link to Heroku.com](http://heroku.com/)


## Built With
[Python 3.7](https://www.python.org/downloads/)

[Flask](http://flask.pocoo.org/)

[Postman](https://www.getpostman.com/)

## Authors

Wilson Gaturu in collaboration with Andela Developers


## Acknowledgments

Big thanks to the team at Andela for making this possible. :)
