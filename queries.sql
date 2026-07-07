-- Available listings
SELECT * FROM listings WHERE status='Available';

-- Listings by category
SELECT category_name, COUNT(*)
FROM listings
JOIN categories ON listings.category_id=categories.category_id
GROUP BY category_name;

-- Requests for listing
SELECT * FROM listing_requests WHERE listing_id=1;

-- Listings by owner
SELECT * FROM listings WHERE owner_id=1;

-- Unread notifications
SELECT * FROM notifications WHERE is_read=FALSE;
