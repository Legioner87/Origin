import  logging
# from waitress import serve
# from users_api import app
from books_api import app
logging.basicConfig(level=logging.INFO)

def main():
    from waitress import serve
    logging.info("Starting server")
    serve(app, port="8000")


if __name__ == '__main__':
    main()

