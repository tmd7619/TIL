
--SET Oprator - UNION
-- UNION : �ߺ��� ������� �����ϰ� ���
-- UNION ALL : �ߺ��� ����� �����ϰ� ���
-- INTERSECT : ������
-- EXCEPT : ������
SELECT  EMP_ID,
        ROLE_NAME
FROM    EMPLOYEE_ROLE
UNION   ALL
SELECT  EMP_ID,
        ROLE_NAME
FROM    ROLE_HISTORY;

--����1�� ����2�� SELECT ����� �ݵ�� ����(�÷�����, ������ Ÿ��)
--�ؾ� �ϹǷ� �̸� ���� DUMMY COLUMN�� ����� �� �ִ�
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

--UNION 50�� �μ����� ������ �������� �����Ͽ� ǥ��

SELECT  *
FROM    EMPLOYEE
WHERE   DEPT_ID = '50' ;


SELECT  EMP_ID,
        EMP_NAME,
        '����' AS ����
FROM    EMPLOYEE
WHERE   MGR_ID IS NOT NULL AND DEPT_ID = '50'
UNION
SELECT  EMP_ID,
        EMP_NAME,
        '������'  -- �Ϲ������� ����1�� ��Ī�� ������ ������ 
FROM    EMPLOYEE
WHERE   MGR_ID IS NULL AND DEPT_ID = '50'
ORDER BY 3;

--����(JOB_TITLE)�� �븮 �Ǵ� ��� ���� ������ ��ȸ (�̸�, ����)
SELECT  *
FROM    EMPLOYEE;

SELECT  EMP_NAME,JOB_TITLE      
FROM    EMPLOYEE
JOIN    JOB USING(JOB_ID)
WHERE   JOB_TITLE = '�븮'
UNION
SELECT  EMP_NAME,JOB_TITLE 
FROM    EMPLOYEE
JOIN    JOB USING(JOB_ID)
WHERE   JOB_TITLE = '���'
ORDER BY 2 ;

--UNION ���� ?
SELECT  EMP_NAME,JOB_TITLE 
FROM    EMPLOYEE
JOIN    JOB USING(JOB_ID)
WHERE   JOB_TITLE IN('�븮','���')
ORDER BY 2 ;

--SUBQUERY
--���¿��̶� �̸��� �̿��Ͽ�
--����(JOB_ID)�� �����ϰ�, ���¿����� �޿�(SALARY)�� ���� ����� �̸�, ����, �޿��� ��ȸ�϶�

SELECT  EMP_NAME, JOB_ID, SALARY
FROM    EMPLOYEE
WHERE   JOB_ID = (  SELECT  JOB_ID
                    FROM    EMPLOYEE
                    WHERE   EMP_NAME = '���¿�' )
AND     SALARY > (  SELECT  SALARY
                    FROM    EMPLOYEE
                    WHERE   EMP_NAME = '���¿�') ;

-- �ּ� �޿��� �޴� ����� �̸�, ����, �޿��� ��ȸ�϶�
-- 1. �ּұ޿� Ȯ��
-- 2. �˻�
-- 3. 

SELECT  EMP_NAME, JOB_ID, SALARY
FROM    EMPLOYEE
WHERE   SALARY = (  SELECT  MIN(SALARY) -- �ּұ޿� Ȯ��, ���� ������1�� -> ������ SUBQUERY
                    FROM    EMPLOYEE ) ;

-- �μ��� �޿������� ���� ���� �μ��� �̸�, �޿������� ��ȸ�϶�
SELECT  DEPT_NAME,
        SUM(SALARY)
FROM    EMPLOYEE
JOIN    DEPARTMENT USING (DEPT_ID)
GROUP BY    DEPT_NAME
HAVING      SUM(SALARY) = ( SELECT  MAX(SUM(SALARY))
                            FROM    EMPLOYEE 
                            GROUP BY DEPT_ID   ) ;

-- ���� �� ��������
-- IN, NOT, IN, ANY, ALL �����ڸ� ���� �� ������������ ����� �� �ִ�.

SELECT  EMP_ID,
        EMP_NAME,
        '������' AS ����
FROM    EMPLOYEE
WHERE   EMP_ID  IN (SELECT MGR_ID FROM EMPLOYEE)

-- ������ ���� �������� NULL���� ������, NOT IN�� �Ҷ� ��ü �������� NULL�� �����ϰ� ��
-- ���� NULL���� ���Ž�������� 
-- IN�� ��� ����

SELECT  EMP_ID,
        EMP_NAME,
        '����' AS ����
FROM    EMPLOYEE
WHERE   EMP_ID NOT IN (SELECT MGR_ID FROM EMPLOYEE
                       WHERE MGR_ID IS NOT NULL) -- NULL �� ���� 
UNION                      
SELECT  EMP_ID,
        EMP_NAME,
        '������' AS ����
FROM    EMPLOYEE
WHERE   EMP_ID  IN (SELECT MGR_ID FROM EMPLOYEE)

-- �� ������ �ڵ带 �ٸ� ���(NOT UNION)���� �����Ѵٸ� ?

--���1
SELECT  EMP_ID,
        EMP_NAME ,
        CASE  
        WHEN MGR_ID IS NOT NULL THEN '����'
        ELSE '����'
        END AS ����
FROM    EMPLOYEE ; 

--��� 2
SELECT  EMP_ID,
        EMP_NAME,
        CASE WHEN EMP_ID IN (SELECT MGR_ID FROM EMPLOYEE) THEN '������ ELSE '���� ' END
FROM    EMPLOYEE ;


--������ �������� ANY, ALL ������--
--ANY �� ������ �ڽ� �ȿ� �ִ� �� ,
--ALL �� ������ �ڽ� �ٱ����� �ִ� �� ���� ����

SELECT  EMP_NAME,
        SALARY
FROM    EMPLOYEE
JOIN    JOB USING (JOB_ID)
WHERE   JOB_TITLE='�븮'
AND     SALARY < ALL
                    (SELECT SALARY
                     FROM   EMPLOYEE
                     JOIN   JOB USING (JOB_ID)
                     WHERE  JOB_TITLE = '����') ; 
                     
                     
-- �ڱ� ����(JOB_ID)�� ��� �޿��� �޴� ������ ��ȸ�϶�
SELECT  EMP_NAME, JOB_TITLE, SALARY
FROM    EMPLOYEE
JOIN    JOB USING(JOB_ID)
WHERE   SALARY IN ( SELECT  TRUNC(AVG(SALARY), -5)
                    FROM    EMPLOYEE
                    GROUP BY    JOB_ID)
-- �̷� ������ �����, �����ε� ��ձ޿�(250)�� �ƴ�, 260 �޴� ����� ������
-- ���� ������ ���߿� �������� �������� ����� �����                   
                    
--������ ���߿� ���� ����
SELECT  EMP_NAME, JOB_TITLE, SALARY
FROM    EMPLOYEE
JOIN    JOB USING(JOB_ID)
WHERE   (JOB_ID, SALARY) IN ( SELECT  JOB_ID, TRUNC(AVG(SALARY), -5)
                    FROM    EMPLOYEE
                    GROUP BY    JOB_ID)

--FROM ���� �������� �ֱ�
--FROM ���� ���������� ������, ������ ���̺��� �������
SELECT  EMP_NAME, JOB_TITLE, SALARY
FROM    (SELECT JOB_ID, TRUNC(AVG(SALARY), -5) AS JOBAVG
        FROM    EMPLOYEE
        GROUP BY    JOB_ID) V
JOIN    EMPLOYEE E ON(V.JOB_ID = E.JOB_ID AND V.JOBAVG = E.SALARY)
JOIN    JOB J ON(E.JOB_ID = J.JOB_ID)


-- ������� ��������
-- �������� ���� ���� ���
SELECT  EMP_NAME, JOB_TITLE, SALARY
FROM    EMPLOYEE E
JOIN    JOB J ON(E.JOB_ID = J.JOB_ID)
WHERE   SALARY = (  SELECT  TRUNC(AVG(SALARY), -5)
                    FROM    EMPLOYEE
                    WHERE   JOB_ID = E.JOB_ID )


--������ EXISTS, NOT EXISTS

SELECT  EMP_ID,
        EMP_NAME,
        '������' AS ����
FROM    EMPLOYEE E
WHERE   EXISTS (SELECT  NULL    -- �����ϸ� TURE
                FROM    EMPLOYEE
                WHERE   E.EMP_ID = MGR_ID)
UNION
SELECT  EMP_ID,
        EMP_NAME,
        '����' AS ����
FROM    EMPLOYEE E2
WHERE   NOT EXISTS (SELECT  NULL --�������� ������ TRUE
                    FROM    EMPLOYEE
                    WHERE   E2.EMP_ID = MGR_ID) 
ORDER BY 3;