
================
 Plone Glossary
================

PloneGlossary ist eine Erweiterung für Plone, mit der sich Glossare
erstellen lassen. Glossare dienen dazu, an einer zentralen Stelle
Begriffe zu erklären, die in den Texten der Website selbst nicht
oder nicht hinreichend erklärt werden. Die Begriffe, die im Glossar
erklärt werden, können in den Texten der Website hervorgehoben und mit
einem :term:`Tooltip` versehen werden, sodass die Benutzer, ohne die
Seite zu verlassen, eine Erklärung des Begriffs erhalten (siehe
Abbildung :ref:`fig_glossar-tooltip`) 

.. _fig_glossar-tooltip:

.. figure:: 
   ./images/tooltip-glossar.*
   :width: 100%
   :alt: Textseite mit markiertem Wort und Begriffsdefinition im
   	 Tooltip

   Begriffsdefinition im Tooltip

Ein Klick auf das markierte Wort bringt den Benutzer zum
entsprechenden Eintrag im Glossar (siehe Abbildung
:ref:`fig_glossareintrag`) .

Die Installation des Zusatzproduktes erfolgt wie in Kapitel
:ref:`sec_konfiguration-erweiterungen` beschrieben.


Hinzufügen eines Glossars
=========================

Nach der Installation von PloneGlossary kann ein weiterer Artikeltyp
mit der Bezeichnung »Glossar« auf der Website hinzugefügt
werden (siehe Abbildung :ref:`fig_hinzufuege-menue-glossary`). 

.. _fig_hinzufuege-menue-glossary:

.. figure:: 
   ./images/hinzufuege-menue-glossary.*
   :width: 60%
   :alt: Das Hinzufüge-Menü mit Eintrag »Glossary«

   Das Hinzufüge-Menü mit Eintrag »Glossary«

Wählen Sie im Hinzufüge-Menü den Eintrag »Glossar« aus, um ein Glossar
anzulegen. Sie können Titel und Beschreibung im Bearbeitungsformular eingeben.
Es ist möglich, auf einer Website mehrere Glossare anzulegen und von
unterschiedlichen Benutzern pflegen zu lassen. Sie können so jeweils
fachspezifische Glossare aufbauen.

.. _fig_neues-glossar:

.. figure::
   ./images/neues-glossar.*
   :width: 100%
   :alt: Ein neu angelegtes Glossar ohne Einträge

   Neu angelegtes Glossar

Hinzufügen einer Begriffsdefinition
===================================

Abbildung :ref:`fig_neues-glossar` zeigt ein neues Glossar mit dem
Titel »Küchenlexikon« unmittelbar nach der Erzeugung. Im Menü
:guilabel:`Hinzufügen` finden Sie den Eintrag :guilabel:`Glossar
Term`. Klicken Sie auf diesen Eintrag, wenn Sie eine
Begriffsdefinition hinzufügen möchten.

.. fig_definition-hinzufuegen:

.. figure::
   ./images/definition-hinzufuegen.*
   :width: 100%
   :alt: Bearbeitungsansicht einer Begriffsdefinition

   Bearbeitungsansicht einer Begriffsdefinition

Im Bearbeitungsformular einer Begriffsdefinition finden Sie folgende
Felder vor:

Begriff
  In dieses Feld wird der Begriff, der definiert werden soll,
  eingetragen.

Varianten
  Im Feld Varianten können Sie abweichende Schreibungen des gleichen
  Begriffs, weitere grammatikalische Formen (konjugierter oder
  deklinierter Begriff) oder Synonyme eintragen. Alle Begriffe, die
  Sie hier eintragen, fungieren später als Link zur Begriffsdefinition.

Definition
  Im Feld Definition wird der Begriff schließlich erklärt. Ihnen
  stehen hier alle Funktionen des Texteditors zur Verfügung.

Speichern Sie anschließend Ihre Eingaben, um zur Anzeige der
Begriffsdefinition zu gelangen.

.. _fig_glossareintrag:

.. figure::
   ./images/glossareintrag.*
   :width: 100%
   :alt: Definition des Begriffs »Pochieren«
   
   Anzeige einer Begriffsdefinition

Navigation im Glossar
=====================

Das Glossar ist alphabetisch sortiert. Es werden pro Seite 30 Einträge
angezeigt. Die übrigen Einträge erscheinen auf Folgeseiten.

Man kann die Anzeige auf Begriffe, die mit einem bestimmten Buchstaben
beginnen, eingrenzen, indem man auf den gewünschten Buchstaben in der
Buchstabenleiste klickt. Der ausgewählte Buchstabe wird hervorgehoben
und die Anzeige auf die entsprechenden Einträge eingeschränkt (siehe
Abbildung :ref:`fig_glossar-navigation`).

.. _fig_glossar-navigation:

.. figure::
   ./images/glossar-navigation.*
   :width: 100%
   :alt: Anzeige eines Glossars

   Anzeige eines Glossars

Über ein Suchfeld kann man im Glossar eine Volltextsuche
durchführen. Falls der gesuchte Begriff nur einmal im Glossar
vorkommt, wird man sofort zur Anzeige der entsprechenden
Begrifferklärung weitergeleitet. Ansonsten werden die Definitionen, in
denen der Suchbegriff vorkommt unterhalb des Suchformulars aufgelistet.

Glossar-Portlet
===============

Das Glossar-Portlet (siehe Abbildung :ref:`fig_portlet-glossar`) zeigt
diejenigen Begriffe an, die im aktuell angezeigten Artikel benutzt und
im Glossar erklärt werden. Die Begriffe sind Verweise zur jeweiligen
Begriffserklärung im Glossar.

.. _fig_portlet-glossar:

.. figure::
   ./images/portlet-glossar.*
   :width: 40%
   :alt: Portlet mit dem Begriff »Pochieren«

   Glossar-Portlet


Konfiguration
=============

Für PloneGlossary gibt es Konfigurationsmöglichkeiten in der
Website-Konfiguration unter der Überschrift »Konfiguration von
Zusatzprodukten«. Sie finden dort nach der Installation von
PloneGlossary einen entsprechenden Verweis, der Sie zum
Konfigurationsformular führt (siehe Abbildung
:ref:`fig_ploneglossary-konfigurieren`).

.. _fig_ploneglossary-konfigurieren:

.. figure::
   ./images/ploneglossary-konfigurieren.*
   :width: 100%
   :alt: Die Konfigurationsmöglichkeiten für PloneGlossary

   Die Konfigurationsmöglichkeiten für PloneGlossary


Das Konfigurationsformular ist folgendermaßen aufgebaut:

Hervorhebungen im Inhalt?  
   Markieren Sie diese Option, wenn die im Glossar erklärten Begriffe
   im Text hervorgehoben werden sollen. 

Länge der Definition
   Mit dieser Option können Sie bestimmen, wie viele Zeichen aus der
   Begriffsdefinition im :term:`Tooltip` angezeigt werden sollen. Wenn
   die gesamte Definition angezeigt werden soll, geben Sie hier ›0‹
   ein. Diese Einstellung begrenzt selbstverständlich nicht die Länge
   der Begriffsdefinition im Glossar selbst.

Auslassungszeichen
   Wenn Sie die Länge der im :term:`Tooltip` angezeigten
   Begriffsdefinition begrenzt haben, informieren die hier
   eingegebenen Zeichen den Benutzer darüber, dass die Definition
   länger als angezeigt ist.

Nicht hervorheben 
   In der Regel ist es nicht wünschenswert, dass die erklärten
   Begriffe überall im Text hervorgehoben werden. Die Hervorhebung
   stört beispielsweise in Verweisen, die ohnehin hervorgehoben sind
   und in Überschriften oder Eingabefeldern, da hier die Hervorhebung
   oft störend ins Auge fällt. In diesem Feld bestimmen Sie die
   HTML-Tags, in denen erklärte Begriffe nicht hervorgehoben werden
   sollen. In der Voreinstellung wird die Hervorhebung in den
   HTML-Tags ›a‹, ›h1‹, ›input‹ und ›textarea‹ unterdrückt.

Erlaubte Portaltypen
   In dieser Liste können Sie bestimmen, in welchen Artikeltypen
   erklärte Begriffe hervorgehoben werden sollen. In der
   Voreinstellung sind »Seite«, »Termin« und »Nachricht« ausgewählt.

Verwende Glossare global für jeden Inhalt?
   Wenn Sie in verschiedenen Bereichen der Website unterschiedliche
   Glossare verwenden, können Sie mit dieser Option bestimmen, ob
   grundsätzlich alle Glossare herangezogen werden sollen, wenn es
   darum geht, erklärte Begriffe im Text hervorzuheben beziehungsweise
   im Glossar-Portlet anzuzeigen oder nur das Glossar, das in der
   entsprechenden Ordner-Hierarchie als erstes gefunden wird. Wenn Sie
   in unterschiedlichen Bereichen der Website fachspezifische Glossare
   pflegen wollen, deren Begriffe nur im jeweiligen Bereich
   hervorgehoben werden sollen, dann belassen Sie es bei der
   Voreinstellung und wählen Sie diese Option nicht an.
 
Generelles Glossar
   In dem Auswahlfeld werden alle Glossare angezeigt, die es auf der
   Website gibt. Sie können hier bestimmen, welche Glossare im
   Einzelnen herangezogen werden, wenn es darum geht, erklärte
   Begriffe im Text hervorzuheben oder im Glossar-Portlet
   anzuzeigen. Wenn alle Glossare herangezogenen werden sollen, dann
   wählen Sie entweder alle oder kein Glossar aus. Beides wirkt sich
   gleich aus.
