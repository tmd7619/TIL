--ERD �󿡼� ���� : ��ĺ�����
--ERD �󿡼� �Ǽ� : �ĺ�����
--ERD ��ǥ, ��, ���� �ľ� �ʿ�

-- table ������ �θ���� �����, �ڽ��� ��������
-- TABLE ���� ���� �ڽĺ��� DROP�ϰ�, �θ� DROP
-- PRIMARY KEY�� �� �ึ�� ������ ���� �ο���. �ߺ��� ���� �÷��� ���� �� ����

--DEFAULT�� �ƹ� ���� �Է����� �ʾƵ� NULL ���� �ƴ϶� 
--������ ���� �⺻������ �ڵ� �Էµǵ��� �ϴ� �������� �Դϴ�.

---NUMBER ���� �� �տ� 0�� ���� ���ڷ� �ν��� ���� ( 8������ �ν��ϱ� ����)

-- DDL ( CREATE, DROP, ALTER )
-- 1. ���̺� ����(��������)

CREATE TABLE TABLE_NAME(
     COLUMN_NAME DATETYPE [DEFAULT EXPR][CONSTRAINT], --�÷� ���� ����
     COLUMN_NAME DATETYPE [DEFAULT EXPR][CONSTRAINT],
     COLUMN_NAME DATETYPE [DEFAULT EXPR][CONSTRAINT],
     COLUMN_NAME DATETYPE [DEFAULT EXPR][CONSTRAINT],
     TABLE_CONSTRAINT --���̺� ���� ����
)

DROP TABLE TEST_MEMBER; --���̺� ����

CREATE TABLE TEST_MEMBER(--���̺� ����
    ID   VARCHAR2(50), --PRIMARY KEY, --�ߺ��� ������� �ʴ� ����
    PWD  VARCHAR2(50) NOT NULL, -- �� ���� ������� �ʴ� ����
    ADDR VARCHAR2(50) DEFAULT 'SEOUL', --DEFAULT ��, �⺻������ ���ԵǴ� ��
    PRIMARY KEY(ID) --TABLE �� ���� �� �� �ִ� �ڸ��̸�, NOT NULL(Į����)�� �Ұ��� PRIMARY KEY(Į����)�� ����
) --#1 �÷������� ���ÿ� ������ �ִ� ���
  - 

INSERT INTO TEST_MEMBER(ID, PWD, ADDR) VALUES('YSSIM', 'YSSIM', 'SEOUL');
INSERT INTO TEST_MEMBER VALUES('YSSIM', 'YSSIM', 'SEOUL'); --PRIMARY KEY�� �����س��� ������ ������ �� �Է� �Ұ���!
INSERT INTO TEST_MEMBER VALUES('yssim', NULL, NULL); --��ҹ��ڸ� �����Ѵ�.
INSERT INTO TEST_MEMBER(ID, PWD) VALUES('ADMIN', 'YSSIM'); --��ҹ��ڸ� �����Ѵ�. 

SELECT *
FROM TEST_MEMBER;

-- 2. �������� (NOT NULL - �÷� ���� ���ุ ����, UNIQUE, PRIMARY KEY, FOREIGEN KEY, CHECK)
-- 2-1. ���������� �����ϴ� ��� : ���̺� ����, �÷� ����

CREATE TABLE TEST_MEMBER(
    ID   VARCHAR2(50) PRIMARY KEY,
    PWD  VARCHAR2(50) PRIMARY KEY,
    ADDR VARCHAR2(50) DEFAULT 'SEOUL'
) --�⺻Ű�� �ϳ����� �Ѵ�. �� ���� �⺻Ű�� ������� �ʴ´�.
  --������ �� ���� ��ƾ� �Ѵٸ�?

CREATE TABLE TEST_MEMBER(
    ID   VARCHAR2(50),
    PWD  VARCHAR2(50),
    ADDR VARCHAR2(50) DEFAULT 'SEOUL',
    PRIMARY KEY(ID, PWD) --�̷� ������ COMPOSITE �Ͽ� ���� �� �ִ�.
)
  
--���� �÷� ��ü�� PRIMARY KEY �̱� ������ �Ʒ�ó�� �Է��� �����ϴ�.
--(YSSIM , YSSIM) ����1
--(YSSIM , ADMIN) ����2
INSERT INTO TEST_MEMBER(ID, PWD, ADDR) VALUES('YSSIM', 'YSSIM', 'SEOUL');
INSERT INTO TEST_MEMBER(ID, PWD, ADDR) VALUES('YSSIM', 'ADMIN', 'SEOUL'); 

SELECT *
FROM TEST_MEMBER;


--ERD ���� �����, LOCATION ���̺��� �����Ͽ� �⺻Ű�� ���̹޴� ���ο� �ܷ� ���̺� �����.
--FK (�θ� �����ϴ� �������̰ų� NULL���� ���)
CREATE TABLE TEST_FK(
       ID      CHAR(3) PRIMARY KEY,
       NAME    VARCHAR(50) NOT NULL,
       LID     CHAR(2) REFERENCES LOCATION(LOCATION_ID)--FK �÷����� ���� ���� �÷�! ��, �θ� �����ϴ� Ű
)                                                      --LOCATION���̺��� �⺻Ű�� LOCATION_ID�� �����Ͽ� LID��� FK�� �������
INSERT INTO TEST_FK VALUES('B', 'YSSIM', 'OT') --LOCATION_ID�� �ִ� ���鸸 �Է��� �����ϱ� ������
INSERT INTO TEST_FK VALUES('S', 'SUPREME', 'A') -- Aó�� LOCATION_ID�� ���� ���� �Է��ϸ� parent key not found��� ������ �߻���Ų��.

--CHAR�� ����ϸ� �ȵǴ� ����?
--���� ����ó��, CHAR�� 3�� �ְ� �Ǹ� �������̰� 3�� �Ǳ� ������,
--�� �߰��� 'A'��� �ѱ����� ���ڸ� �Է��ص� 'A__'ó�� 3���ڷ� �νĵ�
--���� VARCHAR�� �ϴ� ���� ����


--LOCATION ���̺� Ȯ��
SELECT *
FROM LOCATION; 
                              
--TABLE ����
DROP TABLE TEST_FK

--���̺��� �������� �����
CREATE TABLE TEST_FK(
       ID      CHAR(3) PRIMARY KEY,
       NAME    VARCHAR(50) NOT NULL,
       LID     CHAR(2),
       FOREIGN KEY(LID) REFERENCES LOCATION(LOCATION_ID)
)

INSERT INTO TEST_FK VALUES('B', 'YSSIM', 'OT')
INSERT INTO TEST_FK VALUES('S', 'SUP', 'A1')

--JOIN�غ���

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
    SALARY NUMBER CHECK (SALARY > 0),       --0���� ū SALARY ���� �ްڴ�. ���� X 
                                            --NUMBER(7,2) : 7�ڸ��� NUMBER �� �� 2�ڸ��� �Ǽ����� ���ڴ�.
    GENDER CHAR(1) CHECK (GENDER IN ('M', 'F')), --M �Ǵ� F ���� �ްڴ�. 
    PRIMARY KEY (ID, NAME)
)

INSERT INTO TEST_COMPOSITE_PK VALUES('YSSIM', '�ɿ���', -100, 'M') --check constraint (HR.SYS_C007085) violated �߻�/����Է�
INSERT INTO TEST_COMPOSITE_PK VALUES('YSSIM', '�ɿ���', 100, '?') --check constraint (HR.SYS_C007086) violated �߻�/M�Ǵ�F���Է�
INSERT INTO TEST_COMPOSITE_PK VALUES('YSSIM', '�ɿ���', 100, 'm') --check constraint (HR.SYS_C007086) violated �߻�/��ҹ��ڱ���
INSERT INTO TEST_COMPOSITE_PK VALUES('YSSIM', '�ɿ���', 100, 'M') --�����Է�

SELECT *
FROM TEST_COMPOSITE_PK

DROP TABLE TEST_COMPOSITE_FK;

CREATE TABLE TEST_COMPOSITE_FK(
    PID      VARCHAR2(50) PRIMARY KEY,
    ID       VARCHAR2(50) ,
    NAME     VARCHAR2(50) ,
    FOREIGN KEY (ID, NAME) REFERENCES TEST_COMPOSITE_PK (ID, NAME)
)

INSERT INTO TEST_COMPOSITE_FK VALUES('P001', 'YSSIM', '�ɿ���')

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
INSERT INTO TEST_S2 VALUES('TID', '�ɿ���')
INSERT INTO TEST_CHILD VALUES('CID', 'SID', 'TID')


--��(View)�� �ϳ� �̻��� ���̺��̳� �ٸ� ���� �����͸� �� �� �ְ� �ϴ� �����ͺ��̽� ��ü�Դϴ�. 
--���� �����ʹ� �並 �����ϴ� ���̺� ��� ������ ��ġ ���̺�ó�� ����� �� �ֽ��ϴ�. 
--���� ���̺� �Ӹ� �ƴ϶� �ٸ� �並 ������ ���ο� �並 ����� ����� �� �ֽ��ϴ�.
--CREATE [OR REPLACE] VIEW VIEW_NAME(ALIAS) AS SUBQUERY ;

CREATE OR REPLACE VIEW V_EMP(NAME, DEPT)
AS SELECT EMP_NAME, DEPT_ID 
   FROM EMPLOYEE
   WHERE DEPT_ID = '90';

SELECT *
FROM V_EMP ;

-- ������ '���'�� ������ �̸�, �μ��̸�, ������ ���� V_EMP_DEPT_JOB �並 �ۼ��Ͻÿ�

CREATE OR REPLACE VIEW V_EMP_DEPT_JOB("�̸�", "�μ��̸�", "����")
AS SELECT EMP_NAME, DEPT_NAME, JOB_TITLE
   FROM EMPLOYEE
   JOIN JOB USING(JOB_ID)
   JOIN DEPARTMENT USING(DEPT_ID)
   WHERE JOB_TITLE = '���' ;

SELECT *
FROM V_EMP_DEPT_JOB

-- VIEW ����
DROP VIEW V_EMP_DEPT_JOB ;

--SEQUENCE ��ü
--�������� �ڵ����� ���������� �����ϴ� ������ ��ȯ�ϴ� �����ͺ��̽� ��ü�Դϴ�. 
--���� PK���� �ߺ����� �����ϱ����� ����մϴ�. 
--������� �Խ��ǿ� ���� �ϳ� �߰��ɶ����� �۹�ȣ(PK)�� ���ܾ� �Ѵٰ� �غ��ڽ��ϴ�. 
--���� 100������ �� ��ȣ�� �����Ǿ��ִٸ� �� ���� ���� �߰��� �Ǿ��� ��� �� ��ȣ�� 101���� �ϳ��� ROW�� �������־�� �Ұ��Դϴ�. 
--�̶� 101�̶�� ���ڸ� �������� ���� �۹�ȣ�� ���� ū ���� +1�� �ϴ� ������ ��򰡿� �־���ϴµ� 
--�������� ����ϸ� �̷��� ������ �ʿ���� �����ͺ��̽��� ROW�� �߰��ɶ����� �ڵ����� +1�� �����־� �ſ� ���մϴ�.

--����
CREATE SEQUENCE [��������]
INCREMENT BY [��������] --�������ڰ� ����� ���� ������ ���� ����Ʈ�� 1
START WITH [���ۼ���] -- ���ۼ����� ����Ʈ���� �����϶� MINVALUE �����϶� MAXVALUE
NOMINVALUE OR MINVALUE [�ּڰ�] -- NOMINVALUE : ����Ʈ�� ����, �����϶� 1, �����϶� -1028 
                               -- MINVALUE : �ּҰ� ����, ���ۼ��ڿ� �۰ų� ���ƾ��ϰ� MAXVALUE���� �۾ƾ���
NOMAXVALUE OR MAXVALUE [�ִ밪] -- NOMAXVALUE : ����Ʈ�� ����, �����϶� 1027, �����϶� -1
                               -- MAXVALUE : �ִ밪 ����, ���ۼ��ڿ� ���ų� Ŀ���ϰ� MINVALUE���� Ŀ����
CYCLE OR NOCYCLE --CYCLE ������ �ִ밪�� �����ϸ� �ּҰ����� �ٽ� ���� NOCYCLE ������ �ִ밪 ���� �� ������ ��������
CACHE OR NOCACHE --CACHE ������ �޸𸮿� ������ ���� �̸� �Ҵ��ϰ� NOCACHE ������ ���������� �޷θ��� �Ҵ����� ����




CREATE SEQUENCE TEST_SEQ
START WITH   300
INCREMENT BY 2
MAXVALUE     310
NOCYCLE
NOCACHE ;

SELECT TEST_SEQ.NEXTVAL FROM DUAL;
SELECT TEST_SEQ.CURRVAL FROM DUAL;
DROP SEQUENCE TEST_SEQ

--18 ����
--TOP-N �м� : ���ǿ� �´� �ֻ��� ���ڵ� N���� �ĺ��ؾ��ϴ� ��� ����ϴ� ���� ���
--���� 1. ���� 2. ROWNUM 3. �ο��� ������� �ʿ��� ��ŭ �ĺ�


--�μ��� ��ձ޿����� ���� �޿��� ���� ����� ���� �� ����̸�, �޿��� ��ȸ�Ϸ��� �Ѵ�.
--��ձ޿��� ���� 3�ڸ����� �ø�
--FROM ������ SUBQUERY(INLINE VIEW)�� �̿��ؼ� �ۼ�

--���μ�������
( SELECT EMP_NAME, SALARY
  FROM ( SELECT DEPT_ID,  ROUND(AVG(SALARY), -3) AS DAVG
         FROM EMPLOYEE 
         GROUP BY DEPT_ID ) INVIEW --INLINE VIEW�ϱ� ��Ī�� �׳� INVIEW��� ��.
  JOIN   EMPLOYEE E ON (E.DEPT_ID = INVIEW.DEPT_ID)
  WHERE  SALARY > INVIEW.DAVG 
--ORDER BY 3 DESC; --�ε����� ���õǹ�����.
  ORDER BY 2 DESC )


--��������!
SELECT DEPT_ID,  ROUND(AVG(SALARY), -3) AS DAVG
FROM EMPLOYEE 
GROUP BY DEPT_ID

--����ó�� ���̴� ������ ���������� �ѹ� �� Ȱ��

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
-- UPDATE ����(����)
UPDATE TABLE_NAME
SET    [COLUMN_NAME = VALUE , ]
WHERE  CONDITION;
--DELETE ���ڵ� ����, DROP ���̺� ����
DELETE FROM TABLE_NAME
WHERE  CONDITION;

CREATE TABLE TEST_DML(
       ID       VARCHAR2(50) PRIMARY KEY,
       PWD      VARCHAR2(50) NOT NULL,
       NAME     VARCHAR2(50) NOT NULL,
       SALARY   NUMBER       CHECK( SALARY > 0 ),
       MARRIAGE CHAR(1)      CHECK( MARRIAGE IN ('Y', 'N'))
)

INSERT INTO TEST_DML VALUES('YSSIM', 'YSSIM', '�ɿ���', 100, 'N')
INSERT INTO TEST_DML VALUES('SUPREME', 'ADMIN', '������', 100, 'Y')

UPDATE TEST_DML
SET    MARRIAGE = 'N', SALARY = 200
--WHERE  ID = 'YSSIM'; --WHERE ������ ����ؾ߸� ��ü �� �����Ͱ� �ٲ��� �ʴ´�. Ư�� ���� ������Ʈ �� �Ŵϱ�.

DELETE
FROM TEST_DML  --�̷��� ���� ��ü �����Ͱ� ���ư���.
WHERE ID = 'SUPREME' ; --Ư�� ���ڵ� ������ ���� WHERE ���� ����ؼ� ������ �Է������ �Ѵ�.

SELECT *
FROM TEST_DML;



