from src.radpkg import radian
import sys

def main():
   degree = (sys.argv[1])
   result = radian.rad(degree)
   print(result)