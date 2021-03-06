-- database creation
CREATE database IF NOT EXISTS car_simulator_db;
USE car_simulator_db;


-- tables
-- Table: car_state
CREATE TABLE car_state (
    car_id varchar(36) NOT NULL,
    tick_id int NOT NULL,
    distance int NOT NULL,
    speed int NOT NULL,
    current_street_id varchar(36) NOT NULL,
    scenario_id varchar(36) NOT NULL,
    CONSTRAINT car_state_pk PRIMARY KEY (car_id,tick_id)
);

-- Table: scenario
CREATE TABLE scenario (
    id varchar(36) NOT NULL,
    nbr_streets int NOT NULL,
    nbr_intersections int NOT NULL,
    duration decimal(10,5) NOT NULL,
    CONSTRAINT scenario_pk PRIMARY KEY (id)
);

-- Table: tick
CREATE TABLE tick (
    id int NOT NULL,
    scenario_id varchar(36) NOT NULL,
    seconds_elapsed decimal(10,5) NOT NULL,
    CONSTRAINT tick_pk PRIMARY KEY (id,scenario_id)
);

-- foreign keys
-- Reference: car_state_tick (table: car_state)
ALTER TABLE car_state ADD CONSTRAINT car_state_tick FOREIGN KEY car_state_tick (tick_id,scenario_id)
    REFERENCES tick (id,scenario_id);

-- Reference: tick_scenario (table: tick)
ALTER TABLE tick ADD CONSTRAINT tick_scenario FOREIGN KEY tick_scenario (scenario_id)
    REFERENCES scenario (id);


-- USER CREATION

CREATE USER 'user'@'localhost' IDENTIFIED BY 'password'; 

GRANT ALL PRIVILEGES
    ON `car_simulator_db`.* 
    TO 'user'@'localhost';

FLUSH PRIVILEGES;

-- End of file.

