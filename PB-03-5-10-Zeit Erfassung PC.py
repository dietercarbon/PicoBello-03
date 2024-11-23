import machine
import utime

luja = machine.RTC()  # kreiert RTC-Objekt "luja"
#
#
print(luja.datetime())  #druckt 8er-Tuple mit aktueller Zeit:
#  year, month, day, weekday, hours, minutes, seconds, subseconds
#  .datetime() ohne Argument: ermittelt Datum/Zeit
#  .datetime((2022,6,28,2,12,24,0,0)) mit Argument: setzt Datum/Zeit

luja.datetime()
#luja.datetime((2022,6,28,2,12,24,0,0))

while True:
    print(luja.datetime())
    Zeit_8er_Tuple=luja.datetime()
    print(Zeit_8er_Tuple)
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
