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
    -- 
