import math

def calculaDistancia(x1, y1, x2, y2) :
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    return math.sqrt(math.pow(x,2)+math.pow(y,2))

routes = []


def find_paths(node, cities, path, distance):
    # Add way point
    path.append(node)

    # Calculate path length from current to last node
    if len(path) > 1:
        distance += cities[path[-2]][node]

    # If path contains all cities and is not a dead end,
    # add path from last to first city and return.
    if (len(cities) == len(path)) and (path[0] in cities[path[-1]]):
        global routes
        path.append(path[0])
        distance += cities[path[-2]][path[0]]
        print (path, distance)
        routes.append([distance, path])
        return

    # Fork paths for all possible cities not yet used
    for city in cities:
        if (city not in path) and (node in cities[city]):
            find_paths(city, dict(cities), list(path), distance)

def distEntreCid(cities) :
    #recebe as entradas
    n = 3
    x = 0
    y = 0
    for i in range(1,n+1):
        xi = x
        yi = y
        cities[str(i)]=dict()
        for j in range(1,n+1):
            xj = x+i+j
            yj = y
            cities[str(i)][str(j)] = calculaDistancia(xi,yi,xj,yj)
    return cities
        
if __name__ == '__main__':
    cities = dict()
    distEntreCid(cities)
    cities = {
        '1': {'4': 195, '2': 86, '3': 178, '9': 180, '11': 91},
        '2': {'1': 86, '4': 107, '5': 171, '3': 123},
        '3': {'1': 178, '2': 123, '5': 170},
        '4': {'1': 195, '2': 107, '5': 210, '6': 210, '7': 135, '8': 64},
        '5': {'4': 210, '2': 171, '3': 170, '7': 230, '6': 230},
        '6': {'5': 230, '4': 210, '7': 85},
        '7': {'6': 85, '5': 230, '4': 135, '8': 67},
        '8': {'7': 67, '4': 64, '9': 191},
        '9': {'8': 191, '1': 180, '11': 85, '10': 91},
        '10': {'9': 91, '11': 120},
        '11': {'9': 120, '10': 85, '1': 91}
    }
    print ("Start: 1")
    find_paths('1', cities, [], 0)
    print ("\n")
    routes.sort()
    if len(routes) != 0:
        print ("Shortest route: %s" % routes[0])
    else:
        print ("FAIL!")
