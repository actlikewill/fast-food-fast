# fast-food-fast-api
This is an api for a fast food ordering app


[![Build Status](https://travis-ci.com/actlikewill/fast-food-fast.svg?branch=api%2Fv1)](https://travis-ci.com/actlikewill/fast-food-fast)

[![Maintainability](https://api.codeclimate.com/v1/badges/e2cd1d58017013479dbe/maintainability)](https://codeclimate.com/github/actlikewill/fast-food-fast/maintainability)

[![Coverage Status](https://coveralls.io/repos/github/actlikewill/fast-food-fast/badge.svg?branch=api%2Fv1)](https://coveralls.io/github/actlikewill/fast-food-fast?branch=api%2Fv1)



<hr>
 Endpoints created are:
 
 `GET /api/v1/orders` : To get a list of orders<br><br>
 `GET /api/v1/orders/<orderId>` : To fetch a specific order using the order Id<br><br>
 `POST /api/v1/orders?item=<your-item>quantity=<your-quantity>` : To place an order<br><br>
 `PUT /api/v1/orders?status=<accepted> or <declined>` : To update the status of an order
 
 The api is hosted on Heroku at
 
 [https://actlikewill-fastfoodfast.herokuapp.com/api/v1/orders](https://actlikewill-fastfoodfast.herokuapp.com/api/v1/orders)
 
 Use [Postman](https://www.getpostman.com/) to test the various endpoints as specified above.
