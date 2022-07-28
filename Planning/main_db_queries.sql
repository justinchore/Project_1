use test;

CREATE TABLE Users
(
user_id int NOT NULL,
first_name varchar(255) NOT NULL,
last_name varchar(255) NOT NULL,
email_address varchar(255) NOT NULL UNIQUE,
password varchar(255) NOT NULL,
is_admin Bool NOT NULL,
address varchar(255) NOT NULL,
PRIMARY KEY (user_id)
);

#Create user
INSERT INTO Users (user_id, first_name, last_name, email_address, password, is_admin, address)
##values are user input, id will be uiddv4 password will be hashed
VALUES(1, "Justin", "Cho", "justin@justin.com", "Password123!", False, "12345 Somewhere st. CA, USA 12345");

INSERT INTO Users (user_id, first_name, last_name, email_address, password, is_admin, address)
##values are user input, id will be uiddv4 password will be hashed
VALUES(2, "Mark", "Fadriquela", "mark@mark.com", "Password123@", False, "12345 Someplace 
St. PA, USA 54321"), (3, "Amber", "Lai", "amber@amber.com", "Password123#", False, "09876 Shepard Ave. TX, USA 65432"), (5, "Administrator", "A", "admin@admin.com", "Password123$", True, "76543 Coolidge St. NY, USA");

#Log in
SELECT * FROM Users WHERE email_address = "justi@justin.com";
# 
#Create Orders- order_id, order_date, customer_id 
CREATE TABLE Orders
(
	order_id int NOT NULL,
    order_date DATETIME NOT NULL,
    customer_id int NOT NULL,
    is_completed Bool NOT NULL DEFAULT False,
    modified_date DATETIME ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (order_id),
    FOREIGN KEY(customer_id) REFERENCES Users(user_id)
);

DROP Table Orders;

CREATE TABLE OrderItems
(
	order_id int NOT NULL,
    book_id int NOT NULL,
    quantity int DEFAULT 1,
    book_price decimal(8,2) NOT NULL,
    FOREIGN KEY(order_id) REFERENCES Orders(order_id),
    FOREIGN KEY(book_id) REFERENCES Books(book_id)
);

#Create Books:
#Fields: book name, book description, author_id, genre_id, date_added
CREATE TABLE Books
(
	book_id int NOT NULL, #changed to auto increment
	book_title varchar(255) NOT NULL,
    book_description varchar(1000) NOT NULL,
    book_price decimal(8,2) NOT NULL,
    author_id int NOT NULL,
    genre_id int NOT NULL, 
    PRIMARY KEY(book_id),
    FOREIGN KEY(author_id) REFERENCES Authors(author_id),
    FOREIGN KEY(genre_id) REFERENCES Genres(genre_id)
);

SELECT * FROM Books;

CREATE TABLE Authors
(
	author_id int NOT NULL AUTO_INCREMENT,
    author_fname varchar(255) NOT NULL,
    author_lname varchar(255) NOT NULL,
    PRIMARY KEY(author_id)
);


CREATE TABLE Genres
( 
	genre_id int NOT NULL AUTO_INCREMENT,
    genre_name varchar(255) NOT NULL,
    PRIMARY KEY (genre_id)
);

## DATA INTO GENRES
INSERT INTO Genres (genre_name)
VALUES
		("Science Fiction"),
		("Detective and Mystery"),
        ("Action and Adventure"),
		("Classics");

SELECT * FROM Genres;
SELECT * FROM Authors;

### Get all books from one author
SELECT b.book_title, CONCAT(a.author_fname, " ", a.author_lname) AS author_name, b.book_description, b.book_price, g.genre_name
FROM Books as b
JOIN Authors as a
JOIN Genres as g
ON b.author_id = a.author_id AND b.genre_id = g.genre_id
WHERE a.author_fname = 'Raymond' AND a.author_lname='Chandler';

## Get all books of a certain genre
SELECT b.book_title, CONCAT(a.author_fname, " ", a.author_lname) AS author_name, b.book_description, b.book_price, g.genre_name
FROM Books as b
JOIN Authors as a
JOIN Genres as g
ON b.author_id = a.author_id AND b.genre_id = g.genre_id
WHERE g.genre_id = 1; 

## Create View for booksview!
CREATE VIEW books_view AS 
	SELECT b.book_title, CONCAT(a.author_fname, " ", a.author_lname) AS author_name, b.				book_description, b.book_price, g.genre_name
	FROM Books as b JOIN Authors as a JOIN Genres as g
	ON b.author_id = a.author_id AND b.genre_id = g.genre_id
    ORDER BY a.author_lname;
    
## See books_view view data
SELECT * FROM books_view;

## Get all books by author name
SELECT * FROM books_view WHERE author_name LIKE "%Ma%";
	
## Get all books by title
SELECT * FROM books_view WHERE book_title LIKE "%As%";     
	

