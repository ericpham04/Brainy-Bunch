CREATE TABLE categories(
 category_id SERIAL PRIMARY KEY,
 category_name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE listings(
 listing_id SERIAL PRIMARY KEY,
 title VARCHAR(150) NOT NULL,
 description TEXT,
 owner_id INTEGER NOT NULL,
 category_id INTEGER,
 pickup_location VARCHAR(255),
 status VARCHAR(30) DEFAULT 'Available',
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE listing_requests(
 request_id SERIAL PRIMARY KEY,
 listing_id INTEGER NOT NULL,
 user_id INTEGER NOT NULL,
 request_message TEXT,
 request_status VARCHAR(30) DEFAULT 'Pending',
 request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE notifications(
 notification_id SERIAL PRIMARY KEY,
 recipient_id INTEGER,
 message TEXT,
 is_read BOOLEAN DEFAULT FALSE,
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE reports(
 report_id SERIAL PRIMARY KEY,
 listing_id INTEGER,
 reporter_id INTEGER,
 reason TEXT,
 status VARCHAR(20) DEFAULT 'Open',
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
