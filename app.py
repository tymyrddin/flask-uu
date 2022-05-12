from flask_frozen import Freezer
from project import create_app
from flask_fontawesome import FontAwesome

# Call the application factory function to construct a Flask application
# instance using the development configuration
app = create_app()
fa = FontAwesome(app)

# Create an instance of Freezer for generating the static files from
# the Flask application routes ('/', '/data_analysis', etc.)
freezer = Freezer(app)


if __name__ == "__main__":
    # Run the development server that generates the static files
    # using Frozen-Flask
    freezer.run(debug=True)
