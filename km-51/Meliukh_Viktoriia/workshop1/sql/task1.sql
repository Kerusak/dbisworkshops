ALTER TABLE "USER"
    add constraint unique_user
    UNIQUE (email);
    
SELECT *
FROM "USER"

INSERT INTO "USER"
    values(sys_guid(),'Иванович', 'Коля', 'Николаевик', 'ivan@mail.com', ora_hash(84658203), 1);