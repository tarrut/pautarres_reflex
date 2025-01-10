<style type="text/css">

body{ /* Normal  */
      font-size: 14px;
  }
</style>

# Airline Optimization

This project has been carried out during my masters degree in Aerospace
Engineering. In the project, diferent aspects of the job of am airline
are presented. These include:

-   Fleet distribution
-   Revise schedule
-   Aircraft routing

The referent code can be found in the following
[repository](https://github.com/tarrut/Airline-Optimization/tree/main).

## Introduction

Based on forecasts, the airline’s load-factor policy, and marketing
analysis, our airline has proposed providing three daily round-trip
flights from OVB to BTK, GDX, NMA, NYM, PWQ, TOF and UUS.

We have two types of fleet, namely Boeing 737-400 and Airbus A321. The
seating capacities for these two fleet types are 189 and 228 seats
respectively. Furthermore, we have the following information for this
airline:

-   Cost per available seat kilometer (CASK) for B737-400 and A321 are
    0.037€ (3.7 cents) and 0.04€ (4 cents) respectively.
-   Revenue per available seat kilometer (RASK) for B737-400 and A321
    are 0.124€ (12.4 cents) and 0.125€ (12.5 cents) respectively.

Assume that we have 6 and 10 aircrafts in our B737-400 and A321 fleets,
respectively. Due to the small size of our airline we are unable to
recapture passengers that were spilled. Also assume turnaround times of
50 and 65 minutes for these two fleet types respectively. Furthermore,
sit-connection times for crew members will range from 20 to 180 minutes
for B737-400 and 10 to 185 minutes for A321.

### Flight schedule

We have also developed a first draft of our schedule for the next
quarter. The complete flight schedule route, incorporating the 42
flights per day, is presented in the [following
table](https://github.com/tarrut/Airline-Optimization/blob/e653312ae903a598b87b9ac467ad52251428c680/schedule.csv).
All the arrival and departure times are local times.

### Flight information

The [following
table](https://github.com/tarrut/Airline-Optimization/blob/e653312ae903a598b87b9ac467ad52251428c680/flight_info.csv)
presents the demand distribution for each flight as well as distances
between cities. It is assumed that demand for each flight is normally
distributed with the given means and standard deviations.

## Fleet assignment

The first step for assigning each flight to an specific fleet, it is to
compute the cost to every possible assignment. Therefore, for every
flight, the cost of doing it with every fleet available is computed. The
cost can be computed as the operating cost and the spill cost. The
operation cost can be computed like
CASK ⋅ *d*<sub>*k**m*</sub> ⋅ *n*<sub>*s**e**a**t**s*</sub>.
To compute the spill cost first is needed the expected passenger spill:
*n*<sub>*s**p**i**l**l*</sub> = ∫<sub>*c*</sub><sup>∞</sup>(*x* − *c*)*f*(*x*) *d**x*,
where *f*(*x*) is the probability density function (PDF) for the normal
distribution obtained with the mean (*μ*) and the standard variation
(*σ*) of each flight
$$
f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right).
$$
Then, the spilled cost can be estimated like
RASK ⋅ *d*<sub>*k**m*</sub> ⋅ *n*<sub>*s**p**i**l**l*</sub>
Then, linear programming can be applied to determine the best fleet
distribution, with the aim of minimizing the cost. For the presented
case, the result is presented in the following table.

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
<thead>
<tr>
<th style="text-align:center;">
Flight no.
</th>
<th style="text-align:center;">
Fleet
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center;">
EX0001
</td>
<td style="text-align:center;">
Boeing 737-400
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0002
</td>
<td style="text-align:center;">
Boeing 737-400
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0003
</td>
<td style="text-align:center;">
Boeing 737-400
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0004
</td>
<td style="text-align:center;">
Boeing 737-400
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0005
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0006
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0007
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0008
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0009
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0010
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0011
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0012
</td>
<td style="text-align:center;">
Boeing 737-400
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0013
</td>
<td style="text-align:center;">
Boeing 737-400
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0014
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0015
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0016
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0017
</td>
<td style="text-align:center;">
Boeing 737-400
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0018
</td>
<td style="text-align:center;">
Boeing 737-400
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0019
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0020
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0021
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0022
</td>
<td style="text-align:center;">
Boeing 737-400
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0023
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0024
</td>
<td style="text-align:center;">
Boeing 737-400
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0025
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0026
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0027
</td>
<td style="text-align:center;">
Boeing 737-400
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0028
</td>
<td style="text-align:center;">
Boeing 737-400
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0029
</td>
<td style="text-align:center;">
Boeing 737-400
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0030
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0031
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0032
</td>
<td style="text-align:center;">
Boeing 737-400
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0033
</td>
<td style="text-align:center;">
Boeing 737-400
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0034
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0035
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0036
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0037
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0038
</td>
<td style="text-align:center;">
Boeing 737-400
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0039
</td>
<td style="text-align:center;">
Boeing 737-400
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0040
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0041
</td>
<td style="text-align:center;">
Airbus A321
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0042
</td>
<td style="text-align:center;">
Boeing 737-400
</td>
</tr>
</tbody>
</table>

This distribution allows to perform all the flights with the provided
number of aircraft of each fleet.

### Reduction of aircrafts needed

However, it can be computed (using linear programming) if all the
aircrafts are actually needed to cover the provided schedule. It
results, that the minimum number of aircrafts is **15**, less than our
current fleet. Despite this, the 16 aircrafts will be used up from this
point.

### Best combination of aircrafts

It is also quite interesting comparing the total cost of using different
number of aircrafts from both fleets. It results that the best
combination is formed by 8 Boeing 737-400 and 8 Airbus A321 with a
minimum cost of 742023€.

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
<thead>
<tr>
<th style="text-align:center;">
Boeing 737-400 aircrafts
</th>
<th style="text-align:center;">
Airbus A321 aircrafts
</th>
<th style="text-align:center;">
Total daily cost (€)
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center;">
0
</td>
<td style="text-align:center;">
16
</td>
<td style="text-align:center;">
771418
</td>
</tr>
<tr>
<td style="text-align:center;">
1
</td>
<td style="text-align:center;">
15
</td>
<td style="text-align:center;">
762409
</td>
</tr>
<tr>
<td style="text-align:center;">
2
</td>
<td style="text-align:center;">
14
</td>
<td style="text-align:center;">
755414
</td>
</tr>
<tr>
<td style="text-align:center;">
3
</td>
<td style="text-align:center;">
13
</td>
<td style="text-align:center;">
752219
</td>
</tr>
<tr>
<td style="text-align:center;">
4
</td>
<td style="text-align:center;">
12
</td>
<td style="text-align:center;">
749171
</td>
</tr>
<tr>
<td style="text-align:center;">
5
</td>
<td style="text-align:center;">
11
</td>
<td style="text-align:center;">
746775
</td>
</tr>
<tr>
<td style="text-align:center;">
6
</td>
<td style="text-align:center;">
10
</td>
<td style="text-align:center;">
745209
</td>
</tr>
<tr>
<td style="text-align:center;">
7
</td>
<td style="text-align:center;">
9
</td>
<td style="text-align:center;">
742510
</td>
</tr>
<tr>
<td style="text-align:center;font-weight: bold;background-color: rgba(255, 253, 233, 255) !important;">
8
</td>
<td style="text-align:center;font-weight: bold;background-color: rgba(255, 253, 233, 255) !important;">
8
</td>
<td style="text-align:center;font-weight: bold;background-color: rgba(255, 253, 233, 255) !important;">
742023
</td>
</tr>
<tr>
<td style="text-align:center;">
9
</td>
<td style="text-align:center;">
7
</td>
<td style="text-align:center;">
743915
</td>
</tr>
<tr>
<td style="text-align:center;">
10
</td>
<td style="text-align:center;">
6
</td>
<td style="text-align:center;">
746509
</td>
</tr>
<tr>
<td style="text-align:center;">
11
</td>
<td style="text-align:center;">
5
</td>
<td style="text-align:center;">
749700
</td>
</tr>
<tr>
<td style="text-align:center;">
12
</td>
<td style="text-align:center;">
4
</td>
<td style="text-align:center;">
753544
</td>
</tr>
<tr>
<td style="text-align:center;">
13
</td>
<td style="text-align:center;">
3
</td>
<td style="text-align:center;">
760690
</td>
</tr>
<tr>
<td style="text-align:center;">
14
</td>
<td style="text-align:center;">
2
</td>
<td style="text-align:center;">
765543
</td>
</tr>
<tr>
<td style="text-align:center;">
15
</td>
<td style="text-align:center;">
1
</td>
<td style="text-align:center;">
773005
</td>
</tr>
<tr>
<td style="text-align:center;">
16
</td>
<td style="text-align:center;">
0
</td>
<td style="text-align:center;">
784278
</td>
</tr>
</tbody>
</table>

## Aircraft routing

Now every flight is assigned to a fleet, but routings cycles and
maintenance opportunities at the airport where the airline is based have
not been considered. First it has to be checked if with the current
schedule, the airline aircrafts can be routed in a cyclical way while
having enough maintenance opportunities. For the purpose of doing this,
first we have to obtain all the possible routes. This process consists
in:

-   First, all the possible valid one-day routings considering turn
    around-times.
-   Attach each feasible one day routing to all other one-day routings.
-   Each three-day routing has to be examined according to the following
    criteria:
    -   It starts and ends in the same city.
    -   Each day, the route should start where the aircraft started the
        day before.
    -   An overnight stay at the base airport occurs at least once.

Then, an optimization process is now used to select which routes will be
implemented while:

-   Maximizing the maintenance opportunities.
-   Ensuring that each flight is carried out every day.
-   During the period of three days, each aircraft must have at least
    one maintenance opportunity.

It turns out that with the current schedule it is needed 1 extra
B737-400 aircraft and 3 extra A321 aircrafts considering at least one
maintenance opportunity every three days.

The solution for the B737-400 is in the following table:

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
<thead>
<tr>
<th style="text-align:center;">
Routing
</th>
<th style="text-align:center;">
Day 1
</th>
<th style="text-align:center;">
Day 2
</th>
<th style="text-align:center;">
Day 3
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center;">
1
</td>
<td style="text-align:center;">
EX0001-EX0018-EX0027-EX0042
</td>
<td style="text-align:center;">
EX0022-EX0029-EX0038
</td>
<td style="text-align:center;">
EX0013
</td>
</tr>
<tr>
<td style="text-align:center;">
2
</td>
<td style="text-align:center;">
EX0003-EX0033
</td>
<td style="text-align:center;">
EX0032
</td>
<td style="text-align:center;">
EX0004-EX0022-EX0028
</td>
</tr>
<tr>
<td style="text-align:center;">
3
</td>
<td style="text-align:center;">
EX0002-EX0012-EX0028
</td>
<td style="text-align:center;">
EX0003-EX0033
</td>
<td style="text-align:center;">
EX0032
</td>
</tr>
<tr>
<td style="text-align:center;">
4
</td>
<td style="text-align:center;">
EX0032
</td>
<td style="text-align:center;">
EX0004-EX0017-EX0024-EX0039
</td>
<td style="text-align:center;">
EX0002-EX0012-EX0033
</td>
</tr>
<tr>
<td style="text-align:center;">
5
</td>
<td style="text-align:center;">
EX0004-EX0017-EX0024-EX0039
</td>
<td style="text-align:center;">
EX0002-EX0012-EX0028
</td>
<td style="text-align:center;">
EX0003-EX0029-EX0038
</td>
</tr>
<tr>
<td style="text-align:center;">
6
</td>
<td style="text-align:center;">
EX0013
</td>
<td style="text-align:center;">
EX0001-EX0018-EX0027-EX0042
</td>
<td style="text-align:center;">
EX0017-EX0024-EX0039
</td>
</tr>
<tr>
<td style="text-align:center;">
7
</td>
<td style="text-align:center;">
EX0022-EX0029-EX0038
</td>
<td style="text-align:center;">
EX0013
</td>
<td style="text-align:center;">
EX0001-EX0018-EX0027-EX0042
</td>
</tr>
</tbody>
</table>

On the other hand, the routings selected for the A321 are:

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
<thead>
<tr>
<th style="text-align:center;">
Routing
</th>
<th style="text-align:center;">
Day 1
</th>
<th style="text-align:center;">
Day 2
</th>
<th style="text-align:center;">
Day 3
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center;">
1
</td>
<td style="text-align:center;">
EX0016-EX0034
</td>
<td style="text-align:center;">
EX0037
</td>
<td style="text-align:center;">
EX0008
</td>
</tr>
<tr>
<td style="text-align:center;">
2
</td>
<td style="text-align:center;">
EX0006-EX0025-EX0036-EX0040
</td>
<td style="text-align:center;">
EX0010-EX0020-EX0041
</td>
<td style="text-align:center;">
EX0009
</td>
</tr>
<tr>
<td style="text-align:center;">
3
</td>
<td style="text-align:center;">
EX0014-EX0035
</td>
<td style="text-align:center;">
EX0009
</td>
<td style="text-align:center;">
EX0015
</td>
</tr>
<tr>
<td style="text-align:center;">
4
</td>
<td style="text-align:center;">
EX0011-EX0021
</td>
<td style="text-align:center;">
EX0026
</td>
<td style="text-align:center;">
EX0005-EX0011-EX0019
</td>
</tr>
<tr>
<td style="text-align:center;">
5
</td>
<td style="text-align:center;">
EX0026
</td>
<td style="text-align:center;">
EX0007-EX0030
</td>
<td style="text-align:center;">
EX0021
</td>
</tr>
<tr>
<td style="text-align:center;">
6
</td>
<td style="text-align:center;">
EX0007-EX0030
</td>
<td style="text-align:center;">
EX0005-EX0011-EX0021
</td>
<td style="text-align:center;">
EX0026
</td>
</tr>
<tr>
<td style="text-align:center;">
7
</td>
<td style="text-align:center;">
EX0015
</td>
<td style="text-align:center;">
EX0019
</td>
<td style="text-align:center;">
EX0023-EX0031
</td>
</tr>
<tr>
<td style="text-align:center;">
8
</td>
<td style="text-align:center;">
EX0037
</td>
<td style="text-align:center;">
EX0008
</td>
<td style="text-align:center;">
EX0016-EX0034
</td>
</tr>
<tr>
<td style="text-align:center;">
9
</td>
<td style="text-align:center;">
EX0005-EX0023-EX0031
</td>
<td style="text-align:center;">
EX0006-EX0025-EX0036
</td>
<td style="text-align:center;">
EX0014-EX0035
</td>
</tr>
<tr>
<td style="text-align:center;">
10
</td>
<td style="text-align:center;">
EX0008
</td>
<td style="text-align:center;">
EX0016-EX0031
</td>
<td style="text-align:center;">
EX0006-EX0025-EX0036
</td>
</tr>
<tr>
<td style="text-align:center;">
11
</td>
<td style="text-align:center;">
EX0019
</td>
<td style="text-align:center;">
EX0023-EX0034
</td>
<td style="text-align:center;">
EX0037
</td>
</tr>
<tr>
<td style="text-align:center;">
12
</td>
<td style="text-align:center;">
EX0010-EX0020-EX0041
</td>
<td style="text-align:center;">
EX0014-EX0035
</td>
<td style="text-align:center;">
EX0007-EX0030-EX0040
</td>
</tr>
<tr>
<td style="text-align:center;">
13
</td>
<td style="text-align:center;">
EX0009
</td>
<td style="text-align:center;">
EX0015-EX0040
</td>
<td style="text-align:center;">
EX0010-EX0020-EX0041
</td>
</tr>
</tbody>
</table>

### Stranded flights

The need for more aircrafts may be due to some stranded flights. Meaning
that as a consequence of schedule, some flights can not be done during
the same day and have to be carried out during the next day. Some
changes in the schedule can be made manually to reduce the stranded
flights.

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
<thead>
<tr>
<th style="text-align:center;">
Flight no.
</th>
<th style="text-align:center;">
Origin
</th>
<th style="text-align:center;">
Departure time
</th>
<th style="text-align:center;">
Destination
</th>
<th style="text-align:center;">
Arrival time
</th>
<th style="text-align:center;">
Flight time
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center;">
EX0008
</td>
<td style="text-align:center;">
OVB
</td>
<td style="text-align:center;">
09:10
</td>
<td style="text-align:center;">
NMA
</td>
<td style="text-align:center;">
12:10
</td>
<td style="text-align:center;">
03:00
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0009
</td>
<td style="text-align:center;">
OVB
</td>
<td style="text-align:center;">
09:20
</td>
<td style="text-align:center;">
UUS
</td>
<td style="text-align:center;">
14:55
</td>
<td style="text-align:center;">
05:35
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0015
</td>
<td style="text-align:center;">
UUS
</td>
<td style="text-align:center;">
11:50
</td>
<td style="text-align:center;">
OVB
</td>
<td style="text-align:center;">
17:25
</td>
<td style="text-align:center;">
05:35
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0021
</td>
<td style="text-align:center;">
OVB
</td>
<td style="text-align:center;">
14:05
</td>
<td style="text-align:center;">
GDX
</td>
<td style="text-align:center;">
19:30
</td>
<td style="text-align:center;">
05:25
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0026
</td>
<td style="text-align:center;">
GDX
</td>
<td style="text-align:center;">
15:50
</td>
<td style="text-align:center;">
OVB
</td>
<td style="text-align:center;">
21:15
</td>
<td style="text-align:center;">
05:25
</td>
</tr>
</tbody>
</table>
<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
<thead>
<tr>
<th style="text-align:center;">
Flight no.
</th>
<th style="text-align:center;">
Origin
</th>
<th style="text-align:center;">
Departure time
</th>
<th style="text-align:center;">
Destination
</th>
<th style="text-align:center;">
Arrival time
</th>
<th style="text-align:center;">
Flight time
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center;">
EX0008
</td>
<td style="text-align:center;">
OVB
</td>
<td style="text-align:center;">
07:10
</td>
<td style="text-align:center;">
NMA
</td>
<td style="text-align:center;">
10:10
</td>
<td style="text-align:center;">
03:00
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0009
</td>
<td style="text-align:center;">
OVB
</td>
<td style="text-align:center;">
07:00
</td>
<td style="text-align:center;">
UUS
</td>
<td style="text-align:center;">
12:35
</td>
<td style="text-align:center;">
05:35
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0015
</td>
<td style="text-align:center;">
UUS
</td>
<td style="text-align:center;">
13:50
</td>
<td style="text-align:center;">
OVB
</td>
<td style="text-align:center;">
19:25
</td>
<td style="text-align:center;">
05:35
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0021
</td>
<td style="text-align:center;">
OVB
</td>
<td style="text-align:center;">
11:05
</td>
<td style="text-align:center;">
GDX
</td>
<td style="text-align:center;">
16:30
</td>
<td style="text-align:center;">
05:25
</td>
</tr>
<tr>
<td style="text-align:center;">
EX0026
</td>
<td style="text-align:center;">
GDX
</td>
<td style="text-align:center;">
17:50
</td>
<td style="text-align:center;">
OVB
</td>
<td style="text-align:center;">
23:15
</td>
<td style="text-align:center;">
05:25
</td>
</tr>
</tbody>
</table>

### Routing for revised schedule

With the revised schedule it is only needed 1 extra B737-400 aircrafts.

Here are the new routings selected for the B737-400:
<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
<thead>
<tr>
<th style="text-align:center;">
Routing
</th>
<th style="text-align:center;">
Day 1
</th>
<th style="text-align:center;">
Day 2
</th>
<th style="text-align:center;">
Day 3
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center;">
1
</td>
<td style="text-align:center;">
EX0001-EX0018-EX0027-EX0042
</td>
<td style="text-align:center;">
EX0022-EX0029-EX0038
</td>
<td style="text-align:center;">
EX0013
</td>
</tr>
<tr>
<td style="text-align:center;">
2
</td>
<td style="text-align:center;">
EX0003-EX0033
</td>
<td style="text-align:center;">
EX0032
</td>
<td style="text-align:center;">
EX0004-EX0022-EX0028
</td>
</tr>
<tr>
<td style="text-align:center;">
3
</td>
<td style="text-align:center;">
EX0002-EX0012-EX0028
</td>
<td style="text-align:center;">
EX0003-EX0033
</td>
<td style="text-align:center;">
EX0032
</td>
</tr>
<tr>
<td style="text-align:center;">
4
</td>
<td style="text-align:center;">
EX0032
</td>
<td style="text-align:center;">
EX0004-EX0017-EX0024-EX0039
</td>
<td style="text-align:center;">
EX0002-EX0012-EX0033
</td>
</tr>
<tr>
<td style="text-align:center;">
5
</td>
<td style="text-align:center;">
EX0004-EX0017-EX0024-EX0039
</td>
<td style="text-align:center;">
EX0002-EX0012-EX0028
</td>
<td style="text-align:center;">
EX0003-EX0029-EX0038
</td>
</tr>
<tr>
<td style="text-align:center;">
6
</td>
<td style="text-align:center;">
EX0013
</td>
<td style="text-align:center;">
EX0001-EX0018-EX0027-EX0042
</td>
<td style="text-align:center;">
EX0017-EX0024-EX0039
</td>
</tr>
<tr>
<td style="text-align:center;">
7
</td>
<td style="text-align:center;">
EX0022-EX0029-EX0038
</td>
<td style="text-align:center;">
EX0013
</td>
<td style="text-align:center;">
EX0001-EX0018-EX0027-EX0042
</td>
</tr>
</tbody>
</table>
This table shows the maintenance opportunities during the three-day
routings:
<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
<thead>
<tr>
<th style="text-align:center;">
Routing
</th>
<th style="text-align:center;">
Day 1
</th>
<th style="text-align:center;">
Day 2
</th>
<th style="text-align:center;">
Day 3
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center;">
1
</td>
<td style="text-align:center;">
</td>
<td style="text-align:center;">
✓
</td>
<td style="text-align:center;">
</td>
</tr>
<tr>
<td style="text-align:center;">
2
</td>
<td style="text-align:center;">
</td>
<td style="text-align:center;">
✓
</td>
<td style="text-align:center;">
</td>
</tr>
<tr>
<td style="text-align:center;">
3
</td>
<td style="text-align:center;">
</td>
<td style="text-align:center;">
</td>
<td style="text-align:center;">
✓
</td>
</tr>
<tr>
<td style="text-align:center;">
4
</td>
<td style="text-align:center;">
✓
</td>
<td style="text-align:center;">
✓
</td>
<td style="text-align:center;">
</td>
</tr>
<tr>
<td style="text-align:center;">
5
</td>
<td style="text-align:center;">
✓
</td>
<td style="text-align:center;">
</td>
<td style="text-align:center;">
✓
</td>
</tr>
<tr>
<td style="text-align:center;">
6
</td>
<td style="text-align:center;">
</td>
<td style="text-align:center;">
</td>
<td style="text-align:center;">
✓
</td>
</tr>
<tr>
<td style="text-align:center;">
7
</td>
<td style="text-align:center;">
✓
</td>
<td style="text-align:center;">
</td>
<td style="text-align:center;">
</td>
</tr>
<tr>
<td style="text-align:center;">
Total
</td>
<td style="text-align:center;">
3
</td>
<td style="text-align:center;">
3
</td>
<td style="text-align:center;">
3
</td>
</tr>
</tbody>
</table>
The solution for A321 is:
<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
<thead>
<tr>
<th style="text-align:center;">
Routing
</th>
<th style="text-align:center;">
Day 1
</th>
<th style="text-align:center;">
Day 2
</th>
<th style="text-align:center;">
Day 3
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center;">
1
</td>
<td style="text-align:center;">
EX0008-EX0016-EX0034
</td>
<td style="text-align:center;">
EX0030
</td>
<td style="text-align:center;">
EX0009-EX0015
</td>
</tr>
<tr>
<td style="text-align:center;">
2
</td>
<td style="text-align:center;">
EX0023-EX0031
</td>
<td style="text-align:center;">
EX0006-EX0025-EX0036
</td>
<td style="text-align:center;">
EX0005-EX0011-EX0019
</td>
</tr>
<tr>
<td style="text-align:center;">
3
</td>
<td style="text-align:center;">
EX0021-EX0035
</td>
<td style="text-align:center;">
EX0014-EX0035
</td>
<td style="text-align:center;">
EX0021-EX0026
</td>
</tr>
<tr>
<td style="text-align:center;">
4
</td>
<td style="text-align:center;">
EX0007-EX0030-EX0040
</td>
<td style="text-align:center;">
EX0010-EX0020-EX0041
</td>
<td style="text-align:center;">
EX0007-EX0030
</td>
</tr>
<tr>
<td style="text-align:center;">
5
</td>
<td style="text-align:center;">
EX0006-EX0025-EX0036
</td>
<td style="text-align:center;">
EX0005-EX0011-EX0019
</td>
<td style="text-align:center;">
EX0023-EX0031
</td>
</tr>
<tr>
<td style="text-align:center;">
6
</td>
<td style="text-align:center;">
EX0037
</td>
<td style="text-align:center;">
EX0007-EX0037
</td>
<td style="text-align:center;">
EX0008-EX0016-EX0034
</td>
</tr>
<tr>
<td style="text-align:center;">
7
</td>
<td style="text-align:center;">
EX0014-EX0026
</td>
<td style="text-align:center;">
EX0021-EX0026
</td>
<td style="text-align:center;">
EX0014-EX0035
</td>
</tr>
<tr>
<td style="text-align:center;">
8
</td>
<td style="text-align:center;">
EX0005-EX0011-EX0019
</td>
<td style="text-align:center;">
EX0023-EX0034
</td>
<td style="text-align:center;">
EX0037
</td>
</tr>
<tr>
<td style="text-align:center;">
9
</td>
<td style="text-align:center;">
EX0010-EX0020-EX0041
</td>
<td style="text-align:center;">
EX0008-EX0016-EX0031
</td>
<td style="text-align:center;">
EX0006-EX0025-EX0036-EX0040
</td>
</tr>
<tr>
<td style="text-align:center;">
10
</td>
<td style="text-align:center;">
EX0009-EX0015
</td>
<td style="text-align:center;">
EX0009-EX0015-EX0040
</td>
<td style="text-align:center;">
EX0010-EX0020-EX0041
</td>
</tr>
</tbody>
</table>
And, this fleet has 18 maintenance opportunities:
<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
<thead>
<tr>
<th style="text-align:center;">
Routing
</th>
<th style="text-align:center;">
Day 1
</th>
<th style="text-align:center;">
Day 2
</th>
<th style="text-align:center;">
Day 3
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center;">
1
</td>
<td style="text-align:center;">
</td>
<td style="text-align:center;">
✓
</td>
<td style="text-align:center;">
✓
</td>
</tr>
<tr>
<td style="text-align:center;">
2
</td>
<td style="text-align:center;">
</td>
<td style="text-align:center;">
✓
</td>
<td style="text-align:center;">
</td>
</tr>
<tr>
<td style="text-align:center;">
3
</td>
<td style="text-align:center;">
✓
</td>
<td style="text-align:center;">
✓
</td>
<td style="text-align:center;">
✓
</td>
</tr>
<tr>
<td style="text-align:center;">
4
</td>
<td style="text-align:center;">
</td>
<td style="text-align:center;">
✓
</td>
<td style="text-align:center;">
✓
</td>
</tr>
<tr>
<td style="text-align:center;">
5
</td>
<td style="text-align:center;">
✓
</td>
<td style="text-align:center;">
</td>
<td style="text-align:center;">
</td>
</tr>
<tr>
<td style="text-align:center;">
6
</td>
<td style="text-align:center;">
✓
</td>
<td style="text-align:center;">
✓
</td>
<td style="text-align:center;">
</td>
</tr>
<tr>
<td style="text-align:center;">
7
</td>
<td style="text-align:center;">
✓
</td>
<td style="text-align:center;">
✓
</td>
<td style="text-align:center;">
✓
</td>
</tr>
<tr>
<td style="text-align:center;">
8
</td>
<td style="text-align:center;">
</td>
<td style="text-align:center;">
</td>
<td style="text-align:center;">
✓
</td>
</tr>
<tr>
<td style="text-align:center;">
9
</td>
<td style="text-align:center;">
✓
</td>
<td style="text-align:center;">
</td>
<td style="text-align:center;">
</td>
</tr>
<tr>
<td style="text-align:center;">
10
</td>
<td style="text-align:center;">
✓
</td>
<td style="text-align:center;">
</td>
<td style="text-align:center;">
✓
</td>
</tr>
<tr>
<td style="text-align:center;">
Total
</td>
<td style="text-align:center;">
6
</td>
<td style="text-align:center;">
6
</td>
<td style="text-align:center;">
6
</td>
</tr>
</tbody>
</table>
<!-- ## Crew scheduling -->
<!-- ```{r, include=FALSE} -->
<!-- source("crew_scheduling.R") -->
<!-- ``` -->
<!-- Once the aircrafts routings have been selected, a crew has to be assigned to every flight of the airlines. In order to do so, first must be determined every pairing between flight and crew: -->
<!-- - Create all possible one and two.day pairings -->
<!-- - Exclude all the pairings that do not meet the following: -->
<!--   - The pairings end up in JFK over the routing cycle -->
<!--   - For two-day pairings, the first flight of the second day starts at the city where it had ended up the night before. -->
<!--   - The duty does not exceed eight hours of flight time in any given day. -->
<!--   - The sit-connection times are between the allowable minimum and maximum times. -->
<!-- After considering the sit-connection times allowable between 20 and 180 minutes for B737-400 and 10 and 185 minutes for A321, the crew pairing solutions are: -->
<!-- ```{r, echo=FALSE} -->
<!-- source("mp_solver.R") -->
<!-- source("shorten_aircraft_name.R") -->
<!-- fleet_info[, Fleet_short := shorten_aircraft_name(Fleet), by = Fleet] -->
<!-- ind_r1 <- sol_pairings1[, .(day1, day2, total_flight_time)] -->
<!-- tb1 <- merge(ind_r1,one_day_routes1[,.(ind,`Day 1` = route)],by.x = "day1", by.y = "ind") -->
<!-- tb1 <- merge(tb1,one_day_routes1[,.(ind,`Day 2` = route)],by.x = "day2", by.y = "ind") -->
<!-- tb1[, Pairing := .I] -->
<!-- tb1 <- tb1[,.(Pairing, `Day 1`, `Day 2`, total_flight_time)] -->
<!-- tb1[, total_flight_time := as.integer(total_flight_time/3600)] -->
<!-- setnames(tb1, "total_flight_time","Flight hours") -->
<!-- cap1 <- paste(fleet_info[1,Fleet_short],"crew pairing solution") -->
<!-- kable(tb1, align = "c", caption = cap1) %>% -->
<!--   kable_styling(bootstrap_options = c("striped", "hover", "condensed"), -->
<!--                 full_width = FALSE, -->
<!--                 position = "center") -->
<!-- ind_r2 <- sol_pairings2[,.(day1, day2, total_flight_time)] -->
<!-- tb2 <- merge(ind_r2,one_day_routes2[,.(ind,`Day 1` = route)],by.x = "day1", by.y = "ind") -->
<!-- tb2 <- merge(tb2,one_day_routes2[,.(ind,`Day 2` = route)],by.x = "day2", by.y = "ind") -->
<!-- tb2[, Pairing := .I] -->
<!-- tb2 <- tb2[,.(Pairing, `Day 1`, `Day 2`, total_flight_time)] -->
<!-- tb2[, total_flight_time := as.integer(total_flight_time/3600)] -->
<!-- setnames(tb2, "total_flight_time","Flight hours") -->
<!-- cap2 <- paste(fleet_info[2,Fleet_short],"crew pairing solution") -->
<!-- kable(tb2, align = "c", caption = cap2) %>% -->
<!--   kable_styling(bootstrap_options = c("striped", "hover", "condensed"), -->
<!--                 full_width = FALSE, -->
<!--                 position = "center") -->
<!-- ``` -->
<!-- In order to balance the workload among all rosters, we have considered the mean for all valid rosters. This is 17 hours for B737-400 and 17 hours for A321. -->
<!-- ```{r, include=FALSE} -->
<!-- routes_comb <- data.table() -->
<!-- routes_comb$Monday <- as.character(c(1,1,0,0,0,4,4)) -->
<!-- routes_comb$Tuesday <- as.character(c(2,2,1,1,0,0,0)) -->
<!-- routes_comb$Wednesday <- as.character(c(0,0,2,2,1,1,0)) -->
<!-- routes_comb$Thursday <- as.character(c(3,0,0,0,2,2,1)) -->
<!-- routes_comb$Friday <- as.character(c(4,3,3,0,0,0,2)) -->
<!-- routes_comb$Saturday <- as.character(c(0,4,4,3,3,0,0)) -->
<!-- routes_comb$Sunday <- as.character(c(0,0,0,4,4,3,3)) -->
<!-- routes_comb$ind <- 1:nrow(possible_routes_comb) -->
<!-- sol_5 <- rosters1[ind %in% solution3$vars[value == 1, i1], .(r1,r2,W,flight_time)] -->
<!-- sol_5 <- merge(sol_5, routes_comb, by.x = "W", by.y = "ind") -->
<!-- sol_5[, Schedule := .I, by = .I] -->
<!-- final1 <- merge(sol_5, sol_pairings1[,.(day1,day2,ind)], by.x = "r1", by.y = "ind") -->
<!-- final1 <- merge(final1, sol_pairings1[,.(day3 = day1, day4 = day2,ind)], by.x = "r2", by.y = "ind") -->
<!-- final1 <- merge(final1,one_day_routes1[,.(ind, route1 = route)],by.x = "day1", by.y = "ind") -->
<!-- final1 <- merge(final1,one_day_routes1[,.(ind, route2 = route)],by.x = "day2", by.y = "ind") -->
<!-- final1 <- merge(final1,one_day_routes1[,.(ind, route3 = route)],by.x = "day3", by.y = "ind") -->
<!-- final1 <- merge(final1,one_day_routes1[,.(ind, route4 = route)],by.x = "day4", by.y = "ind") -->
<!-- final1[Monday == "1", Monday := route1] -->
<!-- final1[Monday == "2", Monday := route2] -->
<!-- final1[Monday == "3", Monday := route3] -->
<!-- final1[Monday == "4", Monday := route4] -->
<!-- final1[Monday == "0", Monday := "\u2013"] -->
<!-- final1[Tuesday == "1", Tuesday := route1] -->
<!-- final1[Tuesday == "2", Tuesday := route2] -->
<!-- final1[Tuesday == "3", Tuesday := route3] -->
<!-- final1[Tuesday == "4", Tuesday := route4] -->
<!-- final1[Tuesday == "0", Tuesday := "\u2013"] -->
<!-- final1[Wednesday == "1", Wednesday := route1] -->
<!-- final1[Wednesday == "2", Wednesday := route2] -->
<!-- final1[Wednesday == "3", Wednesday := route3] -->
<!-- final1[Wednesday == "4", Wednesday := route4] -->
<!-- final1[Wednesday == "0", Wednesday := "\u2013"] -->
<!-- final1[Thursday == "1", Thursday := route1] -->
<!-- final1[Thursday == "2", Thursday := route2] -->
<!-- final1[Thursday == "3", Thursday := route3] -->
<!-- final1[Thursday == "4", Thursday := route4] -->
<!-- final1[Thursday == "0", Thursday := "\u2013"] -->
<!-- final1[Friday == "1", Friday := route1] -->
<!-- final1[Friday == "2", Friday := route2] -->
<!-- final1[Friday == "3", Friday := route3] -->
<!-- final1[Friday == "4", Friday := route4] -->
<!-- final1[Friday == "0", Friday := "\u2013"] -->
<!-- final1[Saturday == "1", Saturday := route1] -->
<!-- final1[Saturday == "2", Saturday := route2] -->
<!-- final1[Saturday == "3", Saturday := route3] -->
<!-- final1[Saturday == "4", Saturday := route4] -->
<!-- final1[Saturday == "0", Saturday := "\u2013"] -->
<!-- final1[Sunday == "1", Sunday := route1] -->
<!-- final1[Sunday == "2", Sunday := route2] -->
<!-- final1[Sunday == "3", Sunday := route3] -->
<!-- final1[Sunday == "4", Sunday := route4] -->
<!-- final1[Sunday == "0", Sunday := "\u2013"] -->
<!-- final1 <- final1[, `Flight hours` := round(as.numeric(flight_time))] -->
<!-- final1 <- final1[, .(Schedule, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, `Flight hours`)][order(Schedule)] -->
<!-- ``` -->
<!-- ```{r, echo=FALSE} -->
<!-- cap5 <- paste(fleet_info[1,Fleet_short],"crew scheduling solution") -->
<!-- kable(final1, align = "c", caption = cap5) %>% -->
<!--   kable_styling(bootstrap_options = c("striped", "hover", "condensed"), -->
<!--                 full_width = FALSE, -->
<!--                 position = "center") -->
<!-- ``` -->
<!-- <div class = "tocify-extend-page" data-unique = "tocify-extend-page" style = "height: 0;"></div> -->
