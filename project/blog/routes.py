from . import blog_blueprint
from flask import render_template, abort


blog_post_titles = [
    "eu-os-funding",
    "new-password",
    "credentials",
    "defendable-internet",
    "completely-different",
    "nowai",
    "grey-areas",
    "internet-insecurity-trends",
    "panopticon",
    "not-enough",
    "scenario-logics",
    "legitimisation-patterns",
    "ghost-stories",
    "cracked-architecture",
    "information-war-technology",
    "udhr",
    "cracked-surveillance",
    "fvey-alliance",
    "iccpr",
    "oecd-recommendations",
    "data-retention-legislation-eu",
    "gdpr",
    "noble",
    "pagers",
    "mini-clouds",
]


@blog_blueprint.route("/blog/")
def blog():
    return render_template("blog/blog.html")


@blog_blueprint.route("/<blog_title>/")
def posts(blog_title):
    if blog_title not in blog_post_titles:
        abort(404)

    return render_template(f"blog/{blog_title}.html")

