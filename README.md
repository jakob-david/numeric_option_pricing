# Numeric Option Pricing

## Numerical Methods

### Monte Carlo Simulation
The way of pricing an option with a Monte Carlo simulation is quite different to the other ways of option pricing. In contrast to the other methods discussed in this paper, it is not needed to calculate nodes or build a tree in some kind. The procedure is quite simple and can easily be implemented in Microsoft Excel as shown by Hull (2015). First, one calculates the value of the stock after some time 𝑡. For doing this the following formula is needed (Hull, 2015).

$$S(T)=S(0)e^{\left(r-q-\frac{\sigma^2}{2}\right)T+\sigma\epsilon\sqrt T}$$

The problem with this equation is 𝜖, since this is not an exact number. 𝜖 can be simulated by generating a random number and plugging it into the inverse of the normal derivation. After doing that one can calculate one possible outcome of the equation. However, this is, as just said, just one possible outcome, so it is needed to repeat the process over and over. The higher the number of repetitions, the more exact the price will be. Theoretically, if the number of repetitions comes close to infinity the result for a European option would be the same as if calculated analytically using the Black-Scholes formulas.