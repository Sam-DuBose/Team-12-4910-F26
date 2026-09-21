
CREATE TABLE DriverAppLog (
    app_log_id BIGINT NOT NULL AUTO_INCREMENT,
    driver_id INT NOT NULL,
    sponsor_id INT NOT NULL,
    reason VARCHAR(255) NOT NULL,
    datetime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (app_log_id),
    FOREIGN KEY (driver_id) REFERENCES driver_user(user_id),
    FOREIGN KEY (sponsor_id) REFERENCES sponsor_company(sponsor_id)
);