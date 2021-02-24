
--SET Oprator - UNION
-- UNION : 중복된 결과값을 제외하고 출력
-- UNION ALL : 중복된 결과값 포함하고 출력
-- INTERSECT : 교집합
-- EXCEPT : 차집합
SELECT  EMP_ID,
        ROLE_NAME
FROM    EMPLOYEE_ROLE
UNION   ALL
SELECT  EMP_ID,
        ROLE_NAME
FROM    ROLE_HISTORY;

--쿼리1과 쿼리2의 SELECT 목록은 반드시 동일(컬럼개수, 데이터 타입)
--해야 하므로 이를 위해 DUMMY COLUMN을 사용할 수 있다
SELECT  EMP_NAME,
        JOB_ID,
        HIRE_DATE
FROM    EMPLOYEE
WHERE   DEPT_ID = '20'
UNION
SELECT  DEPT_NAME,
        DEPT_ID,
        NULL
FROM    DEPARTMENT
WHERE   DEPT_ID = '20';

--UNION 50번 부서원을 관리자 직원으로 구분하여 표현

SELECT  *
FROM    EMPLOYEE
WHERE   DEPT_ID = '50' ;


SELECT  EMP_ID,
        EMP_NAME,
        '직원' AS 구분
FROM    EMPLOYEE
WHERE   MGR_ID IS NOT NULL AND DEPT_ID = '50'
UNION
SELECT  EMP_ID,
        EMP_NAME,
        '관리자'  -- 일반적으로 쿼리1의 별칭을 따르게 되있음 
FROM    EMPLOYEE
WHERE   MGR_ID IS NULL AND DEPT_ID = '50'
ORDER BY 3;

--직급(JOB_TITLE)이 대리 또는 사원 직원 정보를 조회 (이름, 직급)
SELECT  *
FROM    EMPLOYEE;

SELECT  EMP_NAME,JOB_TITLE      
FROM    EMPLOYEE
JOIN    JOB USING(JOB_ID)
WHERE   JOB_TITLE = '대리'
UNION
SELECT  EMP_NAME,JOB_TITLE 
FROM    EMPLOYEE
JOIN    JOB USING(JOB_ID)
WHERE   JOB_TITLE = '사원'
ORDER BY 2 ;

--UNION 없이 ?
SELECT  EMP_NAME,JOB_TITLE 
FROM    EMPLOYEE
JOIN    JOB USING(JOB_ID)
WHERE   JOB_TITLE IN('대리','사원')
ORDER BY 2 ;

--SUBQUERY
--나승원이란 이름을 이용하여
--직급(JOB_ID)이 동일하고, 나승원보다 급여(SALARY)가 많은 사원의 이름, 직급, 급여를 조회하라

SELECT  EMP_NAME, JOB_ID, SALARY
FROM    EMPLOYEE
WHERE   JOB_ID = (  SELECT  JOB_ID
                    FROM    EMPLOYEE
                    WHERE   EMP_NAME = '나승원' )
AND     SALARY > (  SELECT  SALARY
                    FROM    EMPLOYEE
                    WHERE   EMP_NAME = '나승원') ;

-- 최소 급여를 받는 사원의 이름, 직급, 급여를 조회하라
-- 1. 최소급여 확인
-- 2. 검색
-- 3. 

SELECT  EMP_NAME, JOB_ID, SALARY
FROM    EMPLOYEE
WHERE   SALARY = (  SELECT  MIN(SALARY) -- 최소급여 확인, 행의 개수가1개 -> 단일행 SUBQUERY
                    FROM    EMPLOYEE ) ;

-- 부서별 급여총합이 가장 많은 부서의 이름, 급여총합을 조회하라
SELECT  DEPT_NAME,
        SUM(SALARY)
FROM    EMPLOYEE
JOIN    DEPARTMENT USING (DEPT_ID)
GROUP BY    DEPT_NAME
HAVING      SUM(SALARY) = ( SELECT  MAX(SUM(SALARY))
                            FROM    EMPLOYEE 
                            GROUP BY DEPT_ID   ) ;

-- 다중 행 서브쿼리
-- IN, NOT, IN, ANY, ALL 연산자를 다중 행 서브쿼리에서 사용할 수 있다.

SELECT  EMP_ID,
        EMP_NAME,
        '관리자' AS 구분
FROM    EMPLOYEE
WHERE   EMP_ID  IN (SELECT MGR_ID FROM EMPLOYEE)

-- 다중행 서브 쿼리에서 NULL값이 있으면, NOT IN을 할때 전체 쿼리절은 NULL을 리턴하게 됨
-- 따라서 NULL값을 제거시켜줘야함 
-- IN은 상관 없음

SELECT  EMP_ID,
        EMP_NAME,
        '직원' AS 구분
FROM    EMPLOYEE
WHERE   EMP_ID NOT IN (SELECT MGR_ID FROM EMPLOYEE
                       WHERE MGR_ID IS NOT NULL) -- NULL 값 제거 
UNION                      
SELECT  EMP_ID,
        EMP_NAME,
        '관리자' AS 구분
FROM    EMPLOYEE
WHERE   EMP_ID  IN (SELECT MGR_ID FROM EMPLOYEE)

-- 위 구현한 코드를 다른 방식(NOT UNION)으로 구현한다면 ?

--방법1
SELECT  EMP_ID,
        EMP_NAME ,
        CASE  
        WHEN MGR_ID IS NOT NULL THEN '직원'
        ELSE '직원'
        END AS 구분
FROM    EMPLOYEE ; 

--방법 2
SELECT  EMP_ID,
        EMP_NAME,
        CASE WHEN EMP_ID IN (SELECT MGR_ID FROM EMPLOYEE) THEN '관리자 ELSE '직원 ' END
FROM    EMPLOYEE ;


--다중행 서브쿼리 ANY, ALL 연산자--
--ANY 는 범위가 박스 안에 있는 것 ,
--ALL 은 범위가 박스 바깥으로 있는 것 으로 이해

SELECT  EMP_NAME,
        SALARY
FROM    EMPLOYEE
JOIN    JOB USING (JOB_ID)
WHERE   JOB_TITLE='대리'
AND     SALARY < ALL
                    (SELECT SALARY
                     FROM   EMPLOYEE
                     JOIN   JOB USING (JOB_ID)
                     WHERE  JOB_TITLE = '과장') ; 
                     
                     
-- 자기 직급(JOB_ID)의 평균 급여를 받는 직원을 조회하라
SELECT  EMP_NAME, JOB_TITLE, SALARY
FROM    EMPLOYEE
JOIN    JOB USING(JOB_ID)
WHERE   SALARY IN ( SELECT  TRUNC(AVG(SALARY), -5)
                    FROM    EMPLOYEE
                    GROUP BY    JOB_ID)
-- 이런 쿼리를 만들면, 차장인데 평균급여(250)이 아닌, 260 받는 사원이 존재함
-- 따라서 다중행 다중열 서브쿼리 형식으로 만들어 줘야함                   
                    
--다중행 다중열 서브 쿼리
SELECT  EMP_NAME, JOB_TITLE, SALARY
FROM    EMPLOYEE
JOIN    JOB USING(JOB_ID)
WHERE   (JOB_ID, SALARY) IN ( SELECT  JOB_ID, TRUNC(AVG(SALARY), -5)
                    FROM    EMPLOYEE
                    GROUP BY    JOB_ID)

--FROM 절에 서브쿼리 넣기
--FROM 절에 서브쿼리를 넣으면, 가상의 테이블이 만들어짐
SELECT  EMP_NAME, JOB_TITLE, SALARY
FROM    (SELECT JOB_ID, TRUNC(AVG(SALARY), -5) AS JOBAVG
        FROM    EMPLOYEE
        GROUP BY    JOB_ID) V
JOIN    EMPLOYEE E ON(V.JOB_ID = E.JOB_ID AND V.JOBAVG = E.SALARY)
JOIN    JOB J ON(E.JOB_ID = J.JOB_ID)


-- 상관관계 서브쿼리
-- 현업에서 가장 많이 사용
SELECT  EMP_NAME, JOB_TITLE, SALARY
FROM    EMPLOYEE E
JOIN    JOB J ON(E.JOB_ID = J.JOB_ID)
WHERE   SALARY = (  SELECT  TRUNC(AVG(SALARY), -5)
                    FROM    EMPLOYEE
                    WHERE   JOB_ID = E.JOB_ID )


--연산자 EXISTS, NOT EXISTS

SELECT  EMP_ID,
        EMP_NAME,
        '관리자' AS 구분
FROM    EMPLOYEE E
WHERE   EXISTS (SELECT  NULL    -- 존재하면 TURE
                FROM    EMPLOYEE
                WHERE   E.EMP_ID = MGR_ID)
UNION
SELECT  EMP_ID,
        EMP_NAME,
        '직원' AS 구분
FROM    EMPLOYEE E2
WHERE   NOT EXISTS (SELECT  NULL --존재하지 않으면 TRUE
                    FROM    EMPLOYEE
                    WHERE   E2.EMP_ID = MGR_ID) 
ORDER BY 3;