grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
b_Johnny = sum(grades[2]) / len(grades[2])
b_Bilbo = sum(grades[1]) / len(grades[1])
b_Steve = sum(grades[4]) / len(grades[4])
b_Khendrik = sum(grades[3]) / len(grades[3])
b_Aaron = sum(grades[0]) / len(grades[0])
average_rating = {'Aaron': b_Aaron, 'Bilbo': b_Bilbo, 'Johnny': b_Johnny, 'Khendrik': b_Khendrik, 'Steve': b_Steve}
print(average_rating)
