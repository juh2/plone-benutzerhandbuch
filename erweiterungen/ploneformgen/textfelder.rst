============
 Textfelder
============

.. _sec_kurztext-feld:

Zeichenkettenfeld
=================


Das Zeichenkettenfeld (Abbildung :ref:`fig_kurztext-feld`) dient der
Eingabe einer einzelnen Textzeile. Mit Hilfe verschiedener Validatoren
kann vor dem Absenden des Formulars überprüft werden, ob bestimmte
Bedingungen eingehalten wurden.

.. _fig_kurztext-feld:

.. figure::
   ./images/kurztext-feld.*
   :width: 60%
   :alt: Hinzufügeformular für ein Feld zur Eingabe einer Textzeile

   Feld für Textzeile

Die Einstellungsmöglichkeiten »Titel«, »Hilfe-Feld«, »zwingend
benötigt«, »Standard«, »Maximale Länge« und »Größe« wurden bereits am
Beispiel des Whole Number Fields erklärt (siehe
:ref:`sec_whole-number-field`). 

Das Kurztext-Feld kann zudem versteckt werden.

Mit Hilfe des Validators (siehe Abbildung
:ref:`fig_validator-kurztext`) kann man sicherstellen, dass die
Eingabe bestimmte Bedingungen erfüllt. 

.. _fig_validator-kurztext:

.. figure::
   ./images/validator-kurztext.*
   :width: 50%
   :alt: Optionen für den Validator einer Textzeile

   Validator für Textzeile

Überprüft werden kann:

* ob die Eingabe eine E-Mail-Adresse ist
* ob die Eingabe eine Liste von E-Mail-Adressen ist, die durch Kommas
  getrennt sind
* ob die Eingabe nur druckbare Zeichen enthält
* ob die Eingabe eine korrekt formatierte Webadresse (URL) ist
* ob es sich bei der Eingabe um eine gültige US-Telefonnummer handelt
* ob es sich bei der Eingabe um eine gültige internationale
  Telefonnummer handelt
* ob die Eingabe eine gültige Postleitzahl ist
* ob die Eingabe frei von Links ist

Wenn die Bedingung des Validators nicht erfüllt ist, erhält der
Benutzer eine Warnung mit dem Hinweis, wie er eine korrekte Eingabe
machen kann.

.. _sec_text-feld:

Einfaches Textfeld
==================


Beim Zeilenfeld (Abbildung :ref:`fig_text-feld`) kann ein mehrzeiliger,
nicht formatierter Text eingegeben werden.

.. _fig_text-feld:

.. figure::
   ./images/text-feld.*
   :width: 100%
   :alt: Hinzufügeformular für ein Feld zur Eingabe von Text

   Feld für Text

Die meisten Einstellungsmöglichkeiten wurden bereits in
:ref:`sec_whole-number-field` erklärt. Das Zeilenfeld kann wie das
Zeichenkettenfeld versteckt werden.

Zusätzlich gibt es folgenden Validator:

Text mit Links zurückweisen
   Wenn diese Option ausgewählt wird, darf sich in dem eingegebenen
   Text kein Link zu einer Webseite befinden. Falls dies doch der Fall
   ist, erhält der Benutzer eine Warnung und eine Erläuterung, wie er
   eine gültige Eingabe vornehmen kann.


.. _sec_formatierbarer-text-feld:

Texteingabefeld
===============

Das Texteingabefeld dient dazu, dem Benutzer die
Möglichkeit zu geben, längere formatierte Texte einzugeben und dabei
den Texteditor zu nutzen (siehe Abbildung
:ref:`fig_formatierbarer-text-feld` und :ref:`Textfeld mit Texteditor <fig_formatierbarer-text-feld-anzeige>`).  

.. _fig_formatierbarer-text-feld:

.. figure::
   ./images/formatierbarer-text-feld.*
   :width: 100%
   :alt: Hinzufügeformular für ein Feld für formatierbaren Text

   Feld für formatierbaren Text

Die Konfigurationsmöglichkeiten wurden in
:ref:`sec_whole-number-field` erklärt.   

.. _fig_formatierbarer-text-feld-anzeige:

.. figure::
   ./images/formatierbarer-text-feld-anzeige.*
   :width: 100%
   :alt: Textfeld mit Bedienelementen des Texteditors

   Textfeld mit Texteditor, wie es sich dem Benutzer darstellt

.. _sec_passwort-feld:

Passwort-Feld
=============

Wenn Passwörter eingegeben werden, müssen sie in der Browseranzeige
maskiert werden. Dies gewährleistet das Passwort-Feld (Abbildung
:ref:`fig_passwort-feld`).

.. _fig_passwort-feld:

.. figure::
   ./images/passwort-feld.*
   :width: 100%
   :alt: Hinzufügeformular für ein Passwort-Feld

   Feld für Eingabe eines Passworts

Die Konfigurationsmöglichkeiten entsprechen denen in
:ref:`sec_whole-number-field`. 


.. _sec_zeilen-feld:

Zeilenfeld
==========

Mit dem Zeilenfeld ist die Eingabe von Textzeilen möglich, die
zeilenweise als einzelne Werte weiterverarbeitet werden. So kann man
beispielsweise mit dem Zeilenfeld eine Liste von Teilnehmern
erzeugen, indem man pro Zeile den Namen eines Teilnehmers eingibt.

.. _fig_zeilen-feld:

.. figure::
   ./images/zeilen-feld.*
   :width: 100%
   :alt: Hinzufügeformular für ein Zeilen-Feld

   Zeilen-Feld

Die Konfigurationsmöglichkeiten (siehe Abbildung
:ref:`fig_zeilen-feld`) wurde bereits erklärt. Folgendes ist
noch zu beachten:

Zeilen
   Hiermit legen Sie fest, wie hoch das Eingabefeld im Formular sein
   soll. Wenn der Benutzer mehr Zeilen einträgt, wird ein Scrollbalken
   sichtbar.

