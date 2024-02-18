-- CREATE second_table IF IT DOES NOT EXIST

CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);

-- INSERT MULTIPLE ROWS INTO second_table

INSERT INTO second_tale (id, name, score) VALUES (1, 'John', 10), (2, 'Alex', 3), (3, 'Bob', 14), (4, 'George', 8);
