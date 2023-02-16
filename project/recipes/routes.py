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

courses_recipes_names = [
    "courses-metasploid",
    "courses-cybrary",
    "courses-cisa",
    "courses-antisyphon",
]

games_recipes_names = [
    "games-backdoorsandbreaches",
]

pocs_recipes_names = [
    "pocs-red",
    "pocs-blue",
    "pocs-green",
    "pocs-purple",
]


@recipes_blueprint.route("/")
def recipes():
    return render_template("recipes/recipes.html")


@recipes_blueprint.route("/labs/")
def labs_recipes():
    return render_template("recipes/labs.html")


@recipes_blueprint.route("/courses/")
def courses_recipes():
    return render_template("recipes/courses.html")


@recipes_blueprint.route("/games/")
def games_recipes():
    return render_template("recipes/games.html")


@recipes_blueprint.route("/pocs/")
def pocs_recipes():
    return render_template("recipes/pocs.html")


@recipes_blueprint.route("/scripts/")
def scripts_recipes():
    return render_template("recipes/scripts.html")
