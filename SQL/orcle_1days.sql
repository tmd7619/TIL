--SELECT 구문

SELECT   [특정컬럼 | *(전체컬럼) | 표현식(SELECT - (SUBQUERY)) |DISTINCT |AS 컬럼 별칭-- | ==OR   
FROM     [테이블이름 | JOIN | SELECT - (SUBQUERY) ]  
WHERE    조건식 | SELECT - (SUBQUERY)
GROUP BY 표현식 | SELECT - (SUBQUERY)   
HAVING   조건식
ORDER BY 기준컬럼; -- 가장 마지막에 써야함


-- 전체컬럼 EMPLOYEE
SELECT * 
FROM EMPLOYEE;

-- 특정컬럼

SELECT EMP_NAME
FROM EMPLOYEE;

-- 여러컬럼 가져오기
SELECT EMP_NAME,
        EMP_ID,
        EMP_NO
FROM EMPLOYEE;

-- 컬럼 별칭 지정하기
-- 주의사항: 반드시 문자로 시작해야함(숫자불가), 만약에 특수부호,공백이 들어가게 되면 " " 
-- AS 키워드는 생략이 가능
SELECT EMP_NAME AS "이 름",
        EMP_ID AS 아이디,
        EMP_NO AS 주민번호,
        SALARY AS "급여(원)", -- () 특수부호이기 때문, ""로 묶어주기
        DEPT_ID 부서번호 --AS 없이 별칭 지정
FROM EMPLOYEE;

--DISTINCT : 값의 중복을 제거할 때 사용하는 키워드
SELECT DISTINCT JOB_ID
FROM EMPLOYEE ;

-- 표현식
-- 컬럼 값에 대한 연산을 식으로 작성할 수 있다.

SELECT EMP_NAME AS 사원명,
        SALARY AS 급여,
        (SALARY + (SALARY*BONUS_PCT))*12 AS 연봉
        
FROM EMPLOYEE;

--더미컬럼
--'데이터', "키워드"
SELECT EMP_ID,
        EMP_NAME,
        '재직' AS 근무여부
FROM EMPLOYEE;

SELECT [특정컬럼 | *(전체컬럼) | 표현식 |DISTINCT |AS 컬럼 별칭-- | ==OR   
FROM 테이블이름 
WHERE 조건식(행의 제한)

--부서번호가 90번인 사원들의 정보를 확인하고 싶다면
-- WHERE 행의 제한
-- 조건절에서 연산자를 사용할 수 있다. = : 할당이 아닌 비교연산자
SELECT *
FROM EMPLOYEE
WHERE DEPT_ID = 90 -- 블록잡으면 ;은 안써도 됨

--부서코드가 90이고, 급여를 2000000보다 많이 받는 사원의 이름,부서코드,급여를 조회

SELECT EMP_NAME,
        DEPT_ID,
        SALARY
FROM EMPLOYEE        
WHERE DEPT_ID = 90 AND
        SALARY > 2000000 ;

--부서코드가 90이거나 20번인 사원의 이름,부서코드,급여를 조회

SELECT EMP_NAME,
        DEPT_ID,
        SALARY
FROM EMPLOYEE        
WHERE DEPT_ID = 90 OR DEPT_ID = 20 ;


-- 'XXX님의 월급은 XXXXX원 입니다'
-- || : 연결연산자
-- [컬럼 || 컬럼] [컬럼 ||'문자열']
SELECT EMP_ID || EMP_NAME || SALARY
FROM EMPLOYEE ; 

SELECT EMP_ID ||'의 월급은' ||SALARY||'원입니다'
FROM EMPLOYEE ; 

-- Operator = , > , >=, <, <= , !=
-- BETWEEN AND, LIKE, IS NULL, IN

-- BETWEEN AND
-- 비교하려는 값이 지정한 범위 (상한 값과 하한 값의 경계포함)에 포함되면 TURE를 반환하는 연산자
-- 급여를 3,500,000원보다 많이 받고 5,500,000원보다 적게 받는 직원 이름과 급여 조회]
SELECT EMP_NAME,
        SALARY
FROM    EMPLOYEE
WHERE SALARY BETWEEN 3500000 AND 5500000 ;

--또는 
SELECT
    emp_name,
    salary
FROM
    employee
WHERE
    salary >= 3500000
    AND salary <= 5500000;

-- LIKE 
--EX1)
SELECT
    emp_name,
    salary
FROM
    employee
WHERE
    emp_name LIKE '김%';
--EX2)
SELECT EMP_NAME,PHONE 
FROM EMPLOYEE
WHERE PHONE LIKE '___9%' ;

-- EMAIL ID 중 '_' 앞 자리가 3자리인 직원을 조회한다면
SELECT EMP_NAME, EMAIL
FROM EMPLOYEE
WHERE EMAIL LIKE '___\_%' ESCAPE'\' ; --ESCAPE 뒤에는 문자로 보겠다 아무 특수문자나 상관없음

--'김'씨 성이 아닌 직원의 이름과 급여를 조회
SELECT EMP_NAME, SALARY
FROM   EMPLOYEE
WHERE  EMP_NAME NOT LIKE '김%' ;

--부서가 없는데도 불구하고 보너스를 지급받는 직원의 이름, 부서, 보너스를 조회한다면
--IS NULL, IS NOT NULL
SELECT  EMP_NAME, DEPT_ID, BONUS_PCT
FROM   EMPLOYEE 
WHERE  DEPT_ID IS NULL AND BONUS_PCT IS NOT NULL ;

-- IN = OR
SELECT EMP_NAME, DEPT_ID, SALARY
FROM   EMPLOYEE
WHERE  DEPT_ID IN('90','20') ;

--부서번호가 20번 또는 90번인 사원중 급여가 3000000보다 많이(초과)받는 사원의 이름,급여,부서코드 조회
SELECT  EMP_NAME,SALARY,DEPT_ID
FROM    EMPLOYEE
WHERE   (DEPT_ID = 20 OR DEPT_ID = 90) -- ()를 통해 연산자의 우선순위를 지정해줌  
--WHERE DEPT_ID IN('20','90')
AND     SALARY > 3000000 ;

