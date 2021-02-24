[Additional SELECT - �Լ�]

SELECT *
FROM   TB_STUDENT

--1. ������а�(�а��ڵ� 002) �л����� �й��� �̸�, ���� �⵵�� ���� �⵵�� ����
--������ ǥ���ϴ� SQL ������ �ۼ��Ͻÿ�.( ��, ����� "�й�", "�̸�", "���г⵵" ��
--ǥ�õǵ��� ����.)

SELECT  STUDENT_NO AS �й�, 
        STUDENT_NAME AS �̸�,
        TO_CHAR(ENTRANCE_DATE,'RRRR-MM-DD') AS ���г⵵
FROM    TB_STUDENT
WHERE   DEPARTMENT_NO = '002'
ORDER BY ENTRANCE_DATE ;

--2. �� ������б��� ���� �� �̸��� �� ���ڰ� �ƴ� ������ �� �� �ִٰ� ����. �� ������
--�̸��� �ֹι�ȣ�� ȭ�鿡 ����ϴ� SQL ������ �ۼ��� ����. (* �̶� �ùٸ��� �ۼ��� SQL 
--������ ��� ���� ����� �ٸ��� ���� �� �ִ�. ������ �������� �����غ� ��)

--��1)
SELECT  PROFESSOR_NAME,
        PROFESSOR_SSN
FROM    TB_PROFESSOR
WHERE   LENGTH(PROFESSOR_NAME) != 3 ; 
--��2)
SELECT PROFESSOR_NAME , 
       PROFESSOR_SSN
FROM   TB_PROFESSOR
WHERE  PROFESSOR_NAME NOT LIKE '___';



--3. �� ������б��� ���� �������� �̸��� ���̸� ����ϴ� SQL ������ �ۼ��Ͻÿ�. ��
--�̶� ���̰� ���� ������� ���� ��� ������ ȭ�鿡 ��µǵ��� ����ÿ�. (��, ���� ��
--2000 �� ���� ����ڴ� ������ ��� ����� "�����̸�", "����"�� ����. ���̴� ����������
--�������.) ��ǰ

SELECT PROFESSOR_NAME AS �����̸�,
       TO_NUMBER(TO_CHAR(SYSDATE, 'YYYY')) -  --���� ��¥ �⵵�� 2021��
       TO_NUMBER('19' || SUBSTR(PROFESSOR_SSN, 1, 2)) AS ���� -- 19XX�� ���� �������  �� ���̷� ����ϱ� ������ +1�� ���ʿ� ����
FROM   TB_PROFESSOR
WHERE  SUBSTR(PROFESSOR_SSN, 8, 1) = '1' -- ���ڱ����鸸 �̱�
ORDER BY 2, 1;

--4. �������� �̸� �� ���� ������ �̸��� ����ϴ� SQL ������ �ۼ��Ͻÿ�. ��� �����
--?�̸�? �� �������� ����. (���� 2 ���� ���� ������ ���ٰ� �����Ͻÿ�)

SELECT  SUBSTR(PROFESSOR_NAME,2) AS �̸�
FROM    TB_PROFESSOR

--5. �� ������б��� ����� �����ڸ� ���Ϸ��� ����. ��� ã�Ƴ� ���ΰ�? �̶�, 
--19 �쿡 �����ϸ� ����� ���� ���� ������ �A������. ?????

SELECT  STUDENT_NO, STUDENT_NAME 
FROM    TB_STUDENT
WHERE   TO_NUMBER(TO_CHAR(ENTRANCE_DATE, 'YYYY')) - 
        TO_NUMBER(TO_CHAR(TO_DATE(SUBSTR(STUDENT_SSN, 1, 2), 'RR'), 'YYYY')) > 19 
ORDER BY 1;


--6. 2020 �� ũ���������� ���� �����ΰ�?
SELECT TO_CHAR(TO_DATE('20201225','YYYY/MM/DD'),'DAY') 
FROM DUAL ;

--7. TO_DATE('99/10/11','YY/MM/DD'), TO_DATE('49/10/11','YY/MM/DD') ��
--���� ��� ��� ������ �ǹ�����? �� TO_DATE('99/10/11','RR/MM/DD'), 
--TO_DATE('49/10/11','RR/MM/DD') �� ���� �� �� �� �� �� ���� �ǹ�����?
SELECT TO_CHAR(TO_DATE('99/10/11','YY/MM/DD'), 'YYYY')
FROM DUAL;
SELECT TO_CHAR(TO_DATE('49/10/11','YY/MM/DD'), 'YYYY')
FROM DUAL;

SELECT TO_CHAR(TO_DATE('99/10/11','RR/MM/DD'), 'YYYY')
FROM DUAL;
SELECT TO_CHAR(TO_DATE('49/10/11','RR/MM/DD'), 'YYYY')
FROM DUAL;

--8. �� ������б��� 2000 �⵵ ���� �����ڵ��� �й��� A �� �����ϰ� �Ǿ��ִ�. 
--2000 �⵵ ���� �й��� ���� �л����� �й��� �̸��� �����ִ� SQL ������ �ۼ��Ͻÿ�.
SELECT  STUDENT_NAME,
        STUDENT_NO
FROM    TB_STUDENT
WHERE   STUDENT_NO NOT LIKE'A%'

--9. �й��� A517178 �� �ѾƸ� �л��� ���� �� ������ ���ϴ� SQL ���� �ۼ��Ͻÿ�. ��,
--�̶� ��� ȭ���� ����� "����" �̶�� ������ �ϰ�, ������ �ݿø��Ͽ� �Ҽ��� ���� ��
--�ڸ������� ǥ������.
SELECT  AVG(POINT) AS ����
FROM    TB_GRADE
WHERE   STUDENT_NO = 'A517178'

--10. �а��� �л����� ���Ͽ� "�а���ȣ", "�л���(��)" �� ���·� ����� ����� �������
--��µǵ��� �Ͻÿ�.
SELECT  DEPARTMENT_NO �а���ȣ,
        COUNT(*) "�л���(��)"
FROM    TB_STUDENT
GROUP BY DEPARTMENT_NO
ORDER BY 1;

--11. ���� ������ �������� ���� �л��� ���� �� �� ���� �Ǵ� �˾Ƴ��� SQL ����
--�ۼ��Ͻÿ�.
SELECT  COUNT(*)
FROM    TB_STUDENT
WHERE   COACH_PROFESSOR_NO IS NULL  ; 

--12. �й��� A112113 �� ���� �л��� �⵵ �� ������ ���ϴ� SQL ���� �ۼ��Ͻÿ�. ��, 
--�̶� ��� ȭ���� ����� "�⵵", "�⵵ �� ����" �̶�� ������ �ϰ�, ������ �ݿø��Ͽ�
--�Ҽ��� ���� �� �ڸ������� ǥ������.
SELECT  SUBSTR(TERM_NO,1,4) �⵵ ,
        ROUND(AVG(POINT),1) "�⵵ �� ����"
FROM    TB_GRADE
WHERE   STUDENT_NO = 'A112113'
GROUP BY SUBSTR(TERM_NO,1,4) ; 



--13. �а� �� ���л� ���� �ľ��ϰ��� ����. �а� ��ȣ�� ���л� ���� ǥ���ϴ� SQL ������
--�ۼ��Ͻÿ�.

--���� ���� ���� �ȳ��� 
SELECT  DEPARTMENT_NO �а���ȣ,
        COUNT(*) ���л���
FROM    TB_STUDENT
WHERE   ABSENCE_YN = 'Y'
GROUP BY DEPARTMENT_NO
ORDER BY 1 ;

--���� ���� ����� ���
SELECT DEPARTMENT_NO AS �а��ڵ��,
       SUM(CASE WHEN ABSENCE_YN ='Y' THEN 1 
			     ELSE 0 END) AS "���л� ��"
FROM   TB_STUDENT
GROUP BY DEPARTMENT_NO
ORDER BY 1


--14. �� ���б��� �ٴϴ� ��������(��٣���) �л����� �̸��� ã���� ����. � SQL 
--������ ����ϸ� �����ϰڴ°�? 
SELECT  STUDENT_NAME,
        COUNT(*)
FROM    TB_STUDENT
GROUP BY STUDENT_NAME
HAVING  COUNT(*) >1 -- GROUP BY�� ������ �������ٶ�

15. �й��� A112113 �� ���� �л��� �⵵, �б� �� ������ �⵵ �� ���� ���� , ��
������ ���ϴ� SQL ���� �ۼ��Ͻÿ�. (��, ������ �Ҽ��� 1 �ڸ������� �ݿø��Ͽ�
ǥ������.)

SELECT  SUBSTR(TERM_NO,1,4) �⵵,
        SUBSTR(TERM_NO,5,2) �б�,
        ROUND(AVG(POINT),1) "�б� �� ����"
FROM    TB_GRADE
WHERE   STUDENT_NO = 'A112113'
GROUP BY ROLLUP(SUBSTR(TERM_NO,1,4)), ROLLUP(SUBSTR(TERM_NO,5,2))
ORDER BY 1,2; 

--https://jhnyang.tistory.com/354 �Ѿ� �Լ� ���� (���ؾȵ�..)