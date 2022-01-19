CREATE TABLE dog_room
(
    room_id         INT NOT NULL PRIMARY KEY,
    dog_id          INT NOT NULL,
    hotel_id        INT NOT NULL,
    register_date   DATE,
    unregister_date DATE
);

CREATE TABLE cat_room
(
    room_id         INT NOT NULL PRIMARY KEY,
    cat_id          INT NOT NULL,
    hotel_id        INT NOT NULL,
    register_date   DATE,
    unregister_date DATE
);


CREATE TABLE dog
(
    dog_id   INT NOT NULL PRIMARY KEY,
    owner_id INT NOT NULL,
    dog_name VARCHAR(15),
    dog_age  INT
        CHECK ( dog_age between 1 and 25 )
);

CREATE TABLE cat
(
    cat_id   INT NOT NULL PRIMARY KEY,
    owner_id INT NOT NULL,
    cat_name VARCHAR(15),
    cat_age  INT
        CHECK ( cat_age between 1 and 25 )
);

CREATE TABLE hotel
(
    hotel_id    INT NOT NULL PRIMARY KEY,
    hotel_name  VARCHAR(25),
    hotel_stars INT NOT NULL
        CHECK ( hotel_stars between 1 and 5)

);


CREATE TABLE pet_owner
(
    owner_id   INT PRIMARY KEY NOT NULL,
    owner_name VARCHAR(15),
    owner_age  INT
        CHECK ( owner_age between 1 and 110)
);


INSERT INTO pet_owner(owner_id, owner_name, owner_age)
VALUES (1, 'Peter', 25),
       (2, 'George', 32),
       (3, 'Amy', 67);

INSERT INTO dog(dog_id, owner_id, dog_name, dog_age)
VALUES (1, 1, 'Flyffy', 2),
       (2, 3, 'Bully', 3),
       (3, 1, 'Rousey', 5);

INSERT INTO cat(cat_id, owner_id, cat_name, cat_age)
VALUES (1, 2, 'Tommy', 1),
       (2, 3, 'Jessy', 7),
       (3, 2, 'Bubbles', 3);

INSERT INTO hotel(hotel_id, hotel_name, hotel_stars)
VALUES (1, 'GRAND Pets Hotel', 5),
       (2, 'Pets Heaven', 2);



INSERT INTO dog_room(room_id, dog_id, hotel_id, register_date, unregister_date)
VALUES (1, 1, 1, '2020-06-08', '2020-06-10'),
       (2, 2, 2, '2020-06-10', '2020-06-15'),
       (3, 3, 3, '2020-06-20', '2020-06-23');


INSERT INTO cat_room(room_id, cat_id, hotel_id, register_date, unregister_date)
VALUES (1, 1, 1, '2020-06-08', '2020-06-10'),
       (2, 2, 2, '2020-06-10', '2020-06-15'),
       (3, 3, 3, '2020-06-20', '2020-06-23');


SELECT *
FROM dog_room;


SELECT cat_id
FROM cat_room
WHERE hotel_id = 2;

SELECT *
FROM pet_owner
ORDER BY owner_age DESC;

SELECT count(*)
FROM cat
WHERE cat_age >= 3;


DELETE FROM  cat c
WHERE c.cat_age <= 2;

DELETE FROM dog d
WHERE d.dog_age <=2;
