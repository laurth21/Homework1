# Homework 1
[![license](https://img.shields.io/badge/license-Apache%202.0-black)](https://github.com/laurth21/Homework1/blob/main/LICENSE)

This is the repository of the first homework for the Open Source Energy Modeling course of Laurenz Thoeni
The scope of this project was to understand and learn the fundamental principles of using GitHub and Gitkraken. 
This was done by trying to code a little python program and using commit, push and pull. An additional python 
program should test the functions to make sure all implemented functions work properly.   

## Description of the Python Programs
In the python program [functions.py](/functions.py) there are four functions: 

1. `serialResistor(R1,R2)`: calculates the total resistance of two resistors in series with $R_{total} = R_1 + R_2$
2. `parallelResistor(R1,R2)`: calculates the total resistance of two resistors in parallel with $R_{total} = \frac{R_1 \cdot R_2}{R_1+R_2}$
3. `current(R,U)`: calculates the current throw a resistor $R$ with an applied voltage $U$ with $I = \frac{U}{R}$
4. `DcPower(R,UI,UorI)`: can determine the  power dissipation of the resistor $R$ with the current $I$ throw the 
resistor or voltage $U$. For using $U$ the parameter **UorI** need to be set to 0 and the formula $P = \frac{U^2}{R}$ is used and by setting it to 1 $I$ is used with $P = I^2 \cdot R$. 

The second python program [test_functions.py](/test_functions.py) tests the four functions as mentioned in the beginning of this description.

## Additional Information 
On all python files a ruff run was made to ensure that the code meets the coding style and a new directory .github/workflows was added with two yml-files. 
The first one [run_ruff.yml](.github/workflows/ruff_run.yml) ensures that new added files to this repository meet the coding style. The second one [run_test_on_GitHub.yml](.github/workflows/run_test_on_GitHub.yml) runs the test of the functions on GitHub. 

_Copyright 2024 Thoeni Laurenz_ 
