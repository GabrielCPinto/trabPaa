import math


def calculaDistancia(x1, y1, x2, y2):
    x = abs(float(x1) - float(x2))
    y = abs(float(y1) - float(y2)) 
    return math.sqrt(math.pow(x, 2)+math.pow(y, 2))

def distEntreCid(cities):
    # recebe as entradas
    with open("text.txt", "r") as filestream:
        cidade=[]
        for line in filestream:
            currentline = line.split(",")
            for item in currentline:
                cidade.append(item.split(" "))

    n = int(cidade[0][0])
    for i in range(1, n+1):
        xi = cidade[i][0]
        yi = cidade[i][1]
        cities[str(i)] = dict()
        for j in range(1, n+1):
            xj = cidade[j][0]
            yj = cidade[j][1]
            cities[str(i)][str(j)] = calculaDistancia(xi, yi, xj, yj)
    return cities

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
        print(path, distance)
        routes.append([distance, path])
        return

    # Fork paths for all possible cities not yet used
    for city in cities:
        if (city not in path) and (node in cities[city]):
            find_paths(city, dict(cities), list(path), distance)





if __name__ == '__main__':
    cities = dict()
    distEntreCid(cities)
    
    print("Start: 1")
    find_paths('1', cities, [], 0)
    print("\n")
    routes.sort()
    if len(routes) != 0:
        with open("answers.txt", "w") as filestreamtwo:
            filestreamtwo.write(str(routes[0]))
        print("Shortest route: %s" % routes[0])
    else:
        print("FAIL!")
