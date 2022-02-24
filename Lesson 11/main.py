import  logging
from waitress import serve
# from users_api import app
from books_api import app
logging.basicConfig(level = logging.INFO)
if __name__ == '__main__':
    #logging.info("Starting server")
    serve(app, host='127.0.0.1', port=8041)

