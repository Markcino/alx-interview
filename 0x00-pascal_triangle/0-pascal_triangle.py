def print_triangle(triangle):
  n = len(triangle)
  if n <= 0:
    return []
  triangle = [[1]]
  for i in range(1,n):
    triangle.append([1])
    for j in range(1, i):
      triangle[i].append(1)
    return triangle
