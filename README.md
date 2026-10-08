# Transmission-Loss
A small Python project that models power loss during electricity transmission and visualizes how voltage and transmission distance affect the amount of power lost as heat.
What This Project Does

This project uses simplified electrical equations to calculate:
- Current based on delivered power and voltage
- Total resistance based on conductor resistance per kilometer and transmission distance
Power lost as heat
It then uses Matplotlib to visualize how power loss changes under different transmission conditions.

## Model
This model uses functions to demonstrate the relationship between voltage, distance, resistance, and transmission loss. Real-world power transmission systems involve additional electrical factors that are not included here.

## Experiments
1. Power Loss vs. Voltage
The first experiment keeps the transmission distance, conductor resistance, and delivered power constant while testing several different transmission voltages. The goal is to observe how increasing transmission voltage affects power loss.

2. Power Loss vs. Distance
The second experiment tests several transmission distances at different voltages. The goal is to compare how increasing transmission distance affects power loss and how higher transmission voltages change that relationship.

## Files
physics.py
Contains the functions used for the calculations:
- current_amps() — calculates current from power and voltage
- t_resistance() — calculates total resistance from resistance per kilometer and distance
- p_loss() — calculates power lost as heat
## main.py
Runs the experiments and creates the graphs using Matplotlib.
## Tools Used
- Python
- Matplotlib

## What I Learned
- Writing and organizing Python functions
- Importing functions between Python files
- Using loops to test multiple values
- Working with physical equations in code
- Storing calculated results in lists
- Creating graphs with Matplotlib
- Comparing how changing one variable affects a system's behavior
- Using computational modeling to explore a real-world system


Note: This project is a simplified educational model and is not intended to represent the complete behavior of a real electrical transmission system.
