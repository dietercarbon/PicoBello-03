#==========================================================================
#
# PB-3-4-10-GS_085 HC-SR501 PIR-Alarm LED.py
#
# Verwendung eines HC-SR501 PIR-Sensors und einer LED zur Bewegungserkennung
#
#==========================================================================

import machine  # Importiert das Modul für die Steuerung der Hardware
import utime    # Importiert das Modul für Zeitfunktionen

k = 0  # Zähler, um die Schleifenaktivität zu überwachen

# Initialisiere den PIR-Sensor an GPIO22 als Eingang mit internem Pull-Down-Widerstand
sensor_pir = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Initialisiere die LED an GPIO15 als Ausgang
led = machine.Pin(15, machine.Pin.OUT)

# Funktion, die ausgeführt wird, wenn der PIR-Sensor eine Bewegung erkennt
def pir_handler(pin):
    global k
    utime.sleep_ms(100)  # Kurze Verzögerung zur Entprellung
    if pin.value():  # Wenn der Sensor Bewegung erkennt (Signal ist HIGH)
        print("ALARM! Motion detected!")  # Ausgabe einer Alarmmeldung
        # Blinkt die LED 20-mal, wenn Bewegung erkannt wird
        for i in range(20):
            led.toggle()          # Wechselt den Zustand der LED (an/aus)
            utime.sleep_ms(100)   # Wartezeit von 100 Millisekunden zwischen den Blinks
        k = 0  # Setzt den Zähler zurück

# Interrupt für den PIR-Sensor konfigurieren: Bei steigender Flanke (RISING) wird pir_handler aufgerufen
sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

# Endlosschleife zur Überwachung der Schleifenaktivität
while True:
    print(k, "kein Interrupt")  # Gibt den aktuellen Zählerstand aus, solange kein Interrupt auftritt
    k = k + 1  # Erhöht den Zähler
    utime.sleep(0.2)  # Wartezeit von 0,2 Sekunden

"""
Ausführliche Erklärung des Programms:

Das Programm steuert einen HC-SR501 PIR-Sensor (Passive Infrared Sensor)
und eine LED mit dem Raspberry Pi Pico. Es verwendet einen Interrupt,
um Bewegungen zu erkennen und daraufhin eine Aktion auszulösen
(in diesem Fall das Blinken einer LED).

1. Importieren der benötigten Module

Das Programm verwendet zwei Module:

    machine: Ermöglicht den Zugriff auf die GPIO-Pins des Raspberry Pi Pico.
    utime: Ermöglicht zeitliche Verzögerungen (Delays) und Zeitmessungen.

2. Initialisierung der Hardware

    Der PIR-Sensor wird an GPIO22 angeschlossen und als Eingang konfiguriert.
    Ein interner Pull-Down-Widerstand sorgt dafür, dass der Eingang
    standardmäßig auf LOW gehalten wird, bis der Sensor eine Bewegung erkennt.
    Die LED wird an GPIO15 angeschlossen und als Ausgang definiert.
    Diese LED wird später zur Anzeige von Bewegungsaktivitäten verwendet.

3. Interrupt Service Routine (ISR)

    Die Funktion pir_handler(pin) wird aufgerufen, wenn der PIR-Sensor
    eine Bewegung erkennt (steigende Flanke).
    Eine kurze Verzögerung von 100 ms sorgt für Entprellung, um zu
    verhindern, dass der Sensor zu viele Signale in kurzer Zeit registriert.
    Wenn eine Bewegung erkannt wird (pin.value() ist True), wird
    eine Meldung „ALARM! Motion detected!“ auf dem Bildschirm ausgegeben.
    Danach blinkt die LED 20-mal im Abstand von 100 ms.
    Der Zähler k wird nach dem Blinken zurückgesetzt.

4. Konfigurieren des Interrupts

    Der Interrupt wird so eingerichtet, dass die ISR pir_handler() nur
    bei einer steigenden Flanke (RISING) des Eingangssignals ausgelöst
    wird. Das bedeutet, dass der Handler nur dann aktiviert wird,
    wenn der PIR-Sensor eine Bewegung erkennt.

5. Endlosschleife zur Überwachung

    In der Endlosschleife wird der Zähler k kontinuierlich erhöht
    und alle 0,2 Sekunden ausgegeben.
    Die Ausgabe „kein Interrupt“ zeigt an, dass kein Bewegungsereignis
    erkannt wurde, solange der Interrupt nicht ausgelöst wird.

Zusammenfassung des Verhaltens

Das Programm erkennt Bewegungen mit dem PIR-Sensor und schaltet dann
eine LED ein und aus, um anzuzeigen, dass eine Bewegung detektiert wurde.
Der Zähler k wird verwendet, um zu überwachen, dass das Hauptprogramm
weiterhin läuft, auch wenn keine Bewegungen erkannt werden. Der Einsatz
von Interrupts ermöglicht eine effiziente Reaktion auf Bewegungen,
ohne die CPU unnötig zu belasten.
"""