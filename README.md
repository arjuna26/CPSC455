# About
Final project from Gonzaga's Chaos &amp; Dynamical Systems course, Spring 2024

The full research paper can be found in this repository, look for &rarr; 'Tent Map Research Paper.pdf'

## Tent Map Analysis
The tent map is defined as:

![tentmapfunction](https://github.com/arjuna26/CPSC455/assets/97765080/1f5e115e-86dd-4906-8276-2fe8332a6931)

And looks like:

![Tent_map_2](https://github.com/arjuna26/CPSC455/assets/97765080/d753919b-f09e-400f-991a-cf70a6ba41c5)

In this project, Python and specifically the numpy &amp; matplotlib Python libraries were utilized to provide calculations and graph visualizations to assist in the analysis of chaotic behavior over the tent map.
In order to observe the tent map's behavior, a series of graphs were generated:
* Cobweb/Orbit diagrams &rarr; cobweb.py
* Time Series Plots &rarr; timeseries.py
* Bifurcation Diagram &rarr; bifurcation.py
* Frequency Histograms &rarr; histogram.py
* Lyapunov Exponent Diagram &rarr; lyapunov.py

In summary, the results from the above .py files revealed a pattern of the chaotic behavior of the tent map. When manipulating the "a" parameter, it was found that for $1.4 < a < 2$, the tent map enters it's chaotic regime as you will see in the diagrams below.

## Diagrams

### Cobweb Diagrams: $a = 1.6, a = 1.4$

![x03a1 6](https://github.com/arjuna26/CPSC455/assets/97765080/7c582df8-5515-4d35-b0e4-c83116abb61a)

![x07a1 4](https://github.com/arjuna26/CPSC455/assets/97765080/102b38aa-a3a3-4fd3-b946-aea9d1f39c6e)

### Time Series Plot: $a = 1.6$

![x03a1 6](https://github.com/arjuna26/CPSC455/assets/97765080/523ee24b-4469-47e4-9d18-a53d679758c4)

### Frequency Histograms: $a = 1.6$

![a1 6x08](https://github.com/arjuna26/CPSC455/assets/97765080/5322cd4c-083f-4b47-ba68-28af47b267fb)

### Lyapunov Diagram

![lyapunov diagram](https://github.com/arjuna26/CPSC455/assets/97765080/651e59e5-9890-4f59-904f-f1486bacd307)

### Bifurcation Diagram

![bifurcation_diagram](https://github.com/arjuna26/CPSC455/assets/97765080/e4a71ad8-a065-4491-89f9-3203777bb6ef)



