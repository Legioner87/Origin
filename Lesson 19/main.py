from models import Authors, Books
from models.base import Base, engine
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    Session as SessionType,
)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

def create_author(session: SessionType, username: str) -> Authors:
    author = Authors(name=username)

    session.add(author)
    session.commit()

    return author

def create_book(session: SessionType, title: str, body: str, author_id: int) -> Books:
    author = session.query(Authors).filter_by(id=author_id).one()
    book = Books(title=title, body=body, author_id=author.id)

    session.add(book)
    session.commit()

    return book

def main():
    session = Session()

    # daniel = create_author(session, 'Daniel')
    #
    # another_daniel = session.get(Authors, daniel.id)
    # print("a_daniel: ", another_daniel)
    #
    # oks = create_author(session, 'Oks')
    # another_oks = session.get(Authors, oks.id)
    # print("a_oks: ", another_oks)

    create_book(session, 'From Novokuznetsk with Love!', 'dsadsadsadsadada', 1)
    create_book(session, 'Train 2033', 'dsadsadsadsadada', 2)
    create_book(session, 'Without you :(', 'dsadsadsadsadada', 1)

    session.close()

    # Base.metadata.create_all() # NEVER

if __name__ == '__main__':
    main()