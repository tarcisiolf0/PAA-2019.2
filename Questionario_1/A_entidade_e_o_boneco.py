def min_time(conections, removed, times, pieces, total_time, removed_pieces):
    while(removed_pieces < pieces):
        print("Conections ->", conections)
        small = 1000000
        for j in range(len(conections)):
            print("index_j -> {} | len -> {}".format(j, len(conections)))
            if conections[j][2] < small:
                small = conections[j][2]
                aux = conections[j]
                string_aux = conections[j][0]
                index = j
                print("string_aux {} | index {}".format(string_aux, index))
        print("\n")
        print("aux -> {} | string aux -> {} | small -> {} | conections[j][2] {}".format(aux, string_aux, small, conections[j][2]))
        if removed[string_aux] == 0:
            total_time = total_time + times[string_aux]
            string1, string2 = aux[0], aux[1]
            print("string1-> {} | string2 -> {}".format(string1, string2))
            removed[string1] = 1
            removed[string2] = 1
            print("Removed->", removed)
            del (conections[index])
            removed_pieces = removed_pieces + 1
        else:
            del (conections[index])

        print("\n")
        print("Total_Time -> {}".format(total_time))
        print("Removed Pieces ->", removed)
    return total_time


pieces, strings = input().split(" ")
pieces = int(pieces)
strings = int(strings)
times = input().split(" ")
times = [int(num) for num in times]

removed = pieces*[0]
sums_visited = strings*[0]
conections = list()
sums = list()

for i in range(strings):
    aux = input().split(" ")
    aux = [int(num) for num in aux]
    string1, string2 = aux

    aux2 = times[string1 - 1] + times[string2 - 1]
    aux.append(aux2)
    conections.append(aux)


total_time = 0
removed_pieces = 0

result = min_time(conections, removed, times, pieces, total_time, removed_pieces)
