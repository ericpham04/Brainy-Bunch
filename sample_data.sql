INSERT INTO categories(category_name)
VALUES ('Furniture'),('Electronics'),('Kitchen'),('Books'),('Clothing');

INSERT INTO listings(title,description,owner_id,category_id,pickup_location)
VALUES ('Wooden Desk','Lightly used desk',1,1,'Atlanta');

INSERT INTO listing_requests(listing_id,user_id,request_message)
VALUES (1,2,'I would love this desk.');
