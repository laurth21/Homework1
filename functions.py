def serialResistor(R1,R2):
    """Calculating the overall resistor value of two resistors R1 and R2 in serial by adding their values"""
    return (R1+R2)

def parallelResistor(R1,R2):
    """Calculating the overall resistor value of two resistors R1 and R2 in parallel by multiplying their values and dividing them by their sum"""
    return (R1*R2/(R1+R2))

def current(R,U):
    """Calculating the current throw a resistor by using the Ohm's law"""
    return U/R

def DcPower(R,UI,UorI):
    """Calculating the power by a resistor using the voltage or current throw the resistor"""
    if UorI == 0:
        """0 for using voltage U"""
        return UI**2/R
    elif UorI == 1:
        """1 for using current I"""
        return R*I**2
    else:
        return "Wrong value for the UorI input"
