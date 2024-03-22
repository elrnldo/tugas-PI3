class Person:
  """
  This class represents a person with height and weight properties,
  methods to calculate BMI and compare equality, and overrides the equals method.
  """

  def __init__(bmi, weight, height):
    """
    Initializes a new Person object with the given weight and height.

    Args:
      weight: The weight of the person in kilograms (float).
      height: The height of the person in meters (float).
    """
    bmi.weight = weight
    bmi.height = height

  def BMI_Value(bmi):
    """
    Calculates and returns the BMI of the person.

    Returns:
      The BMI of the person as a decimal value.
    """
    if bmi.height == 0:
      return 0  # Avoid division by zero
    return bmi.weight / (bmi.height * bmi.height)

  def __eq__(bmi, other):
    """
    Overrides the default equality comparison to compare weight and height.

    Args:
      other: Another Person object to compare with.

    Returns:
      True if the weight and height of both objects are equal, False otherwise.
    """
    if not isinstance(other, Person):
      return False  # Only compare with Person objects
    return bmi.weight == other.weight and bmi.height == other.height

# Example usage
person1 = Person(float(input("Enter the weight in Kilogram : ")), float(input("Enter the height in meter: ")))
person2 = Person(float(input("Enter the weight in Kilogram : ")), float(input("Enter the height in meter: ")))

# Compare BMI values (not recommended)
bmi1 = person1.BMI_Value()
bmi2 = person2.BMI_Value()

if bmi1 == bmi2:  # Not ideal due to floating-point precision issues
  print("Person 1 and Person 2 have the same BMI (Compared using BMI_Value).")
else:
  print("Peerson 1 and Person 2 have different BMI(Compared using BMI_Value)")

# Compare Person objects using the overridden __eq__ method
if person1 == person2:
  print("Person 1 and Person 2 are equal (using __eq__).")
else:
  print("Person 1 and Person 2 are not equal.")

