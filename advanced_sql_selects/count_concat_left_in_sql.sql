--LEFT(str, n) takes n number fo chars (a.k.a first n chars) from string

SELECT CONCAT(Name, CONCAT('(',LEFT(Occupation, 1),')'))
FROM OCCUPATIONS
ORDER BY Name Asc;

SELECT CONCAT('There are a total of ', COUNT(Occupation), ' ', LOWER(Occupation), 's.')
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(Occupation) ASC, Occupation;