DB_USER = "example-user"
DB_PASS = "my_cool_secret"
DB_HOST = "127.0.0.1"
DB_PORT = "3306"
DB_NAME = "blog_app"

SQLA_CONNECT_URL=f'mariadb+mariadbconnector://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
SQLA_ECHO=True
