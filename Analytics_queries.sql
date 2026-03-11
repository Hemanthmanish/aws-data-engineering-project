SELECT region,
SUM(revenue) AS total_revenue
FROM sales_fact
GROUP BY region
ORDER BY total_revenue DESC;
