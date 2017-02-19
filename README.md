# flask_gallery_website_python
A gallery website using flask for server side scripting. Built with flask Python, MySQL, Jinja Python, Bootstrap CSS

# Directory Tree for Project
In order to be able to create a project from the repo files, you need to make your dircetories look like this. The virtual environment folder is the containing folder for the project. The other folders except **webapp_gallery** are created automatically in the virtual environment. 

## Linux
```
virtual environment
|
├─ webapp_gallery (folder containing project files)
|   ├── app.py
|   ├── database.py
|   ├── static
|   |    ├ css (contains bootstrap css files)
|   |    ├ fonts (contains bootstrap fonts files)
|   |    ├ images (image storage for gallery)
|   |    ├ js (contains bootstrap js files)
|   |    └── ...
|   └── templates (contains all html files)
|        └── ...
├─ bin
|   └── ...
├─ include
│   └── ...
└─ lib
    └── ...
```
## Windows
```
virtual environment
|
├─ webapp_gallery (folder containing project files)
|   ├── app.py
|   ├── database.py
|   ├── static
|   |    ├ css (contains bootstrap css files)
|   |    ├ fonts (contains bootstrap fonts files)
|   |    ├ images (image storage for gallery)
|   |    ├ js (contains bootstrap js files)
|   |    └── ...
|   └── templates (contains all html files)
|        └── ...
├─ Include
|   └── ...
├─ Lib
│   └── ...
└─ Scripts
    └── ...
```
# Activating Virtual Environments
## Linux
``` /virtual environment$ source activate <name of virtual environment>```

## WIndows
``` /virtual environment/Scripts > activate ```

# Files and Folders
## app.py
Main flask app. Starts the server

## database.py
Contains functions needed to connect to MySQL database>
**NOTE: You need to modify this file.**
Modify the '''config''' dictionary in order to be able to connect to the database.

## templates folder
The templates folder contains html files for the website. It is the default folder where flask looks for all ".html" files call upon from the different functions in the main flask script.

## static folder
* Contains all the bootstrap files (css/javascript)
* folder for storing gallery images


