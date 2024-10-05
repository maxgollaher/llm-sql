# Queries
## Zero Shot Examples
Question 1
* Prompt: What is the total amount of all transactions?
* Query: ```sql
SELECT SUM(Amount) AS TotalAmount FROM `Transaction`;```

* DB Response: ```
[[(Decimal('3199.95'),)]]```

* Friendly Response: 3199.95

---
Question 2
* Prompt: What is the average cost of all items?
* Query: ```sql
SELECT AVG(Price) AS AverageCost FROM Item;```

* DB Response: ```
[[(Decimal('566.656667'),)]]```

* Friendly Response: 566.656667

---
Question 3
* Prompt: What is the most expensive item?
* Query: ```sql
SELECT Name, Price FROM Item ORDER BY Price DESC LIMIT 1;```

* DB Response: ```
[[('Laptop', Decimal('999.99'))]]```

* Friendly Response: Laptop

---
Question 4
* Prompt: Who is my most frequent customer?
* Query: ```sql
SELECT u.Username, COUNT(t.Id) AS TransactionCount
FROM `Transaction` t
JOIN `User` u ON t.UserId = u.Id
GROUP BY u.Id
ORDER BY TransactionCount DESC
LIMIT 1;```

* DB Response: ```
[[('johndoe', 2)]]```

* Friendly Response: johndoe

---
Question 5
* Prompt: What is the most popular item?
* Query: ```sql
SELECT ItemId, COUNT(*) AS PurchaseCount
FROM Transaction
GROUP BY ItemId
ORDER BY PurchaseCount DESC
LIMIT 1;```

* DB Response: ```
[[(1, 2)]]```

* Friendly Response: (1, 2)

---
Question 6
* Prompt: Which items are my least productive?
* Query: ```sql
SELECT Item.Id, Item.Name, SUM(Transaction.Amount) AS TotalAmount
FROM Item
LEFT JOIN Transaction ON Item.Id = Transaction.ItemId
GROUP BY Item.Id, Item.Name
ORDER BY TotalAmount ASC;```

* DB Response: ```
[[(3, 'Headphones', Decimal('199.99')), (2, 'Smartphone', Decimal('999.98')), (1, 'Laptop', Decimal('1999.98'))]]```

* Friendly Response: Headphones

---
Question 7
* Prompt: Who is my most profitable customer?
* Query: ```sql
SELECT u.Username, SUM(t.Amount) AS TotalSpent
FROM `Transaction` t
JOIN `User` u ON t.UserId = u.Id
GROUP BY u.Id
ORDER BY TotalSpent DESC
LIMIT 1;```

* DB Response: ```
[[('alice', Decimal('1499.98'))]]```

* Friendly Response: Alice

---
Question 8
* Prompt: Who is my least profitable customer?
* Query: ```sql
SELECT u.Username, SUM(t.Amount) AS TotalSpent
FROM `Transaction` t
JOIN `User` u ON t.UserId = u.Id
GROUP BY u.Id
ORDER BY TotalSpent ASC
LIMIT 1;```

* DB Response: ```
[[('janedoe', Decimal('499.99'))]]```

* Friendly Response: janedoe

---
## Single Domain Examples
Question 1
* Prompt: What is the total amount of all transactions?
* Query: ```sql
SELECT SUM(Amount) AS total_amount FROM Transaction;```

* DB Response: ```
[[(Decimal('3199.95'),)]]```

* Friendly Response: 3199.95

---
Question 2
* Prompt: What is the average cost of all items?
* Query: ```sql
SELECT AVG(Price) AS average_cost FROM Item;```

* DB Response: ```
[[(Decimal('566.656667'),)]]```

* Friendly Response: 566.656667

---
Question 3
* Prompt: What is the most expensive item?
* Query: ```sql
SELECT Name, Price FROM Item ORDER BY Price DESC LIMIT 1;```

* DB Response: ```
[[('Laptop', Decimal('999.99'))]]```

* Friendly Response: Laptop

---
Question 4
* Prompt: Who is my most frequent customer?
* Query: ```sql
SELECT UserId, COUNT(*) AS frequency FROM Transaction GROUP BY UserId ORDER BY frequency DESC LIMIT 1;```

* DB Response: ```
[[(1, 2)]]```

* Friendly Response: Customer 2

---
Question 5
* Prompt: What is the most popular item?
* Query: ```sql
SELECT ItemId FROM Transaction GROUP BY ItemId ORDER BY COUNT(*) DESC LIMIT 1;```

* DB Response: ```
[[(1,)]]```

* Friendly Response: 1

---
Question 6
* Prompt: Which items are my least productive?
* Query: ```sql
SELECT Name FROM Item WHERE Id NOT IN (SELECT ItemId FROM Transaction);```

* DB Response: ```
[[]]```

* Friendly Response: []

---
Question 7
* Prompt: Who is my most profitable customer?
* Query: ```sql
SELECT UserId, SUM(Amount) AS total_spent FROM Transaction GROUP BY UserId ORDER BY total_spent DESC LIMIT 1;```

* DB Response: ```
[[(3, Decimal('1499.98'))]]```

* Friendly Response: Customer ID 3

---
Question 8
* Prompt: Who is my least profitable customer?
* Query: ```sql
SELECT UserId FROM (SELECT UserId, SUM(Amount) AS total FROM Transaction GROUP BY UserId ORDER BY total ASC LIMIT 1) AS t;```

* DB Response: ```
[[(2,)]]```

* Friendly Response: Customer ID: 2

---
