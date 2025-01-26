---
title: Ollama Product Sheet
author: skr
type: product-sheet
publish: true
tags: 
source: 
dependencies: "[[products]]"
date_created: 2024-11-28
---
---
```ad-tldr
title: TL;DR
Ollama ist eine Open-Source-Plattform zur lokalen Ausführung und Anpassung großer Sprachmodelle (LLMs), die Entwicklern und Forschern die Möglichkeit bietet, Modelle ohne Cloud-Abhängigkeit zu nutzen. Mit Unterstützung für verschiedene Betriebssysteme, einer Vielzahl vortrainierter Modelle und einer benutzerfreundlichen API ermöglicht Ollama eine flexible und datenschutzfreundliche Lösung für Anwendungen wie Chatbots und Textgenerierung. Die Software ist kostenlos und vollständig anpassbar, was sie zu einer hervorragenden Wahl für technikaffine Benutzer macht, die Wert auf Kontrolle und Sicherheit legen. Dieses Product Sheet bietet eine umfassende Übersicht über die Funktionen, Kosten und Sicherheitsmerkmale von Ollama, um informierte Entscheidungen über die Nutzung der Software zu treffen.
```
---
# **Ollama Product Sheet**
## **Grundlegende Informationen**
1. **Hauptzweck der Software**:  
   Ollama ist eine Open-Source-Plattform, die es ermöglicht, große Sprachmodelle (LLMs) lokal auf persönlichen Geräten auszuführen und anzupassen. Sie bietet Entwicklern und Forschern die Möglichkeit, LLMs ohne Cloud-Dienste zu nutzen, wodurch Datenschutz und Kontrolle gewährleistet werden.

2. **Aktuelle Version**:  
   Die neueste Version ist **0.1.33** (Stand: Mai 2024).

3. **Entwickler und Erscheinungsjahr**:  
   Entwickelt von **Ollama Inc.**, veröffentlicht im Jahr **2023**.

4. **Datum des letzten Updates**:  
   Das letzte Update wurde am **3. Mai 2024** veröffentlicht.

---

## **Technische Details**
1. **Unterstützte Betriebssysteme und Plattformen**:  
   - macOS  
   - Linux  
   - Windows (in Preview-Version)  
   - Docker

2. **Minimale Systemanforderungen**:  
   - **RAM**: Mindestens 8 GB für kleinere Modelle (z. B. 7B), 16 GB für größere Modelle (z. B. 13B).  
   - **GPU**: NVIDIA-GPU-Unterstützung für Hardware-Beschleunigung.  
   - **Speicherplatz**: Abhängig von der Modellgröße (z. B. 2 GB für kleinere Modelle, bis zu 55 GB für größere Modelle).

3. **Technische Spezifikationen**:  
   - Unterstützt Modelle wie **Llama 2**, **Mistral**, **Code Llama**, **Gemma** und viele mehr.  
   - Verwendet ein **Modelfile**-System zur Anpassung und Verwaltung von Modellen.  
   - API-Kompatibilität mit OpenAI.

---

## **Hauptfunktionen und Einsatzgebiete**
1. **Beschreibung der wichtigsten Funktionen**:  
   - **Lokale Ausführung von LLMs**: Modelle können direkt auf dem Gerät ausgeführt werden, ohne Cloud-Abhängigkeit.  
   - **Modellbibliothek**: Zugriff auf eine Vielzahl vortrainierter Modelle.  
   - **Anpassung und Erstellung**: Benutzer können Modelle anpassen oder neue erstellen.  
   - **GPU-Beschleunigung**: Optimierte Leistung durch Hardware-Beschleunigung.  
   - **REST-API**: Integration in Anwendungen und Workflows.  
   - **CLI-Unterstützung**: Einfache Verwaltung und Ausführung von Modellen über die Kommandozeile.

2. **Zielgruppe und typische Anwendungsfälle**:  
   - **Zielgruppe**: Entwickler, Forscher, Unternehmen, AI-Enthusiasten.  
   - **Anwendungsfälle**: Entwicklung von Chatbots, Datenanalyse, Textgenerierung, Forschung und Bildung.

---

## **Kosten und Lizenzierung**
1. **Verfügbare Versionen**:  
   - **Kostenlos**: Vollständig Open Source unter der MIT-Lizenz.

2. **Preisstruktur**:  
   - Keine Kosten für die Nutzung oder Anpassung.

3. **Lizenzmodelle**:  
   - Open Source (MIT-Lizenz).

---

## **Integration und Kompatibilität**
1. **Unterstützte Dateiformate und Schnittstellen**:  
   - Unterstützt Modelle im **GGUF**, **PyTorch** und **Safetensors**-Format.  
   - API-Kompatibilität mit OpenAI.

2. **Möglichkeiten zur Integration in bestehende Systeme**:  
   - Integration in Plattformen wie **LangChain**.  
   - REST-API für die Verbindung mit Webanwendungen und Tools.

---

## **Support und Community**
1. **Verfügbare Support-Optionen**:  
   - Community-Support über Discord und GitHub.  
   - Dokumentation und Tutorials auf der offiziellen Webseite.

2. **Dokumentationsressourcen**:  
   - [Offizielle Dokumentation](https://ollama.com/docs)  
   - [GitHub-Repository](https://github.com/ollama/ollama)

3. **Links zur offiziellen Dokumentation und zum Support**:  
   - [Ollama Webseite](https://ollama.com)  
   - [Ollama Discord](https://discord.gg/ollama)

---

## **Sicherheit und Datenschutz**
1. **Sicherheitsfunktionen**:  
   - Lokale Ausführung der Modelle gewährleistet Datenschutz.  
   - Keine Datenübertragung an Drittanbieter.

2. **Einhaltung von Datenschutzbestimmungen**:  
   - DSGVO-konform durch lokale Datenverarbeitung.

---

## **Vor- und Nachteile**
1. **Stärken der Software**:  
   - Vollständig lokal, keine Cloud-Abhängigkeit.  
   - Open Source und kostenlos.  
   - Anpassbare Modelle und einfache Integration.

2. **Schwächen oder potenzielle Einschränkungen**:  
   - Abhängig von der Hardware-Leistung des Benutzers.  
   - CLI-basierte Nutzung erfordert technisches Wissen.

3. **Bewertung des Preis-Leistungs-Verhältnisses**:  
   - Hervorragend, da kostenlos und flexibel.

---

## **Alternativen**
1. **Vergleich mit ähnlichen Konkurrenzprodukten**:  
   - **Hugging Face Transformers**: Größere Modellbibliothek, aber Cloud-abhängig.  
   - **OpenAI API**: Einfacher zu bedienen, aber kostenpflichtig und Cloud-basiert.  
   - **LocalGPT**: Ähnlich lokal, jedoch weniger flexibel.

2. **Unterscheidungsmerkmale und Alleinstellungsmerkmale**:  
   - Vollständig lokal mit OpenAI-kompatibler API.  
   - Anpassbare Modelle durch Modelfile-System.

---

## **Fazit**
1. **Gesamtbewertung der Software**:  
   Ollama ist eine leistungsstarke und flexible Lösung für die lokale Ausführung und Anpassung von LLMs, ideal für Entwickler und Forscher.

2. **Empfehlungen für die optimale Nutzung**:  
   - Nutzen Sie GPU-Beschleunigung für optimale Leistung.  
   - Experimentieren Sie mit der Anpassung von Modellen für spezifische Anwendungsfälle.

3. **Wichtige Entscheidungskriterien für und gegen den Einsatz der Software**:  
   - **Pro**: Datenschutz, Kostenfreiheit, Anpassungsfähigkeit.  
   - **Contra**: Abhängigkeit von Hardware und technischem Wissen.

---

## **Literatur**
- [Offizielle Webseite von Ollama](https://ollama.com)  
- [Ollama GitHub Repository](https://github.com/ollama/ollama)  
- [Ollama Dokumentation](https://ollama.com/docs)  
- [Artikel zu Ollama auf Medium](https://medium.com)
