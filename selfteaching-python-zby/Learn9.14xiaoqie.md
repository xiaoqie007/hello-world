
List each country name where the population is larger than that of 'Russia'.
```SQL
SELECT name FROM world
WHERE population >
    (SELECT population FROM world
    WHERE name = 'Russia')

```

Which country has a population that is more than Canada but less than Poland? Show the name and the population.

```SQL
SELECT name, population FROM world
WHERE population > (SELECT population FROM world WHERE name = 'Canada')
     AND population < (SELECT population FROM world WHERE name = 'Poland') 
```

# ROUND

ROUND(f,p) returns f rounded to p decimal places.

The number of decimal places may be negative, this will round to the nearest 10 (when p is -1) or 100 (when p is -2) or 1000 (when p is -3) etc..

```SQL
ROUND(7253.86, 0)    ->  7254
ROUND(7253.86, 1)    ->  7253.9
ROUND(7253.86,-3)    ->  7000
```

# FLOOR
FLOOR(f) returns the integer value of f

FLOOR(f) give the integer that is equal to, or just less than f. FLOOR always rounds down.

```SQL
FLOOR(2.7) ->  2
FLOOR(-2.7) -> -3
```

Germany (population 80 million) has the largest population of the countries in Europe. Austria (population 8.5 million) has 11% of the population of Germany.

Show the name and the population of each country in Europe. Show the population as a percentage of the population of Germany.

Decimal places
Percent symbol %
You can use the function CONCAT to add the percentage symbol.

```SQL
SELECT name,
     CONCAT(ROUND((100*population/(SELECT population
                           FROM world
                          WHERE name = 'Germany'))), '%')
FROM world
WHERE continent = 'Europe'
```
#ROUND(n),保留小数点数， n= 1：小数点后1位； n = -1，小数点前0的个数

CONCAT 增加一个‘%’号

We can use the word **ALL** to allow >= or > or < or <=to act over a list. For example, you can find the largest country in the world, by population with this query:

```SQL
SELECT name
  FROM world
 WHERE population >= ALL(SELECT population
                           FROM world
                          WHERE population>0)
```

小提示：

> You need the condition population>0 in the sub-query as some countries have null for population.


Find the largest country (by area) in each continent, show the continent, the name and the area:

```SQL
SELECT continent, name, area FROM world x
  WHERE area >= ALL
    (SELECT area FROM world y
        WHERE y.continent=x.continent
          AND area>0)

```

Let’s focus on what I understand so far.


- ALL means each or every
- world x filters for area larger than ALL area in world y continents
- WHERE in world y filters through and inside continents, and that y.continent and x.continent are “merged” attributes and tuples?


I assume that other problems are going to be about world x and world y.





- Using correlated subqueries

A correlated subquery works like a nested loop: the subquery only has access to rows related to a single record at a time in the outer query. The technique relies on table aliases to identify two different uses of the same table, one in the outer query and the other in the subquery.

One way to interpret the line in the WHERE clause that references the two table is “… where the correlated values are the same”.

In the example provided, you would say “select the country details from world where the population is greater than or equal to the population of all countries where the continent is the same”.


Exploring more of world x and world y problems!
The next problem states: List each continent and the name of the country that comes first alphabetically.
SELECT continent, name FROM world x
WHERE name <= ALL(SELECT name FROM world y WHERE y.continent = x.continent)


Some countries have populations more than three times that of any of their neighbours (in the same continent). Give the countries and continents.

SELECT name, continent
FROM world x
WHERE population > ALL(SELECT population*3 FROM world y
                   WHERE x.continet = y.continent
                   AND population > 0, x.name != y.name)
