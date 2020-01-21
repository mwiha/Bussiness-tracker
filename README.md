# BLOG

## Author

Alice Mwihaki

## Description

- TheBlog is a web application that allows users to express themselves through writing articles and posting the in the application.

## Features

- As a user:

1. You can create,view the posts

2. You can delete and comment on the posts

3.You can create an account,login and update your profile

4.post your own blog

## BDD

| Behaviour                    | input                       | Output                                       |
 -------------| :--------:| -----------|
| View all posts | Home page displays all posts  | Home page displays all posts |
|login| Click on **login**|allows user to login into the account using the login form|
|create an account| Click on **sign in**|form which allos users to sign in for the first time|
|post a blog| Click on **Post Blog**|brings an input form for posting a blog|
|like a post/dislike| Click on **like/dislike**|The number of likes and dislikes increases by one |
|comment on a post| Click on **comment**|Display a comment box to allow users to post a comment on a specific blog|
|Update profile| Click on **Profile** |Takes the user to the profile page with options to edit and upload profile picture|

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

## Contacts

- For more information :
alicemwihaki99@gmail.com

## Licence

This project is Licensed under MIT. ©2019 Copyright.
