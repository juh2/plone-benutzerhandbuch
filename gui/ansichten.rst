==================
 Artikelansichten
==================

Mit dem Begriff :term:`Ansicht` wird eins der wichtigsten Elemente in
Plone bezeichnet. Mit Hilfe diverser Artikelansichten werden die
Inhalte einer Website dargestellt und bearbeitet. Welche Ansichten ein
Artikel besitzt, hängt von seinem Typ ab. Sie finden einen Überblick
über Artikelansichten und ihre Funktionen in Kapitel
:ref:`sec_artikeltypen`.

.. _sec_ui-rahmen:

Reiter und Menüs
================

Ein nicht angemeldeter Besucher der Website sieht in der Regel nur die
Anzeigeansicht eines Artikels. Wenn Sie an der Website angemeldet
sind, dürfen Sie jedoch für bestimmte Artikel mehrere Ansichten
sehen. Verschiedene Ansichten eines Artikels werden wie Karteikarten
dargestellt, zwischen denen man mit den Reitern in der grünen Leiste
wechselt. Neben den Reitern für die Ansichten können sich in der
grünen Leiste auch mehrere Ausklappmenüs befinden (siehe Abbildung
:ref:`fig_ui-leiste`).

.. _fig_ui-leiste:

.. figure:: ../images/leiste.*
   :width: 100%

   Reiter und Menüs am Beispiel eines Ordners

Je nachdem wie viel Platz im Browser zur Verfügung steht, sind die Reiter und
Ausklappmenüs entweder nebeneinander oder versetzt untereinander angeordnet. 

Jeder Reiter ist mit dem Namen der Ansicht beschriftet; der Reiter der
angezeigten Ansicht ist optisch hervorgehoben: in der Abbildung ist
die Ansicht :guilabel:`Anzeigen` geöffnet.

Je nach Ihren Berechtigungen sehen Sie folgende Ausklappmenüs:

Aktionen
  Hier können Sie den Artikel kopieren, verschieben, löschen, in der
  Zwischenablage gespeicherte Artikel in den aktuellen Ordner einfügen
  und eine Arbeitskopie des Artikels erstellen (siehe Abschnitt
  :ref:`sec_arbeitskopie-erstellen`).

Darstellung
  Falls es für den Artikel mehrere Darstellungsmöglichkeiten gibt,
  können Sie hier eine auswählen. Bei Ordnern haben Sie die
  Möglichkeit, einen Artikel aus dem Ordner als Anzeige zu setzen
  (siehe Abschnitt :ref:`sec_anzeige-waehlen`).

Hinzufügen
  Sie erstellen einen neuen Artikel im aktuellen Ordner, indem
  Sie hier den gewünschten Artikeltyp auswählen (siehe
  Abschnitt :ref:`sec_artikel-erstellen`).

Status
  Der Titel dieses Menüs zeigt den aktuellen Status des Artikels
  an. Die Menüeinträge sind die möglichen Statuswechsel (siehe
  Abschnitt :ref:`sec_workflow`).


Statusmeldung
=============

Wenn Sie an einem Artikel Veränderungen vornehmen, informiert Plone Sie über
den Erfolg oder Misserfolg Ihrer Aktion. Dazu erscheint unmittelbar nach der
Aktion auf der im Anschluss angezeigten Seite eine
Statusmeldung. Sie befindet sich oberhalb der Artikelansicht und ist farblich
hervorgehoben (siehe Abbildung :ref:`fig_statusmeldung`).

.. _fig_statusmeldung:

.. figure:: ../images/statusmeldung.*
   :width: 80%

   Eine Statusmeldung

Es gibt zwei Klassen von Statusmeldungen, die unterschiedliche Wichtigkeit
besitzen und durch jeweils eigene Farben gekennzeichnet werden:


Information (gelblich)
  beispielsweise die Anmeldebestätigung

.. Warnung (orange)
..   beispielsweise die Warnung vor defekten Verweisen beim Löschen
..   referenzierter Artikel

Fehler (rot)
  beispielsweise beim Speichern unvollständig ausgefüllter Formulare
  (siehe Abbildung :ref:`fig_statusmeldung-fehler`)

  .. _fig_statusmeldung-fehler:
  .. figure::
     ../images/statusmeldung-fehler.*
     :width: 100%
     :alt: Fehler: Bitte korrigieren Sie die angezeigten Fehler
     
     Meldung eines Fehlers


