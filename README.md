## Astrodynamics Simulator

A python based astrodynamics project for learning and implementing orbital mechanics, numerical propagation, and trajectory shaping and analysis.

The project currently focuses on two-body earth propagation and visualization, with the long-term goal of expanding toward interplanetary and small-body analyses.

## Current Features

- Two-body orbital propagation using 'scipy.integrate.solve_ivp'
- Elliptical initial orbit condition (Periapsis radius, eccentricity, and inclination)
- Semi-3D earth and orbit plotting using 'matplotlib'
- Animated spacecraft orbit along the plotted trajectory using 'matplotlib.animation'

## Project Structure
```text
├── src/
│   └── astrosim/
│       ├── constants.py
│       ├── dynamics.py
│       ├── elements.py
│       ├── propagator.py
│       └── plotting.py
│
├── examples/
│   └── two_body_orbit.py
│
├── tests/
├── pyproject.toml
└── README.md
```