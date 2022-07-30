--ADMIN FUNCTIONALITY LIST--

-- Before each functionality check to see if user.is_admin is TRUE!
    
-- 1. See all books
    CREATE VIEW books_view AS 
	SELECT b.book_title, CONCAT(a.author_fname, " ", a.author_lname) AS author_name, b.				book_description, b.book_price, g.genre_name, b.stock
	FROM Books as b JOIN Authors as a JOIN Genres as g
	ON b.author_id = a.author_id AND b.genre_id = g.genre_id
    ORDER BY a.author_lname;
-- 2. Add a book
    -- Get input: 'author firstname' and author lastname
    -- If author doesnt't exist in the Authors table, ask to create a new entry
    SELECT CONCAT(author_fname, " ", author_lname) as author_name FROM Authors WHERE author_name LIKE 'Kurt Vonnegut'; --Gets all authors that is like the input
    -- User will pick from genres
    -- Get title
    -- Enter in Description
    -- Enter book price
    -- Enter in Stock


-- 3. Delete a book
-- 4. Update a book
-- 5. Restock warning
-- 6. Best selling books (top 10?)

--------------------------------------------------------------------

-- 1. See all orders
-- 2. Update order to completed
-- 3. Search orders by user
-- 4. Search order by completed
