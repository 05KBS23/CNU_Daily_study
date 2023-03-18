DROP DATABASE IF EXISTS pokemon;
CREATE DATABASE pokemon;
USE pokemon;
CREATE TABLE mypokemon (
            number int,
            name varchar(20),
            type varchar(20),
            height float,
            weight float,
            attack float,
            defense float,
            speed float
            );
INSERT INTO mypokemon (number, name, type, height, weight, attack, defense, speed)
VALUES (10, 'caterpie', 'bug', 0.3, 2.9, 30, 35, 45),
       (25, 'pikachu', 'electric', 0.4, 6, 55, 40, 90),
       (26, 'raichu', 'electric', 0.8, 30, 90, 55, 110),
       (133, 'eevee', 'normal', 0.3, 6.5, 55, 50, 55),
       (152, 'chikoirita', 'grass', 0.9, 6.4, 49, 65, 45);

/*
MISSION (1)
이브이의 타입을 가져와 주세요.
*/
SELECT type
FROM mypokemon
WHERE name = 'eevee';

/*
MISSION (2)
캐터피의 공격력과 방어력을 가져와 주세요.
*/
SELECT attack, defense
FROM mypokemon
WHERE name = 'caterpie';

/*
MISSION (3)
몸무게가 6kg보다 큰 포켓몬들의 모든 데이터를 가져와 주세요.
*/
SELECT *
FROM mypokemon
WHERE weight > 6;

/*
MISSION (4)
키가 0.5m보다 크고, 몸무게가 6kg보다 크거나 같은 포켓몬들의 이름을 가져와 주세요.
*/
SELECT name
FROM mypokemon
WHERE height > 0.5 AND weight >= 6;

/*
MISSION (5)
포켓몬 테이블에서 공격력이 50 미만이거나, 방어력이 50 미만인 포켓몬들의 이름을
‘weak_pokemon’이라는 별명으로 가져와 주세요.
*/
SELECT name AS weak_pokemon
FROM mypokemon
WHERE attack < 50 OR defense < 50;

/*
MISSION (6)
노말 타입이 아닌 포켓몬들의 데이터를 전부 가져와 주세요.
*/
SELECT *
FROM mypokemon
WHERE type != 'normal';

SELECT *
FROM mypokemon
WHERE NOT(type = 'normal');

/*
MISSION (7)
타입이 (normal, fire, water, grass) 중에 하나인 포켓몬들의 이름과 타입을 가져와 주세요.
*/
SELECT name, type
FROM mypokemon
WHERE type IN ('normal', 'fire', 'water', 'grass');

/*
MISSION (8)
공격력이 40과 60 사이인 포켓몬들의 이름과 공격력을 가져와 주세요.
*/
SELECT name, attack
FROM mypokemon
WHERE attack BETWEEN 40 AND 60;

SELECT name, attack
FROM mypokemon
WHERE attack >= 40 AND attack <= 60;

/*
MISSION (9)
이름에 ‘e’가 포함되는 포켓몬들의 이름을 가져와 주세요.
*/
SELECT name
FROM mypokemon
WHERE name LIKE '%e%';

/*
MISSION (10)
이름에 ‘i’가 포함되고, 속도가 50 이하인 포켓몬 데이터를 전부 가져와 주세요.
*/
SELECT *
FROM mypokemon
WHERE name LIKE '%i%' AND speed <= 50;

/*
MISSION (11)
이름이 ‘chu’로 끝나는 포켓몬들의 이름, 키, 몸무게를 가져와 주세요.
*/
SELECT name, height, weight
FROM mypokemon
WHERE name LIKE '%chu';

/*
MISSION (12)
이름이 ‘e’로 끝나고, 방어력이 50 미만인 포켓몬들의 이름, 방어력을 가져와 주세요.
*/
SELECT name, defense
FROM mypokemon
WHERE name LIKE '%e' AND defense < 50;

/*
MISSION (13)
공격력과 방어력의 차이가 10 이상인 포켓몬들의 이름, 공격력, 방어력을 가져와 주세요.
*/
SELECT name, attack, defense
FROM mypokemon
WHERE attack - defense >= 10 OR defense - attack >= 10;

/*
MISSION (14)
능력치의 합이 150 이상인 포켓몬의 이름과 능력치의 합을 가져와 주세요.
이 떄, 능력치의 합은 ‘total’이라는 별명으로 가져와 주세요.
조건1. 능력치의 합은 공격력, 방어력, 속도의 합을 의미합니다.
*/
SELECT name, attack + defense + speed AS total
FROM mypokemon
WHERE attack + defense + speed >= 150;





