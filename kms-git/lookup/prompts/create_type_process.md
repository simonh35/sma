---
title: Erstelle eine Prozess-Notiz
author: skr
type: prompt
publish: true
tags: 
source: 
dependencies: "[[prompts]]"
date_created: 2024-11-28
---
---
```ad-info
Der Prompt führt den Benutzer durch eine strukturierte Abfolge von Fragen zur Erstellung einer umfassenden Prozessdokumentation, indem er die Eingaben einzeln abfragt und speichert. Ziel ist es, alle relevanten Informationen zu sammeln und in einem klaren, Obsidian-kompatiblen Markdown-Format zu dokumentieren.
```
---
# Prompt
```python
import os
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_input(prompt):
    print("\n" + "="*80 + "\n")
    print(prompt)
    print("\nIhre Antwort (mehrere Zeilen möglich, beenden Sie mit 'ENDE' in einer neuen Zeile):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == 'ENDE':
            break
        lines.append(line)
    return '\n'.join(lines)

def create_process_documentation():
    clear_screen()
    print("Willkommen zur Prozessdokumentation")
    print("Beantworten Sie die folgenden Fragen. Geben Sie 'ENDE' ein, wenn Sie Ihre Antwort abgeschlossen haben.")

    # Dictionary für alle Fragen und deren Kategorien
    questions = {
        "Prozessname": "Wie lautet der Name des Prozesses?",

        "Ziel und Kontext": [
            "Was ist das übergeordnete Ziel des Prozesses?",
            "In welchem Umfeld oder welcher Branche wird der Prozess angewendet?",
            "Welche spezifischen Herausforderungen oder Probleme adressiert der Prozess?"
        ],

        "Eingaben (Inputs)": [
            "Welche Ressourcen oder Materialien werden für den Prozess benötigt?",
            "Woher stammen diese Inputs?"
        ],

        "Schritte und Aktionen": [
            "Beschreiben Sie die einzelnen Schritte des Prozesses in chronologischer Reihenfolge:",
            "Wer ist für welchen Schritt verantwortlich?",
            "Welche Werkzeuge, Technologien oder Methoden werden verwendet?"
        ],

        "Ergebnisse (Outputs)": [
            "Welche Ergebnisse oder Produkte liefert der Prozess?",
            "Wie werden diese Outputs genutzt oder weiterverarbeitet?"
        ],

        "Beteiligte Personen und Rollen": [
            "Welche Rollen oder Personen sind direkt oder indirekt am Prozess beteiligt?",
            "Welche spezifischen Aufgaben oder Verantwortlichkeiten haben sie?"
        ],

        "Kritische Erfolgsfaktoren": [
            "Was sind die Schlüsselaspekte, die für den Erfolg des Prozesses entscheidend sind?",
            "Welche Metriken oder KPIs werden verwendet, um den Erfolg zu messen?"
        ],

        "Herausforderungen und Risiken": [
            "Welche potenziellen Hindernisse oder Risiken könnten den Prozess beeinträchtigen?",
            "Welche Maßnahmen können ergriffen werden, um diese Risiken zu minimieren?"
        ],

        "Optimierungspotenzial": [
            "Welche Schwachstellen oder ineffizienten Schritte gibt es im Prozess?",
            "Welche Verbesserungsvorschläge oder Strategien zur Optimierung können umgesetzt werden?"
        ],

        "Anwendungsbeispiele": [
            "Beschreiben Sie reale Szenarien, in denen der Prozess erfolgreich angewendet wurde:",
            "Welche Erkenntnisse wurden dabei gewonnen?"
        ]
    }

    answers = {}

    # Prozessname zuerst abfragen
    process_name = get_input(questions["Prozessname"]).strip()

    # Alle anderen Kategorien durchgehen
    for category, category_questions in questions.items():
        if category == "Prozessname":
            continue

        clear_screen()
        print(f"\nKategorie: {category}")
        category_answers = []

        if isinstance(category_questions, list):
            for question in category_questions:
                answer = get_input(question)
                category_answers.append(answer)
        else:
            answer = get_input(category_questions)
            category_answers.append(answer)

        answers[category] = category_answers

    # Markdown-Datei erstellen
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"Prozess_{process_name.replace(' ', '_')}_{timestamp}.md"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# Prozessdokumentation: {process_name}\n\n")

        for category, category_answers in answers.items():
            f.write(f"## {category}\n")
            for answer in category_answers:
                f.write(f"{answer}\n\n")
            f.write("\n")

        f.write(f"\n---\nErstellt am: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")

    print(f"\nDie Prozessdokumentation wurde erfolgreich erstellt und in der Datei '{filename}' gespeichert.")

if __name__ == "__main__":
    create_process_documentation()

# Created/Modified files during execution:
# - Prozess_[Name]_[Timestamp].md```