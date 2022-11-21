# project : Advent of Code Day 6 Part I
# author : dasocker
# date : 14.11.2022

##############################################
########### Inputs Importiert ################

inputs = []

with open ("input_day_6.txt") as day6:
    for line in day6.readlines():
        inputs.append(line)

#print(inputs)

##############################################
########### Input umwandlung #################

def input_auslesung(inputs):

    for i in inputs:

        if "on" in i:
            t = i.find(",")
            x1 = i[8:t]
            x1 = int(x1)

            i_2 = i[t+1:]
            t_2 = i_2.find(" ")
            x2 = i_2[0:t_2]
            x2 = int(x2)

            r = i_2.find("through")
            i_3 = i_2[r+8:]

            t_3 = i_3.find(",")
            y1 = i_3[0:t_3]
            y1 = int(y1)

            t_4 = i_3.find(",")
            y2 = i_3[t_4+1:]
            y2 = int(y2)

            lichtschalter_on(x1, x2, y1, y2)


        elif "off" in i:
            t = i.find(",")
            x1 = i[9:t]
            x1 = int(x1)

            i_2 = i[t+1:]
            t_2 = i_2.find(" ")
            x2 = i_2[0:t_2]
            x2 = int(x2)

            r = i_2.find("through")
            i_3 = i_2[r+8:]

            t_3 = i_3.find(",")
            y1 = i_3[0:t_3]
            y1 = int(y1)

            t_4 = i_3.find(",")
            y2 = i_3[t_4+1:]
            y2 = int(y2)

            lichtschalter_off(x1, x2, y1, y2)


        elif "toggle" in i:
            t = i.find(",")
            x1 = i[7:t]
            x1 = int(x1)

            i_2 = i[t + 1:]
            t_2 = i_2.find(" ")
            x2 = i_2[0:t_2]
            x2 = int(x2)

            r = i_2.find("through")
            i_3 = i_2[r + 8:]

            t_3 = i_3.find(",")
            y1 = i_3[0:t_3]
            y1 = int(y1)

            t_4 = i_3.find(",")
            y2 = i_3[t_4 + 1:]
            y2 = int(y2)

            lichtschalter_toggle(x1, x2, y1, y2)


##############################################

# Idee: Dictionary für das grid schreiben, je ein Key für eine Reihe mit den Parametern der Koordinate und dem Status "on" oder "off"
# Umsetzung; Funktion schreiben die mir das Dictionary füllt; zunächst die Liste schreiben (koord + status)
# - diese anhängen für die Reihe & dies dann dem ersten Key im Dict zuweisen,
# wiederholen für alles Keys (Reihen) mit entsprechenden Koords

my_dict = {1: [[(0, 0), "off"], [(0, 1), "off"], [(0, 2), "on"]]}

my_dict[1][0][1] = "on"
#print(my_dict[1][0][1])

###############################################
####### Dictionary Koordinatensystem ##########

dict = {}

def dict_builder_part1(y):

    sublist = []
    x = 0
    for step in range(1000):

        sublist.append([(y, 0 + x), "off"])
        x = x + 1

    return sublist

#print(dict_builder_part1(1))


def dict_builder_part2():

    y = 0
    for step in range (1000):

        dict[y] = dict_builder_part1(y)
        y = y + 1

    return dict

dict_builder_part2()

###############################################
####### Umsetzungsprogess Idee ################

# 964(y2) - 959(x2) = 5   -> 5 steps von 959 werden von off auf on gesetzt

# 759(y1) - 489(x1) = 270 -> in jeweils 270 reihen wird der erste part (von 959 5lichter nach rechts) off->on

#           x1   x2         y1   y2         -> parameter die ich aus dem Input nehme.
#print(dict[489][959]),  dict[759][964]

#print(dict[490][959])

###############################################
############# Testwerte #######################

x1 = 489
x2 = 959

y1 = 759
y2 = 964

##############################################
##### on/off/toggle Funktionen ###############


def lichtschalter_on(x1, x2, y1, y2):
    z = y2 - x2
    u = y1 - x1

    counter =  0
    subcounter = 0
    while counter <= u:

        while subcounter <= z:
            dict[x1+counter][x2+subcounter][1] = "on"

            subcounter = subcounter + 1

        counter = counter + 1
        subcounter = 0


def lichtschalter_off(x1, x2, y1, y2):
    z = y2 - x2
    u = y1 - x1

    counter =  0
    subcounter = 0
    while counter <= u:

        while subcounter <= z:
            dict[x1+counter][x2+subcounter][1] = "off"

            subcounter = subcounter + 1

        counter = counter + 1
        subcounter = 0


def lichtschalter_toggle(x1, x2, y1, y2):
    z = y2 - x2
    u = y1 - x1

    counter =  0
    subcounter = 0
    while counter <= u:

        while subcounter <= z:

            if "on" in dict[x1+counter][x2+subcounter][1]:

                dict[x1+counter][x2+subcounter][1] = "off"

                subcounter = subcounter + 1

            elif "off" in dict[x1+counter][x2+subcounter][1]:

                dict[x1 + counter][x2 + subcounter][1] = "on"

                subcounter = subcounter + 1

        counter = counter + 1
        subcounter = 0


####################################################
########### Funktionstestung #######################


#lichtschalter_on(x1, x2, y1, y2)
#print(dict[666][961])

#lichtschalter_off(x1, x2, y1, y2)
#print(dict[666][961])

#dict[666][961][1] = "on"

#lichtschalter_toggle(x1, x2, y1, y2)
#print(dict[666][961])
#print(dict[666][962])


#####################################################
########### Eingabe des Inputs ######################

input_auslesung(inputs)

#####################################################
############### Ergebnis Zählen #####################

def lösung(k):

    counter = 0
    for x in dict[k]:
        if "on" in x:
            counter = counter + 1
    return counter

def durchgehen():
    z1 = 0
    for x in range(1000):
        z = lösung(x)
        z1 = z1 + z
    return z1


print(durchgehen())                 # Ergebnis !