from flask import render_template, url_for, request, redirect
from app import app
from models import *
from forms import BookComments, RegisterForm, LoginForm
from datetime import datetime
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash

@app.route("/register", methods = ["GET", "POST"])
def register():
    post_data = request.form
    register_form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(data = post_data)
        if form.validate_on_submit():
            user = User(first_name = form.first_name.data, last_name= form.last_name.data, email = form.email.data, username = form.username.data, password = form.password.data)
            user.save()
        return redirect("/login")
    return render_template("register.html", register_form = register_form)

@app.route("/login", methods = ["GET", "POST"])
def login():
    post_data = request.form
    login_form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data = post_data)
        if form.validate_on_submit():
            user = User.query.filter_by(username = form.username.data).first()
            if user and check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect("/user_index")
    return render_template("login.html", login_form = login_form)

@app.route("/user_index")
@login_required
def user_index():
    return render_template("user_index.html", is_active = True)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route("/")
def index():
    all_books = Book.query.all()
    return render_template("index.html", show_basket = False, books = all_books, active = "Home", is_active = False)

@app.route("/product", methods = ["GET", "POST"])
def product():
    book_name = "Incognito (beyinin gizli həyatı)"
    book_price = 12.00
    book_old_price = 15.00
    book_content = """
    Tanınmış nevroloq D.Iqlmenin 20-dən çox dilə tərcümə edilən və 
    indidən klassik əsərə çevrilən bu kitabı beynin sirli dünyasına 
    təcrübələr, elmi biliklər və tarixi faktlar işığında səyahət edir. 
    Kitab tibbi mövzuda olsa da, müəllif yazarlıq məharətini və zəngin 
    biliyini birləşdirərək elmi faktları sadə və müqayisəli dillə 
    oxuyucularına təqdim edir. Müəllif əsər boyu sədaqət geni, 
    qumarbazlara çevrilən parkinson xəstələri, gen-muhit əlaqəsi, 
    "yaxşı" və "pis" gen, şüuraltı və qərarvermə mexanizmi, məsuliyyət 
    anlayışı, beynin insan həyatında rolu kimi bir çox mövzulara toxunur. 
    Alim bu mövzuların beyinlə əlaqəsini izah etməklə kifayətlənmir, 
    beyinlə bağlı müxtəlif formullar və modellər irəli sürür. İnsan 
    psixologiyası və davranışlarına neyron və gen prizmasından baxmağı 
    öyrədir. Elmi-populyar dildə yazılmış bu kitab xüsusən müəllimlər, 
    psixoloqlar, valideynlər, həkimlər üçün mühüm bilikləri ehtiva edir.
    """ 
    book_image_path = url_for('static', filename = "images/Incognito.png")
    book_count = 2
    book_language = "Azərbaycanca"
    book_genre = "Psixologiya"
    book_author = "David Eagleman"
    book_publish = "Qanun Nəşriyyatı"


    post_data = request.form
    form = BookComments()
    if request.method == "POST":
        form = BookComments(data = post_data)
        if form.validate_on_submit():
            date_of_comment = datetime.now()
            comments = Comments(full_name=form.full_name.data, comment = form.comment.data, date_of_comment=date_of_comment)
            comments.save()
            form.full_name.data = ""
            form.comment.data = ""
    all_comments = Comments.query.all()


    return render_template("product.html", show_basket = True, active = "Product", 
    name = book_name, price = book_price, old_price = book_old_price, content = book_content, 
    image = book_image_path, count = book_count, language = book_language, genre = book_genre, 
    author = book_author, publish = book_publish, form = form, all_comments = all_comments, is_active = True)

@app.route("/book/<int:book_id>",  methods = ["GET", "POST"])
def book(book_id):
    all_books = Book.query.all()
    post_data = request.form
    form = BookComments()
    if request.method == "POST":
        form = BookComments(data = post_data)
        if form.validate_on_submit():
            date_of_comment = datetime.now()
            comments = Comments(full_name=form.full_name.data, comment = form.comment.data, date_of_comment=date_of_comment, comment_id = book_id)
            comments.save()
    all_comments = Comments.query.filter_by(comment_id = book_id).all()
    return render_template("book.html", show_basket = True, form = form, book = all_books[book_id], active = "Book", all_comments = all_comments, is_active = True)