SELECT  *
FROM    TB_STUDENT

--1. �л��̸��� �ּ����� ǥ���Ͻÿ�. ��, ��� ����� "�л� �̸�", "�ּ���"�� �ϰ�,
--������ �̸����� �������� ǥ���ϵ��� ����.
SELECT  STUDENT_NAME "�л� �̸�" ,
        STUDENT_ADDRESS �ּ���
FROM    TB_STUDENT
ORDER BY STUDENT_NAME

--2. �������� �л����� �̸��� �ֹι�ȣ�� ���̰� ���� ������ ȭ�鿡 ����Ͻÿ�.
SELECT  STUDENT_NAME,
        STUDENT_SSN
FROM    TB_STUDENT
WHERE   ABSENCE_YN = 'Y'
ORDER BY STUDENT_SSN DESC

--3. �ּ����� �������� ��⵵�� �л��� �� 1900 ��� �й��� ���� �л����� �̸��� �й�, 
--�ּҸ� �̸��� ������������ ȭ�鿡 ����Ͻÿ�. ��, ���������� "�л��̸�","�й�",
--"������ �ּ�" �� ��µǵ��� ����.
SELECT  STUDENT_NAME �л��̸�,
        STUDENT_NO �й�,
        STUDENT_ADDRESS "������ �ּ�"
FROM    TB_STUDENT
WHERE   (STUDENT_ADDRESS LIKE '����%' OR STUDENT_ADDRESS LIKE '��⵵%') AND
        STUDENT_NO NOT LIKE 'A%'
ORDER BY 1 ;

--4. ���� ���а� ���� �� ���� ���̰� ���� ������� �̸��� Ȯ���� �� �ִ� SQL ������
--�ۼ��Ͻÿ�. (���а��� '�а��ڵ�'�� �а� ���̺�(TB_DEPARTMENT)�� ��ȸ�ؼ� ã��
--������ ����) 
--SELECT  PROFESSOR_NAME, 
--        TO_NUMBER(TO_CHAR(SYSDATE, 'YYYY')) -
--        TO_NUMBER('19' || SUBSTR(PROFESSOR_SSN, 1, 2))       
--FROM    TB_PROFESSOR
--WHERE   DEPARTMENT_NO = '005'
--ORDER BY 2 DESC

SELECT  PROFESSOR_NAME,
        PROFESSOR_SSN
FROM TB_PROFESSOR 
WHERE DEPARTMENT_NO='005' 
ORDER BY PROFESSOR_SSN ;

--5. 2004 �� 2 �б⿡ 'C3118100' ������ ������ �л����� ������ ��ȸ�Ϸ��� ����. ������
--���� �л����� ǥ���ϰ�, ������ ������ �й��� ���� �л����� ǥ���ϴ� ������
--�ۼ��غ��ÿ�.
SELECT  STUDENT_NO,
        POINT
FROM    TB_GRADE
WHERE   TERM_NO = '200402' AND CLASS_NO = 'C3118100'
ORDER BY 2 DESC; 

--6. �л� ��ȣ, �л� �̸�, �а� �̸��� �л� �̸����� �������� �����Ͽ� ����ϴ� SQL 
--���� �ۼ��Ͻÿ�.
SELECT  STUDENT_NAME,
        STUDENT_NO,
        D.DEPARTMENT_NAME
FROM    TB_STUDENT S
JOIN    TB_DEPARTMENT D ON D.DEPARTMENT_NO = S.DEPARTMENT_NO
ORDER BY 1 ; 

--7. �� ������б��� ���� �̸��� ������ �а� �̸��� ����ϴ� SQL ������ �ۼ��Ͻÿ�.
SELECT  CLASS_NAME,
        DEPARTMENT_NAME D
FROM    TB_CLASS C
JOIN    TB_DEPARTMENT D ON D.DEPARTMENT_NO = C.DEPARTMENT_NO;

--8. ���� ���� �̸��� ã������ ����. ���� �̸��� ���� �̸��� ����ϴ� SQL ����
--�ۼ��Ͻÿ�.
SELECT  CLASS_NAME,
        PROFESSOR_NAME
FROM    TB_CLASS 
JOIN    TB_CLASS_PROFESSOR USING(CLASS_NO)
JOIN    TB_PROFESSOR USING(PROFESSOR_NO)
ORDER BY 1

--9. 8 ���� ��� �� ���ι���ȸ�� �迭�� ���� ������ ���� �̸��� ã������ ����. �̿�
--�ش��ϴ� ���� �̸��� ���� �̸��� ����ϴ� SQL ���� �ۼ��Ͻÿ�.

SELECT  CLASS_NAME, PROFESSOR_NAME
FROM    TB_CLASS C
JOIN    TB_CLASS_PROFESSOR CP USING(CLASS_NO)
JOIN    TB_PROFESSOR P USING(PROFESSOR_NO)
JOIN    TB_DEPARTMENT D ON(D.DEPARTMENT_NO= P.DEPARTMENT_NO)
WHERE   CATEGORY = '�ι���ȸ'
ORDER BY 1 ASC;


--10. �������а��� �л����� ������ ���Ϸ��� ����. �����а� �л����� "�й�", "�л� �̸�", 
--"��ü ����"�� ����ϴ� SQL ������ �ۼ��Ͻÿ�. (��, ������ �Ҽ��� 1 �ڸ�������
--�ݿø��Ͽ� ǥ������.) -- NULL�� ���־���
SELECT  STUDENT_NO, 
        STUDENT_NAME,   
        ROUND(AVG(POINT),1)
FROM    TB_STUDENT
JOIN    TB_GRADE USING(STUDENT_NO)
WHERE   DEPARTMENT_NO= 059 --�����а�
GROUP BY ROLLUP(STUDENT_NO,STUDENT_NAME);

11. �й��� A313047 �� �л��� �б��� ������ ���� �ʴ�. ���� �������� ������ �����ϱ�
���� �а� �̸�, �л� �̸��� ���� ���� �̸��� �ʿ��ϴ�. �̶� ����� SQL ����
�ۼ��Ͻÿ�. ��, �������� ?�а��̸�?, ?�л��̸�?, ?���������̸�?����
��µǵ��� ����. ��ǰ

SELECT  DEPARTMENT_NAME �а��̸�,
        STUDENT_NAME    �л��̸�,
        PROFESSOR_NAME  ���������̸�
FROM    TB_DEPARTMENT D
JOIN    TB_STUDENT S ON  (S.DEPARTMENT_NO = D.DEPARTMENT_NO)
JOIN    TB_PROFESSOR P ON (P.DEPARTMENT_NO = S.DEPARTMENT_NO)
WHERE   COACH_PROFESSOR_NO = 'P0314';


--12. 2007 �⵵�� '�΁A�����' ������ ������ �л��� ã�� �л��̸��� �����б⸧ ǥ���ϴ�
--SQL ������ �ۼ��Ͻÿ�.
SELECT  STUDENT_NAME,
        TERM_NO
FROM    TB_STUDENT S
JOIN    TB_GRADE USING(STUDENT_NO)
JOIN    TB_CLASS USING(CLASS_NO) 
WHERE   CLASS_NAME = '�ΰ������' AND TERM_NO LIKE '2007%' ;

13. ��ü�� �迭 ���� �� ���� ��米���� �� �� �������� ���� ������ ã�� �� ����
�̸��� �а� �̸��� ����ϴ� SQL ������ �ۼ��Ͻÿ� ��ǰ
SELECT  CLASS_NAME,
        DEPARTMENT_NAME
FROM    TB_DEPARTMENT D
JOIN    TB_CLASS C ON (C.DEPARTMENT_NO = D.DEPARTMENT_NO)
JOIN    TB_CLASS_PROFESSOR USING(CLASS_NO)
GROUP BY CATEGORY = '��ü��'
HAVING 


14. �� ������б� ���ݾƾ��а� �л����� ���������� �Խ��ϰ��� ����. �л��̸���
�������� �̸��� ã�� ���� ���� ������ ���� �л��� ��� "�������� ������?����
ǥ���ϵ��� �ϴ� SQL ���� �ۼ��Ͻÿ�. ��, �������� ?�л��̸�?, ?��������?��
ǥ���ϸ� ���й� �л��� ���� ǥ�õǵ��� ����.

15. ���л��� �ƴ� �л� �� ������ 4.0 �̻��� �л��� ã�� �� �л��� �й�, �̸�, �а�
�̸�, ������ ����ϴ� SQL ���� �ۼ��Ͻÿ�.

16. �Q�������а� ����������� ���� �� ������ �ľ��� �� �ִ� SQL ���� �ۼ��Ͻÿ�.

17. �� ������б��� �ٴϰ� �ִ� �ְ��� �л��� ���� �� �л����� �̸��� �ּҸ� ����ϴ�
SQL ���� �ۼ��Ͻÿ�.

18. ������а����� �� ������ ���� ���� �л��� �̸��� �й��� ǥ���ϴ� SQL ����
�ۼ��Ͻÿ�.

19. �� ������б��� "�Q�������а�"�� ���� ���� �迭 �а����� �а� �� �������� ������
�ľ��ϱ� ���� ������ SQL ���� ã�Ƴ��ÿ�. ��, �������� "�迭 �а���", 
"��������"���� ǥ�õǵ��� �ϰ�, ������ �Ҽ��� �� �ڸ������� �ݿø��Ͽ� ǥ�õǵ���
����.
