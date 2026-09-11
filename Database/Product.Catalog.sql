CREATE TABLE ProductCatalog (
  product_id INT PRIMARY KEY,
  sponsor_id INT NOT NULL,
  product_name VARCHAR(100) NOT NULL,
  description VARCHAR(255),
  point_cost INT NOT NULL,
  Availability BOOLEAN,
  image_url VARCHAR(500)
);
