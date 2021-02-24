--ERD 상에서 점선 : 비식별관계
--ERD 상에서 실선 : 식별관계
--ERD 도표, 선, 관계 파악 필요

-- table 생성은 부모부터 만들고, 자식을 만들어야함
-- TABLE 삭제 또한 자식부터 DROP하고, 부모 DROP
-- PRIMARY KEY는 각 행마다 고유의 값을 부여함. 중복된 값을 컬럼에 넣을 수 없음

--DEFAULT는 아무 값도 입력하지 않아도 NULL 값이 아니라 
--설정한 값이 기본값으로 자동 입력되도록 하는 제약조건 입니다.

---NUMBER 형은 맨 앞에 0이 들어가면 숫자로 인식을 안함 ( 8진수로 인식하기 떄문)

-- DDL ( CREATE, DROP, ALTER )
-- 1. 테이블 생성(제약조건)

CREATE TABLE TABLE_NAME(
     COLUMN_NAME DATETYPE [DEFAULT EXPR][CONSTRAINT], --컬럼 레벨 제약
     COLUMN_NAME DATETYPE [DEFAULT EXPR][CONSTRAINT],
     COLUMN_NAME DATETYPE [DEFAULT EXPR][CONSTRAINT],
     COLUMN_NAME DATETYPE [DEFAULT EXPR][CONSTRAINT],
     TABLE_CONSTRAINT --테이블 레벨 제약
)

DROP TABLE TEST_MEMBER; --테이블 삭제

CREATE TABLE TEST_MEMBER(--테이블 생성
    ID   VARCHAR2(50), --PRIMARY KEY, --중복값 허용하지 않는 조건
    PWD  VARCHAR2(50) NOT NULL, -- 널 값을 허용하지 않는 조건
    ADDR VARCHAR2(50) DEFAULT 'SEOUL', --DEFAULT 즉, 기본값으로 삽입되는 열
    PRIMARY KEY(ID) --TABLE 제 약을 줄 수 있는 자리이며, NOT NULL(칼럼명)은 불가능 PRIMARY KEY(칼럼명)은 가능
) --#1 컬럼생성과 동시에 제약을 주는 방법
  - 

INSERT INTO TEST_MEMBER(ID, PWD, ADDR) VALUES('YSSIM', 'YSSIM', 'SEOUL');
INSERT INTO TEST_MEMBER VALUES('YSSIM', 'YSSIM', 'SEOUL'); --PRIMARY KEY로 설정해놨기 때문에 동일한 값 입력 불가능!
INSERT INTO TEST_MEMBER VALUES('yssim', NULL, NULL); --대소문자를 구분한다.
INSERT INTO TEST_MEMBER(ID, PWD) VALUES('ADMIN', 'YSSIM'); --대소문자를 구분한다. 

SELECT *
FROM TEST_MEMBER;

-- 2. 제약조건 (NOT NULL - 컬럼 레벨 제약만 가능, UNIQUE, PRIMARY KEY, FOREIGEN KEY, CHECK)
-- 2-1. 제약조건을 설정하는 방법 : 테이블 레벨, 컬럼 레벨

CREATE TABLE TEST_MEMBER(
    ID   VARCHAR2(50) PRIMARY KEY,
    PWD  VARCHAR2(50) PRIMARY KEY,
    ADDR VARCHAR2(50) DEFAULT 'SEOUL'
) --기본키는 하나여야 한다. 두 개의 기본키는 허용하지 않는다.
  --하지만 두 개를 잡아야 한다면?

CREATE TABLE TEST_MEMBER(
    ID   VARCHAR2(50),
    PWD  VARCHAR2(50),
    ADDR VARCHAR2(50) DEFAULT 'SEOUL',
    PRIMARY KEY(ID, PWD) --이런 식으로 COMPOSITE 하여 만들 순 있다.
)
  
--다중 컬럼 자체가 PRIMARY KEY 이기 때문에 아래처럼 입력이 가능하다.
--(YSSIM , YSSIM) 조합1
--(YSSIM , ADMIN) 조합2
INSERT INTO TEST_MEMBER(ID, PWD, ADDR) VALUES('YSSIM', 'YSSIM', 'SEOUL');
INSERT INTO TEST_MEMBER(ID, PWD, ADDR) VALUES('YSSIM', 'ADMIN', 'SEOUL'); 

SELECT *
FROM TEST_MEMBER;


--ERD 보고 만들기, LOCATION 테이블을 참조하여 기본키를 전이받는 새로운 외래 테이블 만들기.
--FK (부모에 의존하는 데이터이거나 NULL값을 허용)
CREATE TABLE TEST_FK(
       ID      CHAR(3) PRIMARY KEY,
       NAME    VARCHAR(50) NOT NULL,
       LID     CHAR(2) REFERENCES LOCATION(LOCATION_ID)--FK 컬럼으로 쓰고 싶은 컬럼! 즉, 부모를 참조하는 키
)                                                      --LOCATION테이블의 기본키은 LOCATION_ID를 참조하여 LID라는 FK를 만든거임
INSERT INTO TEST_FK VALUES('B', 'YSSIM', 'OT') --LOCATION_ID에 있는 값들만 입력이 가능하기 때문에
INSERT INTO TEST_FK VALUES('S', 'SUPREME', 'A') -- A처럼 LOCATION_ID에 없는 값을 입력하면 parent key not found라는 오류를 발생시킨다.

--CHAR를 사용하면 안되는 이유?
--위에 예시처럼, CHAR에 3을 주게 되면 고정길이가 3이 되기 때문에,
--행 추가시 'A'라는 한글자의 문자를 입력해도 'A__'처럼 3글자로 인식됨
--따라서 VARCHAR를 하는 것이 좋음


--LOCATION 테이블 확인
SELECT *
FROM LOCATION; 
                              
--TABLE 삭제
DROP TABLE TEST_FK

--테이블레벨 제약으로 만들기
CREATE TABLE TEST_FK(
       ID      CHAR(3) PRIMARY KEY,
       NAME    VARCHAR(50) NOT NULL,
       LID     CHAR(2),
       FOREIGN KEY(LID) REFERENCES LOCATION(LOCATION_ID)
)

INSERT INTO TEST_FK VALUES('B', 'YSSIM', 'OT')
INSERT INTO TEST_FK VALUES('S', 'SUP', 'A1')

--JOIN해보기

SELECT LOC_DESCRIBE, ID
FROM LOCATION
RIGHT JOIN TEST_FK ON (LOCATION_ID = LID)

SELECT *
FROM TEST_FK

SELECT *
FROM LOCATION ;


CREATE TABLE TEST_COMPOSITE_PK (
    ID     VARCHAR2(50),
    NAME   VARCHAR2(50),
    SALARY NUMBER CHECK (SALARY > 0),       --0보다 큰 SALARY 값을 받겠다. 음수 X 
                                            --NUMBER(7,2) : 7자리의 NUMBER 값 중 2자리는 실수형을 쓰겠다.
    GENDER CHAR(1) CHECK (GENDER IN ('M', 'F')), --M 또는 F 값만 받겠다. 
    PRIMARY KEY (ID, NAME)
)

INSERT INTO TEST_COMPOSITE_PK VALUES('YSSIM', '심영석', -100, 'M') --check constraint (HR.SYS_C007085) violated 발생/양수입력
INSERT INTO TEST_COMPOSITE_PK VALUES('YSSIM', '심영석', 100, '?') --check constraint (HR.SYS_C007086) violated 발생/M또는F값입력
INSERT INTO TEST_COMPOSITE_PK VALUES('YSSIM', '심영석', 100, 'm') --check constraint (HR.SYS_C007086) violated 발생/대소문자구분
INSERT INTO TEST_COMPOSITE_PK VALUES('YSSIM', '심영석', 100, 'M') --정상입력

SELECT *
FROM TEST_COMPOSITE_PK

DROP TABLE TEST_COMPOSITE_FK;

CREATE TABLE TEST_COMPOSITE_FK(
    PID      VARCHAR2(50) PRIMARY KEY,
    ID       VARCHAR2(50) ,
    NAME     VARCHAR2(50) ,
    FOREIGN KEY (ID, NAME) REFERENCES TEST_COMPOSITE_PK (ID, NAME)
)

INSERT INTO TEST_COMPOSITE_FK VALUES('P001', 'YSSIM', '심영석')

SELECT *
FROM TEST_COMPOSITE_FK

----------------------PRACTICE

CREATE TABLE TEST_S1(
    SID    VARCHAR(50) PRIMARY KEY,
    PHONE  NUMBER
)

CREATE TABLE TEST_S2(
    TID    VARCHAR(50) PRIMARY KEY,
    NAME   VARCHAR(50) DEFAULT 'DEFAULT'
)

CREATE TABLE TEST_CHILD(
    CID    VARCHAR(50) PRIMARY KEY,
    SID    VARCHAR(50) REFERENCES TEST_S1(SID),
    TID    VARCHAR(50) REFERENCES TEST_S2(TID)
)

SELECT *
FROM TEST_S1

INSERT INTO TEST_S1 VALUES('SID', 01038227541)
INSERT INTO TEST_S2 VALUES('TID', '심영석')
INSERT INTO TEST_CHILD VALUES('CID', 'SID', 'TID')


--뷰(View)는 하나 이상의 테이블이나 다른 뷰의 데이터를 볼 수 있게 하는 데이터베이스 객체입니다. 
--실제 데이터는 뷰를 구성하는 테이블에 담겨 있지만 마치 테이블처럼 사용할 수 있습니다. 
--또한 테이블 뿐만 아니라 다른 뷰를 참조해 새로운 뷰를 만들어 사용할 수 있습니다.
--CREATE [OR REPLACE] VIEW VIEW_NAME(ALIAS) AS SUBQUERY ;

CREATE OR REPLACE VIEW V_EMP(NAME, DEPT)
AS SELECT EMP_NAME, DEPT_ID 
   FROM EMPLOYEE
   WHERE DEPT_ID = '90';

SELECT *
FROM V_EMP ;

-- 직급이 '사원'인 직원의 이름, 부서이름, 직급을 갖는 V_EMP_DEPT_JOB 뷰를 작성하시오

CREATE OR REPLACE VIEW V_EMP_DEPT_JOB("이름", "부서이름", "직급")
AS SELECT EMP_NAME, DEPT_NAME, JOB_TITLE
   FROM EMPLOYEE
   JOIN JOB USING(JOB_ID)
   JOIN DEPARTMENT USING(DEPT_ID)
   WHERE JOB_TITLE = '사원' ;

SELECT *
FROM V_EMP_DEPT_JOB

-- VIEW 삭제
DROP VIEW V_EMP_DEPT_JOB ;

--SEQUENCE 객체
--시퀀스란 자동으로 순차적으로 증가하는 순번을 반환하는 데이터베이스 객체입니다. 
--보통 PK값에 중복값을 방지하기위해 사용합니다. 
--예를들어 게시판에 글이 하나 추가될때마다 글번호(PK)가 생겨야 한다고 해보겠습니다. 
--만약 100번까지 글 번호가 생성되어있다면 그 다음 글이 추가가 되었을 경우 글 번호가 101으로 하나의 ROW를 생성해주어야 할것입니다. 
--이때 101이라는 숫자를 얻으려면 기존 글번호중 가장 큰 값에 +1을 하는 로직을 어딘가에 넣어야하는데 
--시퀀스를 사용하면 이러한 로직이 필요없이 데이터베이스에 ROW가 추가될때마다 자동으로 +1을 시켜주어 매우 편리합니다.

--문법
CREATE SEQUENCE [시퀀스명]
INCREMENT BY [증감숫자] --증감숫자가 양수면 증가 음수면 감소 디폴트는 1
START WITH [시작숫자] -- 시작숫자의 디폴트값은 증가일때 MINVALUE 감소일때 MAXVALUE
NOMINVALUE OR MINVALUE [최솟값] -- NOMINVALUE : 디폴트값 설정, 증가일때 1, 감소일때 -1028 
                               -- MINVALUE : 최소값 설정, 시작숫자와 작거나 같아야하고 MAXVALUE보다 작아야함
NOMAXVALUE OR MAXVALUE [최대값] -- NOMAXVALUE : 디폴트값 설정, 증가일때 1027, 감소일때 -1
                               -- MAXVALUE : 최대값 설정, 시작숫자와 같거나 커야하고 MINVALUE보다 커야함
CYCLE OR NOCYCLE --CYCLE 설정시 최대값에 도달하면 최소값부터 다시 시작 NOCYCLE 설정시 최대값 생성 시 시퀀스 생성중지
CACHE OR NOCACHE --CACHE 설정시 메모리에 시퀀스 값을 미리 할당하고 NOCACHE 설정시 시퀀스값을 메로리에 할당하지 않음




CREATE SEQUENCE TEST_SEQ
START WITH   300
INCREMENT BY 2
MAXVALUE     310
NOCYCLE
NOCACHE ;

SELECT TEST_SEQ.NEXTVAL FROM DUAL;
SELECT TEST_SEQ.CURRVAL FROM DUAL;
DROP SEQUENCE TEST_SEQ

--18 문제
--TOP-N 분석 : 조건에 맞는 최상위 레코드 N개를 식별해야하는 경우 사용하는 쿼리 기법
--원리 1. 정렬 2. ROWNUM 3. 부여된 순번대로 필요한 만큼 식별


--부서별 평균급여보다 많은 급여를 받은 사원의 정보 중 사원이름, 급여를 조회하려고 한다.
--평균급여는 정수 3자리에서 올림
--FROM 절에서 SUBQUERY(INLINE VIEW)를 이용해서 작성

--메인서브쿼리
( SELECT EMP_NAME, SALARY
  FROM ( SELECT DEPT_ID,  ROUND(AVG(SALARY), -3) AS DAVG
         FROM EMPLOYEE 
         GROUP BY DEPT_ID ) INVIEW --INLINE VIEW니까 별칭을 그냥 INVIEW라고 줌.
  JOIN   EMPLOYEE E ON (E.DEPT_ID = INVIEW.DEPT_ID)
  WHERE  SALARY > INVIEW.DAVG 
--ORDER BY 3 DESC; --인덱스가 셔플되버린다.
  ORDER BY 2 DESC )


--서브쿼리!
SELECT DEPT_ID,  ROUND(AVG(SALARY), -3) AS DAVG
FROM EMPLOYEE 
GROUP BY DEPT_ID

--메인처럼 보이는 쿼리를 서브쿼리로 한번 더 활용

SELECT ROWNUM, EMP_NAME, SALARY
FROM ( SELECT EMP_NAME, SALARY
       FROM ( SELECT DEPT_ID,  ROUND(AVG(SALARY), -3) AS DAVG
              FROM EMPLOYEE 
              GROUP BY DEPT_ID ) INVIEW
       JOIN   EMPLOYEE E ON (E.DEPT_ID = INVIEW.DEPT_ID)
       WHERE  SALARY > INVIEW.DAVG 
       ORDER BY 2 DESC )
WHERE ROWNUM = 1;

-- RANK() - WITHIN, OVER
SELECT *
FROM  ( SELECT EMP_NAME, SALARY,
               RANK() OVER(ORDER BY SALARY DESC) AS R
        FROM EMPLOYEE)
WHERE R <= 5;

-- DML (INSERT, UPDATE, DELETE )
-- UPDATE 구문(수정)
UPDATE TABLE_NAME
SET    [COLUMN_NAME = VALUE , ]
WHERE  CONDITION;
--DELETE 레코드 삭제, DROP 테이블 삭제
DELETE FROM TABLE_NAME
WHERE  CONDITION;

CREATE TABLE TEST_DML(
       ID       VARCHAR2(50) PRIMARY KEY,
       PWD      VARCHAR2(50) NOT NULL,
       NAME     VARCHAR2(50) NOT NULL,
       SALARY   NUMBER       CHECK( SALARY > 0 ),
       MARRIAGE CHAR(1)      CHECK( MARRIAGE IN ('Y', 'N'))
)

INSERT INTO TEST_DML VALUES('YSSIM', 'YSSIM', '심영석', 100, 'N')
INSERT INTO TEST_DML VALUES('SUPREME', 'ADMIN', '관리자', 100, 'Y')

UPDATE TEST_DML
SET    MARRIAGE = 'N', SALARY = 200
--WHERE  ID = 'YSSIM'; --WHERE 조건을 사용해야만 전체 다 데이터가 바뀌지 않는다. 특정 값만 업데이트 할 거니까.

DELETE
FROM TEST_DML  --이렇게 쓰면 전체 데이터가 날아간다.
WHERE ID = 'SUPREME' ; --특정 레코드 삭제를 위해 WHERE 절을 사용해서 조건을 입력해줘야 한다.

SELECT *
FROM TEST_DML;



