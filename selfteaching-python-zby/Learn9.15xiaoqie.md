

#13

List every match with the goals scored by each team as shown. This will use "CASE WHEN" which has not been explained in any previous exercises.

Notice in the query given every goal is listed. If it was a team1 goal then a 1 appears in score1, otherwise there is a 0. You could SUM this column to get a count of the goals scored by team1. Sort your result by mdate, matchid, team1 and team2.


```SQL
SELECT game.mdate, 
game.team1, 
SUM(CASE WHEN goal.teamid = game.team1 THEN 1 ELSE 0 END) AS score1,

game.team2,
SUM(CASE WHEN goal.teamid = game.team2 THEN 1 ELSE 0 END) AS score2



FROM game LEFT JOIN goal ON matchid = id

GROUP BY game.id,game.mdate, game.team1, game.team2 
ORDER BY mdate,matchid,team1,team2

```

补充
```SQL
CASE WHEN condition1 THEN value1 
       WHEN condition2 THEN value2  
       ELSE def_value 
  END 

例子：

SELECT name, population
      ,CASE WHEN population<1000000 
            THEN 'small'
            WHEN population<10000000 
            THEN 'medium'
            ELSE 'large'
       END
  FROM bbc