from falcon import App

from  timing_middleware import  TimingMiddleware

from book_views import BooksListResourse,BooksDetailsResourse

middlewares =[
    TimingMiddleware(),
]
books_list = BooksListResourse()
books_details = BooksDetailsResourse()
app = App(middleware = middlewares)
app.add_route("/books",books_list)
app.add_route("/books/{book_id}",books_details)