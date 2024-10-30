from database import get_connection

class Emprestimo():
    def __init__(self, data, user, book):
        self.data = data
        self.user_id = user
        self.book_id = book

    def save(self):
        conn = get_connection()
        conn.execute("INSERT INTO emprestimo(data, user_id, book_id) values(?,?,?)", 
            (self.data, self.user_id, self.book_id))
        conn.commit()
        conn.close()
        return True

    @classmethod
    def all(cls):
        conn = get_connection()
        emprestimo = conn.execute("SELECT * FROM emprestimo").fetchall()
        return emprestimo