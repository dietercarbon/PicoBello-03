#==========================================================================
#
# PB-3-4-20-ElKo_Anwesenheitserkennung Display mit PIR Motion Detector HC-SR501.py
#
# 1 HC-SR501 PIR-Sensor zur Anwesenheitserkennung
#
#==========================================================================

# Bibliotheken laden
from machine import Pin  # Für die Steuerung der GPIO-Pins
from time import sleep   # Für Zeitverzögerungen

# Initialisierung des PIR-Sensors an GPIO22 mit Pull-Down-Widerstand
pir = Pin(22, Pin.IN, Pin.PULL_DOWN)

# Initialisierung der LED an GPIO15, standardmäßig aus
led = Pin(15, Pin.OUT, value=0)

# Initialisierung des Buzzers an GPIO0, standardmäßig aus
buz = Pin(0, Pin.OUT, value=0)

# Warten, bis der PIR-Sensor betriebsbereit ist
print('Warten')
print()
sleep(3)  # 3 Sekunden Wartezeit
print('Bereit')
print()

# Funktion zur Bewegungserkennung, die durch den Interrupt aufgerufen wird
def pir_handler(pin):
    pir_value = pir.value()  # Den aktuellen Zustand des PIR-Sensors lesen
    if pir_value == 1:       # Wenn eine Bewegung erkannt wurde
        alarm()              # Alarm auslösen
        sleep(6)             # Warten, bis sich der Sensor beruhigt hat
        print('Ruhezustand')
        print()

# Funktion zum Auslösen des Alarms
def alarm():
    print('Bewegung erkannt')  # Textausgabe auf die Konsole
    print()
    buz.on()  # Buzzer einschalten
    # LED für eine bestimmte Anzahl an Zyklen blinken lassen
    for i in range(10):
        led.toggle()  # LED ein- und ausschalten
        sleep(0.2)    # Verzögerung von 0,2 Sekunden pro Blink
    buz.off()  # Buzzer ausschalten

# Konfigurieren des Interrupts für den PIR-Sensor (steigende Flanke)
pir.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)
