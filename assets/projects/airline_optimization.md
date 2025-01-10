<style>
  table {
    width: auto !important;
    margin-left: auto;
    margin-right: auto;
    border-collapse: collapse; /* Optional: for better table layout */
  }

  table th, table td {
    text-align: center;
    padding: 8px; /* Optional: adds padding to cells */
    border: 1px solid #ddd; /* Optional: adds border to cells */
  }

  /* Optional: specific style for header row */
  table th {
    background-color: #f2f2f2; /* Light grey */
    font-weight: bold;
  }

  /* Optional: style for the highlighted row */
  tr:hover {
    background-color: #f9f9f9; /* Light hover effect */
  }
</style>

# Airline Optimization

This project was carried out during my master's degree in Aerospace Engineering.
The project explores different aspects of airline operations, including:

-   Fleet distribution
-   Revise schedule
-   Aircraft routing

The referent code can be found in the following
[repository](https://github.com/tarrut/Airline-Optimization/tree/main).

## Introduction

Based on forecasts, the airline’s load-factor policy, and marketing analysis, our airline has proposed providing three daily round-trip flights from OVB to BTK, GDX, NMA, NYM, PWQ, TOF, and UUS.

We have two types of aircraft in our fleet: Boeing 737-400 and Airbus A321. The seating capacities for these two fleet types are 189 and 228 seats, respectively. Furthermore, the following information is available for this airline:

-   Cost per available seat kilometer (CASK) for B737-400 and A321 are 0.037€ (3.7 cents) and 0.04€ (4 cents) respectively.
-   Revenue per available seat kilometer (RASK) for B737-400 and A321 are 0.124€ (12.4 cents) and 0.125€ (12.5 cents) respectively.

The fleet consists of 6 B737-400 aircraft and 10 A321 aircraft. Due to the small size of our airline, we cannot recapture passengers who are spilled. Additionally, turnaround times are 50 and 65 minutes for the B737-400 and A321, respectively. Crew sit-connection times range from 20 to 180 minutes for the B737-400 and from 10 to 185 minutes for the A321.

### Flight schedule

We developed a preliminary schedule for the next quarter. The complete route, which includes 42 flights per day, is presented in the [following
table](https://github.com/tarrut/Airline-Optimization/blob/main/schedule.csv). All departure and arrival times are local.

### Flight information

The [following table](https://github.com/tarrut/Airline-Optimization/blob/main/flight_info.csv) presents the demand distribution for each flight and the distances between cities. Demand for each flight is assumed to be normally distributed, with the specified means and standard deviations.

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

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
  <thead>
    <tr>
      <th style="text-align: center;">Flight no.</th>
      <th style="text-align: center;">Fleet</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center;">EX0001</td>
      <td style="text-align: center;">Boeing 737-400</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0002</td>
      <td style="text-align: center;">Boeing 737-400</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0003</td>
      <td style="text-align: center;">Boeing 737-400</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0004</td>
      <td style="text-align: center;">Boeing 737-400</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0005</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0006</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0007</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0008</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0009</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0010</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0011</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0012</td>
      <td style="text-align: center;">Boeing 737-400</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0013</td>
      <td style="text-align: center;">Boeing 737-400</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0014</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0015</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0016</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0017</td>
      <td style="text-align: center;">Boeing 737-400</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0018</td>
      <td style="text-align: center;">Boeing 737-400</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0019</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0020</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0021</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0022</td>
      <td style="text-align: center;">Boeing 737-400</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0023</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0024</td>
      <td style="text-align: center;">Boeing 737-400</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0025</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0026</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0027</td>
      <td style="text-align: center;">Boeing 737-400</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0028</td>
      <td style="text-align: center;">Boeing 737-400</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0029</td>
      <td style="text-align: center;">Boeing 737-400</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0030</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0031</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0032</td>
      <td style="text-align: center;">Boeing 737-400</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0033</td>
      <td style="text-align: center;">Boeing 737-400</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0034</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0035</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0036</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0037</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0038</td>
      <td style="text-align: center;">Boeing 737-400</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0039</td>
      <td style="text-align: center;">Boeing 737-400</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0040</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0041</td>
      <td style="text-align: center;">Airbus A321</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0042</td>
      <td style="text-align: center;">Boeing 737-400</td>
    </tr>
  </tbody>
</table>


This distribution ensures all flights are performed with the provided fleet.


### Reduction of aircrafts needed

Using linear programming, we determined the minimum number of aircraft required to cover the schedule is 15. However, the current fleet of 16 aircraft will still be used.


### Best combination of aircrafts

The optimal cost is achieved with 8 Boeing 737-400 and 8 Airbus A321 aircraft, resulting in a minimum cost of 742023€.

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
  <thead>
    <tr>
      <th style="text-align: center;">Boeing 737-400 aircrafts</th>
      <th style="text-align: center;">Airbus A321 aircrafts</th>
      <th style="text-align: center;">Total daily cost (€)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center;">0</td>
      <td style="text-align: center;">16</td>
      <td style="text-align: center;">771418</td>
    </tr>
    <tr>
      <td style="text-align: center;">1</td>
      <td style="text-align: center;">15</td>
      <td style="text-align: center;">762409</td>
    </tr>
    <tr>
      <td style="text-align: center;">2</td>
      <td style="text-align: center;">14</td>
      <td style="text-align: center;">755414</td>
    </tr>
    <tr>
      <td style="text-align: center;">3</td>
      <td style="text-align: center;">13</td>
      <td style="text-align: center;">752219</td>
    </tr>
    <tr>
      <td style="text-align: center;">4</td>
      <td style="text-align: center;">12</td>
      <td style="text-align: center;">749171</td>
    </tr>
    <tr>
      <td style="text-align: center;">5</td>
      <td style="text-align: center;">11</td>
      <td style="text-align: center;">746775</td>
    </tr>
    <tr>
      <td style="text-align: center;">6</td>
      <td style="text-align: center;">10</td>
      <td style="text-align: center;">745209</td>
    </tr>
    <tr>
      <td style="text-align: center;">7</td>
      <td style="text-align: center;">9</td>
      <td style="text-align: center;">742510</td>
    </tr>
    <tr style="font-weight: bold; background-color: rgba(255, 253, 233, 255);">
      <td style="text-align: center;">8</td>
      <td style="text-align: center;">8</td>
      <td style="text-align: center;">742023</td>
    </tr>
    <tr>
      <td style="text-align: center;">9</td>
      <td style="text-align: center;">7</td>
      <td style="text-align: center;">743915</td>
    </tr>
    <tr>
      <td style="text-align: center;">10</td>
      <td style="text-align: center;">6</td>
      <td style="text-align: center;">746509</td>
    </tr>
    <tr>
      <td style="text-align: center;">11</td>
      <td style="text-align: center;">5</td>
      <td style="text-align: center;">749700</td>
    </tr>
    <tr>
      <td style="text-align: center;">12</td>
      <td style="text-align: center;">4</td>
      <td style="text-align: center;">753544</td>
    </tr>
    <tr>
      <td style="text-align: center;">13</td>
      <td style="text-align: center;">3</td>
      <td style="text-align: center;">760690</td>
    </tr>
    <tr>
      <td style="text-align: center;">14</td>
      <td style="text-align: center;">2</td>
      <td style="text-align: center;">765543</td>
    </tr>
    <tr>
      <td style="text-align: center;">15</td>
      <td style="text-align: center;">1</td>
      <td style="text-align: center;">773005</td>
    </tr>
    <tr>
      <td style="text-align: center;">16</td>
      <td style="text-align: center;">0</td>
      <td style="text-align: center;">784278</td>
    </tr>
  </tbody>
</table>


## Aircraft routing

Currently, every flight is assigned to a fleet; however, routing cycles and maintenance opportunities at the airline's base airport have not yet been considered. To address this, it is necessary to evaluate whether the current schedule allows the airline's aircraft to be routed cyclically while ensuring adequate maintenance opportunities. This process involves the following steps:

- Generate all valid one-day routings, taking into account turnaround times.
- Combine each feasible one-day routing with other one-day routings to create multi-day route options.
- For each three-day routing, ensure the following:
    - The route starts and ends in the same city.
    - Each day's route begins where the aircraft ended the previous day.
    - At least one overnight stay occurs at the base airport to facilitate maintenance.

Once all possible routes have been identified, an optimization process is applied to select which routes will be implemented. The optimization aims to maximize maintenance opportunities, ensure that each flight is operated daily, and guarantee that each aircraft has at least one maintenance opportunity within a three-day period.

With the current schedule, it has been determined that the airline requires 1 additional B737-400 aircraft and 3 additional A321 aircraft to meet the requirement of at least one maintenance opportunity every three days.

The solution for the B737-400 is presented in the following table:

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
  <thead>
    <tr>
      <th style="text-align: center;">Routing</th>
      <th style="text-align: center;">Day 1</th>
      <th style="text-align: center;">Day 2</th>
      <th style="text-align: center;">Day 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center;">1</td>
      <td style="text-align: center;">EX0001-EX0018-EX0027-EX0042</td>
      <td style="text-align: center;">EX0022-EX0029-EX0038</td>
      <td style="text-align: center;">EX0013</td>
    </tr>
    <tr>
      <td style="text-align: center;">2</td>
      <td style="text-align: center;">EX0003-EX0033</td>
      <td style="text-align: center;">EX0032</td>
      <td style="text-align: center;">EX0004-EX0022-EX0028</td>
    </tr>
    <tr>
      <td style="text-align: center;">3</td>
      <td style="text-align: center;">EX0002-EX0012-EX0028</td>
      <td style="text-align: center;">EX0003-EX0033</td>
      <td style="text-align: center;">EX0032</td>
    </tr>
    <tr>
      <td style="text-align: center;">4</td>
      <td style="text-align: center;">EX0032</td>
      <td style="text-align: center;">EX0004-EX0017-EX0024-EX0039</td>
      <td style="text-align: center;">EX0002-EX0012-EX0033</td>
    </tr>
    <tr>
      <td style="text-align: center;">5</td>
      <td style="text-align: center;">EX0004-EX0017-EX0024-EX0039</td>
      <td style="text-align: center;">EX0002-EX0012-EX0028</td>
      <td style="text-align: center;">EX0003-EX0029-EX0038</td>
    </tr>
    <tr>
      <td style="text-align: center;">6</td>
      <td style="text-align: center;">EX0013</td>
      <td style="text-align: center;">EX0001-EX0018-EX0027-EX0042</td>
      <td style="text-align: center;">EX0017-EX0024-EX0039</td>
    </tr>
    <tr>
      <td style="text-align: center;">7</td>
      <td style="text-align: center;">EX0022-EX0029-EX0038</td>
      <td style="text-align: center;">EX0013</td>
      <td style="text-align: center;">EX0001-EX0018-EX0027-EX0042</td>
    </tr>
  </tbody>
</table>


On the other hand, the routings selected for the A321 are:

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
  <thead>
    <tr>
      <th style="text-align: center;">Routing</th>
      <th style="text-align: center;">Day 1</th>
      <th style="text-align: center;">Day 2</th>
      <th style="text-align: center;">Day 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center;">1</td>
      <td style="text-align: center;">EX0016-EX0034</td>
      <td style="text-align: center;">EX0037</td>
      <td style="text-align: center;">EX0008</td>
    </tr>
    <tr>
      <td style="text-align: center;">2</td>
      <td style="text-align: center;">EX0006-EX0025-EX0036-EX0040</td>
      <td style="text-align: center;">EX0010-EX0020-EX0041</td>
      <td style="text-align: center;">EX0009</td>
    </tr>
    <tr>
      <td style="text-align: center;">3</td>
      <td style="text-align: center;">EX0014-EX0035</td>
      <td style="text-align: center;">EX0009</td>
      <td style="text-align: center;">EX0015</td>
    </tr>
    <tr>
      <td style="text-align: center;">4</td>
      <td style="text-align: center;">EX0011-EX0021</td>
      <td style="text-align: center;">EX0026</td>
      <td style="text-align: center;">EX0005-EX0011-EX0019</td>
    </tr>
    <tr>
      <td style="text-align: center;">5</td>
      <td style="text-align: center;">EX0026</td>
      <td style="text-align: center;">EX0007-EX0030</td>
      <td style="text-align: center;">EX0021</td>
    </tr>
    <tr>
      <td style="text-align: center;">6</td>
      <td style="text-align: center;">EX0007-EX0030</td>
      <td style="text-align: center;">EX0005-EX0011-EX0021</td>
      <td style="text-align: center;">EX0026</td>
    </tr>
    <tr>
      <td style="text-align: center;">7</td>
      <td style="text-align: center;">EX0015</td>
      <td style="text-align: center;">EX0019</td>
      <td style="text-align: center;">EX0023-EX0031</td>
    </tr>
    <tr>
      <td style="text-align: center;">8</td>
      <td style="text-align: center;">EX0037</td>
      <td style="text-align: center;">EX0008</td>
      <td style="text-align: center;">EX0016-EX0034</td>
    </tr>
    <tr>
      <td style="text-align: center;">9</td>
      <td style="text-align: center;">EX0005-EX0023-EX0031</td>
      <td style="text-align: center;">EX0006-EX0025-EX0036</td>
      <td style="text-align: center;">EX0014-EX0035</td>
    </tr>
    <tr>
      <td style="text-align: center;">10</td>
      <td style="text-align: center;">EX0008</td>
      <td style="text-align: center;">EX0016-EX0031</td>
      <td style="text-align: center;">EX0006-EX0025-EX0036</td>
    </tr>
    <tr>
      <td style="text-align: center;">11</td>
      <td style="text-align: center;">EX0019</td>
      <td style="text-align: center;">EX0023-EX0034</td>
      <td style="text-align: center;">EX0037</td>
    </tr>
    <tr>
      <td style="text-align: center;">12</td>
      <td style="text-align: center;">EX0010-EX0020-EX0041</td>
      <td style="text-align: center;">EX0014-EX0035</td>
      <td style="text-align: center;">EX0007-EX0030-EX0040</td>
    </tr>
    <tr>
      <td style="text-align: center;">13</td>
      <td style="text-align: center;">EX0009</td>
      <td style="text-align: center;">EX0015-EX0040</td>
      <td style="text-align: center;">EX0010-EX0020-EX0041</td>
    </tr>
  </tbody>
</table>


### Stranded flights

The need for more aircrafts may be due to some stranded flights. Meaning
that as a consequence of schedule, some flights can not be done during
the same day and have to be carried out during the next day. Some
changes in the schedule can be made manually to reduce the stranded
flights.

Former schedule:
<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
  <thead>
    <tr>
      <th style="text-align: center;">Flight no.</th>
      <th style="text-align: center;">Origin</th>
      <th style="text-align: center;">Departure time</th>
      <th style="text-align: center;">Destination</th>
      <th style="text-align: center;">Arrival time</th>
      <th style="text-align: center;">Flight time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center;">EX0008</td>
      <td style="text-align: center;">OVB</td>
      <td style="text-align: center;">09:10</td>
      <td style="text-align: center;">NMA</td>
      <td style="text-align: center;">12:10</td>
      <td style="text-align: center;">03:00</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0009</td>
      <td style="text-align: center;">OVB</td>
      <td style="text-align: center;">09:20</td>
      <td style="text-align: center;">UUS</td>
      <td style="text-align: center;">14:55</td>
      <td style="text-align: center;">05:35</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0015</td>
      <td style="text-align: center;">UUS</td>
      <td style="text-align: center;">11:50</td>
      <td style="text-align: center;">OVB</td>
      <td style="text-align: center;">17:25</td>
      <td style="text-align: center;">05:35</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0021</td>
      <td style="text-align: center;">OVB</td>
      <td style="text-align: center;">14:05</td>
      <td style="text-align: center;">GDX</td>
      <td style="text-align: center;">19:30</td>
      <td style="text-align: center;">05:25</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0026</td>
      <td style="text-align: center;">GDX</td>
      <td style="text-align: center;">15:50</td>
      <td style="text-align: center;">OVB</td>
      <td style="text-align: center;">21:15</td>
      <td style="text-align: center;">05:25</td>
    </tr>
  </tbody>
</table>

Modified schedule:
<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
  <thead>
    <tr>
      <th style="text-align: center;">Flight no.</th>
      <th style="text-align: center;">Origin</th>
      <th style="text-align: center;">Departure time</th>
      <th style="text-align: center;">Destination</th>
      <th style="text-align: center;">Arrival time</th>
      <th style="text-align: center;">Flight time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center;">EX0008</td>
      <td style="text-align: center;">OVB</td>
      <td style="text-align: center;">07:10</td>
      <td style="text-align: center;">NMA</td>
      <td style="text-align: center;">10:10</td>
      <td style="text-align: center;">03:00</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0009</td>
      <td style="text-align: center;">OVB</td>
      <td style="text-align: center;">07:00</td>
      <td style="text-align: center;">UUS</td>
      <td style="text-align: center;">12:35</td>
      <td style="text-align: center;">05:35</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0015</td>
      <td style="text-align: center;">UUS</td>
      <td style="text-align: center;">13:50</td>
      <td style="text-align: center;">OVB</td>
      <td style="text-align: center;">19:25</td>
      <td style="text-align: center;">05:35</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0021</td>
      <td style="text-align: center;">OVB</td>
      <td style="text-align: center;">11:05</td>
      <td style="text-align: center;">GDX</td>
      <td style="text-align: center;">16:30</td>
      <td style="text-align: center;">05:25</td>
    </tr>
    <tr>
      <td style="text-align: center;">EX0026</td>
      <td style="text-align: center;">GDX</td>
      <td style="text-align: center;">17:50</td>
      <td style="text-align: center;">OVB</td>
      <td style="text-align: center;">23:15</td>
      <td style="text-align: center;">05:25</td>
    </tr>
  </tbody>
</table>


### Routing for revised schedule

With the revised schedule it is only needed 1 extra B737-400 aircrafts.

Here are the new routings selected for the B737-400:

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
  <thead>
    <tr>
      <th style="text-align: center;">Routing</th>
      <th style="text-align: center;">Day 1</th>
      <th style="text-align: center;">Day 2</th>
      <th style="text-align: center;">Day 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center;">1</td>
      <td style="text-align: center;">EX0001-EX0018-EX0027-EX0042</td>
      <td style="text-align: center;">EX0022-EX0029-EX0038</td>
      <td style="text-align: center;">EX0013</td>
    </tr>
    <tr>
      <td style="text-align: center;">2</td>
      <td style="text-align: center;">EX0003-EX0033</td>
      <td style="text-align: center;">EX0032</td>
      <td style="text-align: center;">EX0004-EX0022-EX0028</td>
    </tr>
    <tr>
      <td style="text-align: center;">3</td>
      <td style="text-align: center;">EX0002-EX0012-EX0028</td>
      <td style="text-align: center;">EX0003-EX0033</td>
      <td style="text-align: center;">EX0032</td>
    </tr>
    <tr>
      <td style="text-align: center;">4</td>
      <td style="text-align: center;">EX0032</td>
      <td style="text-align: center;">EX0004-EX0017-EX0024-EX0039</td>
      <td style="text-align: center;">EX0002-EX0012-EX0033</td>
    </tr>
    <tr>
      <td style="text-align: center;">5</td>
      <td style="text-align: center;">EX0004-EX0017-EX0024-EX0039</td>
      <td style="text-align: center;">EX0002-EX0012-EX0028</td>
      <td style="text-align: center;">EX0003-EX0029-EX0038</td>
    </tr>
    <tr>
      <td style="text-align: center;">6</td>
      <td style="text-align: center;">EX0013</td>
      <td style="text-align: center;">EX0001-EX0018-EX0027-EX0042</td>
      <td style="text-align: center;">EX0017-EX0024-EX0039</td>
    </tr>
    <tr>
      <td style="text-align: center;">7</td>
      <td style="text-align: center;">EX0022-EX0029-EX0038</td>
      <td style="text-align: center;">EX0013</td>
      <td style="text-align: center;">EX0001-EX0018-EX0027-EX0042</td>
    </tr>
  </tbody>
</table>


This table shows the maintenance opportunities during the three-day
routings:

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
  <thead>
    <tr>
      <th style="text-align: center;">Routing</th>
      <th style="text-align: center;">Day 1</th>
      <th style="text-align: center;">Day 2</th>
      <th style="text-align: center;">Day 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center;">1</td>
      <td style="text-align: center;"></td>
      <td style="text-align: center;">✓</td>
      <td style="text-align: center;"></td>
    </tr>
    <tr>
      <td style="text-align: center;">2</td>
      <td style="text-align: center;"></td>
      <td style="text-align: center;">✓</td>
      <td style="text-align: center;"></td>
    </tr>
    <tr>
      <td style="text-align: center;">3</td>
      <td style="text-align: center;"></td>
      <td style="text-align: center;"></td>
      <td style="text-align: center;">✓</td>
    </tr>
    <tr>
      <td style="text-align: center;">4</td>
      <td style="text-align: center;">✓</td>
      <td style="text-align: center;">✓</td>
      <td style="text-align: center;"></td>
    </tr>
    <tr>
      <td style="text-align: center;">5</td>
      <td style="text-align: center;">✓</td>
      <td style="text-align: center;"></td>
      <td style="text-align: center;">✓</td>
    </tr>
    <tr>
      <td style="text-align: center;">6</td>
      <td style="text-align: center;"></td>
      <td style="text-align: center;"></td>
      <td style="text-align: center;">✓</td>
    </tr>
    <tr>
      <td style="text-align: center;">7</td>
      <td style="text-align: center;">✓</td>
      <td style="text-align: center;"></td>
      <td style="text-align: center;"></td>
    </tr>
    <tr>
      <td style="text-align: center;">Total</td>
      <td style="text-align: center;">3</td>
      <td style="text-align: center;">3</td>
      <td style="text-align: center;">3</td>
    </tr>
  </tbody>
</table>


The solution for A321 is:

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
  <thead>
    <tr>
      <th style="text-align: center;">Routing</th>
      <th style="text-align: center;">Day 1</th>
      <th style="text-align: center;">Day 2</th>
      <th style="text-align: center;">Day 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center;">1</td>
      <td style="text-align: center;">EX0008-EX0016-EX0034</td>
      <td style="text-align: center;">EX0030</td>
      <td style="text-align: center;">EX0009-EX0015</td>
    </tr>
    <tr>
      <td style="text-align: center;">2</td>
      <td style="text-align: center;">EX0023-EX0031</td>
      <td style="text-align: center;">EX0006-EX0025-EX0036</td>
      <td style="text-align: center;">EX0005-EX0011-EX0019</td>
    </tr>
    <tr>
      <td style="text-align: center;">3</td>
      <td style="text-align: center;">EX0021-EX0035</td>
      <td style="text-align: center;">EX0014-EX0035</td>
      <td style="text-align: center;">EX0021-EX0026</td>
    </tr>
    <tr>
      <td style="text-align: center;">4</td>
      <td style="text-align: center;">EX0007-EX0030-EX0040</td>
      <td style="text-align: center;">EX0010-EX0020-EX0041</td>
      <td style="text-align: center;">EX0007-EX0030</td>
    </tr>
    <tr>
      <td style="text-align: center;">5</td>
      <td style="text-align: center;">EX0006-EX0025-EX0036</td>
      <td style="text-align: center;">EX0005-EX0011-EX0019</td>
      <td style="text-align: center;">EX0023-EX0031</td>
    </tr>
    <tr>
      <td style="text-align: center;">6</td>
      <td style="text-align: center;">EX0037</td>
      <td style="text-align: center;">EX0007-EX0037</td>
      <td style="text-align: center;">EX0008-EX0016-EX0034</td>
    </tr>
    <tr>
      <td style="text-align: center;">7</td>
      <td style="text-align: center;">EX0014-EX0026</td>
      <td style="text-align: center;">EX0021-EX0026</td>
      <td style="text-align: center;">EX0014-EX0035</td>
    </tr>
    <tr>
      <td style="text-align: center;">8</td>
      <td style="text-align: center;">EX0005-EX0011-EX0019</td>
      <td style="text-align: center;">EX0023-EX0034</td>
      <td style="text-align: center;">EX0037</td>
    </tr>
    <tr>
      <td style="text-align: center;">9</td>
      <td style="text-align: center;">EX0010-EX0020-EX0041</td>
      <td style="text-align: center;">EX0008-EX0016-EX0031</td>
      <td style="text-align: center;">EX0006-EX0025-EX0036-EX0040</td>
    </tr>
    <tr>
      <td style="text-align: center;">10</td>
      <td style="text-align: center;">EX0009-EX0015</td>
      <td style="text-align: center;">EX0009-EX0015-EX0040</td>
      <td style="text-align: center;">EX0010-EX0020-EX0041</td>
    </tr>
  </tbody>
</table>

And, this fleet has 18 maintenance opportunities:

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
  <thead>
    <tr>
      <th style="text-align: center;">Routing</th>
      <th style="text-align: center;">Day 1</th>
      <th style="text-align: center;">Day 2</th>
      <th style="text-align: center;">Day 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center;">1</td>
      <td style="text-align: center;"></td>
      <td style="text-align: center;">✓</td>
      <td style="text-align: center;">✓</td>
    </tr>
    <tr>
      <td style="text-align: center;">2</td>
      <td style="text-align: center;"></td>
      <td style="text-align: center;">✓</td>
      <td style="text-align: center;"></td>
    </tr>
    <tr>
      <td style="text-align: center;">3</td>
      <td style="text-align: center;">✓</td>
      <td style="text-align: center;">✓</td>
      <td style="text-align: center;">✓</td>
    </tr>
    <tr>
      <td style="text-align: center;">4</td>
      <td style="text-align: center;"></td>
      <td style="text-align: center;">✓</td>
      <td style="text-align: center;">✓</td>
    </tr>
    <tr>
      <td style="text-align: center;">5</td>
      <td style="text-align: center;">✓</td>
      <td style="text-align: center;"></td>
      <td style="text-align: center;"></td>
    </tr>
    <tr>
      <td style="text-align: center;">6</td>
      <td style="text-align: center;">✓</td>
      <td style="text-align: center;">✓</td>
      <td style="text-align: center;"></td>
    </tr>
    <tr>
      <td style="text-align: center;">7</td>
      <td style="text-align: center;">✓</td>
      <td style="text-align: center;">✓</td>
      <td style="text-align: center;">✓</td>
    </tr>
    <tr>
      <td style="text-align: center;">8</td>
      <td style="text-align: center;"></td>
      <td style="text-align: center;"></td>
      <td style="text-align: center;">✓</td>
    </tr>
    <tr>
      <td style="text-align: center;">9</td>
      <td style="text-align: center;">✓</td>
      <td style="text-align: center;"></td>
      <td style="text-align: center;"></td>
    </tr>
    <tr>
      <td style="text-align: center;">10</td>
      <td style="text-align: center;">✓</td>
      <td style="text-align: center;"></td>
      <td style="text-align: center;">✓</td>
    </tr>
    <tr>
      <td style="text-align: center;">Total</td>
      <td style="text-align: center;">6</td>
      <td style="text-align: center;">6</td>
      <td style="text-align: center;">6</td>
    </tr>
  </tbody>
</table>
