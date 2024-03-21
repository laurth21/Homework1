from functions import parallelResistor, serialResistor, current, DcPower


def test_serialResistor():
    assert serialResistor(2,4)==6
    assert serialResistor(0, 1) == 1
    assert serialResistor(1, -5) == "Negative value for resistor"
    assert serialResistor(2.55, 3.45) == 6


def test_parallelResistor():
    assert parallelResistor(1, 1) == 0.5
    assert parallelResistor(0, 3) == 0
    assert parallelResistor(2, -2) == "Negative value for resistor"
    assert parallelResistor(0, 0) == "Can't divide by zero"


def test_current():
    assert current(2, 3) == 3 / 2
    assert current(0, 2) == "Can't divide by zero or negative value for R"
    assert current(3, 0) == 0


def test_DcPower():
    assert DcPower(1, 5, 1) == 25
    assert DcPower(1, 0, 1) == 0
    assert DcPower(-1, 4, 1) == "Negative value for R"
    assert DcPower(2, 2, 0) == 2
    assert DcPower(1, 0, 0) == 0
    assert DcPower(0, 2, 0) == "Can't divide by zero or negative value for R"
    assert DcPower(-1, 4, 0) == "Can't divide by zero or negative value for R"
    assert DcPower(1, 1, 2) == "Wrong value for the UorI input"
    assert DcPower(0, 0, -1) == "Wrong value for the UorI input"
