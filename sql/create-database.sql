-- Drop existing tables
DROP TABLE IF EXISTS `Transaction`;
DROP TABLE IF EXISTS `Item`;
DROP TABLE IF EXISTS `User`;

-- Create User table
CREATE TABLE `User` (
    `Id` INT,
    `Username` VARCHAR(50) NOT NULL,
    `Email` VARCHAR(100) NOT NULL,
    `Password` VARCHAR(200) NOT NULL,
    `FirstName` VARCHAR(50) NULL,
    `LastName` VARCHAR(50) NULL,
    CONSTRAINT PK_Users PRIMARY KEY (`Id`)
);

-- Create Item table
CREATE TABLE `Item` (
    `Id` INT NOT NULL,
    `Name` VARCHAR(100) NOT NULL,
    `Price` DECIMAL(10, 2) NOT NULL,
    `Description` VARCHAR(200) NULL,
    CONSTRAINT `PK_Item` PRIMARY KEY (`Id`)
);

-- Create Transaction table
CREATE TABLE `Transaction` (
    `Id` INT NOT NULL,
    `ItemId` INT NOT NULL,
    `UserId` INT NOT NULL,
    `Amount` DECIMAL(10, 2) NOT NULL,
    `CreatedAt` DATETIME NOT NULL,
    CONSTRAINT FK_Transaction_User FOREIGN KEY (`UserId`) REFERENCES `User` (`Id`),
    CONSTRAINT FK_Transaction_Item FOREIGN KEY (`ItemId`) REFERENCES `Item` (`Id`)
);