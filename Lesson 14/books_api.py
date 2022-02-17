from falcon import App
from kombu import Connection
import config

from timing_middleware import TimingMiddleware
from stat_middleware import StatMiddleware

from book_views import BooksListResourse, BooksDetailsResourse

connection = Connection(config.AMQP_CONNECTION_URL)
stats_middleware = StatMiddleware(
    connection=connection,
    queue_name=config.STAT_QUEUE_NAME,
)
middlewares =[
    stats_middleware,
    TimingMiddleware(),
]
books_list = BooksListResourse()
books_details = BooksDetailsResourse()
app = App(middleware = middlewares)
app.add_route("/books",books_list)
app.add_route("/books/{book_id}", books_details)