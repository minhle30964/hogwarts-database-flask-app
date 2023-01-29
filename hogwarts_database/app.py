# Making necessary imports
import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request

# Configuring the application
app = Flask(__name__)

# Ensuring the templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configuring the CS50 Library to use SQLite database
db = SQL("sqlite:///characters.db")


# Route for when the user accesses the homepage of the web application
@app.route("/")
# Function index
def index():
    # Returning rendered template of index.html (html file for homepage)
    return render_template("index.html")


# Route for when the user accesses the character database of the web application
@app.route("/database")
# Function database
def database():
    # Initializing a variable to contain all information of all characters in the SQL database
    info = db.execute("SELECT * FROM characters")
    # Returning rendered template of database.html and passing in variable characters set to the info variable above
    return render_template("database.html", characters = info)


# Route for when the user accesses the character's information from the database or search of the web application
@app.route("/view", methods=["GET"])
# Function view
def view():
    # Getting the id of the character whom the user would like to view
    id = request.args.get("id")
    # Initializing a variable to contain all information of this specific character
    info = db.execute("SELECT * FROM characters WHERE Id = ?", id)[0]
    # Returning rendered template of character.html and passing in variable characters set to the info variable above
    return render_template("character.html", character = info)


# Route for when the user makes a search for a character using the search bar of the web application
@app.route("/search", methods=["GET"])
# Function search
def search():
    # Getting the search query that the user inputted into the search bar
    search_query = request.args.get("query")
    # Initializing a variable to contain all information of all characters whose name contains the search query
    info = db.execute("SELECT * FROM characters WHERE Name LIKE ?", "%" + search_query + "%")
    # Returning rendered template of results.html and passing in variable characters set to the info variable above
    return render_template("results.html", characters = info)
