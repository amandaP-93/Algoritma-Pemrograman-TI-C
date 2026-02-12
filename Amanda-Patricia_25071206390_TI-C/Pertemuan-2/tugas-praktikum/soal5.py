import math

def jarak(x1, y1, x2, y2):
    hasil = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return hasil

print("Jarak =", jarak(1, 2, 4, 6))
