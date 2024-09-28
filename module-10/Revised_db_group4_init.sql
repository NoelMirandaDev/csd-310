-- Creates Database for Outland Adventures  

CREATE DATABASE Outland_Adventures;  
USE Outland_Adventures; 

-- Creates Department Table  
CREATE TABLE Department(   
    DepartmentID INT AUTO_INCREMENT PRIMARY KEY,   
    Department_Name VARCHAR(100)  
); 
  
-- Creates Employees Table  
CREATE TABLE Employees (   
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,   
    Name VARCHAR(100) NOT NULL,   
    DepartmentID INT,    
    CONSTRAINT fk_department   
        FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)   
        ON DELETE SET NULL  
); 

-- Creates Equipment Table  
CREATE TABLE Equipment(   
    EquipmentID INT AUTO_INCREMENT PRIMARY KEY,  
    Equipment_Name VARCHAR (250)  
);  

-- Creates Trip_Information Table  
CREATE TABLE Trip_Information(   
    TripID INT AUTO_INCREMENT PRIMARY KEY,   
    Trip_Date DATE,   
    Location VARCHAR(100),  
    EmployeeID INT,  
    CONSTRAINT fk_employees   
        FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)   
        ON DELETE SET NULL  
); 

-- Creates Booking Table   
CREATE TABLE Booking(
    BookingID INT AUTO_INCREMENT PRIMARY KEY,   
    TripID INT,   
    Date_Booked DATE,   
    CONSTRAINT fk_tripID   
        FOREIGN KEY (TripID) REFERENCES Trip_Information(TripID)   
        ON DELETE SET NULL  
); 

-- Creates Customers Table  
CREATE TABLE Customers(   
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,   
    Name VARCHAR(100),   
    Contact_Info VARCHAR(150),   
    Visa_Status BOOLEAN,   
    Payment_Status BOOLEAN,   
    Inoculations_Status BOOLEAN,  
    Equipment_Bought BOOLEAN,  
    Equipment_Rented BOOLEAN,  
    BookingID INT,    
    CONSTRAINT fk_bookingID   
        FOREIGN KEY (BookingID) REFERENCES Booking(BookingID)   
        ON DELETE SET NULL
); 

-- Creates Inventory Table  
CREATE TABLE Inventory(   
    ItemID INT AUTO_INCREMENT PRIMARY KEY,  
    Date_On_Shelf DATE,   
    Bought_Rented ENUM('bought', 'rented'),  
    EquipmentID INT,  
    CustomerID INT,  
    CONSTRAINT fk_customerID   
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)   
        ON DELETE SET NULL,  
    CONSTRAINT fk_equipmentID   
        FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID)   
        ON DELETE SET NULL  
); 

-- Inserts Data to Department Table  
INSERT INTO Department (DepartmentID, Department_name)   
VALUES  
(1, 'Tourism and Guides'),  
(2, 'Marketing'),  
(3, 'Supply Management'),  
(4, 'Software Development'),  
(5, 'Executive Management'),  
(6, 'Customer Service'); 

-- Inserts Data to Equipment Table  
INSERT INTO Equipment (EquipmentID, Equipment_Name)  
VALUES  
(1, 'First Aid Kit'),  
(2, 'Hiking Boots'),  
(3, 'Tent'),  
(4, 'Hiking Backpack'),  
(5, 'Headlamps'),  
(6, 'Sleeping Bag'); 

-- Inserts Data to Employees Table  
INSERT INTO Employees (EmployeeID, Name, DepartmentID)   
VALUES  
(1, 'Bylthe Timmerson', 5),  
(2, 'Jim Ford', 5),  
(3, 'John "Mac" Macnell', 1),  
(4, 'D.B. "Duke" Marland', 1),  
(5, 'Anita Gallegos', 2),  
(6, 'Dimitri Stravopolous', 3),  
(7, 'Mei Wong', 4),  
(8, 'Josh Smith', 6); 

-- Inserts Data to Trip_Information Table  
INSERT INTO Trip_Information (TripID, Trip_Date, Location, EmployeeID)   
VALUES  
(50, '2024-10-26', 'Africa - Cape Town', 3),  
(51, '2024-11-26', 'Africa - Lagos', 3),  
(52, '2025-01-15', 'Asia - Hong Kong', 4),  
(53, '2025-02-20', 'Asia - Singapore', 3),  
(54, '2025-03-11', 'Asia - Beijing', 4),  
(55, '2025-04-28', 'Southern Europe - Rome', 4); 

-- Inserts Data to Booking Table   
INSERT INTO Booking (BookingID, TripID, Date_Booked)   
VALUES   
(1001, 50, '2024-01-05'),  
(1002, 51, '2024-02-10'),  
(1003, 50, '2024-04-08'),  
(1004, 53, '2024-06-01'),  
(1005, 52, '2024-03-03'),  
(1006, 54, '2024-08-13'); 

-- Inserts Data to Customers Table  
INSERT INTO Customers (CustomerID, Name, Contact_Info, Visa_Status, Payment_Status, Inoculations_Status, Equipment_Bought, Equipment_Rented, BookingID)   
VALUES  
(100, 'Mike Jones', 'mikjones@example.com', FALSE, TRUE, TRUE, TRUE, FALSE, 1001),  
(101, 'Jacob Reynolds', 'jreynolds@example.com', TRUE, TRUE, TRUE, FALSE, TRUE, 1002),  
(102, 'Brian Davey', 'Bdavey@example.com', FALSE, TRUE, TRUE, FALSE, TRUE, 1003),  
(103, 'James Anderson', 'janderson@example.com', TRUE, FALSE, TRUE, FALSE, TRUE, 1004),  
(104, 'Donna Watson', 'dwatson@example.com', TRUE, TRUE, FALSE, FALSE, TRUE, 1005),  
(105, 'Peter Parker', 'pparker@example.com', FALSE, TRUE, TRUE, TRUE, FALSE, 1006); 


-- Inserts Data to Inventory Table  
INSERT INTO Inventory (ItemID, Date_On_Shelf, Bought_Rented, EquipmentID, CustomerID)  
VALUES  
(1000, '2022-01-13', 'bought', 1, 100),  
(1001, '2023-05-12', 'rented', 2, 101),  
(1002, '2024-02-20', 'rented', 3, 102),  
(1003, '2020-12-30', 'rented', 4, 103),  
(1004, '2024-06-09', 'rented', 5, 104),  
(1005, '2024-05-02', 'bought', 6, 105); 

