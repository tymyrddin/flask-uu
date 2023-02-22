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
    "games-securityawareness",
    "games-pivotsandpayloads",
    "games-cryptogo",
    "games-doxed",
    "games-dataheist",
    "games-decisionsanddisruptions",
    "games-cornucopia",
    "games-backdoorsandbreaches",
    "games-cisacards",
]

writeups_recipes_names = [
    "writeups-red",
    "writeups-blue",
    "writeups-green",
    "writeups-purple",
]

screencasts_recipes_names = [
    "screencasts-business",
    "screencasts-deserialisation",
    "screencasts-webcache",
]

bbh_recipes_names = [
    "bbh-openbbh",
    "bbh-intigrity",
    "bbh-hackerone",
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


@recipes_blueprint.route("/writeups/")
def writeups_recipes():
    return render_template("recipes/writeups.html")


@recipes_blueprint.route("/screencasts/")
def screencasts_recipes():
    return render_template("recipes/screencasts.html")


@recipes_blueprint.route("/scripts/")
def scripts_recipes():
    return render_template("recipes/scripts.html")


@recipes_blueprint.route("/bbh/")
def bbh_recipes():
    return render_template("recipes/bbh.html")
