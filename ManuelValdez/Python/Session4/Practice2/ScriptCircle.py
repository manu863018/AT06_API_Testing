from CircleArea import calculateCircleArea
from CirclePerimeter import calculateCirclePerimeter


radius = int(input("insert circle radius: "))
print("circle with radius", radius, ",has an area of:", calculateCircleArea(radius))
print("circle with radius", radius, ",has a perimiter of:", calculateCirclePerimeter(radius))