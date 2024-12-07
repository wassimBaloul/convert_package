from convert import celsius_to_fahrenheit, meters_to_feet, kg_to_pounds

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40

def test_meters_to_feet():
    assert round(meters_to_feet(1), 2) == 3.28
    assert round(meters_to_feet(10), 2) == 32.81

def test_kg_to_pounds():
    assert round(kg_to_pounds(1), 2) == 2.2
    assert round(kg_to_pounds(10), 2) == 22.05

if __name__ == "__main__":
    test_celsius_to_fahrenheit()
    test_meters_to_feet()
    test_kg_to_pounds()
    print("All tests passed!")