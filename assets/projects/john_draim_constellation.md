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
    text-align: center;
  }

  /* Optional: style for the highlighted row */
  tr:hover {
    background-color: #f9f9f9; /* Light hover effect */
  }
</style>

# Analysing John Draim's Satellite Constellation

## Introduction
In the 1980s, John Draim proposed a ground-breaking satellite constellation design using just four satellites to achieve full global coverage. This design, based on a perturbed tetrahedral configuration, offers substantial economic advantages and a wide range of applications, including communications, Earth observation, and meteorology.

This project focuses on analysing Draim's constellation over a two-day period. Key tasks include calculating orbital parameters, converting coordinate systems, and visualizing the results.

## Objective
The primary goal is to:
- Compute the orbital parameters for the constellation.
- Transform satellite positions between coordinate systems.
- Visualize the satellite ground tracks and assess coverage.

## Input Data

The constellation is modeled as a modified tetrahedron with the following orbital parameters:

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
  <thead>
    <tr>
      <th>Satellite</th>
      <th>Inclination</th>
      <th>Orbital Period (h)</th>
      <th>Eccentricity (e)</th>
      <th>Argument of Perigee (ω)</th>
      <th>RAAN (Ω)</th>
      <th>Mean Anomaly (M₀)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>S1</td>
      <td>31.3°</td>
      <td>26.49</td>
      <td>0.263</td>
      <td>-90°</td>
      <td>0°</td>
      <td>0°</td>
    </tr>
    <tr>
      <td>S2</td>
      <td>31.3°</td>
      <td>26.49</td>
      <td>0.263</td>
      <td>90°</td>
      <td>90°</td>
      <td>270°</td>
    </tr>
    <tr>
      <td>S3</td>
      <td>31.3°</td>
      <td>26.49</td>
      <td>0.263</td>
      <td>-90°</td>
      <td>180°</td>
      <td>180°</td>
    </tr>
    <tr>
      <td>S4</td>
      <td>31.3°</td>
      <td>26.49</td>
      <td>0.263</td>
      <td>90°</td>
      <td>270°</td>
      <td>90°</td>
    </tr>
  </tbody>
</table>


A file, `SATPT.txt`, contains satellite position and velocity data over one year at 600-second intervals.

## Geocentric Satellite coordinates
Satellite coordinates in the Earth-Centered Earth-Fixed (ECEF) system were transformed to spherical geocentric coordinates (r, λ, ϕ) using MATLAB’s `cart2sph` function. The geocentric distance was plotted as a function of time, revealing periodic sinusoidal behaviour.

## Satellite Ground Tracks
The spherical coordinates were used to plot ground tracks over the Earth’s surface in the geocentric Terrestrial Reference Frame (TRF). The analysis showed periodic patterns consistent with orbital parameters.


<div style="display: flex; justify-content: center; align-items: center;">
    <video controls width="640" height="360">
      <source src="../images/john_draim_constellation/ground_track_video.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
</div>

## Coverage  
A latitude-longitude grid was created to determine the coverage provided by the satellites at each grid point. Coverage was assessed based on satellite elevation angles exceeding 5°. The study period revealed that most regions were covered by 1–2 satellites at any given time, with minimal instances of no coverage.

<div style="display: flex; justify-content: center; align-items: center;">
    <video controls width="640" height="360">
      <source src="../images/john_draim_constellation/coverage_video.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
</div>

## Coordinate Transformation to Celestial Reference Frame (CRF)  
Satellite positions were transformed from TRF to CRF using the Greenwich Mean Sidereal Time. This inertial system provided a stable frame for visualizing orbits.

## Tetrahedron Visualization 
The modified tetrahedral configuration was visualized over a full constellation period. As expected, the satellite positions formed non-equilateral triangles due to the perturbed tetrahedron setup.

## Conclusion

John Draim's four-satellite constellation achieves near-complete global coverage with minimal satellite redundancy. This study validates the feasibility of the design through numerical analysis and visualizations. The results highlight the potential of optimized constellations for various practical applications.


## References

- Draim, J. "Four-Satellite Full Earth Coverage Constellations," [Publication Details].
- MATLAB documentation for coordinate transformations.


