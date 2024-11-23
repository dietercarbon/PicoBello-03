#==========================================================================
#
# PB-3-2-10-I2C-Geräte mit Adresse anzeigen_Kom.py
#
# (keine Bauteile)
#
#==========================================================================
#
# Bibliotheken laden
from machine import Pin, I2C

# Initialisierung I2C-Pins
i2c_sda = Pin(20)
i2c_scl = Pin(21)

# Initialisierung I2C
i2c = I2C(0,sda=i2c_sda,scl=i2c_scl,freq=100000)

# I2C-Bus-Scan
print('Scan I2C Bus...')
devices = i2c.scan()

# Scanergebnis ausgeben
if len(devices) == 0:
    print('Kein I2C-Gerät gefunden!')
else:
    print('I2C-Geräte gefunden:', len(devices))
    for device in devices:
        print('Dezimale Adresse:', device, '| Hexadezimale Adresse:', hex(device))
        
"""
Das Programm initialisiert einen I2C-Bus auf dem Raspberry Pi Pico und führt
dann einen Scan auf dem Bus durch, um alle angeschlossenen I2C-Geräte zu
finden. Es nutzt die MicroPython-Bibliotheken machine.Pin und machine.I2C.

Zunächst werden die Pins für SDA (Serial Data) und SCL (Serial Clock)
initialisiert, die für die Kommunikation mit I2C-Geräten benötigt werden.
Dazu werden die Pins 20 und 21 verwendet, die speziell für I2C auf dem Pico
vorgesehen sind.

Anschließend wird ein I2C-Objekt erstellt und auf den zuvor initialisierten
Pins ausgeführt. Die Frequenz des Busses wird auf 100 kHz gesetzt.

Dann wird der I2C-Bus gescannt, um alle angeschlossenen Geräte zu finden.
Wenn kein Gerät gefunden wird, wird eine entsprechende Nachricht ausgegeben.
Andernfalls werden die gefundenen Geräte und ihre Adressen sowohl in dezimaler
als auch in hexadezimaler Form ausgegeben.

Das Programm ist gut strukturiert und verwendet aussagekräftige Variablennamen,
was die Lesbarkeit erhöht. Es könnte jedoch erweitert werden, um spezifischere
Informationen über die gefundenen Geräte zu liefern.

Zusammenfassend sucht das Programm nach allen angeschlossenen I2C-Geräten
auf dem Raspberry Pi Pico und gibt ihre Adressen aus.

Kommentar zum Programm-Code (verbal):

Das Programm beginnt mit der Initialisierung der SDA- und SCL-Pins, die für
die Kommunikation mit I2C-Geräten benötigt werden. Dazu werden die Pins 20
und 21 verwendet. Anschließend wird ein I2C-Objekt erstellt und auf den zuvor
initialisierten Pins ausgeführt. Die Frequenz des Busses wird auf 100 kHz
gesetzt.

Dann wird der I2C-Bus gescannt, um alle angeschlossenen Geräte zu finden.
Dies wird mithilfe der i2c.scan()-Funktion durchgeführt, die eine Liste
mit den Adressen aller gefundenen Geräte zurückgibt. Wenn kein Gerät
gefunden wird, wird eine entsprechende Nachricht ausgegeben. Andernfalls
werden die gefundenen Geräte und ihre Adressen sowohl in dezimaler als
auch in hexadezimaler Form ausgegeben.

Das Programm ist einfach und übersichtlich gestaltet und verwendet
aussagekräftige Variablennamen, was die Lesbarkeit erhöht. Es könnte
jedoch erweitert werden, um spezifischere Informationen über die gefundenen
Geräte zu liefern. Insgesamt ist es ein nützliches Werkzeug zum Auffinden
aller angeschlossenen I2C-Geräte auf dem Raspberry Pi Pico.
"""
