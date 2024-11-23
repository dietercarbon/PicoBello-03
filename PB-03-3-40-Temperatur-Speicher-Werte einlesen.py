#==========================================================================
#
# PB-3-3-40-Temperatur-Speicher-Werte einlesen_Kom.py
#
# (keine Bauteile)
#
#==========================================================================
#
DateiIn = open("Keller-Temperaturen.txt","r")

for i in range(11):
    print(DateiIn.readline())
    
DateiIn.close()

"""
Das Programm öffnet die Datei "Keller-Temperaturen.txt" im Lesemodus und gibt
die ersten 11 Zeilen der Datei in der Kommandozeile/Shell aus. Anschließend
wird die Datei wieder geschlossen.

Kommentar im Programm-Code selbst:

Das Programm öffnet die Textdatei "Keller-Temperaturen.txt" im Lesemodus und
liest die ersten 11 Zeilen der Datei mit der readline() Funktion ein. Jede
ausgelesene Zeile wird in der Kommandozeile/Shell mit der print() Funktion
ausgegeben. Danach wird die Datei mit close() wieder geschlossen.

Das Programm dient dazu, die Temperaturwerte aus einer zuvor erstellten
Textdatei namens "Keller-Temperaturen.txt" auszulesen und in der
Kommandozeile/Shell auszugeben. Die Ausgabe beschränkt sich dabei
auf die ersten 11 Zeilen der Datei.

Das Einlesen und Ausgeben der Zeilen erfolgt in einer Schleife, die insgesamt
11 Mal durchlaufen wird. In jedem Durchlauf wird mit der readline() Funktion
eine Zeile aus der Datei eingelesen und mit der print() Funktion ausgegeben.

Nachdem alle 11 Zeilen ausgegeben wurden, wird die Datei mit close() wieder
geschlossen.

Die Ausgabe der Temperaturwerte dient zur Überprüfung der korrekten
Funktionsweise des vorherigen Programms, das die Temperaturwerte in die
Datei geschrieben hat.
"""