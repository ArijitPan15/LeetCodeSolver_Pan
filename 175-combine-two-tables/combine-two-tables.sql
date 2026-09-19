SELECT
    p.firstname,
    p.lastname,
    a.city,
    a.state
FROM person AS p
LEFT JOIN address AS a
    ON p.personid = a.personid;
