from classes.Stock import Stock
from classes.Analytic import Analytic
from classes.MonteCarlo import MonteCarlo
from classes.BinomialTree import BinomialTree
from classes.TrinomialTree import TrinomialTree

stock = Stock()
stock.setKind('call')

Ana = Analytic(stock)
MC = MonteCarlo(stock)
B = BinomialTree(stock)
T = TrinomialTree(stock)

print(Ana.calculate())
print(MC.calculate(1000))
print(B.calculate(10))
print(T.calculate(10))
