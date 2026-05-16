import csv
import json
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


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source not in ["json", "csv"]:
        return render_template(
            "product_display.html", error="Wrong source"
        )

    if source == "json":
        data = read_json()
    else:
        data = read_csv()

    if product_id:
        try:
            product_id = int(product_id)
            filtered_data = [
                p for p in data if p.get("id") == product_id
            ]
            if not filtered_data:
                return render_template(
                    "product_display.html",
                    error="Product not found",
                )
            data = filtered_data
        except ValueError:
            return render_template(
                "product_display.html",
                error="Product not found",
            )

    return render_template("product_display.html", products=data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
