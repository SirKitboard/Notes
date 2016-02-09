# CSE 305 Homework 1

## Aditya Balwani, SBUID : 109353920

### Question 3.7

Lets say we have a table PERSON with attributes FirstName and LastName. Now lets say we have two tupples for Person {Adi,null} and {null,Balwani}. Now Lets say the null in the first tupple becomes Balwani and the null in the second tupple becomes Adi. So now both the tupples are identical and they will be come one

This is not possible when one of the attributes is defined as non-null because in that case no two tupples will have have an identical attribute. For example, in the earlier example lets say FirstName is non-null. So in that case, the second tupple cannot have first name Aditya, and it wont become identical.

### Question 3.8

#### Students Table

    CREATE TABLE STUDENT (
        Id  INTEGER,
        Name CHAR(50) NOT NULL,
        Address CHAR(100),
        Status CHAR(10) default 'freshman',
        PRIMARY KEY (Id)
    )

#### Professors Table

    CREATE TABLE PROFESSOR (
        Id INTEGER,
        Name CHAR (50),
        DeptId Departments,
        PRIMARY KEY (Id)
    )

#### Courses

    CREATE TABLE COURSE (
        CrsCode CHAR(9),
        DeptId Departments,
        CrsName CHAR(30),
        Descr CHAR(200),
        PRIMARY KEY (CrsCode),
        UNIQUE (DeptId,CrsName)
    )

    CREATE DOMAIN Departments CHAR(3)
        CHECK ( VALUE IN ('CSE','MAT','EGL','MUS','PHY','CHE'))

#### Transcript

    CREATE TABLE TRANSCRIPT (
        StudId INTEGER,
        CrsCode CHAR(9),
        Semester Semesters,
        Grade Grades,
        PRIMARY KEY (StudId, CrsCode, Semester),
        FOREIGN KEY (StudId) REFERENCES STUDENT(Id)
            ON DELETE NO ACTION
            ON UPDATE CASCADE,
        FOREIGN KEY (CrsCode) REFERENCES COURSE(CrsCode)
            ON DELETE NO ACTION
            ON UPDATE CASCADE,
        FOREIGN KEY (CrsCode, Semester) REFERENCES TEACHING (CrsCode,Semester)
            ON DELETE NO ACTION
            ON UPDATE CASCADE
    )

    CREATE DOMAIN Semesters CHAR(6)
        CHECK ( VALUE IN ('fall','spring','winter','summer'))

    CREATE DOMAIN Grades CHAR(1)
        CHECK ( VALUE IN ('A','B','C','D','F','I'))

#### Teaching

    CREATE TABLE Teaching (
        ProfId INTEGER
        CrsCode CHAR(9)
        Semester Semesters
        PRIMARY KEY (CrsCode,Semester)
        FOREIGN KEY (ProfId) REFERENCES PROFESSOR(Id)
            ON DELETE NO ACTION
            ON UPDATE CASCADE,
        FOREIGN KEY (CrsCode) REFERENCES COURSE(CrsCode)
            ON DELETE SET NULL
            ON UPDATE CASCADE
    )
