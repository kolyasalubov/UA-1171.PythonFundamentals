def distance(x1, y1, x2, y2):
    return round(((pow((x2-x1),2)+pow((y2-y1),2))**0.5),2)

print(distance(1,1,0,0))