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

#adding a 'PAID" column to Orders
ALTER TABLE Orders
ADD is_paid bool NOT NULL 
DEFAULT False;

ALTER TABLE Orders
ADD paid_date DATETIME DEFAULT NULL;


#Create an Order
INSERT INTO Orders (order_id, order_date, customer_id, modified_date)
VALUES(2, '2022-07-24 12:20:56', 3, null);



SELECT * FROM Orders;


CREATE TABLE OrderItems
(
	order_id int NOT NULL,
    book_id int NOT NULL,
    quantity int DEFAULT 1,
    book_price decimal(8,2) NOT NULL,
    FOREIGN KEY(order_id) REFERENCES Orders(order_id),
    FOREIGN KEY(book_id) REFERENCES Books(book_id)
);

ALTER TABLE OrderItems
ADD orderItem_id int PRIMARY KEY NOT NULL; 

##Create an OrderItem!
##To check the stock of the item against the user input, all we need to do is return the stock
SELECT stock FROM Books WHERE Books.book_id = 43;

##Delete an orderItem by id:
SELECT * FROM orderItems;
##Make sure we get the quantity
#save this value:
SELECT book_id, quantity FROM OrderItems WHERE orderItem.id; ##input;
# Update the quantity. if a user deletes an item from their order, then the quantity should be added on to the STOCK
SELECT stock FROM Books WHERE book_id = 43;
SELECT quantity FROM OrderItems WHERE orderItem_id = 1234;
SET @new_stock := (SELECT stock FROM Books WHERE book_id = 43) + (SELECT quantity FROM OrderItems WHERE orderItem_id = 1234);
SELECT @new_stock;
UPDATE Books SET stocks = @new_stock;

DELETE FROM OrderItems WHERE orderItem.id; ##input

## If stock is greater than the user input, let's subtract the input amount from the stock
UPDATE Books SET stock = 23 WHERE book_id = 43;

## Check the new quantity of the book
SELECT * FROM Books WHERE book_id = 43;

## Now create the orderItem
INSERT INTO OrderItems (orderItem_id, order_id, book_id, quantity, book_price)
VALUES(1234,1, 43, 2, 6.00);

## Now Show user the contents of their cart #CREATE VIEW FOR THIS
SELECT b.book_title, 
CONCAT(a.author_fname,' ', a.author_lname) as author,
oi.quantity, oi.book_price 
FROM OrderItems as oi JOIN Orders as o JOIN Books as b JOIN Authors as a
ON oi.order_id = o.order_id AND oi.book_id = b.book_id AND b.author_id = a.author_id
WHERE oi.order_id = 1;

##CREATE VIEW (Needs where condition of order id)
DROP VIEW cart_view;
CREATE VIEW cart_view AS
SELECT b.book_title, 
CONCAT(a.author_fname,' ', a.author_lname) as author,
oi.order_id, oi.quantity, oi.book_price
FROM OrderItems as oi JOIN Orders as o JOIN Books as b JOIN Authors as a
ON oi.order_id = o.order_id AND oi.book_id = b.book_id AND b.author_id = a.author_id;

###CHECKOUT###
## Get total price of order!
SELECT SUM(quantity * book_price) as order_total FROM cart_view
WHERE order_id = 1;
## Update is_paid in order record
UPDATE Orders SET is_paid = 1 WHERE order_id IN (1, 2);
## SET paid_date
UPDATE Orders SET paid_date = NOW() WHERE order_id = 1;
SELECT * FROM Orders;

###USER ORDER HISTORY###
## Get all of the user's orders
SELECT * FROM Orders WHERE customer_id = 1;
## Get total price of order
SELECT SUM(quantity*book_price) as order_total FROM cart_view
WHERE order_id = 1;
## Get all items from order:
SELECT * FROM cart_view WHERE order_id = 1;
## Search by text:
SELECT o.order_id, o.order_date, o.is_completed, o.is_paid FROM Orders as o JOIN OrderItems as oi JOIN Books b JOIN Authors a
ON o.order_id = oi.order_id AND oi.book_id = b.book_id AND b.author_id = a.author_id
WHERE b.book_title LIKE '%ray%'
OR a.author_fname LIKE '%ray%' OR a.author_lname LIKE '%ray%';



SELECT * FROM OrderItems;

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
	SELECT b.book_title, CONCAT(a.author_fname, " ", a.author_lname) AS author_name, b.				book_description, b.book_price, g.genre_name, b.stock
	FROM Books as b JOIN Authors as a JOIN Genres as g
	ON b.author_id = a.author_id AND b.genre_id = g.genre_id
    ORDER BY a.author_lname;
    
DROP VIEW books_view;
    
## See books_view view data
SELECT * FROM Books;

## Get all books by author name
SELECT * FROM books_view WHERE author_name LIKE "%Ma%";
	
## Get all books by title
SELECT * FROM books_view WHERE book_title LIKE "%As%";     

## Adding a column to books
ALTER TABLE Books
ADD stock int NOT NULL 
DEFAULT 25;



######ADMIN STUFF###########
##See all books : use the books_view
##Adding a book:
##First, ask for the author. To check to see if the author exists in the Author's table
SELECT author_id FROM Authors WHERE author_fname = 'Kurt' AND author_lname = 'Vonnegut';
## If an id is returned, we can use this ID as a foreign key in Book Table
## If null is returned, ask if they want to add a new author to the database. if yes:



	

