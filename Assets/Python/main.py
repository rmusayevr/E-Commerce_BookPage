import pymysql.cursors, sys

connection = pymysql.connect(host = "localhost",
                             port = 3306,
                             user = "root",
                             password = "12345",
                             db = "Project",
                             charset = "utf8mb4",
                             cursorclass = pymysql.cursors.DictCursor)

def create_table():
    try:
        with connection.cursor() as cursor:
            sql = """
                create table Book_info (
                    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    title varchar(255) NOT NULL,
                    author varchar(255) NOT NULL,
                    published_at date,
                    exist BOOLEAN DEFAULT TRUE,
                    language varchar(255) NOT NULL,
                    price DOUBLE(16, 2)
                );
            """
            cursor.execute(sql)
        connection.commit()
        print("Table was created!")
    except:
        print("Table has already been created")
def create_book(title, author, published_at, exist, language, price):
    count = 0
    with connection.cursor() as cursor:
        sql = """
            select * from Book_info;
        """
        cursor.execute(sql)
        all_book = cursor.fetchall()
    for i in range(len(all_book)):
        if all_book[i]["title"] != title and all_book[i]["author"] != author:
            count += 1
    if count == len(all_book):
        with connection.cursor() as cursor:
            sql = """
                insert into Book_info(title, author, published_at, exist, language, price) values (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (title, author, published_at, exist, language, price))
        connection.commit()
    else:
        print("There is a book with this title and author! Try to write another book!")
def show_all():
    with connection.cursor() as cursor:
        sql = """
            select * from Book_info;
        """
        cursor.execute(sql)
        all_book = cursor.fetchall()
        if len(all_book) == 0:
            return "There is no book in table!"
        else:
            return all_book
def show_book(id):
    with connection.cursor() as cursor:
        sql = """
            select * from Book_info where id = %s;
        """
        cursor.execute(sql, (id))
        book = cursor.fetchone()
        if book == None:
            return "There is no book with this ID in table! Try again!"
        else:
            return book
def change_status(id):
    with connection.cursor() as cursor:
        sql = """
            update Book_info set exist = not exist where id = %s;
        """
        cursor.execute(sql, (id))
    connection.commit()
def change_price(id, new_price):
    with connection.cursor() as cursor:
        sql = """
                update Book_info set price = %s where id = %s;
            """
        cursor.execute(sql, (new_price, id))
    connection.commit()
def remove(id):
    with connection.cursor() as cursor:
        sql = """
            delete from Book_info where id = %s;
        """
        cursor.execute(sql, (id))
    connection.commit()
def search(word):
    with connection.cursor() as cursor:
        sql = f"select * from Book_info where title like '%{word}%' or author like '%{word}%'"
        cursor.execute(sql)
        return cursor.fetchall()

command = ""
for i in sys.argv[1:]:
    command = command + i + " "

if command == "add table ":
    create_table()
elif command == "add book ":
    Title = input("Enter the name of the book: ")
    Author = input("Enter the name of the author: ")
    Published_at = input("Enter the time when book was published: ")
    Exist = input("Does the book exist?(0 or 1): ")
    Language = input("Enter the language of the book: ")
    Price = float(input("Enter the price of the book (with 2 decimal places):"))
    create_book(Title, Author, Published_at, Exist, Language, Price)
elif command == "show all ":
    print(show_all())
elif command == "show book ":
    ID = int(input("Enter the ID of the book which you want to see: "))
    print(show_book(ID))
elif command == "change status ":
    ID = int(input("Enter the ID of the book which you want to update its status: "))
    change_status(ID)
elif command == "change price ":
    ID = int(input("Enter the ID of the book which you want to update its price: "))
    New_price = float(input("Enter the price of the book (with 2 decimal places):"))
    change_price(ID, New_price)
elif command == "remove ":
    ID = int(input("Enter the ID of the book which you want to remove from table: "))
    remove(ID)
elif command == "search ":
    Word = str(input("Enter the word that you want to search in title or author name: "))
    print(search(Word))