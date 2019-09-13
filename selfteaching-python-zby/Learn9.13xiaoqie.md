

SQL :
Apostrophe

Find all details of the prize won by EUGENE O'NEILL

Escaping single quotes
You can't put a single quote in a quote string directly. You can use two single quotes within a quoted string.

how ?

```SQL
SELECT * FROM nobel
WHERE winner  like  'EUGENE O''NEILL'
```

Knights in order

List the winners, year and subject where the winner starts with Sir. Show the the most recent first, then by name order.

```SQL
SELECT winner, yr, subject
FROM nobel
WHERE winner like 'Sir%'
ORDER by yr DESC, winner 
```


The expression subject IN ('Chemistry','Physics') can be used as a value - it will be 0 or 1.

Show the 1984 winners and subject ordered by subject and winner name; but list Chemistry and Physics last.

```SQL
SELECT winner, subject,ORDER BY subject IN ('Physics','Chemistry')
 FROM nobel
 WHERE yr=1984
 ORDER BY subject IN ('Physics','Chemistry'), subject,winner
 # CASE WHEN subject IN ('Physics','Chemistry') THEN 1 ELSE 0 END,subject,winner

```