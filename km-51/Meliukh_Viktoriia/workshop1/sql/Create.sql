/*==============================================================*/
/* DBMS name:      ORACLE Version 12c                           */
/* Created on:     11.11.2018 20:30:17                          */
/*==============================================================*/


alter table BOOKING
   drop constraint FK_BOOKING_B_TO_C_CLASSROO;

alter table BOOKING
   drop constraint FK_BOOKING_B_TO_L_LESSON;

alter table BOOKING
   drop constraint FK_BOOKING_HAS_USER;

drop index B_TO_C_FK;

drop index B_TO_L_FK;

drop index HAS_FK;

drop table BOOKING cascade constraints;

drop table CLASSROOM cascade constraints;

drop table LESSON cascade constraints;

drop table "USER" cascade constraints;

/*==============================================================*/
/* Table: BOOKING                                               */
/*==============================================================*/
create table BOOKING (
   BOOKING_ID           VARCHAR2(32)          not null,
   USER_ID              VARCHAR2(32)          not null,
   LESSON_ID            VARCHAR2(32)          not null,
   CLASSROOM_ID         VARCHAR2(32)          not null,
   BOOKINGDATE          DATE                  not null,
   constraint PK_BOOKING primary key (BOOKING_ID)
);

/*==============================================================*/
/* Index: HAS_FK                                                */
/*==============================================================*/
create index HAS_FK on BOOKING (
   USER_ID ASC
);

/*==============================================================*/
/* Index: B_TO_L_FK                                             */
/*==============================================================*/
create index B_TO_L_FK on BOOKING (
   LESSON_ID ASC
);

/*==============================================================*/
/* Index: B_TO_C_FK                                             */
/*==============================================================*/
create index B_TO_C_FK on BOOKING (
   CLASSROOM_ID ASC
);

/*==============================================================*/
/* Table: CLASSROOM                                             */
/*==============================================================*/
create table CLASSROOM (
   CLASSROOM_ID         VARCHAR2(32)          not null,
   CLASSROOMNUM         INTEGER               not null,
   HOUSINGNUMBER        INTEGER               not null,
   NUMBEROFSEATS        INTEGER               not null,
   MULTIMEDIA           INTEGER               not null,
   constraint PK_CLASSROOM primary key (CLASSROOM_ID)
);

/*==============================================================*/
/* Table: LESSON                                                */
/*==============================================================*/
create table LESSON (
   LESSON_ID            VARCHAR2(32)                 not null,
   LESSONNUMBER      INTEGER                      not null,
   BTIME                VARCHAR2(5)                  not null,
   ETIME                VARCHAR2(5)                  not null,
   constraint PK_LESSON primary key (LESSON_ID)
);

/*==============================================================*/
/* Table: "USER"                                                */
/*==============================================================*/
create table "USER" (
   USER_ID              VARCHAR2(32)          not null,
   FNAME                VARCHAR2(20)          not null,
   MNAME                VARCHAR2(20)          not null,
   LNAME                VARCHAR2(20)          not null,
   EMAIL                VARCHAR2(20)          not null,
   PASSWORD             VARCHAR2(20)          not null,
   EMAILISCHECKED       INTEGER               not null,
   constraint PK_USER primary key (USER_ID)
);

alter table BOOKING
   add constraint FK_BOOKING_B_TO_C_CLASSROO foreign key (CLASSROOM_ID)
      references CLASSROOM (CLASSROOM_ID);

alter table BOOKING
   add constraint FK_BOOKING_B_TO_L_LESSON foreign key (LESSON_ID)
      references LESSON (LESSON_ID);

alter table BOOKING
   add constraint FK_BOOKING_HAS_USER foreign key (USER_ID)
      references "USER" (USER_ID);


/*------MANUALY ADDED CHECK CONSTRAINTS-----------*/


alter table "USER"
    add constraint check_f_name 
    check(REGEXP_LIKE(FNAME, '[А-Яа-я]{1,20}', 'c'));
  
alter table "USER"
    add constraint check_m_name 
    check(REGEXP_LIKE(MNAME, '[А-Яа-я]{1,20}', 'c')); 
  
alter table "USER"
    add constraint check_l_name 
    check(REGEXP_LIKE(LNAME, '[А-Яа-я]{1,20}', 'c'));

alter table "USER"
    add constraint check_e_mail
    check(REGEXP_LIKE(EMAIL, '^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$', 'i'));

alter table "USER"
    add constraint cehck_pass
    check(REGEXP_LIKE(PASSWORD, '\d{1,20}'));

alter table "USER"
    add constraint check_e_checked
    check(EMAILISCHECKED IN (0, 1));

alter table "CLASSROOM"
    add constraint uq_number_housing
    UNIQUE  (CLASSROOMNUM, HOUSINGNUMBER);

alter table lesson
    add constraint uq_lesson_number
    UNIQUE (lessonnumber);
  