import numpy as np

integers = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f"integers: {integers}")

odds = integers[integers % 2 == 1]
print(f'odds: {odds}')

new_odds = np.where(integers % 2 == 1, -1, integers)
print(f'new_odds: {new_odds}')

integer_two_rows = integers.reshape(2, -1)
print(f'integer_two_rows: {integer_two_rows}')

integer_two_columns = integers.reshape(-1, 2)
print(f'integer_two_columns: {integer_two_columns}')

a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
concatenated_vertical = np.concatenate([a, b], axis=0)
print(f'vertical: {concatenated_vertical}')

concatenated_horizontal = np.concatenate([a, b], axis=1)
print(f'horizontal: {concatenated_horizontal}')

arr = np.random.random((5, 3))
media = np.mean(arr)
mediana = np.median(arr)
desviacion = np.std(arr)
print(f'media: {media} mediana: {mediana} desviacion: {desviacion}')

rand_arr = np.random.random((5, 3))
rand_three_decimal = np.around(rand_arr, decimals=3)
print(f'three_decimal: {rand_three_decimal}')

