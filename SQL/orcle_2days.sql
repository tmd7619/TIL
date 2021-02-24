
-- 함수 유형
-- 반환 결과에 따라 단일 행 함수와 그룹 함수로 구분 
-- 단일 행 함수 - input N개 - output N개 
-- 그룹 함수 - input N개 - output 1개
-- 함수는 SELECT, WHERE 적용 가능하다

-- < 단일행 함수 > --

--LENGTH() : NUMBER -> 문자의 갯수를 반환하는 함수
--문자열 -> CHAR(고정길이) , VARCHAR2(가변길이)
-- Orcle  한글 1문자 : 3BYTE , 영문 1문자 : 1BYTE
-- CHAR 타입은 한글 갯수를 다르게 계산함 -> VARCHAR2를 사용하는 것이 좋음
SELECT CHARTYPE,
        LENGTH(CHARTYPE),
        VARCHARTYPE,
        LENGTH(VARCHARTYPE)
FROM COLUMN_LENGTH;

--LPAD / RPAD : 문자열에 길이를 덧붙이는 함수
--정렬효과를 가져오기 위해서 사용하는 경우가 많다

SELECT EMAIL, LPAD(EMAIL,15,'.') -- LPAD는 오른쪽으로 정렬됨,  길이를 15로 맞추고 빈공간은 .으로 채우겠다
FROM EMPLOYEE ;

SELECT EMAIL, RPAD(EMAIL,30,'.') 
FROM EMPLOYEE ;

SELECT  EMAIL, RPAD(EMAIL,30,'.'), LPAD(EMAIL,30,' '),
        LENGTH(LPAD(EMAIL,30,' '))
FROM EMPLOYEE;

-- TRIM / LTRIM / RTRIM : 문자를 제거할 때 사용하는 함수
-- DUAL : DUMMY TABLE
SELECT  TRIM('  TEST  '), -- 양옆 공백 제거 
        LENGTH(TRIM('  TEST  '))
FROM DUAL ;

SELECT  RTRIM('  TEST  '), -- 오른쪽 공백 제거 
        LENGTH(RTRIM('  TEST  '))
FROM DUAL ;

SELECT  LTRIM('123123TEST','123'), -- 123이 패턴이 아니라, 1 OR 2 OR 3 으로 봐야함 
        RTRIM('XYZYYYTEST','TEST'),  -- 이하 동일
        TRIM(LEADING '1' FROM 'TEST1'), -- LTRIM으로, 왼쪽부터 1을 제거하겠다
        TRIM(TRAILING '1' FROM '123TEST111') -- RTRIM으로, 오른쪽부터 1을 제거하겠다
FROM DUAL ;

--SUBSTR('문자열 중에서','몇번째자리부터','몇개의 자리수를 가져오겠다')
SELECT SUBSTR('THIS IS A TEST', 6, 2) FROM DUAL;
SELECT SUBSTR('THIS IS A TEST', -6, 5) FROM DUAL;

--ROUND() : 지정한 자릿수에서 반올림 하는 함수
--대시멀 플레이스가 0보다 크면 소수자리, 0보다 작으면 정수자리 에서 반올림

SELECT ROUND(125.315) FROM DUAL; -- 소수점 첫번째 자리에서 반올림
SELECT ROUND(125.315,0) FROM DUAL -- 0은 위에 값과 동일하게 나오며, 생략 가능
SELECT ROUND(125.315,1) FROM DUAL -- 소수점 첫번째 자리까지 남기겠다 -> 2번째에서 반올림
SELECT ROUND(125.315,-1) FROM DUAL -- 정수 첫번째 자리에서 반올림 
SELECT ROUND(125.315,-2) FROM DUAL

--TRUNC() : 지정한 자릿수에서 버림 하는 함수
SELECT TRUNC(125.315) FROM DUAL; 
SELECT TRUNC(125.315,0) FROM DUAL;
SELECT TRUNC(125.315,1) FROM DUAL;
SELECT TRUNC(125.315,-1) FROM DUAL

-- 날짜함수 
SELECT SYSDATE FROM DUAL;

--ADD_MONTHS(data, N): 지정한 만큼의 달 수를 더한 날짜를 반환하는 함수
-- data : 기준이 되는 날짜
-- N    : date에 더하려는 월 수
SELECT  EMP_NAME,
        HIRE_DATE,
        ADD_MONTHS(HIRE_DATE,240) AS 20년후 -- HIRE_DATE의 20년후
FROM    EMPLOYEE ; 

--MONTHS_BETWEEN(data1, data2) : 지정한 두 날짜 사이의 월 수를 반환하는 함수
-- data1 > data2 : 양수 반환
-- data1 < data2 : 음수 반환

--'2010년 1월 1일'기준으로 입사한지 10년이 넘은 직원들의 근무년수 조회
SELECT  EMP_NAME,
        HIRE_DATE,
        TRUNC(MONTHS_BETWEEN(SYSDATE,HIRE_DATE)/12) AS 근무년수
FROM    EMPLOYEE
WHERE   MONTHS_BETWEEN(SYSDATE,HIRE_DATE) > 120;

-- 문자열 INSTR(string,searchChar,[position,occurrence]) : 해당 문자의 인덱스번지를 리턴
-- email 컬럼 값의 '@vvc.com'문자열 중 .앞의 문자 'c' 위치를 구하고 싶다면?
SELECT *
FROM EMPLOYEE;

SELECT  EMAIL,
        INSTR(EMAIL, 'c',-1,2) 위치,
        INSTR(EMAIL,'c',INSTR(EMAIL,'.')-1)
FROM    EMPLOYEE ; 

-- 데이터 타입 변환 함수 
-- TO_CHAR : NUMBER/DATE 타입을 CHARACTER타입으로 변환하는 함수

SELECT TO_CHAR(1234,'99999') FROM DUAL; -- 1234
SELECT TO_CHAR(1234,'09999') FROM DUAL; -- 01234
SELECT TO_CHAR(1234,'L9999') FROM DUAL; -- 원화표시1234
SELECT TO_CHAR(1234,'$9999') FROM DUAL; -- 달러표시1234
SELECT TO_CHAR(1234,'99,999') FROM DUAL; -- 1,234
SELECT TO_CHAR(1234,'09,999') FROM DUAL; -- 01,234
SELECT TO_CHAR(1234,'999') FROM DUAL;   -- ####

-- TO_CHAR :(날짜|숫자, 표현방식) -> 문자열 
-- 정해진 FORMAT 형식을 따라야함 !
SELECT  SYSDATE,
        TO_CHAR(SYSDATE,'AM Q YYYY-MM-DD HH:MI:SS') "별 칭" -- 별칭 줄때, 공백이나 특수문자가 있을 경우 ""으로 ! 
FROM DUAL;

SELECT  EMP_NAME,
        HIRE_DATE,
        TO_CHAR(HIRE_DATE,'YYYY "년" MM"월" DD"일"') ,  -- ""을 통해 임의로 형식을 변경할 수 있음 
        SUBSTR(HIRE_DATE, 1, 2) || '년' 
FROM    EMPLOYEE;

        
FROM    EMPLOYEE; 

--SUBSTR(문자|날짜) 

SELECT TO_DATE('20210112','YYYYMMDD') -- 들어오는 문자에 맞게 형식을 똑같이 지정해줘야함
FROM DUAL;

SELECT TO_CHAR(TO_DATE('20100101', 'YYYYMMDD'), 'YYYY, MON')
--SELECT TO_CHAR('20210112','YYYY, MON') -- 형식이 다르기 때문에 ERROR
FROM DUAL;

SELECT  TO_CHAR(TO_DATE('041030 143000', 'YYMMDD HH24MISS'),
        'DD-MON-YY HH:MI:SS PM') 
FROM DUAL;

SELECT TO_DATE('980630', 'YYMMDD') FROM DUAL;

SELECT  TO_CHAR(TO_DATE('980630','YYMMDD'),
        'YYYY.MM.DD') FROM DUAL;

SELECT  HIRE_DATE
FROM    EMPLOYEE
WHERE   TO_CHAR(HIRE_DATE,  'YYMMDD') = '900401' ; 
--데이트 타입에 시분초가 포함될경우, 연월일로는 찾을 수가 없음 
--따라서 컬럼을 YYMMDD형태로 변형시킴

-- YYYY : 현재 세기를 기준으로 정해짐 EX) '981212' -> 2098년 12월~ 
-- RRRR : 년도 두자리가 50-99일경우, 이전 세기를 반환 0-49는 현재 세기

SELECT  EMP_NAME,
        HIRE_DATE,
        TO_CHAR(TO_DATE(HIRE_DATE, 'RR/MM/DD') , 'YYYY')
FROM    EMPLOYEE
WHERE   EMP_NAME = '한선기'; 

--  주민번호 앞자리 뒷자리 쪼개기 TO_NUMBER(CHAR) -> NUMBER
SELECT  EMP_NO, 
        SUBSTR(EMP_NO,1,6) ,
        SUBSTR(EMP_NO,8) ,
        TO_NUMBER( SUBSTR(EMP_NO, 1 , 6) ) + TO_NUMBER( SUBSTR(EMP_NO,8))
FROM    EMPLOYEE ;
--왼쪽정렬 : STRING, 오른쪽정렬 : NUMBER


-- 기타함수 NVL : NULL을 지정한 값으로 반환하는 함수
SELECT  EMP_NAME, SALARY, NVL(BONUS_PCT,0) -- BONUS_PCT가 NULL이면, 0으로 대체하겠다
FROM    EMPLOYEE
WHERE   SALARY > 3500000;

SELECT  EMP_NAME,
        (SALARY*12)+((SALARY*12)*BONUS_PCT)
FROM    EMPLOYEE
WHERE   SALARY > 3500000; -- 결과가 NULL값으로 나오기에,

SELECT  EMP_NAME,
        (SALARY*12)+       --NVL함수사용
        ( (SALARY*12)*NVL(BONUS_PCT,0) )
FROM    EMPLOYEE
WHERE   SALARY > 3500000;

-- DECODE : SELECT 구문으로 IF-ELSE논리를 제한적으로 구현한 오라클 DBMS 전용함수
SELECT  EMP_NO,
        DECODE(SUBSTR(EMP_NO,8,1) ,
        '1' , '남자', '3', '남자', '여자') AS GENDER
FROM    EMPLOYEE ;

SELECT  EMP_ID , -- 오류?
        EMP_NAME ,
        DECODE(MGR_ID , NULL, 'ADMIN', MRG_ID),
        NVL(MGR_ID, 'ADMIN') 
FROM    EMPLOYEE
WHERE   JOB_ID = 'J4' ;

--직원의 직급별 인상급여를 확인하고싶다
--J7 -> 20% 인상
--J6 -> 15% 인상
--J5 -> 10% 인상
--나머지 직급은 인상이 X
SELECT  EMP_NAME,
        JOB_ID,
        SALARY,
        DECODE(JOB_ID ,
            'J7', SALARY * 1.2 ,
            'J6', SALARY * 1.15 ,
            'J5', SALARY * 1.1 ,
            SALARY)AS "인상 급여"
FROM    EMPLOYEE ;

-- CASE expi WHEN search1 TEHN result1 .... END

--case1)
SELECT  EMP_NAME,
        JOB_ID,
        SALARY,
        CASE JOB_ID 
            WHEN 'J7' THEN SALARY * 1.2 
            WHEN 'J6' THEN SALARY * 1.15 
            WHEN 'J5' THEN SALARY * 1.1 
            ELSE SALARY
        END AS "인상 급여"
FROM    EMPLOYEE;

--case2) 더 선호되는 구문 
SELECT  EMP_NAME,
        JOB_ID,
        SALARY,
        CASE WHEN JOB_ID = 'J7 SALARY * 1.2 
             WHEN JOB_ID = 'J6 SALARY * 1.15 
             WHEN JOB_ID = 'J5 SALARY * 1.1 
            ELSE SALARY
        END AS "인상 급여"
FROM    EMPLOYEE;

 --Group Function(집계함수, 그룹함수)
 -- group by
 -- 그룹 함수가 SELECT 절 사용되면 다른 컬럼은 정의 불가
 -- 그룹 함수는 NULL 값 제거 후 연산을 하므로 주의요망

SELECT SUM(SALARY),  SUM(DISTINTC SALARY)  -- EMP_NAME ERROR
FROM EMPLOYEE; 

SELECT  AVG(BONUS_PCT)
        ROUND( AVG(NVL(BONUS_PCT,0)),2)
FROM    EMPLOYEE;
-- MIN ,MAX, COUNT -> ANY

SELECT  MIN(SALARY), MAX(SALARY),
        MIN(HIRE_DATE), MAX(HIRE_DATE),
        MIN(JOB_ID), MAX(JOB_ID)
FROM EMPLOYEE ;

SELECT COUNT(*), COUNT(JOB_ID), COUNT(DISTINCT JOB_ID)
FROM EMPLOYEE ;

--부서번호가 50이거나, 부서번호가 존재하지 않는 사원의 이름, 급여를 조회해라
-- 높은 급여순으로 볼려면? ORDER BY[기준컬럼][ASC|DESC]
SELECT  EMP_NAME,
        SALARY
FROM    EMPLOYEE
WHERE   DEPT_ID = '50' OR DEPT_ID IS NULL 
ORDER BY SALARY DESC ; 

-- 입사일이 03년 1월 1일 이후 입사자들의 이름, 입사일, 부서번호를 조회
--단) 부서번호가 높은순으로 정렬하고 같으면 입사일이 빠른 순서로 정렬하고 같으면 이름이 빠른 순서로 정렬

SELECT  EMP_NAME 이름,
        HIRE_DATE 입사일,
        DEPT_ID 부서
FROM    EMPLOYEE
WHERE   HIRE_DATE > TO_DATE('03/01/01' , 'RR/MM/DD') 
ORDER BY DEPT_ID DESC NULLS LAST , HIRE_DATE, EMP_NAME
--ORDER BY 3 DESC NULLS LAST , 2, 1
--ORDER BY 부서 DESC NULLS LAST , 입사일, 이름;

-- GROUP BY [기준컬럼]
-- 부서별 평균급여 -- WHERE X WHY? WHERE는 행에 대한 조건
SELECT  DEPT_ID, 
        JOB_ID , 
        ROUND(AVG(SALARY),-5) AS 급여평균
FROM    EMPLOYEE
GROUP BY ROLLUP( DEPT_ID, JOB_ID)  -- GROUP BY에 정의된 속성은 SELECT절에도 정의 가ㅡㄴㅇ
ORDER BY DEPT_ID ; -- 오름차순
-- ROLLUP() : 각각 그룹에 대한 누계합, 총합을 보여줌

-- 평균급여가 300이상?
SELECT  DEPT_ID, ROUND(AVG(SALARY),-5) AS 급여평균
FROM    EMPLOYEE
GROUP BY DEPT_ID  
HAVING  AVG(SALARY) > 3000000
ORDER BY 급여평균 DESC;



-- 성별에 따른 급여 평균을 구한다면?
SELECT  DECODE( SUBSTR(EMP_NO,8,1),
                '1', '남자', '3', '남자' , '여자'),
        AVG(SALARY)

FROM    EMPLOYEE
GROUP BY DECODE( SUBSTR(EMP_NO,8,1), -- GROUP BY는 INDEX,별칭 지정이 안됨
                '1', '남자', '3', '남자' , '여자')
ORDER BY 2 DESC ; 

--CASE ? 
SELECT  CASE SUBSTR(EMP_NO,8,1)
            WHEN '1' THEN '남자'
            WHEN '3' THEN '남자'
            ELSE  여자
        END ,
        AVG(SALARY)
FROM    EMPLOYEE
GROUP BY CASE SUBSTR(EMP_NO,8,1)
            WHEN '1' THEN '남자'
            WHEN '3' THEN '남자'
            ELSE  여자
        END 
ORDER BY 2 DESC ; 


--ORDER BY 사용 예

SELECT  EMP_NAME, SALARY
FROM    EMPLOYEE
WHERE   DEPT_ID = '50'
OR      DEPT_ID IS NULL
ORDER BY SALARY DESC;

SELECT  EMP_NAME, HIRE_DATE, DEPT_ID
FROM    EMPLOYEE
WHERE   HIRE_DATE > TO_DATE('20030101','YYYYMMDD')
ORDER BY DEPT_ID DESC, HIRE_DATE, EMP_NAME;

SELECT  EMP_NAME 이름,
        HIRE_DATE 입사일,
        DEPT_ID 부서코드
FROM    EMPLOYEE
WHERE   HIRE_DATE > TO_DATE('20030101','YYYYMMDD')
ORDER BY 부서코드 DESC, 입사일, 이름 ; -- 컬럼별칭을 적용할 수 있다
-- ORDER BY 3 DESC 2, 1 ; --INDEX 사용 가능

-- GROUP BY 사용 예
-- 컬럼 별칭이나 컬럼 기술 순서는 사용할 수 없음

SELECT  EMP_NAME, DEPT_ID, COUNT(*) AS COUNT --집계함수가 사용되었기 때문에 GROUP BY에 EMP_NAME까지 지정해야함
FROM    EMPLOYEE
GROUP BY EMP_NAME, DEPT_ID

-- HAVING 
SELECT  DEPT_ID, SUM(SALARY)
FROM    EMPLOYEE
GROUP BY DEPT_ID
HAVING  SUM(SALARY) > 900000;

SELECT  DEPT_ID, SUM(SALARY)
FROM    EMPLOYEE
WHERE   SUM(SALARY)> 900000 -- ERROR WHERE절에는 그룹 함수를 사용할 수 없음 
GROUP BY DEPT ID ; 
