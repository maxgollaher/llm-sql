INSERT INTO `User` (`Id`, `Username`, `Email`, `Password`, `FirstName`, `LastName`)
VALUES
    (1, 'johndoe', 'johndoe@example.com', 'password123', 'John', 'Doe'),
    (2, 'janedoe', 'janedoe@example.com', 'password456', 'Jane', 'Doe'),
    (3, 'alice', 'alice@example.com', 'password789', 'Alice', 'Smith');

INSERT INTO `Item` (`Id`, `Name`, `Price`, `Description`)
VALUES
    (1, 'Laptop', 999.99, 'A high-performance laptop'),
    (2, 'Smartphone', 499.99, 'A latest-gen smartphone'),
    (3, 'Headphones', 199.99, 'Noise-cancelling over-ear headphones');

INSERT INTO `Transaction` (`Id`, `ItemId`, `UserId`, `Amount`, `CreatedAt`)
VALUES
    (1, 1, 1, 999.99, '2024-10-01 10:30:00'),
    (2, 2, 2, 499.99, '2024-10-02 11:00:00'),
    (3, 3, 1, 199.99, '2024-10-03 12:15:00'),
    (4, 1, 3, 999.99, '2024-10-04 09:45:00'),
    (5, 2, 3, 499.99, '2024-10-05 14:20:00');
