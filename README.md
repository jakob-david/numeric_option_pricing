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

$$d\Delta f = \left( \frac{\partial f}{\partial S} \mu S +\frac{\partial f}{\partial t} + \frac{1}{2}\frac{\partial^{2} f}{\partial^{2} x^{2}} \sigma^{2} S^{2}\right) \Delta t+\frac{\partial f}{\partial x} \sigma S \epsilon \sqrt{\Delta t}$$

Because these equations are differential equations, every formula that solves the equation represents the change of value in an option price according to an Itô process. For European call ($c$) or put ($p$) options with a known dividend yield this equation actually can be solved analytically with the result shown below (Morton, 1973) (Hull, 2015).

$$c_{price}=\ S_{0\ }e^{-qT}N\left(d_1\right)-Ke^{-eT}\ N(d_2)$$

$$p_{price}=\ {Ke^{-eT}\ N\left(d_2\right)-S}_{0\ }e^{-qT}N\left(d_1\right)$$

where $d_{1\ }$ and $d_2 is$ are given by

$$d_1=\ \frac{\ln{\left(\frac{S_0}{K}\right)}+\left(r-q+\frac{{\ \sigma}^2}{2}\right)T}{\sigma\ \sqrt T}$$

$$d_2=\ \frac{\ln{\left(\frac{S_0}{K}\right)}+\left(r-q-\frac{{\ \sigma}^2}{2}\right)T}{\sigma\ \sqrt T}$$

In these equations $S_0$ is the spot price of the stock, $K$ is the strike price of the option, $r$ is the risk-free interest rate, $q$ is the dividend yield of the underlying, $\sigma$ its volatility and $T$ is the time until the maturity of the stock. If the underlying of the option does not pay dividends, the dividend yield is zero. 

## Numerical Methods
It is very easy to calculate the current price of a European option since it is possible to find a suitable analytical solution for equation. As mentioned earlier this is not always the case. For instance, an American option can be exercised at any time and thus, as of today, an analytical solution for the Black-Scholes-Morten differential equation is known. For problems like this it is needed to use numerical methods. These were described already shortly above. To use this method’s formula the discrete version is needed. All the methods described in this section were coded in the course of this paper and can be found in Appendix A. Among others Press (1992), Ødegaard (2014) and (Hull, 2015) were used for the coding. 

### Binomial Tree
The binomial tree approach is illustrated in Figure 2. The root of the tree is the spot price. Now there are two possibilities. Either the stock moves up with a certain probability or moves down with a certain probability. From the so obtained nodes the stock can again either go up or down. This goes on as long as it is wanted. Since it makes no difference whether the stock moves first up and then down or vice versa the two nodes merge. For coding the Algorithm Thurman (2018) was used. 

<p align="center">
    <img width="500" src="./zz_pictures_for_readme/picture_2.png" alt="Figure 3"><br>
    <em>
    Figure 2: Illustration of a binomial tree used for option pricing. (Hull, 2015)
    </em>
</p>

Since the values for $S_0$ are the same in the last layer the value of the option for that layer can be calculated with $\max\funcapply(S_ou^jd^{N-1}-K,\ 0)$ for a call option and $\max\funcapply(K-S_ou^jd^{N-1},\ 0)$ for a put option. This can be derived from the equations. The next step is not that easy. Now it is needed to go back step by step to the beginning of the binomial tree. To give an example, to obtain the value of $S_0u^3$ from Figure 2, $S_0u^4$ and $S_0u^2$ are needed. In the end the value of the root node is obtained which is an approximation for the real value of the option. The exact formulas can also be derived. (Hull, 2015)

$$p=\frac{a-d}{u-d}$$

$$u=eσ∆t$$

$$d=e-σ∆t$$

where 

$$a=e(r-q)∆t$$

Hull (2015) specifies the formulas for working a binomial tree for American Options backwards. Because an American option can be exercised at any time a max function is needed at every node. For a call option this gives

$$f_{i,\ j}=\max\funcapply{S_0u^jd^{i-j}-K,\ e-r∆t[pfi+1,j+1+(1-p)fi+1,j]}$$

and for a put option 

$$f_{i,\ j}=\max\funcapply{{K-\ S}_0u^jd^{i-j},\ e-r∆t[pfi+1,j+1+(1-p)fi+1,j]}$$

In these equations $i$ is the time interval and $j$ identifies the different nodes per time interval. As an example, $S_0u^3$ from Figure 2 would be $f_{3,3}$. When evaluating a European option, the max function is not needed, and it is easy to see that 

$$f_{i,\ j}=e-r∆t pfi+1,j+1+(1-p)fi+1,j$$

### Monte Carlo Simulation
The way of pricing an option with a Monte Carlo simulation is quite different to the other ways of option pricing. In contrast to the other methods discussed in this paper, it is not needed to calculate nodes or build a tree in some kind. The procedure is quite simple and can easily be implemented in Microsoft Excel as shown by Hull (2015). First, one calculates the value of the stock after some time 𝑡. For doing this the following formula is needed (Hull, 2015).

$$S(T)=S(0)e^{\left(r-q-\frac{\sigma^2}{2}\right)T+\sigma\epsilon\sqrt T}$$

The problem with this equation is 𝜖, since this is not an exact number. 𝜖 can be simulated by generating a random number and plugging it into the inverse of the normal derivation. After doing that one can calculate one possible outcome of the equation. However, this is, as just said, just one possible outcome, so it is needed to repeat the process over and over. The higher the number of repetitions, the more exact the price will be. Theoretically, if the number of repetitions comes close to infinity the result for a European option would be the same as if calculated analytically using the Black-Scholes formulas.