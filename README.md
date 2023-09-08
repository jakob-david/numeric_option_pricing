# Numeric Option Pricing

## Theory 

### Wiener Process 
A process where the value of a variable changes over time in an uncertain way is called a stochastic process. Furthermore, a Markov process is a special kind of stochastic process. At this particular process only the current value of the variable is relevant for the prediction of the future value. A stock price is thought to follow a Markov process (Hull, 2015).

According to Hull (Hull, 2015: p. 304) a process is a Wiener process if two properties hold true: 

- Property 1: The change $∆z$ during a small period of time $∆t$ is $\Delta z = \epsilon \sqrt{\Delta t}$, where $\epsilon$ has a standard normal distribution $\phi(0,1)$.

- Property 2: 	The values of $∆z$ for any two different short intervals of time are independent. 

A generalized Wiener Process has the following form (Hull, 2015)

$$dx=a\ dt+b\ dz$$

In this case $a$ and $b$ are constant. The term $a\ ∆t$ is known to be the drift rate and $b\ \epsilon∆t$ as the variance rate. One can apply this process to a stock to assume the path of a stock price (Hull, 2015): 

$$dS=\mu Sdt+\sigma dz$$

Here $∆S$ is the change in the stock price $u$ the expected return and $\sigma$ the volatility of the stock. Using this formula and a form of Monte Carlo simulation one can generate a random outcome of one process for a stock price (Hull, 2015) as is shown in Figure 1. 

<p align="center">
    <img width="500" src="./zz_pictures_for_readme/picture_1.png" alt="Figure 3"><br>
    <em>
    Figure 1: A generated random example of the change of a stock price.
    </em>
</p>

### Itô’s Lemma 
Based on the Wiener process another more complex process can be defined. This one is called an Itô’s process and is defined as follows (Hull, 2015)

$$dx=a\left(x,\ t\right)dt+b\left(x,t\right)\ dz$$

This time $a$ and $b$ are not constant but functions from $x$ and t. It can also be written in its discrete form 

$$∆x=a(x,t) ∆t+b(x,t) ϵ∆t$$

This equation of course assumes that the drift and the variance rate keep constant when moving form $t$ to $t+∆t$ (Hull, 2015).

Supposing one has a process like above, the variable $x$ has a drift rate of $a(x,t)$ and a variance of rate described by $b(x,t)$. Itô (1951) found that any function $G(x,t)$ follows the process

$$dG=\ \left(\frac{\partial G}{\partial x}a+\frac{\partial G}{\partial t}+\frac{1}{2}\frac{\partial^2G}{\partial x^2}b^2\right)dt+\frac{\partial G}{\partial x}b\ dz$$

### Black-Scholes-Merton Model
As shown before a Wiener process can be used to simulate the path of a stock price. This is shown in Figure 1. Furthermore, a stock can as well follow an Itô’s process. However, to do so the differential equation needs to be adapted. By combining the Wiener process with it one can obtain the Black-Scholes-Merton differential equation shown below. (Hull, 2015)

$$df=\ \left(\frac{\partial f}{\partial S}\mu\ S+\frac{\partial f}{\partial t}+\frac{1}{2}\frac{\partial^2f}{\partial x^2}\sigma^2S^2\right)dt+\frac{\partial f}{\partial x}\sigma\ S\ dz$$

where $\mu$ is the expected return, $\sigma$ the volatility of the stock and $S$ the current stock price. The equation can also be written discretely. Also, the same assumption must be made when moving form $t$ to $t+∆t$.

## Numerical Methods

### Monte Carlo Simulation
The way of pricing an option with a Monte Carlo simulation is quite different to the other ways of option pricing. In contrast to the other methods discussed in this paper, it is not needed to calculate nodes or build a tree in some kind. The procedure is quite simple and can easily be implemented in Microsoft Excel as shown by Hull (2015). First, one calculates the value of the stock after some time 𝑡. For doing this the following formula is needed (Hull, 2015).

$$S(T)=S(0)e^{\left(r-q-\frac{\sigma^2}{2}\right)T+\sigma\epsilon\sqrt T}$$

The problem with this equation is 𝜖, since this is not an exact number. 𝜖 can be simulated by generating a random number and plugging it into the inverse of the normal derivation. After doing that one can calculate one possible outcome of the equation. However, this is, as just said, just one possible outcome, so it is needed to repeat the process over and over. The higher the number of repetitions, the more exact the price will be. Theoretically, if the number of repetitions comes close to infinity the result for a European option would be the same as if calculated analytically using the Black-Scholes formulas.