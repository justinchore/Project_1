-- -Creating a user:
    -- User is prompted "login or create account"
    -- if create account:
            INSERT INTO Users (user_id, first_name, last_name, email_address, password, is_admin, address)
            --values are user input, id will be uiddv4 password will be hashed
            --after validation:
            VALUES(1, "Justin", "Cho", "justin@justin.com", "Password123!", False, "12345 Somewhere st. CA, USA 12345");
        -- The user is logged in -> directed to the main menu (genre, search)
    -- if login:
            -- ask for email, then password
            -- search for email first. If email doesn't exist in the database(null), direct user back to the main menu
            SELECT * FROM Users WHERE email_address = "justin@justin.com";
            -- if user exists, check password
                -- compare data.password with userinput
                -- if successful, direct to books menu. If failed, take user back to input. 
    
-- User's Order
    -- Order Creation Process:
        -- When the user selects a book to put into their order:
                SELECT stock FROM Books WHERE Books.book_id = 43;
            -- if the user's quantity is greater than the book's stock, nothing happens.
        -- Order is made, then an orderItem (with quantity) is created with the selected book
        -- Needed information to create order: 
            -- 1. User's id.
        -- Query to create an Order:
            INSERT INTO Orders (order_id, order_date, customer_id, modified_date)
            VALUES(1, '2022-07-28 12:45:56', 1, null);

            INSERT INTO Orders (order_id, order_date, customer_id, modified_date)
            VALUES(2, '2022-07-24 12:20:56', 3, null);
        -- order_id: from(uuid)
        -- order_date: from(python when user checks out)
        -- customer_id: from(user class or saved dictionary)
        -- modified_date: null to start, changes when admin marks completed
    
    -- OrderItems Process:
        -- Order is made, now let's connect the selected book to the order
        -- The book is: "The Long goodbye by Raymond Chandler"
            --43,"The Long Goodbye","A hard-boiled detective story about gangsters, rich people, dames, drunks, adulterers, and writers. Down-and-out drunk Terry Lennox has a problem: his millionaire wife is dead and he needs to get out of LA fast",6.00,24,2,25
            --44,"Farewell, My Lovely","Private detective Philip Marlowe is investigating a dead-end missing person case when he sees a felon, Moose Malloy, barging into a nightclub called Florian's, looking for his ex-girlfriend Velma Valento. The club has changed owners, so no one now there knows her.",4.99,24,2,25

        -- The user is: justin@justin.com

        -- Query to set orderItem and connect to order:
            --1. Let's change the book's stock according to the quantity given by user
                -- book info given by the currently selected book.
                UPDATE Books SET stock = 23 WHERE book_id = 43;
            --2. Now Create the OrderItem:
                INSERT INTO OrderItems (orderItem_id, order_id, book_id, quantity, book_price) VALUES(1234,1, 43, 2, 6.00);
            --3. Show the contents of order:
                -- Information we need: current order id. 
                SELECT b.book_title, CONCAT(a.author_fname,' ', a.author_lname) as author, oi.quantity, oi.book_price 
                FROM OrderItems as oi JOIN Orders as o JOIN Books as b JOIN Authors as a
                ON oi.order_id = o.order_id AND oi.book_id = b.book_id AND b.author_id = a.author_id 
                --VIEW(cart_view)
                WHERE oi.order_id = 1;

-- Ask user if they want to checkout, or keep shopping
    -- if checkout:
        -- Checking out affects the is_paid field in order
        -- Information needed: Total price of order, gotten from order -> orderItems, then update is_paid field.
        -- Get total price of order: Returns a decimal value
            SELECT SUM(quantity * book_price) as order_total FROM cart_view
            WHERE order_id = 1; 
        -- Checkout, then update the order is_paid and paid_date
            UPDATE Orders SET is_paid = 1 WHERE order_id = 1
            UPDATE Orders SET paid_date = NOW() 
            --NOW()+1 for format
        -- Take user back to main menu
    
    -- if keep shopping, take them back to the books page (preferably where they were)
    -- if exit, logout and shut down

-- Show user all of their orders.
    -- search by author, book_title
    -- sort by desc date, or asc date

    -- Show all of user's orders. All we need is customer_id
        SELECT * FROM Orders WHERE customer_id = 1;
    -- Sort by paid_date:
        SELECT * FROM Orders WHERE customer_id ORDER BY paid_date;
    -- Search by text of OrderItem:
        SELECT o.order_id, o.order_date, o.is_completed, o.is_paid FROM Orders as o JOIN OrderItems as oi JOIN Books b JOIN Authors a
        ON o.order_id = oi.order_id AND oi.book_id = b.book_id AND b.author_id = a.author_id
        WHERE b.book_title LIKE '%ray%'
        OR a.author_fname LIKE '%ray%' OR a.author_lname LIKE '%ray%';
    -- Show total price of order:
        SELECT SUM(quantity * book_price) as order_total FROM cart_view
        WHERE order_id = 1;
    -- Shows all items from order:
        SELECT * FROM cart_view WHERE order_id = 1; 
    



        


    

    



