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
            --
        -- The user is: justin@justin.com
        -- Query to set orderItem and connect to order:


