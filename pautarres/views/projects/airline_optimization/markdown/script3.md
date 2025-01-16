## Fleet assignment

The first step for assigning each flight to a specific fleet is to compute the cost for every possible assignment. Therefore, for every flight, the cost of performing it with each available fleet is computed. 

The cost can be computed as the sum of the operating cost and the spill cost. The operating cost can be calculated as:

$$
\text{CASK} \cdot d_{km} \cdot n_{seats}.
$$

To compute the spill cost, the expected passenger spill is first needed:

$$
n_{spill} = \int_{c}^{\infty} (x - c) f(x) \; dx,
$$

where $f(x)$ is the probability density function (PDF) for the normal distribution, obtained using the mean $(\mu)$ and the standard deviation $(\sigma)$ of each flight:

$$
f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right).
$$

The spilled cost can then be estimated as:

$$
\text{RASK} \cdot d_{km} \cdot n_{spill}.
$$

Finally, linear programming can be applied to determine the best fleet distribution with the aim of minimizing the total cost. For the presented case, the result is summarized in the following table.