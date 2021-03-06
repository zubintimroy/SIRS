# The SIRS Model
This is a python project that produces a SIRS Model simulation for visualisation using matplotlib or output measurement. Cells are either Susceptible (S),Infected (I), Recovered (R) or Immune (Im).

Rules:
1. S -> I with probability p1 if at least one nearest neighbour is I, otherwise remains S
2. I -> R with probability p2
3. R -> S with probability p3
4. Immune cells remain immune (i.e in the R state)

Requires p1,p2,p3 and fraction of immune cells as input in the main.py.

## Setup Python Virtual Environment and Install Packages
- ``` python -m pip install -U pip ```
- ``` pip install virtualenv ```
- ``` python -m venv env ```
- ``` pip install -r requirements.txt ```

## Activate Virtual Environment and Running the Script
- ``` .\env\Scripts\activate ```
- ``` python main.py Mode Size of Lattice p1 p2 p3 fraction of immune ```

## Outputs
Example output.txt files and python scripts using matplotlib to visualize the data include:

### No immunity
- Heatmap of average infected fraction and variance of infected sites for p1 against p3 with  ``` p2 = 0.5  ```
- Plot of variance of infected sites for p1 with  ``` p2 = p3 = 0.5  ``` with error bars

### With Immunity
- Average infected fraction of sites as a function of the immune fraction with error bars

