CREATE TABLE PointChangeLog (
    point_log_id BIGINT NOT NULL AUTO_INCREMENT,
    driver_id INT NOT NULL,
    points_change INT NOT NULL,
    reason VARCHAR(255) NOT NULL,
    datetime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (logID),
    FOREIGN KEY (driverID)REFERENCES driver_user(userID)
);