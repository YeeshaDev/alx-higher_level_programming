#!/usr/bin/python3
BaseGeometry = __import__('6-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Statu
