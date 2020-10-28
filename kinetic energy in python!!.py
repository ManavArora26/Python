Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("This program calculates the kinetic energy of a moving object.")
This program calculates the kinetic energy of a moving object.
>>> m_string = input("Enter the object's mass in kilograms: ")
Enter the object's mass in kilograms: 23
>>> m = float(m_string)
>>> v_string = input("Enter the object's speed in meters per second: ")
Enter the object's speed in meters per second: 344
>>> v = float(v_string)
>>> e = 0.5 * m * v * v
>>> print("The object has " + str(e) + " joules of energy.")
The object has 1360864.0 joules of energy.
>>> 