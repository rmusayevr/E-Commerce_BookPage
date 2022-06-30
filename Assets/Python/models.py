from extensions import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Genre(db.Model):
    __tablename__ = "Genre"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    genre_name = db.relationship("Book", backref = "genre")

    def __repr__(self):
        return self.name
    
    def __init__(self, name):
        self.name = name
    def save(self):
        db.session.add(self)
        db.session.commit()

class Language(db.Model):
    __tablename__ = "Language"
    id = db.Column(db.Integer, primary_key = True)
    lang_code = db.Column(db.String(10), nullable = False)
    lang_name = db.Column(db.String(50), nullable = False)
    lang = db.relationship("Book", backref = "language")
    def __repr__(self):
        return self.lang_name
    
    def __init__(self, lang_code, lang_name):
        self.lang_code = lang_code
        self.lang_name = lang_name
    def save(self):
        db.session.add(self)
        db.session.commit()

class Book(db.Model):
    __tablename__ = "Book"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    author = db.Column(db.String(50), nullable = False)
    price = db.Column(db.Float(), nullable = False)
    description = db.Column(db.Text, nullable = False)
    image_url = db.Column(db.Text, nullable = False)
    stock = db.Column(db.Integer, nullable = False)
    genre_id = db.Column(db.Integer, db.ForeignKey("Genre.id"), nullable = False)
    language_id = db.Column(db.Integer, db.ForeignKey("Language.id"), nullable = False)

    def __repr__(self):
        return self.title
    
    def __init__(self, title, author, price, description, image_url, stock, genre_id, language_id):
        self.title = title
        self.author = author
        self.price = price
        self.description = description
        self.image_url = image_url
        self.stock = stock
        self.genre_id = genre_id
        self.language_id = language_id
    def save(self):
        db.session.add(self)
        db.session.commit()

class Comments(db.Model):
    __tablename__ = "Comments"
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(30), nullable = False)
    comment = db.Column(db.Text, nullable = False)
    date_of_comment = db.Column(db.DateTime)
    comment_id = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return self.full_name
    
    def __init__(self, full_name, comment, date_of_comment, comment_id):
        self.full_name = full_name
        self.comment = comment
        self.date_of_comment = date_of_comment
        self.comment_id = comment_id

    def save(self):
        db.session.add(self)
        db.session.commit()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(30), nullable = False, unique = True)
    username = db.Column(db.String(30), nullable = False, unique = True)
    password = db.Column(db.String(255), nullable = False)
    is_active = db.Column(db.Boolean, default = True)
    is_superuser = db.Column(db.Boolean, default = True)

    def __init__(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)


    def save(self):
        db.session.add(self)
        db.session.commit()

    def check_password(self, password):
        return check_password_hash(self.password, password)

    