from decimal import Decimal
from jinja2 import Environment, FileSystemLoader

from dataclasses import dataclass
from utils import read_csv


template_env = Environment(loader=FileSystemLoader(searchpath="./templates"))


def display_price(value: Decimal) -> str:
    value = Decimal(value)
    return "Free" if not value else f"£{Decimal(value):.2f}"


template_env.filters["display_price"] = display_price

template = template_env.get_template("index.html")


@dataclass
class Book:

    id: int
    listed_at: str
    name: str
    price: Decimal
    type: str
    contact: str
    available: str


books = read_csv("books.csv", cls=Book)


html = template.render(items=books)


with open("index.html", "w") as file:
    file.write(html)

print("Done")



