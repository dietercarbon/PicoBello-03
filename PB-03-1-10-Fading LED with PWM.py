#==========================================================================
#
# PB-3-1-10-Fading LED with PWM_Kom.py
#
#  1 LED, 1 Widerstand, 1 Potentiometer
#
#==========================================================================

import machine
import utime

poti = machine.ADC(0)
led = machine.PWM(machine.Pin(15))
led.freq(1000)

while True:
    wertpoti = poti.read_u16()
    print(wertpoti)
    led.duty_u16(wertpoti)
    utime.sleep(0.05)

"""
Dieses MicroPython-Programm ist für den Raspberry Pi Pico-Mikrocontroller geschrieben und liest einen analogen Wert von
einem Potentiometer (Poti) über den ADC-Kanal 1 ein. Der eingelesene Wert wird dann auf eine LED ausgegeben, die an Pin 15
angeschlossen ist. Die LED leuchtet mit einer PWM-Frequenz von 1000 Hz und der Duty Cycle (Tastverhältnis) wird durch den
Potentiometerwert gesteuert. Das Programm wird in einer Endlosschleife ausgeführt und verzögert jeweils 50 Millisekunden
zwischen den Schleifendurchläufen.

Zunächst werden zwei Module importiert: "machine" und "utime". "machine" ist das Modul, das alle Funktionen enthält, die zur
Interaktion mit der Hardware des Raspberry Pi Pico erforderlich sind, und "utime" ist ein Modul, das Funktionen zur Zeitmessung
bereitstellt.

Als nächstes werden zwei Objekte erstellt. Das erste Objekt, "poti", wird durch die Verwendung der Klasse "ADC" aus dem
Modul "machine" erstellt. Der Parameter 1 gibt an, dass der ADC-Kanal 1 verwendet wird. Das zweite Objekt, "led", wird durch
die Verwendung der Klasse "PWM" aus dem Modul "machine" erstellt. Der Pin 15 wird als Parameter übergeben und die
PWM-Frequenz wird auf 1000 Hz eingestellt.

Dann beginnt die Endlosschleife. In jeder Iteration der Schleife wird der aktuelle Potentiometerwert als 16-Bit-Integer mit der
Funktion "read_u16()" von dem "poti"-Objekt gelesen. Dieser Wert wird dann auf die LED angewendet, indem die
Funktion "duty_u16()" des "led"-Objekts aufgerufen wird und der Potentiometerwert als Parameter übergeben wird.
Schließlich wird das Programm mit der Funktion "sleep()" von "utime" für 50 Millisekunden verzögert und die Schleife
beginnt erneut.

Zusammenfassend misst dieses Programm den Wert eines Potentiometers und steuert eine LED mit diesem Wert,
indem es den Duty Cycle der LED-PWM mit dem gemessenen Potentiometerwert ändert. Dies kann nützlich sein, um die
Helligkeit einer LED oder die Geschwindigkeit eines Motors zu steuern.
"""