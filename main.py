from classes.Stock import Stock
from classes.Analytic import Analytic
from classes.MonteCarlo import MonteCarlo
from classes.BinomialTree import BinomialTree
from classes.TrinomialTree import TrinomialTree
from classes.ImplicitFD import ImplicitFD
from classes.ExplicitFD import ExplicitFD
from classes.CrankNicolson import CrankNicolson

stock = Stock()
stock.setKind('call')

Ana = Analytic(stock)
MC = MonteCarlo(stock)
B = BinomialTree(stock)
T = TrinomialTree(stock)
IDF = ImplicitFD(stock)
EDF = ExplicitFD(stock)
CN = CrankNicolson(stock)

print(Ana.calculate())
print(MC.calculate(1000))
print(B.calculate(10))
print(T.calculate(10))
print(IDF.calculate(100, 100, 'm'))
print(EDF.calculate(100, 100, 'm'))
print(CN.calculate(100, 100, 'm'))

