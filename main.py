from general_classes.Option import Option
from general_classes.Simulation import Simulation


my_sim = Simulation(Option())

Option().plot_random_stock_price_path(100)

# print(my_sim.calculate_analytic())

# my_sim.plot_trinomial_tree(1, 10)
# my_sim.plot_crank_nicolson(1, 20, 1, 50, 'n')


