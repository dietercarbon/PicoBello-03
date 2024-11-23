import machine
import utime

# Erstelle ein RTC-Objekt für den DS3231 (Beispieladresse 0x68)
luja = machine.RTC()
luja.datetime((2022, 6, 28, 2, 16, 30, 0, 0))  # Initialisiere mit Startzeit (Jahr, Monat, Tag, Wochentag, Stunden, Minuten, Sekunden, Subsekunden)

# Rufe die aktuelle Zeit von der RTC ab
#print(luja.datetime())

while True:
    print("1: ",luja.datetime())
    Zeit_8er_Tuple=luja.datetime()
    print("2: ",Zeit_8er_Tuple)
    Jahr=Zeit_8er_Tuple[0]
    Monat=Zeit_8er_Tuple[1]
    Tag=Zeit_8er_Tuple[2]
    TagNummer=Zeit_8er_Tuple[3]
    Stunde=Zeit_8er_Tuple[4]
    Minute=Zeit_8er_Tuple[5]
    Sekunde=Zeit_8er_Tuple[6]
    datum=Zeit_8er_Tuple[2]
    
    print("aktuell: ",Tag,".",Monat,".",Jahr,"    ",Stunde,":",Minute,":",Sekunde)
    print()
    utime.sleep(1)


'''
Der Raspberry Pi Pico verfügt über einen Echtzeituhr (RTC)-Baustein, der die aktuelle
Zeit und das aktuelle Datum bereitstellen kann. In MicroPython wird die Uhrzeit über
das machine.RTC()-Objekt abgerufen und eingestellt. Beachte jedoch, dass der Pico
keine integrierte RTC hat, daher wird die Zeit nicht aufrechterhalten, wenn der
Strom ausgeschaltet wird. Die Zeit muss nach jedem Neustart des Pico erneut
eingestellt werden.

In deinem Code verwendest du das machine.RTC()-Objekt, um ein RTC-Objekt
mit dem Namen "luja" zu erstellen. Danach verwendest du luja.datetime() zum
Abrufen der aktuellen Zeit. Der Rückgabewert von luja.datetime() ist
ein 8er-Tuple mit den Elementen:

    Jahr (year)
    Monat (month)
    Tag (day)
    Wochentag (weekday)
    Stunden (hours)
    Minuten (minutes)
    Sekunden (seconds)
    Subsekunden (subseconds)

In deinem Beispiel wird die aktuelle Zeit durch print(luja.datetime()) auf
der Konsole ausgegeben.

Wenn du die Zeit manuell setzen möchtest, kannst du dies mit der
Methode luja.datetime((Jahr, Monat, Tag, Wochentag, Stunden, Minuten,
Sekunden, Subsekunden)) tun, wobei du die entsprechenden Werte ersetzt.
Beachte, dass der Wochentag von 0 (Montag) bis 6 (Sonntag) geht.
'''