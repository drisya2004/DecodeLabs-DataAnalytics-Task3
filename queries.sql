-- ==============================
-- PROJECT 3: SQL DATA ANALYSIS
-- ==============================


-- ------------------------------
-- 1. VIEW SAMPLE RECORDS
-- ------------------------------
-- Understand dataset structure
SELECT order_id, date, customer_id, product, total_price
FROM orders
LIMIT 10;


-- ------------------------------
-- 2. TOTAL NUMBER OF ORDERS
-- ------------------------------
-- Count total transactions in dataset
SELECT COUNT(*) AS total_orders
FROM orders;


-- ------------------------------
-- 3. DELIVERED ORDERS
-- ------------------------------
-- Filter only successfully delivered orders
SELECT order_id, customer_id, product, total_price, order_status
FROM orders
WHERE order_status = 'Delivered';


-- ------------------------------
-- 4. HIGHEST ORDER VALUE SORTING
-- ------------------------------
-- Identify high-value transactions
SELECT order_id, customer_id, product, total_price
FROM orders
ORDER BY total_price DESC;


-- ------------------------------
-- 5. TOTAL REVENUE
-- ------------------------------
-- Total business revenue
SELECT SUM(total_price) AS total_revenue
FROM orders;


-- ------------------------------
-- 6. AVERAGE ORDER VALUE
-- ------------------------------
-- Average spending per order
SELECT AVG(total_price) AS average_order_value
FROM orders;


-- ------------------------------
-- 7. ORDERS BY PAYMENT METHOD
-- ------------------------------
-- Understand customer payment preferences
SELECT payment_method, COUNT(*) AS number_of_orders
FROM orders
GROUP BY payment_method;


-- ------------------------------
-- 8. REVENUE BY PRODUCT
-- ------------------------------
-- Product-wise revenue contribution
SELECT product, SUM(total_price) AS revenue
FROM orders
GROUP BY product
ORDER BY revenue DESC;


-- ------------------------------
-- 9. TOP SELLING PRODUCTS
-- ------------------------------
-- Products with highest quantity sold
SELECT product, SUM(quantity) AS total_quantity_sold
FROM orders
GROUP BY product
ORDER BY total_quantity_sold DESC;


-- ------------------------------
-- 10. ORDER STATUS DISTRIBUTION
-- ------------------------------
-- Delivered, Pending, Cancelled breakdown
SELECT order_status, COUNT(*) AS total_orders
FROM orders
GROUP BY order_status;


-- ------------------------------
-- 11. REVENUE BY REFERRAL SOURCE
-- ------------------------------
-- Marketing channel performance
SELECT referral_source, SUM(total_price) AS revenue
FROM orders
GROUP BY referral_source
ORDER BY revenue DESC;


-- ------------------------------
-- 12. MOST USED COUPON CODES
-- ------------------------------
-- Discount usage analysis
SELECT coupon_code, COUNT(*) AS usage_count
FROM orders
WHERE coupon_code IS NOT NULL
GROUP BY coupon_code
ORDER BY usage_count DESC;


-- ------------------------------
-- 13. AVERAGE ORDER VALUE BY PRODUCT
-- ------------------------------
-- Product-wise customer spending behavior
SELECT product, AVG(total_price) AS avg_order_value
FROM orders
GROUP BY product
ORDER BY avg_order_value DESC;


-- ------------------------------
-- 14. TOP 10 HIGH VALUE ORDERS
-- ------------------------------
-- Identify premium transactions
SELECT order_id, customer_id, total_price
FROM orders
ORDER BY total_price DESC
LIMIT 10;


-- ------------------------------
-- 15. POPULAR PAYMENT METHODS (>5 ORDERS)
-- ------------------------------
-- Frequently used payment methods
SELECT payment_method, COUNT(*) AS number_of_orders
FROM orders
GROUP BY payment_method
HAVING COUNT(*) > 5
ORDER BY number_of_orders DESC;