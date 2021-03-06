# Level 1

- 상위 N개 레코드 조회

```sql
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1
```

- 여러 기준으로 정렬

```sql
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC
```

- 이름이 있는 / 없는 ID 조회

```sql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL	# WHERE NAME IS NULL
ORDER BY ANIMAL_ID
```

- NULL 처리하기

```sql
SELECT ANIMAL_TYPE, IFNULL(NAME, "No name") AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
# IFNULL(A, B): A 값이 NULL이면 B, 아니면 A
```

- 최대값 구하기

```sql
SELECT MAX(DATETIME) AS 시간
FROM ANIMAL_INS
```

# Level 2

- 고양이와 개는 몇마리 있을까

```sql
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY
CASE ANIMAL_TYPE
    WHEN "Cat" THEN 1
    WHEN "Dog" THEN 2
    ELSE 3
END
```

- 최소값 구하기(가장 먼저 들어온 동물)

```sql
SELECT MIN(DATETIME) AS 시간
FROM ANIMAL_INS
```

- DATETIME에서 DATE로 변환

```sql
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS 날짜	# Y는 대문자
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```

- 중성화 여부 파악하기

```sql
SELECT ANIMAL_ID, NAME,
CASE
    WHEN SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O'
    ELSE 'X'
END AS 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```

- 이름에 EL 들어가는 동물 찾기

```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%EL%' AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME
```

- 동명 동물 수 찾기

```sql
SELECT NAME, COUNT(NAME) AS COUNT
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) > 1	# WHERE은 집계 함수 사용 X.
ORDER BY NAME
```

- 중복 제거하기

```sql
SELECT COUNT(DISTINCT NAME) AS count
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
```

- 동물 수 구하기

```sql
SELECT COUNT(ANIMAL_ID) AS count
FROM ANIMAL_INS
```

- 루시와 엘라 찾기

```sql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME = 'Ella' OR NAME = 'Lucy' OR NAME = 'Pickle' OR NAME = 'Rogan' OR NAME = 'Sabrina' OR NAME = 'Mitty'
```

- 입양 시각 구하기(1)

```sql
SELECT HOUR(DATETIME) AS HOUR, COUNT(DATETIME) AS COUNT
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) <= 19
GROUP BY HOUR(DATETIME)
ORDER BY HOUR
```

- 없어진 기록 찾기

```sql
SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_OUTS OUTS
LEFT OUTER JOIN ANIMAL_INS INS
ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE INS.ANIMAL_ID is NULL
ORDER BY OUTS.ANIMAL_ID
```

- 오랜 기간 보호한 동물(1)

```sql
SELECT A.NAME, A.DATETIME
FROM ANIMAL_INS A LEFT JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL
ORDER BY A.DATETIME
LIMIT 3
```

- 오랜 기간 보호한 동물(2)

```sql
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A, ANIMAL_OUTS B
WHERE A.ANIMAL_ID = B.ANIMAL_ID
ORDER BY B.DATETIME - A.DATETIME DESC
LIMIT 2
```

- 있었는데요 없었습니다

```sql
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A, ANIMAL_OUTS B
WHERE A.ANIMAL_ID = B.ANIMAL_ID AND A.DATETIME > B.DATETIME
ORDER BY A.DATETIME
```

- 헤비 유저가 소유한 장소

```sql
SELECT ID, NAME, HOST_ID
FROM PLACES
WHERE HOST_ID IN
(SELECT HOST_ID
FROM PLACES
GROUP BY HOST_ID
HAVING COUNT(HOST_ID) >= 2
ORDER BY ID)
```

