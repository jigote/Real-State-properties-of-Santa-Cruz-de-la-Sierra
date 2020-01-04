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
