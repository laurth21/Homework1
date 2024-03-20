def serialResistor(R1,R2):
    """Calculating the overall resistor value of two resistors R1 and R2 in serial by adding their values"""
    if R1 < 0 or R2 < 0:
        return "Negative value for resistor"
    else: return (R1+R2)

def parallelResistor(R1,R2):
    """Calculating the overall resistor value of two resistors R1 and R2 in parallel by multiplying their values and dividing them by their sum"""
    if R1 == 0 and R2 == 0:
        return "Can't divide by zero"
    elif R1 < 0 or R2 < 0:
        return "Negative value for resistor"
    else:
        return (R1*R2/(R1+R2))

def current(R,U):
    """Calculating the current throw a resistor by using the Ohm's law"""
    if R <= 0:
        return "Can't divide by zero or negative value for R"
    else:
        return U/R

def DcPower(R,UI,UorI):
    """Calculating the power by a resistor using the voltage or current throw the resistor"""
    if UorI == 0:
        # 0 for using voltage U
        if R <= 0:
            return "Can't divide by zero or negative value for R"
        else:
            return UI**2/R
    elif UorI == 1:
        #1 for using current I
        return R*I**2
    else:
        #when the input for UorI isn't 0 or 1 -> return an error message
        return "Wrong value for the UorI input"