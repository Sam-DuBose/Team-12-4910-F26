CREATE TABLE SponsorUser (
    sponsor_user_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    sponsor_id INT NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,

    PRIMARY KEY (sponsor_user_id),
    FOREIGN KEY (user_id) REFERENCES UserAccount(user_id),
    FOREIGN KEY (sponsor_id) REFERENCES Sponsor(sponsor_id)
);
