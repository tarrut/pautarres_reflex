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