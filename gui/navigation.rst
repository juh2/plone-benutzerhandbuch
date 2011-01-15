.. _sec_navigation:

============
 Navigation
============

Es gibt im Großen und Ganzen zwei Möglichkeiten, sich gezielt durch
eine Plone-Website zu bewegen:

* Orientierung an der Ordnerhierarchie: Hauptnavigation und
  Navigationsportlet, Übersicht und Verzeichnispfad
* Suche: Sofortsuche und erweiterte Suche


Ordnerhierarchie
================

Es gibt vier Elemente auf fast jeder Seite einer Plone-Website, mit deren
Hilfe Sie sich durch ihre Ordnerhierarchie bewegen können: die
Hauptnavigation, das Navigationsportlet, die Übersicht und den
Verzeichnispfad. Diese Elemente ergänzen einander. Hauptnavigation,
Navigationsportlet und Übersicht geben einen Überblick über den
Inhalt der Website, wobei der Schwerpunkt beim Portlet auf dem gerade
besuchten Teil liegt. Der Verzeichnispfad teilt Ihnen mit, an welcher Stelle
in der Ordnerhierarchie der Website Sie sich befinden.

Hauptnavigation
---------------

Die Hauptnavigation ist auf jeder Seite der Website verfügbar. Sie befindet
sich im Seitenkopf (siehe Abbildung :ref:`fig_hauptnavigation`) und
enthält Verweise auf wichtige Stellen der Website.

.. _fig_hauptnavigation:

.. figure:: ../images/hauptnavigation.*
   :width: 80%

   Hauptnavigation und Verzeichnispfad

Plone bringt einige dieser Verweise bereits mit (siehe
Tabelle :ref:`Einträge in Navigation <tab_hauptnavigation>`).

.. _tab_hauptnavigation:

.. table:: Die Elemente in der Hauptnavigation

   +-------------+---------------------------+----------------------------+
   | Titel       | Ziel                      | siehe Seite                |
   +=============+===========================+============================+
   | Startseite  | Anzeige des Wurzelordners |                            |
   +-------------+---------------------------+----------------------------+
   | Nachrichten | Nachrichtenüberblick      | :ref:`sec_nachricht`       |
   +-------------+---------------------------+----------------------------+
   | Termine     | Terminübersicht           | :ref:`sec_termin`          |
   +-------------+---------------------------+----------------------------+
   | Benutzer    | Benutzersuche             | :ref:`sec_mitgliedersuche` |
   +-------------+---------------------------+----------------------------+


Zusätzlich zu den genannten Einträgen erzeugt Plone in der
Grundeinstellung weitere Verweise auf alle Ordner, die sich direkt im
Wurzelordner der Website befinden. Die Verweise sind mit dem Titel des
jeweiligen Ordners beschriftet. Falls die Website entsprechend
konfiguriert ist, nimmt Plone auf diese Weise nicht nur Ordner,
sondern auch andere Artikeltypen aus dem Wurzelordner, die Sie
einsehen dürfen, in die Hauptnavigation auf.

.. _sec_navigation-portlet:

Navigationsportlet
------------------

Das Navigationsportlet (siehe Abbildung :ref:`fig_portlet-navigation`)
zeigt einen Teil der Website als Ordnerbaum an. Dabei werden wiederum
nur solche Ordner und Artikel aufgeführt, die der jeweilige Benutzer
einsehen darf. Viele Eigenschaften des Navigationsportlets hängen von
der Konfiguration der Website ab. Per Voreinstellung wird das Portlet
auf der Startseite nicht angezeigt, sondern erscheint erst in den
einzelnen Ordnern der Website.

.. _fig_portlet-navigation:

.. figure:: ../images/portlet-navigation.*
   :width: 40%

   Navigationsportlet

Da die Ordnerhierarchie einer großen Website sehr umfangreich und
unübersichtlich werden kann, wird nie der gesamte Baum gleichzeitig
dargestellt. Das Navigationsportlet zeigt stets nur den Teil Ihrer
Website an, der sich innerhalb eines Ordners befindet und den gerade
besuchten Artikel enthält.

Per Voreinstellung beginnt die Anzeige immer mit einem Ordner, der
selbst direkt im Wurzelordner der Website liegt. Damit bildet das
Navigationsportlet gerade ein Gegenstück zur Hauptnavigation. Ob der
betreffende Ordner selbst als oberster Eintrag im Navigationsportlet
auftaucht, hängt ebenfalls von der Konfiguration ab.

Der Eintrag für den gerade besuchten Artikel wird grau
hinterlegt. Jeder Eintrag im Navigationsportlet ist ein Verweis zu
einem Ordner oder einem anderen Artikel.

Da das Navigationsportlet wie alle Portlets für jeden Ordner, ja sogar
für einzelne Artikel, individuell konfiguriert werden kann, ist es
möglich, dass es sich nicht auf jeder Seite gleichartig verhält.

.. _sec_sitemap:

Übersicht
---------

Unter den Verweisen im Fuß jeder Seite finden Sie die Übersicht.  Die
Übersicht, oft auch »Sitemap« genannt, ist eine Baumdarstellung aller
Artikel der Website, die mit dem Wurzelordner beginnt und bis zu einer
bestimmten Tiefe der Ordnerhierarchie reicht. Per Voreinstellung
werden Ordner bis zur dritten Ebene erfasst (siehe Abbildung
:ref:`fig_sitemap`). Es werden auch hier nur die Artikel
berücksichtigt, die der Benutzer betrachten darf. Jeder Eintrag in der
Übersicht ist ein Verweis zur Anzeige des jeweiligen Artikels.

.. _fig_sitemap:

.. figure:: ../images/sitemap.*
   :width: 100%

   Übersicht

Verzeichnispfad
---------------

Sie können den Verzeichnispfad, englisch »breadcrumb menu«, als eine
Art Brotkrumenspur verstehen, die den Wurzelordner der Website durch
die Ordnerhierarchie hindurch mit dem aktuell angezeigten Artikel
verbindet. Das erste Element des Pfads ist der Wurzelordner der
Website (siehe Abbildung :ref:`fig_hauptnavigation`). Danach folgen
alle Unterordner, in die Sie nacheinander wechseln müssen, um vom
Wurzelordner zum gerade angezeigten Artikel zu gelangen. Der aktuelle
Artikel bildet den letzten Teil des Pfads. Alle Elemente des
Verzeichnispfads sind Verweise zu den jeweiligen Orten auf der
Website.

.. _sec_suche:

Suche
=====

Sie können den Inhalt einer Plone-Website durchsuchen. So finden Sie
beispielsweise alle Artikel, die ein bestimmtes Wort enthalten. Plone
stellt Ihnen sowohl ein einfaches Suchfeld als auch eine erweiterte
Suche zur Verfügung. Sie finden immer nur solche Artikel, die Sie auch
einsehen dürfen.

Die Liste der Suchergebnisse enthält für jeden Treffer den Titel und
die Beschreibung, eine Prozentangabe zur Relevanz, den Ersteller, das
Datum der letzten Änderung und die Kategorien.  Ein Symbol links vom
Titel zeigt Ihnen den Artikeltyp an. Der Titel ist ein Verweis zum
jeweiligen Artikel. Listen mit mehr als 30 Treffern werden auf mehrere
Seiten verteilt, wobei Sie jeweils am Ende der Seiten Verweise zu den
anderen Teillisten finden.

.. _sec_sofortsuche: 

Suchfeld
--------

In das Suchfeld im Kopf jeder Plone-Seite können Sie einen oder mehrere
Suchbegriffe eingeben. Bereits während der Eingabe zeigt Plone in der Sofortsuche
Treffer an (siehe Abbildung :ref:`fig_sofortsuche`).

.. _fig_sofortsuche:

.. figure:: ../images/sofortsuche.*
   :width: 70%

   Sofortsuche

Sie können sich sowohl mit den Pfeiltasten durch die Liste bewegen und
mit der Eingabetaste ein Ergebnis auswählen, als auch die Maus dafür
benutzen. Wenn Sie Javascript ausgeschaltet haben, steht Ihnen die
Sofortsuche nicht zur Verfügung.

Mit der Schaltfläche :guilabel:`Suche` führen Sie eine Volltextsuche
in Titel, Beschreibung und Inhalt aller Artikel der Website
durch. Wenn Sie nur in dem Ordner suchen wollen, in dem Sie sich
gerade befinden, markieren Sie direkt unterhalb des Suchfeldes die
Option :guilabel:`nur im aktuellen Bereich`.

Komplexe Suchen und Stoppwörter
-------------------------------

Wenn Sie bei einer Suche mehrere Suchbegriffe eingeben, findet Plone
Artikel, die jeden der Begriffe enthalten. Dabei können die Begriffe
an beliebigen Stellen im Text stehen. Um nach einer Wortgruppe zu
suchen, die als Ganzes im Artikeltext vorkommt, schreiben Sie sie in
Anführungszeichen.

Sie können auch nach Artikeln suchen, die mindestens eines von
mehreren Suchwörtern enthalten, indem Sie die Suchwörter mit ``OR``
(»oder«) verknüpfen. Dadurch werden in der Regel mehr Artikel gefunden
als bei einer Suche nach Artikeln mit allen Suchwörtern. Neben ``OR``
gibt es auch die Verknüpfungsoperation ``AND`` (»und«), die
gleichbedeutend damit ist, mehrere Wörter einfach hintereinander zu
schreiben.

Sie können beide Arten der Verknüpfung von Suchbegriffen mischen. Wenn
Sie beispielsweise nach einem Seminar oder einem Workshop für
Textverarbeitung suchen, können Sie die Suche »Textverarbeitung AND
(Seminar OR Workshop)« eingeben. In diesem Beispiel findet Plone
Artikel, in denen sowohl das Wort »Textverarbeitung« als auch
wenigstens einer der Begriffe »Seminar« und »Workshop« vorkommt.

Stoppwörter, also häufig benutzte Wörter wie »der«, »die«, »das«,
werden von Plone bei einer Suchanfrage ignoriert.

Komplexe Suchen mit Verknüpfungen oder Wortgruppen sowie die Filterung
von Stoppwörtern stehen in der Sofortsuche nicht zur Verfügung. Wenn
Sie diese Funktionen benutzen wollen, müssen Sie eine reguläre
Suchanfrage über die Schaltfläche :guilabel:`Suche` durchführen oder
die erweiterte Suche benutzen.

Erweiterte Suche
----------------

In der Ergebnisliste des Suchfelds finden Sie einen Verweis zum
Formular für die erweiterte Suche. Damit können Sie Ihre Suche
verfeinern, indem Sie beispielsweise die zu durchsuchenden
Artikeleigenschaften einschränken oder andere Suchkriterien als die
Volltextsuche auswählen. Das Formular für die erweiterte Suche (siehe
Abbildung :ref:`fig_erweiterte-suche`) ist folgendermaßen aufgebaut.

.. _fig_erweiterte-suche:

.. figure::
   ../images/erweiterte-suche.*
   :width: 80%
   :alt: Das Formular für die erweiterte Suche

   Erweiterte Suche

Gesuchter Text
   Dies ist das Feld für die Volltextsuche. Es verhält sich ebenso wie
   das Feld auf dem einfachen Suchformular.

Stichworte
   In dem Auswahlmenü können Sie beliebig viele Stichworte
   auswählen. Die Suche findet dann Artikel, die entweder alle Stichworte
   enthalten oder mindestens eins dieser Stichworte, je nachdem,
   welche Option Sie unterhalb des Auswahlmenüs aktivieren.

Mehr Suchoptionen
~~~~~~~~~~~~~~~~~

.. |pfeil| image:: ../images/plone_images/arrowRight.png

Um das Formular übersichtlich zu halten, sind die weiteren
Suchoptionen eingeklappt. Sie können sie durch einen Klick auf das
Pfeilsymbol |pfeil| aufklappen. 

.. _fig_mehr-suchoptionen:

.. figure::
   ../images/mehr-such-optionen.*
   :width: 80%
   :alt: Weitere aufklappte Suchoptionen

   Weitere aufgeklappte Suchoptionen

Artikeltyp 
  Kreuzen Sie die Artikeltypen an, die bei der Suche eingeschlossen
  werden sollen. Das Setzen oder Entfernen des Häkchens bei
  :guilabel:`Alle/Keine auswählen` wirkt sich auf alle Artikeltypen
  aus.

Neue Artikel seit
  Hiermit können Sie die Suche zeitlich eingrenzen, in dem Sie nur
  nach den Artikeln suchen, die in einem bestimmten Zeitraum neu
  hinzugekommen sind. Zur Auswahl stehen:

  * Immer (Voreinstellung, bedeutet keine zeitliche Einschränkung)
  * Zuletzt angemeldet (Eingrenzung auf die Artikel, die seit Ihrer
    letzten Anmeldung hinzugekommen sind.)
  * Gestern (Artikel, die in den letzten 24 Stunden hinzugekommen sind.)
  * Letzte Woche 
  * Letzter Monat

Revisionsstatus 
 Diese Option grenzt die Suchergebnisse auf Artikel mit dem
  gewünschten Status ein. Zur Auswahl stehen alle verfügbaren
  Status. Angezeigt werden nur die Artikel, auf die der Benutzer
  zugreifen darf. Anonymen Benutzern steht die Option nicht zur
  Verfügung.

Autor
  Diese Option grenzt die Suchergebnisse auf Artikel ein, die von dem
  ausgewählten Autor verfasst wurden. Im Auswahlmenü finden Sie die
  Benutzernamen der zur Auswahl stehenden Autoren. 

Anzeigeoptionen
~~~~~~~~~~~~~~~

Mit Hilfe der Anzeigeoptionen können Sie Einfluss auf die Darstellung
der Suchergebnisse nehmen. 

Suchergebnisse
  Sie können die Ergebnisse sortieren nach:

  * Relevanz (Voreinstellung)
  * Erstellungsdatum
  * Änderungsdatum
  * Titel 

Ergebnisse pro Seite
  Mit dieser Option können Sie festlegen, ob 30, 60 oder 90 Treffer
  pro Seite angezeigt werden sollen. Werden mehr Artikel gefunden,
  werden die Ergebnisse auf mehreren Seiten verteilt, die Sie
  nacheinander aufrufen können. 

Die Ergebnisse einer erweiterten Suche müssen alle angegebenen
Kriterien gleichzeitig erfüllen. Irrelevante Angaben schränken daher
die Suche unnötig ein. Mit folgenden Werten und Eingaben stellen Sie
sicher, dass die Suchergebnisse nicht eingeschränkt werden:

* für ein Textfeld: keine Eingabe
* für die Stichwortsuche: keine Auswahl
* für Artikeltyp und Revisionsstatus: jeden Wert erlauben
* für die Altersgrenze für neue Artikel: »immer«
* für den Autor: »jeder Autor«

.. _sec_suchportlet:

Suchportlet
-----------

Ihre Website kann so konfiguriert sein, dass das Suchfeld in einem eigenen
Portlet erscheint (siehe Abbildung :ref:`fig_portlet-suche`).

.. _fig_portlet-suche:

.. figure:: ../images/portlet-suche.*
   :width: 40%

   Suchportlet

Das Suchportlet funktioniert genauso wie das Suchfeld im
Seitenkopf. Sie können allerdings die Suchergebnisse nicht auf den
Bereich eingrenzen, in dem Sie sich gerade befinden.
