
-- �Լ� ����
-- ��ȯ ����� ���� ���� �� �Լ��� �׷� �Լ��� ���� 
-- ���� �� �Լ� - input N�� - output N�� 
-- �׷� �Լ� - input N�� - output 1��
-- �Լ��� SELECT, WHERE ���� �����ϴ�

-- < ������ �Լ� > --

--LENGTH() : NUMBER -> ������ ������ ��ȯ�ϴ� �Լ�
--���ڿ� -> CHAR(��������) , VARCHAR2(��������)
-- Orcle  �ѱ� 1���� : 3BYTE , ���� 1���� : 1BYTE
-- CHAR Ÿ���� �ѱ� ������ �ٸ��� ����� -> VARCHAR2�� ����ϴ� ���� ����
SELECT CHARTYPE,
        LENGTH(CHARTYPE),
        VARCHARTYPE,
        LENGTH(VARCHARTYPE)
FROM COLUMN_LENGTH;

--LPAD / RPAD : ���ڿ��� ���̸� �����̴� �Լ�
--����ȿ���� �������� ���ؼ� ����ϴ� ��찡 ����

SELECT EMAIL, LPAD(EMAIL,15,'.') -- LPAD�� ���������� ���ĵ�,  ���̸� 15�� ���߰� ������� .���� ä��ڴ�
FROM EMPLOYEE ;

SELECT EMAIL, RPAD(EMAIL,30,'.') 
FROM EMPLOYEE ;

SELECT  EMAIL, RPAD(EMAIL,30,'.'), LPAD(EMAIL,30,' '),
        LENGTH(LPAD(EMAIL,30,' '))
FROM EMPLOYEE;

-- TRIM / LTRIM / RTRIM : ���ڸ� ������ �� ����ϴ� �Լ�
-- DUAL : DUMMY TABLE
SELECT  TRIM('  TEST  '), -- �翷 ���� ���� 
        LENGTH(TRIM('  TEST  '))
FROM DUAL ;

SELECT  RTRIM('  TEST  '), -- ������ ���� ���� 
        LENGTH(RTRIM('  TEST  '))
FROM DUAL ;

SELECT  LTRIM('123123TEST','123'), -- 123�� ������ �ƴ϶�, 1 OR 2 OR 3 ���� ������ 
        RTRIM('XYZYYYTEST','TEST'),  -- ���� ����
        TRIM(LEADING '1' FROM 'TEST1'), -- LTRIM����, ���ʺ��� 1�� �����ϰڴ�
        TRIM(TRAILING '1' FROM '123TEST111') -- RTRIM����, �����ʺ��� 1�� �����ϰڴ�
FROM DUAL ;

--SUBSTR('���ڿ� �߿���','���°�ڸ�����','��� �ڸ����� �������ڴ�')
SELECT SUBSTR('THIS IS A TEST', 6, 2) FROM DUAL;
SELECT SUBSTR('THIS IS A TEST', -6, 5) FROM DUAL;

--ROUND() : ������ �ڸ������� �ݿø� �ϴ� �Լ�
--��ø� �÷��̽��� 0���� ũ�� �Ҽ��ڸ�, 0���� ������ �����ڸ� ���� �ݿø�

SELECT ROUND(125.315) FROM DUAL; -- �Ҽ��� ù��° �ڸ����� �ݿø�
SELECT ROUND(125.315,0) FROM DUAL -- 0�� ���� ���� �����ϰ� ������, ���� ����
SELECT ROUND(125.315,1) FROM DUAL -- �Ҽ��� ù��° �ڸ����� ����ڴ� -> 2��°���� �ݿø�
SELECT ROUND(125.315,-1) FROM DUAL -- ���� ù��° �ڸ����� �ݿø� 
SELECT ROUND(125.315,-2) FROM DUAL

--TRUNC() : ������ �ڸ������� ���� �ϴ� �Լ�
SELECT TRUNC(125.315) FROM DUAL; 
SELECT TRUNC(125.315,0) FROM DUAL;
SELECT TRUNC(125.315,1) FROM DUAL;
SELECT TRUNC(125.315,-1) FROM DUAL

-- ��¥�Լ� 
SELECT SYSDATE FROM DUAL;

--ADD_MONTHS(data, N): ������ ��ŭ�� �� ���� ���� ��¥�� ��ȯ�ϴ� �Լ�
-- data : ������ �Ǵ� ��¥
-- N    : date�� ���Ϸ��� �� ��
SELECT  EMP_NAME,
        HIRE_DATE,
        ADD_MONTHS(HIRE_DATE,240) AS 20���� -- HIRE_DATE�� 20����
FROM    EMPLOYEE ; 

--MONTHS_BETWEEN(data1, data2) : ������ �� ��¥ ������ �� ���� ��ȯ�ϴ� �Լ�
-- data1 > data2 : ��� ��ȯ
-- data1 < data2 : ���� ��ȯ

--'2010�� 1�� 1��'�������� �Ի����� 10���� ���� �������� �ٹ���� ��ȸ
SELECT  EMP_NAME,
        HIRE_DATE,
        TRUNC(MONTHS_BETWEEN(SYSDATE,HIRE_DATE)/12) AS �ٹ����
FROM    EMPLOYEE
WHERE   MONTHS_BETWEEN(SYSDATE,HIRE_DATE) > 120;

-- ���ڿ� INSTR(string,searchChar,[position,occurrence]) : �ش� ������ �ε��������� ����
-- email �÷� ���� '@vvc.com'���ڿ� �� .���� ���� 'c' ��ġ�� ���ϰ� �ʹٸ�?
SELECT *
FROM EMPLOYEE;

SELECT  EMAIL,
        INSTR(EMAIL, 'c',-1,2) ��ġ,
        INSTR(EMAIL,'c',INSTR(EMAIL,'.')-1)
FROM    EMPLOYEE ; 

-- ������ Ÿ�� ��ȯ �Լ� 
-- TO_CHAR : NUMBER/DATE Ÿ���� CHARACTERŸ������ ��ȯ�ϴ� �Լ�

SELECT TO_CHAR(1234,'99999') FROM DUAL; -- 1234
SELECT TO_CHAR(1234,'09999') FROM DUAL; -- 01234
SELECT TO_CHAR(1234,'L9999') FROM DUAL; -- ��ȭǥ��1234
SELECT TO_CHAR(1234,'$9999') FROM DUAL; -- �޷�ǥ��1234
SELECT TO_CHAR(1234,'99,999') FROM DUAL; -- 1,234
SELECT TO_CHAR(1234,'09,999') FROM DUAL; -- 01,234
SELECT TO_CHAR(1234,'999') FROM DUAL;   -- ####

-- TO_CHAR :(��¥|����, ǥ�����) -> ���ڿ� 
-- ������ FORMAT ������ ������� !
SELECT  SYSDATE,
        TO_CHAR(SYSDATE,'AM Q YYYY-MM-DD HH:MI:SS') "�� Ī" -- ��Ī �ٶ�, �����̳� Ư�����ڰ� ���� ��� ""���� ! 
FROM DUAL;

SELECT  EMP_NAME,
        HIRE_DATE,
        TO_CHAR(HIRE_DATE,'YYYY "��" MM"��" DD"��"') ,  -- ""�� ���� ���Ƿ� ������ ������ �� ���� 
        SUBSTR(HIRE_DATE, 1, 2) || '��' 
FROM    EMPLOYEE;

        
FROM    EMPLOYEE; 

--SUBSTR(����|��¥) 

SELECT TO_DATE('20210112','YYYYMMDD') -- ������ ���ڿ� �°� ������ �Ȱ��� �����������
FROM DUAL;

SELECT TO_CHAR(TO_DATE('20100101', 'YYYYMMDD'), 'YYYY, MON')
--SELECT TO_CHAR('20210112','YYYY, MON') -- ������ �ٸ��� ������ ERROR
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
--����Ʈ Ÿ�Կ� �ú��ʰ� ���Եɰ��, �����Ϸδ� ã�� ���� ���� 
--���� �÷��� YYMMDD���·� ������Ŵ

-- YYYY : ���� ���⸦ �������� ������ EX) '981212' -> 2098�� 12��~ 
-- RRRR : �⵵ ���ڸ��� 50-99�ϰ��, ���� ���⸦ ��ȯ 0-49�� ���� ����

SELECT  EMP_NAME,
        HIRE_DATE,
        TO_CHAR(TO_DATE(HIRE_DATE, 'RR/MM/DD') , 'YYYY')
FROM    EMPLOYEE
WHERE   EMP_NAME = '�Ѽ���'; 

--  �ֹι�ȣ ���ڸ� ���ڸ� �ɰ��� TO_NUMBER(CHAR) -> NUMBER
SELECT  EMP_NO, 
        SUBSTR(EMP_NO,1,6) ,
        SUBSTR(EMP_NO,8) ,
        TO_NUMBER( SUBSTR(EMP_NO, 1 , 6) ) + TO_NUMBER( SUBSTR(EMP_NO,8))
FROM    EMPLOYEE ;
--�������� : STRING, ���������� : NUMBER


-- ��Ÿ�Լ� NVL : NULL�� ������ ������ ��ȯ�ϴ� �Լ�
SELECT  EMP_NAME, SALARY, NVL(BONUS_PCT,0) -- BONUS_PCT�� NULL�̸�, 0���� ��ü�ϰڴ�
FROM    EMPLOYEE
WHERE   SALARY > 3500000;

SELECT  EMP_NAME,
        (SALARY*12)+((SALARY*12)*BONUS_PCT)
FROM    EMPLOYEE
WHERE   SALARY > 3500000; -- ����� NULL������ �����⿡,

SELECT  EMP_NAME,
        (SALARY*12)+       --NVL�Լ����
        ( (SALARY*12)*NVL(BONUS_PCT,0) )
FROM    EMPLOYEE
WHERE   SALARY > 3500000;

-- DECODE : SELECT �������� IF-ELSE���� ���������� ������ ����Ŭ DBMS �����Լ�
SELECT  EMP_NO,
        DECODE(SUBSTR(EMP_NO,8,1) ,
        '1' , '����', '3', '����', '����') AS GENDER
FROM    EMPLOYEE ;

SELECT  EMP_ID , -- ����?
        EMP_NAME ,
        DECODE(MGR_ID , NULL, 'ADMIN', MRG_ID),
        NVL(MGR_ID, 'ADMIN') 
FROM    EMPLOYEE
WHERE   JOB_ID = 'J4' ;

--������ ���޺� �λ�޿��� Ȯ���ϰ�ʹ�
--J7 -> 20% �λ�
--J6 -> 15% �λ�
--J5 -> 10% �λ�
--������ ������ �λ��� X
SELECT  EMP_NAME,
        JOB_ID,
        SALARY,
        DECODE(JOB_ID ,
            'J7', SALARY * 1.2 ,
            'J6', SALARY * 1.15 ,
            'J5', SALARY * 1.1 ,
            SALARY)AS "�λ� �޿�"
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
        END AS "�λ� �޿�"
FROM    EMPLOYEE;

--case2) �� ��ȣ�Ǵ� ���� 
SELECT  EMP_NAME,
        JOB_ID,
        SALARY,
        CASE WHEN JOB_ID = 'J7 SALARY * 1.2 
             WHEN JOB_ID = 'J6 SALARY * 1.15 
             WHEN JOB_ID = 'J5 SALARY * 1.1 
            ELSE SALARY
        END AS "�λ� �޿�"
FROM    EMPLOYEE;

 --Group Function(�����Լ�, �׷��Լ�)
 -- group by
 -- �׷� �Լ��� SELECT �� ���Ǹ� �ٸ� �÷��� ���� �Ұ�
 -- �׷� �Լ��� NULL �� ���� �� ������ �ϹǷ� ���ǿ��

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

--�μ���ȣ�� 50�̰ų�, �μ���ȣ�� �������� �ʴ� ����� �̸�, �޿��� ��ȸ�ض�
-- ���� �޿������� ������? ORDER BY[�����÷�][ASC|DESC]
SELECT  EMP_NAME,
        SALARY
FROM    EMPLOYEE
WHERE   DEPT_ID = '50' OR DEPT_ID IS NULL 
ORDER BY SALARY DESC ; 

-- �Ի����� 03�� 1�� 1�� ���� �Ի��ڵ��� �̸�, �Ի���, �μ���ȣ�� ��ȸ
--��) �μ���ȣ�� ���������� �����ϰ� ������ �Ի����� ���� ������ �����ϰ� ������ �̸��� ���� ������ ����

SELECT  EMP_NAME �̸�,
        HIRE_DATE �Ի���,
        DEPT_ID �μ�
FROM    EMPLOYEE
WHERE   HIRE_DATE > TO_DATE('03/01/01' , 'RR/MM/DD') 
ORDER BY DEPT_ID DESC NULLS LAST , HIRE_DATE, EMP_NAME
--ORDER BY 3 DESC NULLS LAST , 2, 1
--ORDER BY �μ� DESC NULLS LAST , �Ի���, �̸�;

-- GROUP BY [�����÷�]
-- �μ��� ��ձ޿� -- WHERE X WHY? WHERE�� �࿡ ���� ����
SELECT  DEPT_ID, 
        JOB_ID , 
        ROUND(AVG(SALARY),-5) AS �޿����
FROM    EMPLOYEE
GROUP BY ROLLUP( DEPT_ID, JOB_ID)  -- GROUP BY�� ���ǵ� �Ӽ��� SELECT������ ���� ���Ѥ���
ORDER BY DEPT_ID ; -- ��������
-- ROLLUP() : ���� �׷쿡 ���� ������, ������ ������

-- ��ձ޿��� 300�̻�?
SELECT  DEPT_ID, ROUND(AVG(SALARY),-5) AS �޿����
FROM    EMPLOYEE
GROUP BY DEPT_ID  
HAVING  AVG(SALARY) > 3000000
ORDER BY �޿���� DESC;



-- ������ ���� �޿� ����� ���Ѵٸ�?
SELECT  DECODE( SUBSTR(EMP_NO,8,1),
                '1', '����', '3', '����' , '����'),
        AVG(SALARY)

FROM    EMPLOYEE
GROUP BY DECODE( SUBSTR(EMP_NO,8,1), -- GROUP BY�� INDEX,��Ī ������ �ȵ�
                '1', '����', '3', '����' , '����')
ORDER BY 2 DESC ; 

--CASE ? 
SELECT  CASE SUBSTR(EMP_NO,8,1)
            WHEN '1' THEN '����'
            WHEN '3' THEN '����'
            ELSE  ����
        END ,
        AVG(SALARY)
FROM    EMPLOYEE
GROUP BY CASE SUBSTR(EMP_NO,8,1)
            WHEN '1' THEN '����'
            WHEN '3' THEN '����'
            ELSE  ����
        END 
ORDER BY 2 DESC ; 


--ORDER BY ��� ��

SELECT  EMP_NAME, SALARY
FROM    EMPLOYEE
WHERE   DEPT_ID = '50'
OR      DEPT_ID IS NULL
ORDER BY SALARY DESC;

SELECT  EMP_NAME, HIRE_DATE, DEPT_ID
FROM    EMPLOYEE
WHERE   HIRE_DATE > TO_DATE('20030101','YYYYMMDD')
ORDER BY DEPT_ID DESC, HIRE_DATE, EMP_NAME;

SELECT  EMP_NAME �̸�,
        HIRE_DATE �Ի���,
        DEPT_ID �μ��ڵ�
FROM    EMPLOYEE
WHERE   HIRE_DATE > TO_DATE('20030101','YYYYMMDD')
ORDER BY �μ��ڵ� DESC, �Ի���, �̸� ; -- �÷���Ī�� ������ �� �ִ�
-- ORDER BY 3 DESC 2, 1 ; --INDEX ��� ����

-- GROUP BY ��� ��
-- �÷� ��Ī�̳� �÷� ��� ������ ����� �� ����

SELECT  EMP_NAME, DEPT_ID, COUNT(*) AS COUNT --�����Լ��� ���Ǿ��� ������ GROUP BY�� EMP_NAME���� �����ؾ���
FROM    EMPLOYEE
GROUP BY EMP_NAME, DEPT_ID

-- HAVING 
SELECT  DEPT_ID, SUM(SALARY)
FROM    EMPLOYEE
GROUP BY DEPT_ID
HAVING  SUM(SALARY) > 900000;

SELECT  DEPT_ID, SUM(SALARY)
FROM    EMPLOYEE
WHERE   SUM(SALARY)> 900000 -- ERROR WHERE������ �׷� �Լ��� ����� �� ���� 
GROUP BY DEPT ID ; 
