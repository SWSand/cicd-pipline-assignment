from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

def create_app(env='dev'):
    app = Flask(__name__)

    # app.config['SECRET_KEY'] = 'your-secret-key'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    # db.init_app(app)

    @app.route('/')
    def index():
        return "Index"
    
    @app.route('/profile')
    def profile():
        return "Profile"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)