import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    try:
        with open("products.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv():
    products = []
    try:
        with open("products.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                products.append(row)
    except FileNotFoundError:
        pass
    return products


def read_sql(product_id=None):
    products = []
    try:
        conn = sqlite3.connect("products.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        if product_id:
            cursor.execute(
                "SELECT id, name, category, price FROM Products WHERE id = ?",
                (product_id,),
            )
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")

        rows = cursor.fetchall()
        for row in rows:
            products.append(dict(row))

        conn.close()
    except sqlite3.Error:
        return None
    return products


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source not in ["json", "csv", "sql"]:
        return render_template(
            "product_display.html", error="Wrong source"
        )

    if source == "json":
        data = read_json()
        if product_id:
            try:
                product_id = int(product_id)
                data = [p for p in data if p.get("id") == product_id]
            except ValueError:
                data = []

    elif source == "csv":
        data = read_csv()
        if product_id:
            try:
                product_id = int(product_id)
                data = [p for p in data if p.get("id") == product_id]
            except ValueError:
                data = []

    elif source == "sql":
        if product_id:
            try:
                product_id = int(product_id)
            except ValueError:
                return render_template(
                    "product_display.html",
                    error="Product not found",
                )
        data = read_sql(product_id)

        if data is None:
            return render_template(
                "product_display.html",
                error="Database error",
            )

    if not data:
        return render_template(
            "product_display.html", error="Product not found"
        )

    return render_template("product_display.html", products=data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
