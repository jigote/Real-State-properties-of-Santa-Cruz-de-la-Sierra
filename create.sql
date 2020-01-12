CREATE TABLE departamentos (
    id SERIAL PRIMARY KEY,
    edificio VARCHAR NOT NULL,
    dirección VARCHAR NOT NULL,
    duración INTEGER NOT NULL
);

CREATE TABLE visitantes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR NOT NULL,
    departamento_id INTEGER REFERENCES departamentos
);


CREATE TABLE form_info (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    lastName VARCHAR NOT NULL,
    cellphone INTEGER NULL,
    email VARCHAR NOT NULL
);

SELECT edificio, duración, nombre FROM departamentos 
    JOIN visitantes ON visitantes.departamento_id = departamentos.id
    WHERE nombre = 'Alice';


SELECT edificio, duración, nombre FROM departamentos 
    LEFT JOIN visitantes ON visitantes.departamento_id = departamentos.id
    WHERE nombre = 'Alice';



CREATE INDEX idx_direction
ON departamentos (dirección);

SELECT * FROM departamentos USE (idx_direction);


ALTER TABLE departamentos 
DROP INDEX idx_direction;

SELECT departamento_id FROM visitantes GROUP BY departamento_id HAVING COUNT(*) > 1;

/* nested queries*/
SELECT * FROM departamentos WHERE id IN (SELECT departamento_id FROM visitantes GROUP BY departamento_id HAVING COUNT(*) > 1);
