-- Q. gender가 1인 경우는 남자를 gender가 2인 경우에는 여자를 출력하시오.
SELECT 
  id,
  CASE
    WHEN gender = 1 THEN '남자'
    WHEN gender = 2 THEN '여자'
  END
FROM healthcare
LIMIT 3;

-- Q. 나이에 따라 청소년(~18), 청년(~30), 중장년(~64)로 출력하시오.
SELECT 
  last_name,
  age,
  CASE
    WHEN age < 18 THEN '청소년'
    WHEN age <= 30 THEN '청년'
    WHEN age <= 64 THEN '중장년'
  END
FROM users
LIMIT 3;

-- Q. users에서 가장 나이가 작은 사람의 수는?
SELECT
  COUNT(*)
FROM users
WHERE age = (SELECT MIN(age) FROM users);

-- Q. users에서 평균 계좌 잔고가 높은 사람의 수는?
SELECT
  COUNT(*)
FROM users
WHERE balance > (SELECT AVG(balance) FROM users);

-- Q. users에서 유은정과 같은 지역에 사는 사람의 수는?
SELECT
  COUNT(*)
FROM users
WHERE country = (
  SELECT country
  FROM users 
  WHERE first_name = '은정' AND last_name = '유'
);

-- Q. 전체 인원과 평균 연봉, 평균 나이를 출력하세요.
SELECT
  (SELECT COUNT(*) FROM users) AS 총인원,
  (SELECT AVG(balance) FROM users) AS 평균연봉,
  (SELECT AVG(age) FROM users) AS 평균나이
;

-- Q. users에서 이은정과 같은 지역에 사는 사람의 수는? (동명이인)
SELECT COUNT(*)
FROM users
WHERE country IN (
  SELECT country
  FROM users
  WHERE first_name = '은정' AND last_name = '이'
);

-- Q.특정 성씨에서 가장 어린 사람들의 이름과 나이
SELECT
  last_name,
  first_name,
  age
FROM users
WHERE (last_name, age) IN (
  SELECT last_name, MIN(age)
  FROM users
  GROUP BY last_name)
ORDER BY last_name;
