author: dasocker
date: 28.10.22

########### Day 3.2 Part I ##############
inputs = "override me"

#öffnet die textdatei mit den Inputs für Day3 & speichert diese in eine Variable "inputs"
with open("day3.txt") as day3:
    inputs = day3.read()

#überprüfung ob die Inputs da sind, welchen type sie haben und wie lang die länge des datensatzes
print(inputs)
print((type(inputs)))
print(len(inputs))

#leere liste zum befüllen mit koordinaten
koordinaten = []

#funktion um für jeden input eine einzelne koordinate zu erstellen, welche in die leere liste eingefügt wird (als tuples)
def was_mache_ich(my_input):
    position = (0, 0)

    for element in my_input:
        if element == "^":

           position = (position[0], position[1] + 1)
           koordinaten.append(position)


        if element == ">":

            position = (position[0] + 1, position[1])
            koordinaten.append(position)


        if element == "<":

            position = (position[0] - 1, position[1])
            koordinaten.append(position)


        if element == "v":

            position = (position[0], position[1] - 1)
            koordinaten.append(position)


was_mache_ich(inputs)                           #ausführen der funktion

#verlaufskontrolle
#print(koordinaten)
#print(len(koordinaten))


#neue liste zum befüllen aller "doppelten" koordinaten, um doppelte auszusortieren
pop_koords = []

#funktion um doppelte koordinaten in die leere liste zu schreiben
def entferne_doppelte_koordinaten(my_koord):
    for element in my_koord:
        if element not in pop_koords:
            pop_koords.append(element)

entferne_doppelte_koordinaten(koordinaten)      #ausführen der funktion

#verlaufskontrolle
#print(pop_koords)
#print(len(pop_koords))                          #die länge gibt alle häuser an, die mindestens ein geschenk erhalten haben - jedoch muss für die lösung noch +1 dazu, für den startpunkt (0, 0). *




############################ Day 3 Part II ################################

santa_liste_part_II = []
robo_santa_liste_part_II = []

def santa_und_robo_santa(x):

    santa = 0
    robo_santa = 0

    position_santa = (0, 0)
    position_robo_santa = (0, 0)

    for element in x:

        if santa <= robo_santa:

            if element == "^":
                position_santa = (position_santa[0], position_santa[1] + 1)
                santa_liste_part_II.append(position_santa)
                santa = santa + 1

            if element == ">":
                position_santa = (position_santa[0] + 1, position_santa[1])
                santa_liste_part_II.append(position_santa)
                santa = santa + 1

            if element == "<":
                position_santa = (position_santa[0] - 1, position_santa[1])
                santa_liste_part_II.append(position_santa)
                santa = santa + 1

            if element == "v":
                position_santa = (position_santa[0], position_santa[1] - 1)
                santa_liste_part_II.append(position_santa)
                santa = santa + 1

        elif santa > robo_santa:

            if element == "^":
                position_robo_santa = (position_robo_santa[0], position_robo_santa[1] + 1)
                robo_santa_liste_part_II.append(position_robo_santa)
                robo_santa = robo_santa + 1

            if element == ">":
                position_robo_santa = (position_robo_santa[0] + 1, position_robo_santa[1])
                robo_santa_liste_part_II.append(position_robo_santa)
                robo_santa = robo_santa + 1

            if element == "<":
                position_robo_santa = (position_robo_santa[0] - 1, position_robo_santa[1])
                robo_santa_liste_part_II.append(position_robo_santa)
                robo_santa = robo_santa + 1

            if element == "v":
                position_robo_santa = (position_robo_santa[0], position_robo_santa[1] - 1)
                robo_santa_liste_part_II.append(position_robo_santa)
                robo_santa = robo_santa + 1


santa_und_robo_santa(inputs)
print(santa_liste_part_II)                          # print verlaufskontrollen
print(len(santa_liste_part_II))
print(robo_santa_liste_part_II)
print(len(robo_santa_liste_part_II))

print("\n")

final_list = []                                     # liste zum befüllen nach aussortieren doppelter koordinaten

def entferne_doppelte_koordinaten_part_II(l_1, l_2):

    for element in l_1:
        if element not in final_list:
            final_list.append(element)

    for element in l_2:
        if element not in final_list:
            final_list.append(element)

entferne_doppelte_koordinaten_part_II(santa_liste_part_II, robo_santa_liste_part_II)
print(final_list)
print(len(final_list))                              # ergebnis für Part II *
print(final_list.count((0, 0)))                     # prüfen ob der startpunkt mit drin ist, oder noch dazugenommen werden muss wie in Part I
