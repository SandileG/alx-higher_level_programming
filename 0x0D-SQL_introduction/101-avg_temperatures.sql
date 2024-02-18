-- Select the city and calculate the average temperature for each city

SELECT city, AVG(temperature) AS avg_temp
FROM weather
GROUP BY city
ORDER BY avg_temp DESC;
