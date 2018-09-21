# Fast-Food-Fast-api
This is an api for a fast food ordering app


[![Build Status](https://travis-ci.com/actlikewill/fast-food-fast.svg?branch=api%2Fv1)](https://travis-ci.com/actlikewill/fast-food-fast)

[![Maintainability](https://api.codeclimate.com/v1/badges/e2cd1d58017013479dbe/maintainability)](https://codeclimate.com/github/actlikewill/fast-food-fast/maintainability)

[![Coverage Status](https://coveralls.io/repos/github/actlikewill/fast-food-fast/badge.svg?branch=api%2Fv1)](https://coveralls.io/github/actlikewill/fast-food-fast?branch=api%2Fv1)

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5e56bbfcb29341d185ae034e743654da)](https://www.codacy.com/app/actlikewill/fast-food-fast?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=actlikewill/fast-food-fast&amp;utm_campaign=Badge_Grade)



<hr>

This branch created the endpoints for the api that will be used in the application.


| Endpoint  | Description |
| ------------- | ------------- |
| `GET /api/v1/orders` | To get a list of orders |
| `GET /api/v1/orders/<orderId>`|To fetch a specific order using the order Id |
| `POST /api/v1/orders?item=<your-item>quantity=<your-quantity>` | To place an order  |
| `PUT /api/v1/orders?status=<accepted> or <declined>`| To update the status of an order  |
 

 The api is hosted on Heroku at
 
 [https://actlikewill-fastfoodfast.herokuapp.com/api/v1/orders](https://actlikewill-fastfoodfast.herokuapp.com/api/v1/orders)
 
 Use [Postman](https://www.getpostman.com/) to test the various endpoints as specified above.
