from flask import Flask

application = app = Flask(__name__)
application.debug = True

# Initialize Flask extensions here

# Register blueprints here
from app.agents import bp as agents_bp
application.register_blueprint(agents_bp, url_prefix='/agents')

from app.main import bp as main_bp
application.register_blueprint(main_bp)

@application.route('/test/')
def test_page():
    return '<h1>Testing the Flask applicationFactory Pattern</h1>'


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()