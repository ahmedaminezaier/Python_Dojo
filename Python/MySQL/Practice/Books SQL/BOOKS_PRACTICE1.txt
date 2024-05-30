SELECT * FROM books_schema.users;
-- Insert 5 different users
INSERT INTO users (name) VALUES ('Jane Amsden');
INSERT INTO users (name) VALUES ('Emily Dixon');
INSERT INTO users (name) VALUES ('Theodore Dostoevsky');
INSERT INTO users (name) VALUES ('William Shapiro');
INSERT INTO users (name) VALUES ('Lao Xiu');

-- Insert 5 books with the following names
INSERT INTO books (title, num_of_pages) VALUES ('C Sharp', 100);
INSERT INTO books (title, num_of_pages) VALUES ('Java', 200);
INSERT INTO books (title, num_of_pages) VALUES ('Python', 300);
INSERT INTO books (title, num_of_pages) VALUES ('PHP', 400);
INSERT INTO books (title, num_of_pages) VALUES ('Ruby', 500);

-- Change the name of the C Sharp book to C#
UPDATE books SET title = 'C#' WHERE title = 'C Sharp';

-- Change the first name of the 4th user to Bill
UPDATE users SET name = 'Bill Shapiro' WHERE name = 'William Shapiro';

-- Have the first user favorite the first 2 books
SELECT * FROM users 
JOIN favorites ON users.id = favorites.user_id 
JOIN books ON books.id = favorites.book_id;



-- Have the second user favorite the first 3 books
SELECT * FROM books_schema.favorites;
INSERT INTO favorites (user_id, book_id) VALUES (2, 1);
INSERT INTO favorites (user_id, book_id) VALUES (2, 2);
INSERT INTO favorites (user_id, book_id) VALUES (2, 3);

-- Have the third user favorite the first 4 books
SELECT * FROM books_schema.favorites;
INSERT INTO favorites (user_id, book_id) VALUES (3, 1);
INSERT INTO favorites (user_id, book_id) VALUES (3, 2);
INSERT INTO favorites (user_id, book_id) VALUES (3, 3);
INSERT INTO favorites (user_id, book_id) VALUES (3, 4);

-- Have the fourth user favorite all the books
SELECT * FROM books_schema.favorites;
INSERT INTO favorites (user_id, book_id) VALUES (4, 1);
INSERT INTO favorites (user_id, book_id) VALUES (4, 2);
INSERT INTO favorites (user_id, book_id) VALUES (4, 3);
INSERT INTO favorites (user_id, book_id) VALUES (4, 4);
INSERT INTO favorites (user_id, book_id) VALUES (4, 5);

-- Retrieve all the users who favorited the 3rd book
SELECT u.name
FROM users u
JOIN favorites f ON u.id = f.user_id
WHERE f.book_id = 3;

-- Remove the first user from the 3rd book's favorites
DELETE FROM favorites
WHERE user_id = 1 AND book_id = 3;

-- Have the 5th user favorite the 2nd book
INSERT INTO favorites (user_id, book_id, created_at, updated_at) VALUES (5, 2, NOW(), NOW());

-- Find all the books that the 3rd user favorited
SELECT b.title
FROM books b
JOIN favorites f ON b.id = f.book_id
WHERE f.user_id = 3;

-- Find all the users that favorited the 5th book
SELECT u.name
FROM users u
JOIN favorites f ON u.id = f.user_id
WHERE f.book_id = 5;