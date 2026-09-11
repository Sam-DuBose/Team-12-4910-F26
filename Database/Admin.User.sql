  CREATE TABLE AdminUser (
    admin_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);
