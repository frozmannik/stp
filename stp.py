import os
routes = []

file = open('result.txt','w')

def find_paths(node, cities, path, distance):
    # Add way point
    path.append(node)

    # Calculate path length from current to last node
    if len(path) > 1:
        #   print("HERE {}".format(cities[path[-2]][node]))
        distance += cities[path[-2]][node]

    # If path contains all cities and is not a dead end,
    # add path from last to first city and return.
    if (len(cities) == len(path)) and (cities[path[-1]].has_key(path[0])): # if whole cities is equal path
        global routes
        path.append(path[0])
        distance += cities[path[-2]][path[0]]
        result = str(path) + str(distance) +'\n'
        #print path, distance
        file.write(result)
        routes.append([distance, path])
        return

    # Fork paths for all possible cities not yet used
    for city in cities:
        if (city not in path) and (cities[city].has_key(node)):
            find_paths(city, dict(cities), list(path), distance)


if __name__ == '__main__':
    cities = {
        'RV': {'S': 195, 'UL': 86, 'M': 178, 'BA': 180, 'Z': 91},
        'UL': {'RV': 86, 'S': 107, 'N': 171, 'M': 123},
        'M': {'RV': 178, 'UL': 123, 'N': 170},
        'S': {'RV': 195, 'UL': 107, 'N': 210, 'F': 210, 'MA': 135, 'KA': 64},
        'N': {'S': 210, 'UL': 171, 'M': 170, 'MA': 230, 'F': 230},
        'F': {'N': 230, 'S': 210, 'MA': 85},
        'MA': {'F': 85, 'N': 230, 'S': 135, 'KA': 67},
        'KA': {'MA': 67, 'S': 64, 'BA': 191},
        'BA': {'KA': 191, 'RV': 180, 'Z': 85, 'BE': 91},
        'BE': {'BA': 91, 'Z': 120},
        'Z': {'BA': 120, 'BE': 85, 'RV': 91}
    }


    test = {
        'A': {'B' : 1, 'C': 7, 'D': 6},
        'B': {'A': 1, 'D': 2, 'C': 4},
        'C': {'A': 7, 'B': 4, 'D': 3},
        'D': {'B': 2, 'C':3, 'A' : 6}
    }
    for node in cities:
        find_paths(node, cities, [], 0)
        #print "\n"
        routes.sort()

    if len(routes) != 0:
        print "Result saved in result.txt file"
        print "Shortest route: %s" % routes[0]
    else:
        print "FAIL!"

