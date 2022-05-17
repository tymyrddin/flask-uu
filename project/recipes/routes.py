from . import recipes_blueprint
from flask import render_template


@recipes_blueprint.route("/")
def recipes():
    return render_template("recipes/recipes.html")
