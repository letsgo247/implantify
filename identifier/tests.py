from django.test import TestCase

# Create your tests here.

with open('../models/classes.txt','r') as f:
    labelInfo = f.read()

print(labelInfo)