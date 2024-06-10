SELECT c.CustomerId, COUNT(o.OrderId) AS OrderCount
FROM Customer c
LEFT JOIN Orders o ON c.CustomerId = o.CustomerId
GROUP BY c.CustomerId;