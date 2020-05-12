import numpy as np
data_type =[('name','S15'),('class','int'),('height',float)]
students_details=[('Jame',5,48.5),('Nail',6,52.5),('Paul',5,42.10),('Pit',5,40.1)]
# create a structured array
students=np.array(students_details, dtype=data_type)
print('Original array: ')
print(students)
print(" Sort by height ")
print(np.sort(students, order='height'))
