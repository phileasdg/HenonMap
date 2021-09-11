import matplotlib.pyplot as plt


# Henon map plotter:
def find_next_point(x, y):
    # x, y = starting coordinates
    new_x = y + 1 - 1.4 * x ** 2
    new_y = 0.3 * x
    return new_x, new_y


def find_points_for_n_iterations(x, y, n):
    x_coord_list = []
    y_coord_list = []
    for i in range(n):
        x, y = find_next_point(x, y)
        x_coord_list.append(x)
        y_coord_list.append(y)
    return x_coord_list, y_coord_list


henon_x_coordinates, henon_y_coordinates = find_points_for_n_iterations(1, 1, 100000)
# print(henon_x_coordinates, henon_y_coordinates)

plt.scatter(henon_x_coordinates, henon_y_coordinates, s=.5)
plt.show()
