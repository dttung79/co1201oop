from book import Book

def test_book_01():
    b = Book(1, 'Python 101', 'Doan Trung Tung', 100.0)
    assert b.id == 1
    assert b.title == 'Python 101'
    assert b.author == 'Doan Trung Tung'
    assert b.price == 100.0

def test_book_02():
    try:
        b = Book(1, '', 'Doan Trung Tung', 100.0)
        assert False
    except ValueError as e:
        assert str(e) == 'Title cannot be empty'