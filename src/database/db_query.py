
def scenario_nbr():
    return "SELECT COUNT(*) AS Qtd_Cenarios FROM scenario"

def total_car_nbr():
    return "SELECT COUNT(DISTINCT(car_state.car_id)) AS Total_de_Carros FROM car_state GROUP BY car_state.car_id"

def total_street_nbr():
    return "SELECT SUM(scenario.nbr_streets) AS Qtd_Ruas FROM scenario"

def total_intersection_nbr():
    return "SELECT SUM(scenario.nbr_intersections) AS Qtd_Interseccoes FROM scenario"

def total_mean_speed():
    return """SELECT AVG(car_state.speed) AS Velocidade_Media FROM car_state"""

def total_max_distance():
    return """SELECT MAX(car_state.distance) AS Distancia_Maxima FROM car_state"""

def total_mean_duration():
    return """SELECT AVG(scenario.duration) Duracao_Media FROM scenario"""

def scenario_with_most_cars():
    return "SELECT COUNT(DISTINCT(car_state.car_id)) AS Cenario_com_mais_carros FROM car_state GROUP BY car_state.scenario_id ORDER BY COUNT(DISTINCT(car_state.car_id)) DESC LIMIT 1"

#############

def nbr_cars_per_scenario(scenario_id):
    return f"""SELECT COUNT(DISTINCT(car_state.car_id)) AS Nro_de_Carros_no_Cenario FROM car_state WHERE car_state.scenario_id = {scenario_id}"""

def nbr_streets_per_scenario(scenario_id):
    return f"""SELECT nbr_streets FROM scenario WHERE scenario.scenario_id = {scenario_id}"""

def nbr_intersection_per_scenario(scenario_id):
    return f"""SELECT nbr_intersections FROM scenario WHERE scenario.scenario_id = {scenario_id}"""

def mean_speed_per_scenario(scenario_id):
    return f"""SELECT AVG(car_state.speed) AS Velocidade_Media FROM car_state WHERE car_state.scenario_id = {scenario_id}"""

def max_distance_per_scenario(scenario_id):
    return f"""SELECT MAX(car_state.distance) AS distancia_maxima FROM car_state WHERE car_state.scenario_id = {scenario_id}"""

def scenario_current_duration(scenario_id):
    return f"""SELECT MAX(tick) AS duracao_atual FROM tick WHERE tick.scenario_id = {scenario_id}"""

def vehicles_per_street(scenario_id):
    return f"""SELECT current_street_id, COUNT(DISTINCT(car_state.car_id)) AS qtd_carros FROM car_state WHERE car_state.scenario_id = {scenario_id} GRUP BY current_street_id"""