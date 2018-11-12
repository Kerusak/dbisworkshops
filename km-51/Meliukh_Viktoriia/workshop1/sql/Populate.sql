/* INSERTS INTO CLASSROOM*/

INSERT INTO classroom
    values(sys_guid(),95,15,20,0);
    
INSERT INTO classroom
    values(sys_guid(),96,15,25,0);
    
INSERT INTO classroom
    values(sys_guid(),97,15,60,1);
    
INSERT INTO classroom
    values(sys_guid(),93,15,20,1);

INSERT INTO classroom
    values(sys_guid(),100,15,35,1);
    
INSERT INTO classroom
    values(sys_guid(),106,15,45,0);
    
INSERT INTO classroom
    values(sys_guid(),105,15,75,1);
    
INSERT INTO classroom
    values(sys_guid(),103,15,20,0);
    
/*LESSON*/
INSERT INTO lesson
    values(sys_guid(), 1, '9-30', '10-05');

INSERT INTO lesson
    values(sys_guid(), 2, '10-25', '10-05');
    
INSERT INTO lesson
    values(sys_guid(), 3, '10-25', '12-00');
    
INSERT INTO lesson
    values(sys_guid(), 4, '12.20', '13.55');
    
INSERT INTO lesson
    values(sys_guid(), 5, '12.20', '13.55');
    
INSERT INTO lesson
    values(sys_guid(), 6, '14.15', '15.50');
    
INSERT INTO lesson
    values(sys_guid(), 7, '14.15', '15.50');
    
INSERT INTO lesson
    values(sys_guid(), 8, '14.15', '15.50');

/*USERS*/

INSERT INTO "USER"
    values(sys_guid(),'Иван', 'Иванович', 'Иванов', 'ivan@mail.com', ora_hash(1111), 1);
    
INSERT INTO "USER"
    values(sys_guid(),'Васильев', 'Виктор', 'Григорьевич', 'nik@mail.com', ora_hash(1234), 1);
    
INSERT INTO "USER"
    values(sys_guid(),'Иванченко','Ваня','Петрович','iv@mail.com', ora_hash(45679), 1);
    
INSERT INTO "USER"
    values(sys_guid(),'Богомол','Универ','Медецинский','petro@mail.com', ora_hash(47532), 1);
    
INSERT INTO "USER"
    values(sys_guid(),'Самбуров','Алексей','Гантченко','oma@mail.com', ora_hash(56832), 1);


/*BOOKINGS*/

INSERT INTO booking
    values(
        sys_guid(),
        (SELECT USER_ID FROM "USER" WHERE email = 'ivan@mail.com'),
        (SELECT LESSON_ID FROM lesson WHERE lesson.lessonnumber = 1 ),
        (SELECT CLASSROOM_ID FROM classroom WHERE  classroom.classroomnum = 95 AND classroom.housingnumber = 15),
        CURRENT_DATE -20);
    
INSERT INTO booking
    values(
        sys_guid(),
        (SELECT USER_ID FROM "USER" WHERE email = 'nik@mail.com'),
        (SELECT LESSON_ID FROM lesson WHERE lesson.lessonnumber = 2 ),
        (SELECT CLASSROOM_ID FROM classroom WHERE  classroom.classroomnum = 96 AND classroom.housingnumber = 15),
        CURRENT_DATE -19);

INSERT INTO booking
    values(
        sys_guid(),
        (SELECT USER_ID FROM "USER" WHERE email = 'iv@mail.com'),
        (SELECT LESSON_ID FROM lesson WHERE lesson.lessonnumber = 1 ),
        (SELECT CLASSROOM_ID FROM classroom WHERE  classroom.classroomnum = 100 AND classroom.housingnumber = 15),
        CURRENT_DATE -18);
        
INSERT INTO booking
    values(
        sys_guid(),
        (SELECT USER_ID FROM "USER" WHERE email = 'petro@mail.com'),
        (SELECT LESSON_ID FROM lesson WHERE lesson.lessonnumber = 1 ),
        (SELECT CLASSROOM_ID FROM classroom WHERE  classroom.classroomnum = 93 AND classroom.housingnumber = 15),
        CURRENT_DATE -17);
    
INSERT INTO booking
    values(
        sys_guid(),
        (SELECT USER_ID FROM "USER" WHERE email = 'oma@mail.com'),
        (SELECT LESSON_ID FROM lesson WHERE lesson.lessonnumber = 1 ),
        (SELECT CLASSROOM_ID FROM classroom WHERE  classroom.classroomnum = 106 AND classroom.housingnumber = 15),
        CURRENT_DATE -16);
        
INSERT INTO booking
    values(
        sys_guid(),
        (SELECT USER_ID FROM "USER" WHERE email = 'ivan@mail.com'),
        (SELECT LESSON_ID FROM lesson WHERE lesson.lessonnumber = 1 ),
        (SELECT CLASSROOM_ID FROM classroom WHERE  classroom.classroomnum = 103 AND classroom.housingnumber = 15),
        CURRENT_DATE + 10);
    
    


SELECT * FROM booking;
SELECT * FROM classroom;
SELECT * FROM "USER";
SELECT * FROM lesson;