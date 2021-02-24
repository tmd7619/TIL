--SELECT ����

SELECT   [Ư���÷� | *(��ü�÷�) | ǥ����(SELECT - (SUBQUERY)) |DISTINCT |AS �÷� ��Ī-- | ==OR   
FROM     [���̺��̸� | JOIN | SELECT - (SUBQUERY) ]  
WHERE    ���ǽ� | SELECT - (SUBQUERY)
GROUP BY ǥ���� | SELECT - (SUBQUERY)   
HAVING   ���ǽ�
ORDER BY �����÷�; -- ���� �������� �����


-- ��ü�÷� EMPLOYEE
SELECT * 
FROM EMPLOYEE;

-- Ư���÷�

SELECT EMP_NAME
FROM EMPLOYEE;

-- �����÷� ��������
SELECT EMP_NAME,
        EMP_ID,
        EMP_NO
FROM EMPLOYEE;

-- �÷� ��Ī �����ϱ�
-- ���ǻ���: �ݵ�� ���ڷ� �����ؾ���(���ںҰ�), ���࿡ Ư����ȣ,������ ���� �Ǹ� " " 
-- AS Ű����� ������ ����
SELECT EMP_NAME AS "�� ��",
        EMP_ID AS ���̵�,
        EMP_NO AS �ֹι�ȣ,
        SALARY AS "�޿�(��)", -- () Ư����ȣ�̱� ����, ""�� �����ֱ�
        DEPT_ID �μ���ȣ --AS ���� ��Ī ����
FROM EMPLOYEE;

--DISTINCT : ���� �ߺ��� ������ �� ����ϴ� Ű����
SELECT DISTINCT JOB_ID
FROM EMPLOYEE ;

-- ǥ����
-- �÷� ���� ���� ������ ������ �ۼ��� �� �ִ�.

SELECT EMP_NAME AS �����,
        SALARY AS �޿�,
        (SALARY + (SALARY*BONUS_PCT))*12 AS ����
        
FROM EMPLOYEE;

--�����÷�
--'������', "Ű����"
SELECT EMP_ID,
        EMP_NAME,
        '����' AS �ٹ�����
FROM EMPLOYEE;

SELECT [Ư���÷� | *(��ü�÷�) | ǥ���� |DISTINCT |AS �÷� ��Ī-- | ==OR   
FROM ���̺��̸� 
WHERE ���ǽ�(���� ����)

--�μ���ȣ�� 90���� ������� ������ Ȯ���ϰ� �ʹٸ�
-- WHERE ���� ����
-- ���������� �����ڸ� ����� �� �ִ�. = : �Ҵ��� �ƴ� �񱳿�����
SELECT *
FROM EMPLOYEE
WHERE DEPT_ID = 90 -- ��������� ;�� �Ƚᵵ ��

--�μ��ڵ尡 90�̰�, �޿��� 2000000���� ���� �޴� ����� �̸�,�μ��ڵ�,�޿��� ��ȸ

SELECT EMP_NAME,
        DEPT_ID,
        SALARY
FROM EMPLOYEE        
WHERE DEPT_ID = 90 AND
        SALARY > 2000000 ;

--�μ��ڵ尡 90�̰ų� 20���� ����� �̸�,�μ��ڵ�,�޿��� ��ȸ

SELECT EMP_NAME,
        DEPT_ID,
        SALARY
FROM EMPLOYEE        
WHERE DEPT_ID = 90 OR DEPT_ID = 20 ;


-- 'XXX���� ������ XXXXX�� �Դϴ�'
-- || : ���Ῥ����
-- [�÷� || �÷�] [�÷� ||'���ڿ�']
SELECT EMP_ID || EMP_NAME || SALARY
FROM EMPLOYEE ; 

SELECT EMP_ID ||'�� ������' ||SALARY||'���Դϴ�'
FROM EMPLOYEE ; 

-- Operator = , > , >=, <, <= , !=
-- BETWEEN AND, LIKE, IS NULL, IN

-- BETWEEN AND
-- ���Ϸ��� ���� ������ ���� (���� ���� ���� ���� �������)�� ���ԵǸ� TURE�� ��ȯ�ϴ� ������
-- �޿��� 3,500,000������ ���� �ް� 5,500,000������ ���� �޴� ���� �̸��� �޿� ��ȸ]
SELECT EMP_NAME,
        SALARY
FROM    EMPLOYEE
WHERE SALARY BETWEEN 3500000 AND 5500000 ;

--�Ǵ� 
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
    emp_name LIKE '��%';
--EX2)
SELECT EMP_NAME,PHONE 
FROM EMPLOYEE
WHERE PHONE LIKE '___9%' ;

-- EMAIL ID �� '_' �� �ڸ��� 3�ڸ��� ������ ��ȸ�Ѵٸ�
SELECT EMP_NAME, EMAIL
FROM EMPLOYEE
WHERE EMAIL LIKE '___\_%' ESCAPE'\' ; --ESCAPE �ڿ��� ���ڷ� ���ڴ� �ƹ� Ư�����ڳ� �������

--'��'�� ���� �ƴ� ������ �̸��� �޿��� ��ȸ
SELECT EMP_NAME, SALARY
FROM   EMPLOYEE
WHERE  EMP_NAME NOT LIKE '��%' ;

--�μ��� ���µ��� �ұ��ϰ� ���ʽ��� ���޹޴� ������ �̸�, �μ�, ���ʽ��� ��ȸ�Ѵٸ�
--IS NULL, IS NOT NULL
SELECT  EMP_NAME, DEPT_ID, BONUS_PCT
FROM   EMPLOYEE 
WHERE  DEPT_ID IS NULL AND BONUS_PCT IS NOT NULL ;

-- IN = OR
SELECT EMP_NAME, DEPT_ID, SALARY
FROM   EMPLOYEE
WHERE  DEPT_ID IN('90','20') ;

--�μ���ȣ�� 20�� �Ǵ� 90���� ����� �޿��� 3000000���� ����(�ʰ�)�޴� ����� �̸�,�޿�,�μ��ڵ� ��ȸ
SELECT  EMP_NAME,SALARY,DEPT_ID
FROM    EMPLOYEE
WHERE   (DEPT_ID = 20 OR DEPT_ID = 90) -- ()�� ���� �������� �켱������ ��������  
--WHERE DEPT_ID IN('20','90')
AND     SALARY > 3000000 ;

