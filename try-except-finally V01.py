try:
    # Versuch, einige Aktionen auszuführen
    num1 = int(input("Geben Sie eine Zahl ein: "))
    num2 = int(input("Geben Sie eine weitere Zahl ein: "))
    result = num1 / num2

    # Wenn keine Ausnahme auftritt, wird dieser Block ausgeführt
    print("Ergebnis der Division:", result)

except ValueError:
    # Behandlung, wenn eine ValueError-Ausnahme auftritt (z. B. wenn die Eingabe keine Zahl ist)
    print("Ungültige Eingabe. Bitte geben Sie gültige Zahlen ein.")

except ZeroDivisionError:
    # Behandlung, wenn eine ZeroDivisionError-Ausnahme auftritt (z. B. wenn versucht wird, durch 0 zu teilen)
    print("Teilen durch Null ist nicht erlaubt.")

finally:
    # Dieser Block wird immer ausgeführt, unabhängig davon, ob eine Ausnahme aufgetreten ist oder nicht
    print("Das Programm wird beendet.")


'''

In diesem Beispiel versucht das Programm, zwei Zahlen einzulesen und zu teilen.
Es gibt zwei except-Blöcke, einer für den Fall, dass eine ValueError-Ausnahme
auftritt (z. B. wenn der Benutzer keine Zahl eingibt), und der andere für
den Fall, dass eine ZeroDivisionError-Ausnahme auftritt (z. B. wenn der
Benutzer 0 als den Teiler eingibt). Der finally-Block wird immer ausgeführt,
unabhängig davon, ob eine Ausnahme aufgetreten ist oder nicht.

In MicroPython, genau wie in der vollständigen Python-Implementierung,
ermöglicht das try, except, und finally Konstrukt die Behandlung von
Ausnahmen (Exceptions) in einem Programm. Hier ist eine detaillierte
Erklärung jedes Teils mit einem Beispiel:

    try: Der try-Block enthält den Code, der möglicherweise eine
    Ausnahme auslöst. Der Code innerhalb dieses Blocks wird überwacht,
    und wenn eine Ausnahme auftritt, wird zum entsprechenden except-Block gesprungen.

    except: Der except-Block wird ausgeführt, wenn im try-Block eine
    Ausnahme auftritt. Hier können Sie den Code für die Behandlung der
    spezifischen Ausnahme platzieren. Es können auch mehrere except-Blöcke
    für verschiedene Arten von Ausnahmen vorhanden sein.

    finally: Der finally-Block enthält Code, der unabhängig davon, ob
    eine Ausnahme auftritt oder nicht, immer ausgeführt wird. Dieser
    Block ist optional, aber wenn er vorhanden ist, wird der darin
    enthaltene Code am Ende ausgeführt, bevor das Programm aus dem
    try-except-finally-Konstrukt austritt.
'''