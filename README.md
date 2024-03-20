# Homework 1
[![license](https://img.shields.io/badge/license-Apache%202.0-black)](https://github.com/laurth21/Homework1/blob/main/LICENSE)

Copyright 2024 Thoeni Laurenz 

This is the repository of the first homework for the Open Source Energy Modeling course of Laurenz Thoeni
The scope of this project was to understand and learn the fundamental principles of using GitHub and Gitkraken. 
This was done by trying to code a little pyton program and using commit, push and pull. An additional pyton 
program should test the functions to make sure all implemented functions work properly.   

## Description of the Pyton Program
In the pyton program **functions.py** there are four functions: 

1. `serialResistor(R1,R2)`: calculates the total resistance of two resistors in series with $R_{total} = R_1 + R_2$

2. `parallelResistor(R1,R2)`: calculates the total resistance of two resistors in parallel with $R_{total} = \frac{R_1 \cdot R_2}{R_1+R_2}$
3. `current(R,U)`: calculates the current throw a resistor $R$ with an applied voltage $U$ with $I = \frac{U}{R}$
4. `DcPower(R,UI,UorI)`: can determine the  power dissipation of the resistor $R$ with the current $I$ throw the 
resistor or voltage $U$. For using $U$ the parameter **UorI** need to be set to 0 and the formula $P = \frac{U^2}{R}$ is used and by setting it to 1 $I$ is used with $P = I^2 \cdot R$. 

The second pyton program **test_functions.py** tests the four functions as mentioned in the beginning of this description.
