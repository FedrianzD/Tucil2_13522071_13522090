import matplotlib.pyplot as plt
import function
point1 = (0,0)
point2 = (3,3)
point3 = (6,0)
point4 = (5,0)
point5 = (5,5)
arr = [point1,point2,point3,point4, point5]
# jaw = function.bejir(point1, point2, point3, 1, 2)
# print(len(sol))
# sol2 = function.bejirBrute(point1, point2, point3, 1)
sol2 = function.bejir2(arr, 1, 2)
sol3 = function.bejir3(arr, 1, 2)
# print(jaw[0])
# print(jaw[1])
print(sol2[0])
print()
print(sol2[1])
print(sol3)

# print(function.mid((4,1.125), (5.125,1)))

# if __name__ == "__main__":
#     point1 = (1,0)
#     point2 = (3,4)
#     point3 = (5,0)
#     sol = []
#     sol = bejir(point1, point2, point3, 1, 3)
#     print(sol)
#     plt.plot([point[0] for point in sol], [point[1] for point in sol], 'ro-')
#     plt.plot([point[0] for point in sol], [point[1] for point in sol], 'b-', label='Kurva Graf Bezier dengan Algoritma Titik Tengah')
#     plt.plot(point1[0], point1[1], 'go')
#     plt.plot(point2[0], point2[1], 'go')
#     plt.plot(point3[0], point3[1], 'go')
#     plt.plot([1, 3], [0, 4], 'r-')
#     plt.plot([3, 5], [4, 0], 'r')
#     plt.title('Kurva Graf Bezier dengan Algoritma Titik Tengah')
#     plt.legend()
#     plt.show()