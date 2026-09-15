CREATE TABLE Sponsor ( 
  sponsor_id INT PRIMARY KEY,
  sponsor_name VARCHAR(100) NOT NULL,
  point_value DECIMAL(10,2) NOT NULL DEFAULT 0.01
);
