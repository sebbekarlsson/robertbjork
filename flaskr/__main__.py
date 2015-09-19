from flaskr import app
from models import initialize_database

if __name__ == '__main__':
    initialize_database()
    app.run()