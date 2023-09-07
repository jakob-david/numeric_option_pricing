from general_classes.Stock import Stock
from other_methods.Analytic import Analytic
from other_methods.MonteCarlo import MonteCarlo
from other_methods.BinomialTree import BinomialTree
from other_methods.TrinomialTree import TrinomialTree
from finite_difference_methods.ImplicitFD import ImplicitFD
from finite_difference_methods.ExplicitFD import ExplicitFD
from finite_difference_methods.CrankNicolson import CrankNicolson

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

