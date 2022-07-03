from unicodedata import name
from pygame import Cursor
import mysql.connector

# DB Connection
DB_HOST = 'localhost'
DB_DATABASE = 'car_simulator_db'
DB_USER = 'user'
DB_PASSWORD = 'password'

def create_connection(host, database, user, passwd):
    try:
        return mysql.connector.connect(
            host = host,
            database = database,
            user = user,
            passwd = passwd
        )
    except mysql.connector.Error as error:
        print("Error: {}".format(error))
        return None

def connect():
    return create_connection(DB_HOST, DB_DATABASE, DB_USER, DB_PASSWORD)

def close_connection(conn):
    conn.close()


def insert_scenario(conn, simulation_data:dict):
    cursor = conn.cursor()

    insert = f""" INSERT INTO scenario (
                    id,
                    nbr_streets,
                    nbr_intersections, 
                    duration
                )
                VALUES ({simulation_data['id']},
                        {simulation_data['nbr_streets']},
                        {simulation_data['nbr_intersections']},
                        {simulation_data['duration']}
                );
    """

    cursor.execute(insert)
    conn.commit()

def insert_car_state(conn, car_state_data:dict):
    cursor = conn.cursor()

    insert = f""" INSERT INTO car_state (
                    car_id,
                    tick_id,
                    scenario_id,
                    distance,
                    current_street_id,
                    speed
                )
                VALUES ({car_state_data['id']},
                        {car_state_data['tick_counter']},
                        {car_state_data['simulation_id']},
                        {car_state_data['distance']},
                        {car_state_data['street_id']},
                        {car_state_data['speed']}
                );
    """

    cursor.execute(insert)
    conn.commit()

def insert_tick(conn, tick_data:dict):
    cursor = conn.cursor()

    insert = f""" INSERT INTO tick (
                    id,
                    scenario_id,
                    seconds_elapsed
                )
                VALUES ({tick_data['tick_counter']},
                        {tick_data['simulation_id']},
                        {tick_data['time']}
                );
    """

    cursor.execute(insert)
    conn.commit()

def erase_database(conn):
    cursor = conn.cursor()

    cursor.execute("DELETE FROM car_state")
    cursor.execute("DELETE FROM tick")
    cursor.execute("DELETE FROM scenario")
    conn.commit()


# if __name__ == "__main__":
#     conn = connect()
#     # insert_scenario(conn, {
#     #     "id": 1,
#     #     "nbr_streets": 2,
#     #     "nbr_intersections": 1,
#     #     "duration": 10
#     # })
#     # insert_tick(conn, {
#     #     "tick_counter": 1,
#     #     "simulation_id": 1,
#     #     "time": 0
#     # })
#     # insert_car_state(conn, {
#     #     "id": 1,
#     #     "tick_counter": 1,
#     #     "simulation_id": 1,
#     #     "distance": 0,
#     #     "street_id": 1,
#     #     "speed": 0
#     # })
#     # erase_database(conn)
#     conn.close()
#     print("Done")