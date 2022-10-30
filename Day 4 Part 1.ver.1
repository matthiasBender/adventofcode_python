# author : dasocker
# date : 30.10.22

############ Advent of Code: Year 2015, Day 4 - Part I #################

# Gedankengang : Zuerst habe ich gegoogelt wie ich einen MD5 Hash auslese/erzeuge etc, dann eine Zahl hinzugefügt.
#                Im nächsten Schritt habe ich den Hash mit steigender Zahl in eine Liste gespeichert,
#               -> Idee ist; nun die Hashes die mit 5 "0" beginnen rauszufiltern, um dann hoffentlich zu backtracken
#                  welche Zahl diesem Hash zugesetzt wurde, aka die position dieses Hashes in der Liste ermitteln.

# ausprobieren, lernen was / wie hashes funktionieren, versuche ideenansätze zu erdenken / umzusetzen
    # (

import hashlib as hash

input = "bgvyzdsv"
print(input)
#print(hash(input))

result = hash.md5(input.encode())
#print(result)
print(result.hexdigest())

print("")

########### hash + zahl generieren

x = 123
input_with_int = "bgvyzdsv" + str(x)
result_with_int = hash.md5(input_with_int.encode())
print(result_with_int.hexdigest())

print("")
#number = list((range(10)))
#print(number)

#input_with_int = input + str(number)
#print(input_with_int)
print("lets try out stuff")
print("\n")


# )


################################

counter = 0
hash_ergebnisse = []
while counter < 1000000:
    counter = counter + 1
    input_with_int = "bgvyzdsv" + str(counter)
    result_with_int = hash.md5(input_with_int.encode())
#    result_with_int.hexdigest()
    hash_ergebnisse.append(result_with_int.hexdigest())

#print(hash_ergebnisse)
#print(type(hash_ergebnisse[0]))                             #nachschauen mit was für einem type ich hier arbeite

gefilterte_ergebnisse = list(filter(lambda x: "00000" in x, hash_ergebnisse))       #ergoogelt, wünsche mir aber ein lösung die ich selbst besser verstehe.

gef_ergebnisse_2 = []
indexcounter = 0
for element in hash_ergebnisse:
    indexcounter = indexcounter + 1
    if True == element.startswith("00000"):                 # .startwith gibt lediglich ein Bool wert zurück,- // wie komme ich nun an den index?
#        bitte = element.index(element.startswith("00000"))  # TypeError: must be str, not bool
        print(indexcounter)                                     #mögliches ergebnis? Index des elementes, dass mit 5x("0") beginnt.
        gef_ergebnisse_2.append(element)


print(gef_ergebnisse_2)                                     # offensichtlich der einzigste string in 1mio eingaben der mit 5x"0" beginnt. :)
print(gefilterte_ergebnisse[11])
print(len(gefilterte_ergebnisse))

test = gefilterte_ergebnisse[11]                            #erster hash der mit "00000" startet (aus 38 mit "00000" drinnen, aber sie starten nicht alle mit "00000")
