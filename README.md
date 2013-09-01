Das Plone Benutzerhandbuch
==========================

Das Plone-Benutzerhandbuch enthält eine Dokumentation des Content-Management-Systems Plone in der Version 4. Es richtet sich an Benutzer, die als Autoren und Redakteure mit Plone arbeiten, sowie an Administratoren, die Plone konfigurieren und administrieren.

Voraussetzungen
---------------

Um das Plone Benutzerhandbuch zu generieren, ist folgende Software erforderlich:

- TeX
- Sphinx

Formatierung des Handbuchs
--------------------------

Klonen Sie das Repository und wechseln Sie in den neu erzeugten Ordner. Dort können Sie die Ausgabeformate HTML, PDF und ePub mit folgendem Befehl erzeugen:

	make pdflatex epub html

Die Ausgabeformate finden Sie anschließend in dem Ordner `_build`.