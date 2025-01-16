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

We developed a preliminary schedule for the next quarter. The complete route, which includes 42 flights per day, is presented in the following table. All departure and arrival times are local.