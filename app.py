# ============================================================
# app.py
# Flask application for your personal one-page portfolio site
# ============================================================

from flask import Flask, render_template
import json,os

#app = Flask(__name__)

app = Flask(__name__, static_folder='static', template_folder='templates')

# Load configuration data from config.json
with open('config.json') as config_file:
    config = json.load(config_file)


@app.route('/')
def home():
    """
    Render the main index page.
    Pass configuration data to the HTML template.
    """
    return render_template('index.html', config=config)


if __name__ == '__main__':
    # Development server for local testing.
    # For production, you’ll use a WSGI server (e.g., Gunicorn or Waitress).
    app.run(debug=True)
