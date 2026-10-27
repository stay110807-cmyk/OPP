CREATE DATABASE login_mvc;

CREATE TABLE users {
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    name_user VARCHAR(50) NOT NULL,
    password_user VARCHAR(50) NOT NULL,
    email_user VARCHAR(100) NOT NULL
}

