# gallery-website-python
A gallery website using flask for server side scripting. Built with flask Python, MySQL, Jinja Python, Bootstrap CSS.

## Set up
* Create a database `gallery`.
* Create a table called `image_data` with VARCHAR columns `name` CHAR, `tags` and `image_link`.
* Put the database details in the `config` file.

## app.py
Main flask app. Starts the server

## database.py
Contains functions needed to connect to MySQL database. **You need to modify this file**.
Modify the `config` dictionary to be able to connect to the database.

## templates folder
The templates folder contains html files for the website. It is the default folder where flask looks for all ".html" files call upon from the different functions in the main flask script.

## static folder
* Contains `fonts`,`css`,`js` all the bootstrap folders and files
* Contains `images` folder for storing gallery images
