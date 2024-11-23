#==========================================================================
#
# PB-3-1-20-Fading LED with PWM auto_Kom.py
#
#  1 LED, 1 Widerstand
#
#==========================================================================

import machine
import utime

#poti = machine.ADC(0)
led = machine.PWM(machine.Pin(15))
led.freq(1000)

zuwachs=2000
pause=2

while True:
    print("es wird: heller ...")
    utime.sleep(pause)
    for hell in range(1,65536,zuwachs):
        led.duty_u16(hell)
        print("heller: ",hell)
        utime.sleep(0.05)
        
    print("es wird: dunkler ...")
    utime.sleep(pause)
    for hell in range(65536,1,-zuwachs):
        led.duty_u16(hell)
        print("dunkler: ",hell)
        utime.sleep(0.05)
        
"""
Das Programm ist eine Schleife, die die Helligkeit einer an Pin 15 angeschlossenen LED erhöht und verringert. Es gibt zwei
Variablen, zuwachs und pause, die jeweils auf 2000 und 2 festgelegt sind. zuwachs bestimmt, wie viel die Helligkeit bei jedem
Schritt erhöht oder verringert wird, während pause angibt, wie lange das Programm zwischen jeder Erhöhung oder Verringerung
der Helligkeit pausiert.

Im Hauptteil des Codes wird zuerst die PWM-Frequenz der LED auf 1000 Hz festgelegt. Dann beginnt die Schleife, die sich
endlos wiederholt, bis das Programm unterbrochen wird. Das Programm beginnt mit einer Ausgabe auf der Konsole, dass
die Helligkeit erhöht wird, und wartet dann für pause Sekunden.

Dann wird eine Schleife ausgeführt, die die Helligkeit von 1 (minimale Helligkeit) bis 65535 (maximale Helligkeit) in Schritten
von zuwachs erhöht. Bei jedem Schritt wird die Helligkeit auf die LED angewendet, die aktuelle Helligkeit auf der Konsole
ausgegeben und das Programm pausiert für 0,05 Sekunden.

Danach wird eine weitere Ausgabe auf der Konsole gemacht, die besagt, dass die Helligkeit reduziert wird, und wieder pause
Sekunden gewartet. Eine Schleife wird ausgeführt, die die Helligkeit von 65535 (maximale Helligkeit) auf 1 (minimale Helligkeit)
in Schritten von -zuwachs verringert. Bei jedem Schritt wird die Helligkeit auf die LED angewendet, die aktuelle Helligkeit auf
der Konsole ausgegeben und das Programm pausiert für 0,05 Sekunden.

Das Programm wird dann von vorne gestartet und beginnt wieder mit der Erhöhung der Helligkeit.
"""
        