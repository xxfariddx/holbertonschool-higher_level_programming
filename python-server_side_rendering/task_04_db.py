#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv
import os
import sqlite3

app = Flask(__name__)


def get_data_from_db():
    """
    get_data_from_db

    Return a tuple from DB with products information
    The tuple is converted into dictionnary to be displayed in HTML

    Returns:
        dict: data from DB (products informations)
    """
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    data_tuple = cursor.fetchall()
    connection.close()

    # Switch tuple to lsit of dict (empty list to store into dict)
    data = []

    for item in data_tuple:
        # Create a dictionnary for each product
        product = {
            'id': item[0],
            'name': item[1],
            'category': item[2],
            'price': item[3]
        }
        
        # Append dictionnary to list
        data.append(product)

    return data


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/items")
def items():
    try:
        with open("items.json", "r") as file:
            data = json.load(file)
            items = data.get("items", [])

        return render_template("items.html", items=items)

    except FileNotFoundError:
        return "Items file not found", 404

    except json.JSONDecodeError:
        return "Error decoding JSON", 500


@app.route("/products")
def products():
    # Get from request
    source = request.args.get("source")
    product_id = request.args.get("id")

    data = []

    if source == "json":

        try:
            with open("products.json", 'r') as file:
                reader = json.load(file)
                data = reader

        except FileNotFoundError:
            return render_template(
                "product_display.html", error="File not found")

        except json.JSONDecodeError:
            return render_template(
                "product_display.html", error="Error decoding JSON")

    elif source == "csv":

        try:
            with open("products.csv", newline="") as file:
                reader = csv.DictReader(file)
                data = list(reader)

        except FileNotFoundError:
            return render_template(
                "product_display.html", error="File not found")

        except json.JSONDecodeError:
            return "Error decoding JSON", 500

    elif source == "sql":
        data = get_data_from_db()

    else:
        return render_template("product_display.html", error="Wrong source")

    # Append a dictionnary with only one element to fit with HTML prerequisites
    if product_id:
        filtered = []
        item_found = False
        for item in data:
            if str(item.get("id")) == product_id:
                item_found = True
                filtered.append(item)

        if item_found is True:
            return render_template("product_display.html", products=filtered)
        else:
            return render_template(
                "product_display.html", error="Product not found")

    return render_template("product_display.html", products=data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
