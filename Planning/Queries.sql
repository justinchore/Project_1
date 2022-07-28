-- 1. Get all of the books from an author:
--     - Show user list of authors.
--     - User chooses one author
--     - Query: 
                SELECT b.book_title, CONCAT(a.author_fname, " ", a.author_lname) AS author_name, b.book_description, b.book_price, g.genre_name
                FROM Books as b JOIN Authors as a JOIN Genres as g
                ON b.author_id = a.author_id AND b.genre_id = g.genre_id
                WHERE a.author_fname = 'Raymond' 
                AND a.author_lname = 'Chandler';

        -- Returns back a table of books with the following: title, author, description, price, genre

--      - User selects a book. Show description, and genre


-- 2. Get all books of a certain Genre: 
        -- - User is presented with genres
             SELECT genre_name FROM Genres
        -- When user selects a genre:
             
-- 3. Search all books, filter by string: