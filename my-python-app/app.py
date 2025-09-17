from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "Docker for Beginners", "author": "Libin Daniel"},
    {"id": 2, "title": "Python Essentials", "author": "Jane Doe"}
]

@app.route('/', methods=['GET'])
def home():
    return "Hello from Flask in Docker!"

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    return jsonify(book) if book else ("Book not found", 404)

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    updated_data = request.get_json()
    for book in books:
        if book["id"] == book_id:
            book.update(updated_data)
            return jsonify(book)
    return ("Book not found", 404)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return ("Book deleted", 204)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
