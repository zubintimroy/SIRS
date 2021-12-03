# The SIR Model
This is a python project that produces a SIR Model simulation for visualisation or output measurement. Cells are either Susceptible (S),Infected (I), Recovered (R) or Immune (Im).

Rules:
1. S -> I with probability p1 if at least one nearest neighbour is I, otherwise remains S
2. I -> R with probability p2
3. R -> S with probability p3
4. Immune cells remain immune

Requires p1,p2,p3 and fraction of immune cells as input in the main.py.
