DROP DATABASE IF EXISTS pokemon;
CREATE DATABASE pokemon;
USE pokemon;
CREATE TABLE mypokemon (
	 number INT,
       name	VARCHAR(20),
       type	VARCHAR(10),
       attack INT,
       defense INT,
       capture_date DATE
);
INSERT INTO mypokemon (number, name, type, attack, defense, capture_date)
VALUES (10, 'caterpie', 'bug', 30, 35, '2019-10-14'),
	   (25, 'pikachu', 'electric', 55, 40, '2018-11-04'),
	   (26, 'raichu', 'electric', 90, 55, '2019-05-28'),
      	  (125, 'electabuzz', 'electric', 83, 57, '2020-12-29'),
	   (133, 'eevee', 'normal', 55, 50, '2021-10-03'),
     	   (137, 'porygon', 'normal', 60, 70, '2021-01-16'),
	   (152, 'chikoirita', 'grass', 49, 65, '2020-03-05'),
     	  (153, 'bayleef', 'grass', 62, 80, '2022-01-01');

### DAY 5 ###
          
# 1

select name, length(name)
from mypokemon
order by length(name);

# 2

SELECT name, RANK() OVER (ORDER BY defense DESC) AS defense_rank
FROM mypokemon;

# 3

SELECT name, DATEDIFF('2022-02-14', capture_date) AS days
FROM mypokemon;

SELECT name, DATEDIFF(capture_date, '2022-02-14') AS days
FROM mypokemon;

# 1

select name, RIGHT(name,3) from mypokemon as last_char ;

# 2 

select name, LEFT(name,2) from mypokemon as left2 ;

# 3

select name, replace(name, "o", "O") from mypokemon as bigO where name like "%o%";

# 4 눈여겨서 다시 복습하기!!! 

select name, upper(CONCAT(LEFT(type, 1), RIGHT(type, 1))) as 'type_code', type from mypokemon ;

# 5

select name, length(name) from mypokemon where length(name) > 8 ;

# 6

select round(avg(attack)) as avg_of_attack from mypokemon; 

#7
select round(avg(defense)) as avg_of_defense from mypokemon; 

#8
select name, attack^2 as attack2 from mypokemon where length(name) < 8 ;
#9
select name, attack / 2 as div2 from mypokemon ;

#10
select name, abs(attack - defense) as diff from mypokemon where attack <= 50 ;

# 11

select now(), current_date() as now_date, current_time() as now_time ;

#12
select name, month(capture_date) as month_num , monthname(capture_date) as month_eng 
from mypokemon;

#13

SELECT DAYOFWEEK(capture_date) AS day_num, DAYNAME(capture_date) AS day_eng
FROM mypokemon;

#14
SELECT YEAR(capture_date) AS year, MONTH(capture_date) AS month, DAY(capture_date) AS day
FROM mypokemon;

#### DAY 6 ####

#실습 1-1
select type, avg(weight) 
from mypokemon
where length(name) > 5 
group by type 
having avg(weight) >= 20
ORDER BY 2 desc ;

#실습 1-2

select type, min(height), max(height) 
from mypokemon
where number < 200
group by type
having max(weight) >= 10 and min(weight) >= 2
ORDER BY 2 DESC, 3 desc ;

DROP DATABASE IF EXISTS pokemon;
CREATE DATABASE pokemon;
USE pokemon;
CREATE TABLE mypokemon (
	number  int,
       name	varchar(20),
       type	varchar(10),
       height	float,
       weight	float
);
INSERT INTO mypokemon (number, name, type, height, weight)
VALUES (10, 'caterpie', 'bug', 0.3, 2.9),
	   (25, 'pikachu', 'electric', 0.4, 6),
	   (26, 'raichu', 'electric', 0.8, 30),
          (125, 'electabuzz', 'electric', 1.1, 30),
	   (133, 'eevee', 'normal', 0.3, 6.5),
          (137, 'porygon', 'normal', 0.8, 36.5),
	   (152, 'chikoirita', 'grass', 0.9, 6.4),
          (153, 'bayleef', 'grass', 1.2, 15.8),
          (172, 'pichu', 'electric', 0.3, 2),
          (470, 'leafeon', 'grass', 1, 25.5); 
#실습 2-1

select type, avg(height)
from mypokemon
group by type;

#실습 2-2

select type, avg(weight)
from mypokemon
group by type;

#실습 2-3

select type, avg(height), avg(weight)
from mypokemon
group by type;

#실습 2-4

select type, avg(height)
from mypokemon
group by type
having avg(height) > 0.5;

#실습 2-5

select type, avg(height)
from mypokemon
group by type
having avg(weight) >= 20;

#2-6

select type, sum(number)
from mypokemon
group by type ;

# 2-7

select type, count(1)
from mypokemon
where height > 0.5 
group by type ;

# 2-8

select type, min(height)
from mypokemon
group by type ;

# 2-9
select type, max(weight)
from mypokemon
group by type ;

# 2-10
select type
from mypokemon
group by type 
having min(height) > 0.5 and max(weight) < 30;






