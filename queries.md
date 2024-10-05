# Queries
## Zero Shot Examples
Question 1
* Prompt: What is the total amount of all transactions?
* Query: 
```mysql
SELECT SUM(Amount) AS TotalAmount FROM `Transaction`;
```

* DB Response: 
```text
[[(Decimal('3199.95'),)]]
```

* Friendly Response: 3199.95

---
Question 2
* Prompt: What is the average cost of all items?
* Query: 
```mysql
SELECT AVG(Price) AS AverageCost FROM Item;
```

* DB Response: 
```text
[[(Decimal('566.656667'),)]]
```

* Friendly Response: 566.656667

---
Question 3
* Prompt: What is the most expensive item?
* Query: 
```mysql
SELECT Name, Price FROM Item ORDER BY Price DESC LIMIT 1;
```

* DB Response: 
```text
[[('Laptop', Decimal('999.99'))]]
```

* Friendly Response: Laptop

---
Question 4
* Prompt: Who is my most frequent customer?
* Query: 
```mysql
SELECT UserId, COUNT(*) AS PurchaseCount
FROM Transaction
GROUP BY UserId
ORDER BY PurchaseCount DESC
LIMIT 1;
```

* DB Response: 
```text
[[(1, 2)]]
```

* Friendly Response: Customer ID: 1

---
Question 5
* Prompt: What is the most popular item?
* Query: 
```mysql
SELECT ItemId, COUNT(*) AS PurchaseCount
FROM `Transaction`
GROUP BY ItemId
ORDER BY PurchaseCount DESC
LIMIT 1;
```

* DB Response: 
```text
[[(1, 2)]]
```

* Friendly Response: (1, 2)

---
Question 6
* Prompt: Which items are my least productive?
* Query: 
```mysql
SELECT Item.Id, Item.Name, SUM(Transaction.Amount) AS TotalAmount
FROM Item
LEFT JOIN Transaction ON Item.Id = Transaction.ItemId
GROUP BY Item.Id, Item.Name
ORDER BY TotalAmount ASC;
```

* DB Response: 
```text
[[(3, 'Headphones', Decimal('199.99')), (2, 'Smartphone', Decimal('999.98')), (1, 'Laptop', Decimal('1999.98'))]]
```

* Friendly Response: Headphones

---
Question 7
* Prompt: Who is my most profitable customer?
* Query: 
```mysql
SELECT u.Username, SUM(t.Amount) AS TotalSpent
FROM `Transaction` t
JOIN `User` u ON t.UserId = u.Id
GROUP BY u.Id
ORDER BY TotalSpent DESC
LIMIT 1;
```

* DB Response: 
```text
[[('alice', Decimal('1499.98'))]]
```

* Friendly Response: Alice

---
Question 8
* Prompt: Who is my least profitable customer?
* Query: 
```mysql
SELECT u.Username, SUM(t.Amount) AS TotalSpent
FROM `Transaction` t
JOIN `User` u ON t.UserId = u.Id
GROUP BY u.Id
ORDER BY TotalSpent ASC
LIMIT 1;
```

* DB Response: 
```text
[[('janedoe', Decimal('499.99'))]]
```

* Friendly Response: janedoe

---
## Single Domain Examples
Question 1
* Prompt: What is the total amount of all transactions?
* Query: 
```mysql
SELECT SUM(Amount) AS total_amount FROM Transaction;
```

* DB Response: 
```text
[[(Decimal('3199.95'),)]]
```

* Friendly Response: 3199.95

---
Question 2
* Prompt: What is the average cost of all items?
* Query: 
```mysql
SELECT AVG(Price) AS average_cost FROM Item;
```

* DB Response: 
```text
[[(Decimal('566.656667'),)]]
```

* Friendly Response: 566.656667

---
Question 3
* Prompt: What is the most expensive item?
* Query: 
```mysql
SELECT Name, Price FROM Item ORDER BY Price DESC LIMIT 1;
```

* DB Response: 
```text
[[('Laptop', Decimal('999.99'))]]
```

* Friendly Response: Laptop

---
Question 4
* Prompt: Who is my most frequent customer?
* Query: 
```mysql
SELECT UserId, COUNT(*) AS purchase_count FROM Transaction GROUP BY UserId ORDER BY purchase_count DESC LIMIT 1;
```

* DB Response: 
```text
[[(1, 2)]]
```

* Friendly Response: Customer ID 1

---
Question 5
* Prompt: What is the most popular item?
* Query: 
```mysql
SELECT ItemId FROM Transaction GROUP BY ItemId ORDER BY COUNT(*) DESC LIMIT 1;
```

* DB Response: 
```text
[[(1,)]]
```

* Friendly Response: 1

---
Question 6
* Prompt: Which items are my least productive?
* Query: 
```mysql
SELECT Name FROM Item WHERE Id NOT IN (SELECT DISTINCT ItemId FROM Transaction);
```

* DB Response: 
```text
[[]]
```

* Friendly Response: []

---
Question 7
* Prompt: Who is my most profitable customer?
* Query: 
```mysql
SELECT UserId, SUM(Amount) AS total_spent FROM Transaction GROUP BY UserId ORDER BY total_spent DESC LIMIT 1;
```

* DB Response: 
```text
[[(3, Decimal('1499.98'))]]
```

* Friendly Response: Customer ID 3

---
Question 8
* Prompt: Who is my least profitable customer?
* Query: 
```mysql
SELECT UserId FROM Transaction GROUP BY UserId ORDER BY SUM(Amount) ASC LIMIT 1;
```

* DB Response: 
```text
[[(2,)]]
```

* Friendly Response: Customer ID: 2

---
