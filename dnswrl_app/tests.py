from django.test import TestCase

# Create your tests here.

disease_posible_set = {}
disease_posible_set['感冒0'] = 5
disease_posible_set['感冒1'] = 3
disease_posible_set['感冒2'] = 2
disease_posible_set['感冒3'] = 9
disease_posible_set['感冒4'] = 5
disease_posible_set['感冒5'] = 1

l = sorted(disease_posible_set.items(), key=lambda disease_posible_set:disease_posible_set[1])
print(l[-1][0])

disease_posible_set2 = {}
if len(disease_posible_set2) == 0:
    print('NONE')
else:
    print('Not None')