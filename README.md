# Fast-Food-Fast-api
This is an api for a fast food ordering app


[![Build Status](https://travis-ci.com/actlikewill/fast-food-fast.svg?branch=api%2Fv1)](https://travis-ci.com/actlikewill/fast-food-fast) [![Maintainability](https://api.codeclimate.com/v1/badges/e2cd1d58017013479dbe/maintainability)](https://codeclimate.com/github/actlikewill/fast-food-fast/maintainability) [![Coverage Status](https://coveralls.io/repos/github/actlikewill/fast-food-fast/badge.svg?branch=api%2Fv1)](https://coveralls.io/github/actlikewill/fast-food-fast?branch=api%2Fv1) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/5e56bbfcb29341d185ae034e743654da)](https://www.codacy.com/app/actlikewill/fast-food-fast?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=actlikewill/fast-food-fast&amp;utm_campaign=Badge_Grade)



<hr>

This branch created the endpoints for the api that will be used in the application.


| Endpoint  | Description |
| ------------- | ------------- |
| `GET /api/v1/orders` | To get a list of orders |
| `GET /api/v1/orders/<orderId>`|To fetch a specific order using the order Id |
| `POST /api/v1/orders` | To place an order  |
| `PUT /api/v1/orders?status=<accepted> or <declined>`| To update the status of an order  |
|`GET /api/menu`| To view to menu items |
|`POST` /api/menu | To add new menu items |
|`GET /api/menu/<menu_id>`| To view a single menu item details |
|`PUT| /api/menu/<menu_id>`| To edit a single menu item using the id|


Create a folder and clone the repository using the following command:

     `git clone https://github.com/actlikewill/fast-food-fast.git`


The api uses the python flask framework. You will need to have python 3 installed to test it locally.

Create a virtual environment using the following command on your terminal:

    `python -m venv venv`

Activate the environment using:
    
    `source venv/scripts/activate`

You will need to install the dependencies from the requirements file. 
In the active virtual environment use the following command:

    `pip install -r requirements.txt`

To launch the api use the command:

    `python manage.py runserver`

The api will run at your localhost on port:5000

    `http://localhost:5000/api/v1`

The api only accepts json formatted requests. The best tool to use for this is Postman

The documentation on how to you form queries can be found at this link published using Postman.

[Fast Food Fast -Api Documentation](https://documenter.getpostman.com/view/5281813/RWaRM5Ph)

 The api is hosted on Heroku at:
 
 [https://actlikewill-fastfoodfast.herokuapp.com/api/v1/orders](https://actlikewill-fastfoodfast.herokuapp.com/api/v1/orders)
 
 Use [Postman](https://www.getpostman.com/) to test the various endpoints as specified above.
