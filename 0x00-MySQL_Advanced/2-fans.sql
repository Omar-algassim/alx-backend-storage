-- show fans number in origin 

SELECT origin, COUNT(*) AS nb_fans 
FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;