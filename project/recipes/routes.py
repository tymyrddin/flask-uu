from . import recipes_blueprint
from flask import render_template

labs_recipes_names = [
    "labs-thm",
    "labs-portswigger",
    "labs-htb",
    "labs-rootme",
    "labs-btlo",
    "labs-offsec",
]

scripts_recipes_names = [
    "scripts-network",
    "scripts-webapp",
    "scripts-cicd",
    "scripts-bash",
    "scripts-ps",
]


@recipes_blueprint.route("/")
def recipes():
    return render_template("recipes/recipes.html")


@recipes_blueprint.route("/labs/")
def labs_recipes():
    return render_template("recipes/labs.html")


@recipes_blueprint.route("/scripts/")
def scripts_recipes():
    return render_template("recipes/scripts.html")