# CSE 305 Homework 1

## Aditya Balwani, SBUID : 109353920

### Question 4.17

```SQL

CREATE DOMAIN MAJORS CHAR(10)
  CHECK ( VALUE IN ('CSE', 'BME', 'MAT', 'MAT', 'HUM', 'ART', 'MEC', 'undeclared'));

CREATE TABLE Student (
  ID INTEGER AUTO_INCREMENT,
  Name CHAR(50) NOT NULL,
  Majors CHAR(10) NOT NULL,
  PRIMARY KEY (ID)
);

CREATE TABLE Class(
  Semester CHAR(10),
  CrsCode CHAR (10),
  Room CHAR (30),
  PRIMARY KEY (Semester, CrsCode)
);

CREATE TABLE Takes (
  StudentID INTEGER,
  CrsCode CHAR(10),
  Semester CHAR(10),
  PRIMARY KEY (StudentID, CrsCode, Semester),
  FOREIGN KEY (Semester, CrsCode)
    REFERENCES Class(Semester, CrsCode)
    ON DELETE CASCADE,
  FOREIGN KEY (StudentID)
    REFERENCES Student(ID)
    ON DELETE CASCADE
);
```

### Question 5.10

#### SQL

1.
```SQL
SELECT C.DeptID, C.CrsCode, C.CrsName, C.Descr
FROM Course C, Teaching T
WHERE Course.CrsCode = T.CrsCode AND T.ProfID IN (
  SELECT Id FROM Professor WHERE DeptID IN ('EE','MGT')
)
```
2.
```SQL
SELECT S.Name
FROM Student S, Transcript T1, Transcript T2
WHERE S.Id = T1.StudId AND S.Id = T2.StudId AND  T1.Semester != T2.Semester
  AND T1.Semester = 's1997' AND T2.Semester = 'F1998'
GROUP BY S.Id
```
3.
```SQL
CREATE VIEW TaughtBy(StudId, ProfId, DeptId) AS
  SELECT S.Id, P.Id, P.DeptID
  FROM Student S, Professor P, Teaching T, Transcript TR
  WHERE S.ID = TR.StudID AND P.ID = T.ProfId
  AND T.Semester = TR.Semester AND T.CrsCode = TR.CrsCode
  GROUP BY S.ID, P.ID;

SELECT S.Name
FROM Student S, TaughtBy T1, TaughtBy T2
WHERE S.Id = T1.StudId AND S.Id = T2.StudId
  AND T1.DeptId != T2.DeptId
GROUP BY S.ID;
```
4.
```SQL
SELECT C.CrsCode
FROM Course C
WHERE C.DeptId = 'MGT' AND
  NOT EXISTS (
  (
    SELECT S.ID
    FROM Student S
    WHERE S.ID NOT IN (
      SELECT T.StudId
      FROM Transcript T
      WHERE C.CrsCode = T.CrsCode
    )
  )
);
```
5.
```SQL
SELECT DISTINCT(Cou.DeptID)
FROM Course Cou, Teaching Te
WHERE Te.CrsCode = Cou.CrsCode
  AND NOT EXISTS(
    SELECT CrsCode
    FROM Course Co
    WHERE Co.DeptID = Cou.DeptID AND Co.CrsCode NOT IN (
      SELECT C.CrsCode
      FROM Teaching T, Course C
      WHERE T.CrsCode = C.CrsCode AND C.DeptID = Co.DeptID AND T.ProfId = Te.ProfId)
)
```

<div class="page-break"></div>

#### Relational Algebra

<ol>
  <li> π <sub>C.DeptID, C.CrsCode, C.CrsName, C.Descr</sub>(σ <sub>C.deptID = 'EE' | C.deptID = 'MGT'</sub>(Course &#8904; Teaching))<br/><br/></li>
  <li> π Sn.Name (σ <sub>T1.Semster = 's1997' & T2.Semester = 'f1998'</sub>(Transcript T1 &#8904;<sub>T1.StudId = S.Id</sub> Student S &#8904;<sub>S.id = T2.StudId</sub> Transcript T2))<br/><br/></li>
  <li>TaughtBy => π <sub>S.Id, P.Id, P.DeptId</sub> (Student S &#8904;<sub> S.ID=TR.StudId</sub> Transcript Tr &#8904; Teaching T &#8904;<sub>T.ProfId = P.ID</sub> Professor P)<br/>
  π <sub>S.Name</sub> (σ <sub>T1.DeptId != T2.DeptID</sub> (TaughtBy T1 &#8904; <sub>T1.StudId = S.Id</sub> Student S &#8904; <sub>S.Id = T2.StudId</sub> TaughtBy T2))
  <br/><br/></li>
  <li>π <sub>C.CrcCode, S.StudID</sub> (σ<sub> C.DeptID='MGT'</sub> (Transcript &#8904; Student) / π <sub>StudIDM</sub> (Student))<br/><br/></li>
  <li>π <sub>Cou.DeptID</sub> (Course Cou &#8904; Teaching Te) / π <sub>Co.CrsCode</sub> (σ<sub> Co.DeptID = Cou.DeptID AND C.DeptID = Co.DeptID AND T.ProfId = Te.ProfId</sub> (Teaching T &#8904; Course C)) <br/><br/></li>
</ol>
