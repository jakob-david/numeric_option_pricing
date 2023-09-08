from general_classes.Stock import Stock
from general_classes.simulation import Simulation


my_sim = Simulation(Stock())

print(my_sim.calculate_analytic())


