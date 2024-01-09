-- petlebi_create.sql

CREATE TABLE IF NOT EXISTS petlebi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255),
    name VARCHAR(255),
    price VARCHAR(50),
    category VARCHAR(255),
    stock VARCHAR(10),
    images TEXT,
    brand VARCHAR(255),
    origin VARCHAR(255),
    barkod VARCHAR(255),
    skt VARCHAR(20),
    description TEXT
);
