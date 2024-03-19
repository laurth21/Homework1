def serialResistor(R1,R2):
    return (R1+R2)

def parallelResistor(R1,R2):
    return (R1*R2/(R1+R2))

def current(R,U):
    return U/R
