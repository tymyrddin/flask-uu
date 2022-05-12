from . import recipes_blueprint
from flask import render_template, abort


@recipes_blueprint.route("/")
def recipes():
    return render_template("recipes/recipes.html")


