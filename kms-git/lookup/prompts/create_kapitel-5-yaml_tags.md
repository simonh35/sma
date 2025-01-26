---
title: Generiere spezifische YAML-Tags
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
Der Prompt zielt darauf ab, eine optimierte Tag-Liste für eine Obsidian-Notiz zu erstellen, die speziell für die Integration in Knowledge Graphs geeignet ist. Er fordert die Identifizierung zentraler Konzepte, Hierarchien, Verknüpfungen und spezifischer Merkmale des gegebenen Textes, um eine strukturierte und relevante Liste von Tags zu generieren.
```
---
# Prompt
```
Für die letzte Antwort:

ODER

"[Hier den zuvor eingegebenen Text einfügen]"

-----

# Ziel:
Erstelle eine optimierte Tag-Liste für eine Obsidian-Notiz, die speziell für die Verwendung in Knowledge Graphs optimiert ist. Die Tags sollen zentrale Konzepte, Hierarchien, Verknüpfungen und spezifische Merkmale der Notiz erfassen. Die Ausgabe soll klar strukturiert und priorisiert sein, um die Integration in ein Wissensnetzwerk zu erleichtern.

# Eingabe:
- **Text der Notiz**: `[TEXT]`

# Ziel:
Erstelle eine präzise, strukturierte und hierarchisch optimierte Tag-Liste, die den Text `[TEXT]` für die Integration in Knowledge Graphs vorbereitet.

# Analyseschritte:
1. **Kernthemen (40%)**: Identifiziere die zentralen Konzepte und Hauptthemen des Textes `[TEXT]` (max. 3 Tags). Verwende, wo sinnvoll, allgemein gebräuchliche Abkürzungen oder Kurzformen (z. B. `ML` für `MachineLearning`). **Vermeide Umlaute** (ä, ö, ü) in den Tags.
2. **Hierarchie (30%)**: Ordne die Notiz in ein bestehendes Wissensnetz ein, indem übergeordnete Kategorien identifiziert werden (max. 2 Tags). Nutze auch hier Abkürzungen, wenn sie allgemein anerkannt sind (z. B. `AI` für `ArtificialIntelligence`). **Vermeide Umlaute** in den Tags.
3. **Verknüpfungen (20%)**: Erfasse Beziehungen zu verwandten Konzepten oder Notizen (max. 3 Tags). Berücksichtige auch hier die Verwendung von Abkürzungen und **vermeide Umlaute**.
4. **Spezifika (10%)**: Erfasse einzigartige Merkmale oder spezifische Methoden des Textes (max. 2 Tags). Verwende Abkürzungen, wenn sie die Klarheit erhöhen, und **vermeide Umlaute**.

---

### Formatierungsrichtlinien:
- Verwende **CamelCase** für zusammengesetzte Begriffe.
- Verwende allgemein gebräuchliche Abkürzungen und Kurzformen, wo sinnvoll und verfügbar.
- **Vermeide Umlaute** (ä, ö, ü) in den Tags.
- Begrenze die Anzahl der Tags auf **maximal 10**, sortiert nach Relevanz.
- Priorisiere die Tags basierend auf der Gewichtung der Analyseschritte.
- Die Ausgabe erfolgt im YAML-Format.

---

# Ausgabeformat:
Die generierte Tag-Liste soll in einer Markdown-Code-Umgebung im folgenden Format ausgegeben werden:

tags:
- PrimärTag
- KategorieTag1
- KategorieTag2
- VerknüpfungsTag1
- VerknüpfungsTag2
- VerknüpfungsTag3
- MethodenTag1
- MethodenTag2

