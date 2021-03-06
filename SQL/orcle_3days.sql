
--JOIN
--TABLE의 별칭은 AS를 쓰는것이 아님

SELECT  *
FROM    EMPLOYEE

SELECT  *
FROM    DEPARTMENT

--EMPLOYEE 테이블에 NULL 값이 2개가 존재, 따라서 결괏값은 22개가 아닌 20개

--ORACLE 전용 조인 구문
SELECT  EMP_NAME, DEPT_NAME,
        D.DEPT_ID
FROM    EMPLOYEE E,
        DEPARTMENT D
WHERE   E.DEPT_ID = D.DEPT_ID;


-- ANSI 표준 구문
-- ANSI 표준 구문에는 USING과 ON 밖에 없음
SELECT  EMP_NAME,
        DEPT_NAME
FROM    EMPLOYEE
JOIN    DEPARTMENT USING(DEPT_ID); -- 컬럼이름이 같기 때문에 USING 사용

SELECT  EMP_NAME,
        DEPT_NAME
FROM    EMPLOYEE E
JOIN    DEPARTMENT D ON(E.DEPT_ID = D.DEPT_ID) 
WHERE   JOB_ID = 'J6';  -- WHERE 절 사용 가능

SELECT  EMP_NAME , 
        DEPT_NAME , 
        LOC_DESCRIBE
FROM    EMPLOYEE E
JOIN    DEPARTMENT  D USING(DEPT_ID)
JOIN    LOCATION    L ON(L.LOCATION_ID = D.LOC_ID)

--OUTER JOIN
SELECT  EMP_NAME , 
        DEPT_NAME 
FROM    EMPLOYEE 
FULL JOIN    DEPARTMENT USING(DEPT_ID)
--RIGHT JOIN DEPARTMENT USING(DEPT_ID)
--LEFT JOIN DEPARTMENT USING(DEPT_ID)

-- ORCLE 전용 JOIN은 OUTER JOIN이 될까?
SELECT  EMP_NAME, DEPT_NAME,
        D.DEPT_ID
FROM    EMPLOYEE E,
        DEPARTMENT D
WHERE   E.DEPT_ID(+) = D.DEPT_ID -- == D.DEPT_ID의 모든 데이터 출력
--WHERE E.DEPT_ID = D.DEPT_ID(+) -- == E.DEPT_ID의 모든 데이터 출력
--FULL JOIN은 불가



-- NON - EQUI JOIN

--ORCLE
SELECT  EMP_NAME ,
        SALARY ,
        SLEVEL
FROM    EMPLOYEE, SAL_GRADE
WHERE   SALARY BETWEEN LOWEST AND HIGHEST;

--ANCI 표준
SELECT  EMP_NAME,
        SALARY ,
        SLEVEL
FROM    EMPLOYEE
JOIN    SAL_GRADE ON(SALARY BETWEEN LOWEST AND HIGHEST) ;

--SELF JOIN
SELECT  E.EMP_NAME, M.EMP_NAME, S.EMP_NAME
FROM    EMPLOYEE E
LEFT JOIN   EMPLOYEE M ON(E.MGR_ID = M.EMP_ID)
LEFT JOIN   EMPLOYEE S ON(M.MGR_ID = S.EMP_ID)
ORDER BY 1;



--직급이 대리이고 지역이 아시아로 시작하는 필터링
SELECT  E.EMP_NAME ,
        E.SALARY ,
        J.JOB_TITLE ,
        SLEVEL  ,  
        D.DEPT_NAME ,
        L.LOC_DESCRIBE ,
        C.COUNTRY_NAME
FROM    EMPLOYEE E
JOIN    JOB J ON E.JOB_ID = J.JOB_ID
JOIN    SAL_GRADE ON(SALARY BETWEEN LOWEST AND HIGHEST) 
JOIN    DEPARTMENT D ON D.DEPT_ID = E.DEPT_ID -- == DEPARTMENT D USING(DEPT_ID)
JOIN    LOCATION L ON L.LOCATION_ID = D.LOC_ID
JOIN    COUNTRY C ON C.COUNTRY_ID = L.COUNTRY_ID 
WHERE   JOB_TITLE = '대리' AND LOC_DESCRIBE LIKE '아시아%' ;

