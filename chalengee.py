# Soal 1
""" Buat sebuah program yang jika kita berikan sebuah input array seperti
 [1,2,3,4,5] maka akan menghasilkan output [1,4,9,16,25]!
 """

 # Input array
# input_array = [1, 2, 3, 4, 5] 
#     # Menggunakan list comprehension untuk menghasilkan output
# output_array = [x**2 for x in input_array]
# print(output_array) 

# Soal 2
"""Buat sebuah program dimana jika input yang diberikan adalah 
[1,2,3,4,5] maka outputnya adalah [“ganjil”,”genap”,”ganjil”,”genap”,”ganjil”]
"""
# Input array
# input_array = [1, 2, 3, 4, 5]

# # Menggunakan list comprehension untuk menghasilkan output
"""cara 1"""
# output_array = ["ganjil"if  x%2 != 0 else  "genap" for x in input_array]
# print(output_array)

"""cara 2"""
# def GanjilGenap(input_array):
#     hasil = []

#     for x in input_array:
#         if x % 2 == 0:
#          hasil.append("genap")
#     else:
#          hasil.append("ganjil")

#     return hasil

# input_array = [1,2,3,4,5]
# print(input_array)
# outputArray = GanjilGenap(input_array)
# print(outputArray)
# Soal 3
"""
Buat sebuah program dimana jika input yang diberikan adalah 
[[1,2,3],[2,3,4],[3,4,5]] maka outputnya adalah [6,9,12]!
"""
"""cara 1"""
# input_array  = [[1,2,3],[2,3,4],[3,4,5]]
# output_array = [sum(x)for x in input_array]

# print(output_array)

"""cara 2"""

# input_array  = [[1,2,3],[2,3,4],[3,4,5]]
# output_array = []
# for x in input_array:
#     output_array.append(x[0] * x[1] + x[2])

# print(output_array)

# soal 4
input_array = [[0, 1, 2, 4], [0, 4, 2, 3], [0, 101, 200, 99]]
output_array = []
for x in input_array:
    max_value = max(x)
    max_index = x.index(max_value)
    output_array.append(max_index)

print(output_array)
