===============
 Auswahlfelder
===============

.. _sec_checkbox-field:

Checkbox-Feld
=============

Bei einer Checkbox kann der Benutzer, der das Formular ausfüllt, ein
Häkchen setzen oder nicht.  

.. _fig_checkbox-feld:

.. figure::
   ./images/checkbox-feld.*
   :width: 80%
   :alt: Hinzufügeformular für ein Checkbox-Feld

   Checkbox

Neben den bekannten Konfigurationsmöglichkeiten gibt es folgende
Besonderheiten (siehe Abbildung :ref:`fig_checkbox-feld`):

Standard
   Wenn diese Option ausgewählt wird, ist im Formular bei der Checkbox
   bereits ein Häkchen gesetzt. 

Validator
   Mit Hilfe des Validators können Sie sicherstellen, dass bei der
   Checkbox das Häkchen gesetzt wurde (ist ausgewählt) oder nicht (ist
   nicht ausgewählt). In der Voreinstellung wird keine Prüfung
   vorgenommmen (Keins). Diese Option eignet sich zum Beispiel dafür,
   die Anerkennung von Nutzungsbedingungen beim Absenden des Formulars
   zu erzwingen.

Anzeigetext für "True"
   Auf der Danke-Seite wird der Benutzer darüber informiert, welche
   Eingaben er gemacht hat. Hier können Sie statt der voreingestellten
   »1« eine verständlichere Formulierung wie zum Beispiel
   »Nutzungsbedingungen anerkannt« eintragen.

Anzeigetext für "False"
   Wie beim True Display String können Sie hier eine Formulierung
   eintragen, die auf der Danke-Seite angezeigt wird, wenn das Häkchen
   nicht gesetzt wurde: zum Beispiel »Ich will keine Werbung
   erhalten«.

.. _sec_datum-und-zeit-feld:    

Datums- und Zeitfeld
====================

Das Datums- und Zeitfeld erleichtert dem Benutzer die Eingabe von
Datums- und Zeitangaben. 

.. _fig_datum-zeit-feld:

.. figure::
   ./images/datum-zeit-feld.*
   :width: 80%
   :alt: Hinzufügeformular für ein Datums- und Uhrzeit-Feld

   Feld für Datum und Uhrzeit

Neben den bekannten Konfigurationsmöglichkeiten ist Folgendes zu
beachten (siehe Abbildung :ref:`fig_datum-zeit-feld`):

Standard
   Für die Vorgabe eines Standard-Datums stehen Ihnen mehrere Formate
   zur Verfügung, zum Beispiel: 1963/04/13, 1963-04-13 oder
   13.04.1963. Uhrzeiten: 18:00, 18.00, 6:00pm

Zeit-Auswahl-Optionen anzeigen
   Wenn die Eingabe einer Uhrzeit nicht sinnvoll ist, können Sie diese
   Option abwählen. Die Auswahlmenüs für die Eingabe einer Uhrzeit
   stehen dann auf dem Formular nicht zur Verfügung.

Erstes Jahr
   Das erste Jahr, das im Auswahlmenü zur Verfügung stehen soll.

Letztes Jahr
   Das letzte Jahr, das im Auswahlmenü zur Verfügung stehen soll.

Anzahl zukünftiger Jahre
   Wenn Sie kein letztes Jahr angegeben haben, können Sie hier die
   Anzahl der in der Zukunft liegenden Jahre angeben, die im
   Auswahlmenü angezeigt werden sollen. 

.. _sec_auswahl-feld: 

Auswahlfeld
===========

Mit Hilfe eines Auswahlfeldes kann der Benutzer unter vorgegebenen
Werten eine Auswahl treffen. Er kann dabei immer nur einen Wert
auswählen. 

.. _fig_auswahl-feld:

.. figure::
   ./images/auswahl-feld.*
   :width: 80%
   :alt: Hinzufügeformular für ein Auswahl-Feld

   Auswahlfeld

Beim Anlegen eines Auswahlfeldes ist Folgendes zu beachten (siehe
Abbildung :ref:`fig_auswahl-feld`):

Standard
   Falls Sie eine Vorgabe machen möchten, müssen Sie in dieses Feld
   den gewünschten »Wert« schreiben. Dieser kann von der
   »Bezeichnung«, die im Formular angezeigt wird abweichen. 

Optionen 
   Die Auswahlmöglichkeiten, die zur Wahl stehen: pro Option eine Zeile. 

   Sie können hier eine spezielle Schreibweise benutzen. Dadurch können Sie die
   Bezeichnung für die Option, die im Formular benutzt wird, von dem Wert, der
   weiterverarbeitet wird, trennen. Das Format ist »Wert|Bezeichnung«. Wenn Sie
   ein solches Format benutzen, müssen Sie bei Vorgabe eines Standards den
   »Wert« benutzen.

Präsentations-Widget
   Sie können das Formularfeld auf zwei Arten darstellen: als
   Auswahlmenü (Dropdown-Menü) oder mit Radiobuttons. Man kann die
   Wahl des Widgets auch Plone überlassen (Voreinstellung). Abbildung
   :ref:`fig_auswahl-feld-anzeige` zeigt beide Möglichkeiten.

.. _fig_auswahl-feld-anzeige:

.. figure::
   ./images/auswahl-feld-anzeige.*
   :width: 70%
   :alt: Auswahlfeld mit Auswahlmenü oder mit Radiobuttons

   Auswahlfeld mit Auswahlmenü (links) und Radiobuttons (rechts)

.. _sec_mehrfach-auswahl-feld:

Mehrfachauswahlfeld
===================

Während beim Auswahl-Feld der Benutzer nur eine Option auswählen kann,
kann er beim Mehrfach-Auswahl-Feld (Abbildung
:ref:`fig_mehrfach-auswahl-feld`) mehrere Möglichkeiten auswählen. 

.. _fig_mehrfach-auswahl-feld:

.. figure::
   ./images/mehrfach-auswahl-feld.*
   :width: 80%
   :alt: Hinzufügeformular für ein Mehrfach-Auswahl-Feld

   Feld für Mehrfach-Auswahl

Die Einstellungsmöglichkeiten wurden bereits erklärt. Abbildung
:ref:`fig_mehrfach-auswahl-feld-wert-bezeichnung` zeigt ein Beispiel für die
Notation »Wert|Bezeichnung«, die in :ref:`sec_auswahl-feld` erklärt wurde.
Abbildung :ref:`fig_mehrfach-auswahl-feld-anzeige` zeigt die beiden möglichen
Präsentations-Widgets.

.. _fig_mehrfach-auswahl-feld-wert-bezeichnung:

.. figure::
   ./images/mehrfach-auswahl-feld-wert-bezeichnung.*
   :width: 80%
   :alt: Schreibweise von Wert und Bezeichnung

   Schreibweise Wert|Bezeichnung


.. _fig_mehrfach-auswahl-feld-anzeige:

.. figure::
   ./images/mehrfach-auswahl-feld-anzeige.*
   :width: 80%
   :alt: Anzeigevarianten eines Mehrfach-Auswahl-Feldes

   Mehrfachauswahl-Feld mit Auswahlfeld (links) und Checkboxen (rechts)


.. _sec_bewertungs-feld:

Bewertungsfeld
==============

Ein Bewertungs-Feld gibt dem Benutzer die Möglichkeit, anhand
einer vorgegebenen Skala eine Bewertung vorzunehmen. 

.. _fig_bewertungs-feld:

.. figure::
   ./images/bewertungs-feld.*
   :width: 80%
   :alt: Hinzufügeformular für ein Bewertungs-Feld

   Bewertungs-Feld

In der Bearbeitungsansicht dieses Formularfeldes ist Folgendes zu
beachten (siehe Abbildung :ref:`fig_bewertungs-feld`):

Fragen 
   In dieses Feld werden die Punkte eingetragen, die bewertet werden
   sollen. Pro Zeile ein zu bewertender Punkt. Dies können wie die
   Bezeichnung des Feldes nahelegt »Fragen« sein, wie zum Beispiel:
   »Wie hat Ihnen das Seminar gefallen?« Es können aber auch Aussagen
   sein, die der Benutzer bewerten soll.

Antworten
   In dieses Feld tragen Sie die Bewertungsskala ein. Pro
   Skaleneinheit eine Zeile. In der Voreinstellung finden Sie eine
   beispielhafte Skala vor, die die Zustimmung zu einer Aussage ausdrücken
   soll.

Abbildung :ref:`fig_bewertungs-feld-anzeige` zeigt die Anzeige eines
Bewertungs-Feldes. 

.. _fig_bewertungs-feld-anzeige:

.. figure::
   ./images/bewertungs-feld-anzeige.*
   :width: 80%
   :alt: Anzeige des Bewertungs-Felds

   Bewertungs-Feld Anzeige




