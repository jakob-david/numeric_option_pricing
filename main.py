from general_classes.Option import Option
from general_classes.Simulation import Simulation


my_sim = Simulation(Option())

Option().plot_random_stock_price_path(100)

print(my_sim.calculate_analytic())

my_sim.plot_monte_carlo(1, 2000, 100)
my_sim.plot_binomial_tree(1, 10)
my_sim.plot_trinomial_tree(1, 10)
my_sim.plot_explicit_fd(1, 40, 1, 20, 'n')
my_sim.plot_implicit_fd(1, 40, 1, 20, 'n')
my_sim.plot_crank_nicolson(1, 40, 1, 20, 'n')


