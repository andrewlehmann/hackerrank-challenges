/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT CITY, LENGTH(CITY)
FROM (SELECT CITY, MIN(LENGTH(CITY))
      FROM STATION
      GROUP BY CITY
      ORDER BY LENGTH(CITY) ASC, CITY ASC)
WHERE ROWNUM = 1;

SELECT CITY, LENGTH(CITY)
FROM (SELECT CITY, MAX(LENGTH(CITY))
     FROM STATION
     GROUP BY CITY
     ORDER BY LENGTH(CITY) DESC, CITY ASC)
WHERE ROWNUM = 1;