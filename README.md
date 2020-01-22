# Bussiness-Online

## Author

Alice Mwihaki

## Description

- This web application allows users to order products of their choice by listing the products then sending the order to the bussiness owner.

## Features

- As a user:

1. You can create account,login,signup

2. You can view products

3.You can order by listing the products in the form

## BDD

| Behaviour                    | input                       | Output                                       |
 -------------| :--------:| -----------|
| View all products | Bussiness page displays all products  | Bussiness page displays all products |
| View all products | Home page displays lista of products  | Home page displays all list products |
|login| Click on **login**|allows user to login into the account using the login form|
|create an account| Click on **sign in**|form which allows users to sign in for the first time|
|List products| Click on **new order**|brings an input form for listing products|
|update/delete| Click on **update/delete**|can updatedor delete the list|

## Technology used

- python
- Flask
- Bootsrap

## Running the application

Modify the start.sh file with your own api key.
To run the app type the commands in your terminal
 install all the dependencies listed in the requirements.txt file
> $ chmod a+x start.sh
>
> $ ./start.sh

## Testing the appication

To run the tests for the class in your terminal
 > $ python3.6 manage.py test

## Known Bugs

- The side bar is not functioning
- The buttons are not functioning
- Unable to post list of items

## Future implements

- The customer, to see the history of all the purchases he/she.
- Business owner,to see a list of all the sales have made.
- Business owner,to see the total amount of sales have made.
- Customer,to receive an error message if tried to purchase a product that’s out of stock.

## Contacts

- For more information :
alicemwihaki99@gmail.com

## Licence

This project is Licensed under MIT. ©2019 Copyright.
