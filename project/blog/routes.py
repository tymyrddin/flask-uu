from . import blog_blueprint
from flask import render_template, abort


blog_post_titles = [
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
]


@blog_blueprint.route("/blog/")
def blog():
    return render_template("blog/blog.html")


@blog_blueprint.route("/<blog_title>/")
def posts(blog_title):
    if blog_title not in blog_post_titles:
        abort(404)

    return render_template(f"blog/{blog_title}.html")


@blog_blueprint.route("/about/")
def about():
    return render_template("blog/about.html")


@blog_blueprint.route("/registration/")
def registration():
    return render_template("blog/registration.html")
