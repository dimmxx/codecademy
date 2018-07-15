class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!

class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
      self.hours = hours
      return hours * 12
  def full_time_wage(self, hours):
    self.hours = hours
    return super(PartTimeEmployee, self).calculate_wage(hours)



first = Employee("dick")
second = PartTimeEmployee("steve")
milton = PartTimeEmployee("Milton")

print first.calculate_wage(10)
print second.calculate_wage(10)
print milton.full_time_wage(10)


