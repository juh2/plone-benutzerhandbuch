.. |close| image:: ../images/pb_close.png

.. todo:: 
   Neue Screenshots anfertigen, wenn Übersetzung vervollständigt ist.

.. _sec_kollektion:

============
 Kollektion
============

Oft möchte man Artikel, die sich in unterschiedlichen Ordnern einer Website
befinden an einem Ort zusammenfassen. Dies kann beispielsweise eine
Nachrichtenübersicht sein oder eine Liste aller Artikel, die sich einem
bestimmten Thema widmen. Diese Aufgabe wird in Plone mit Hilfe von Kollektionen gelöst.

Eine Kollektion sieht aus wie ein Ordner, ist aber eine gespeicherte
Suchanfrage. Die Ergebnisse der Suche werden so aufgelistet, als ob sich die
Artikel in einem gemeinsamen Ordner befinden.  Plone hält die Artikelauswahl
anhand der einmal eingestellten Suchkriterien stets aktuell.

Anzeige
=======

Nach außen verhalten sich Kollektionen wie Ordner. Wie bei Ordnern gibt es
verschiedene Darstellungen für die Anzeigeansicht, aus denen Sie im
Darstellungsmenü wählen können:

* Kurzfassung
* Gesamter Inhalt
* Tabelle
* Album
* Liste

Als Beispiel zeigt Abbildung :ref:`fig_kollektion` die Darstellung als Liste.

.. _fig_kollektion:

.. figure:: ../images/kollektion.*
   :width: 100%
   
   Darstellung einer Kollektion als Liste

Die Darstellungsvarianten funktionieren so wie bei Ordnern. Die tabellarische
Darstellung ist in der Bearbeitungsansicht der Kollektion konfigurierbar. 

Wie Ordner besitzen Kollektionen auch keinen eigenen redaktionellen Inhalt. 

.. _sec_kollektion-bearbeiten:

Bearbeitungsansicht
===================

Wenn Sie eine Kollektion hinzufügen, gelangen Sie in die
Bearbeitungsansicht, in der Sie neben dem Titel und der Zusammenfassung
auch die Suchkriterien eingeben können.

.. _fig_kollektion-bearbeiten-oben:

.. figure:: ../images/kollektion-bearbeiten-oben.*
   :alt: Die obere Hälfte des Bearbeitungsformulars

   Bearbeitungsansicht einer Kollektion (oberer Teil)

Unterhalb der Zusammenfassung geben Sie die Suchkriterien mit Hilfe
eines Auswahlmenüs ein. Es stehen dort diverse Suchparameter zur
Verfügung, die in drei Gruppe sortiert sind: datumsbezogene Kriterien,
Textkriterien und Metadaten.

Daten
   * Freigabedatum 
   * Änderungsdatum 
   * Erstellungsdatum 
   * Ablaufdatum 
   * Terminende 
   * Terminanfang 
Metadata
   * Kurzname (id)
   * Artikeltyp 
   * Ort
   * Ersteller
   * Status 
Text
   * Searchable text
   * Stichwort 
   * Beschreibung
   * Titel

Wenn Sie einen dieser Parameter auswählen, verändert sich die
Darstellung der Anzeige. Es erscheinen zwei weitere Auswahlmenüs. Das
erste kann eine logische Verknüpfung enthalten oder das
Auswahlkriterium genauer eingrenzen Im zweiten neuen Auswahlmenü
wählen Sie den gewünschten Wert aus. In dem Beispiel in
Abb. :ref:`fig_kollektion-suchkriterium-type` wurde der Parameter
»Artikeltyp« ausgewählt. Im zweiten Auswahlmenü befindet sich
der logische Operator »Ist« und im dritten Auswahlmenü erscheinen die
zur Verfügung stehenden Artikeltypen.

.. todo:: Neuer Screenshot

.. _fig_kollektion-suchkriterium-type:

.. figure::
   ../images/kollektion-suchkriterium-type.*
   :alt: Auswahl von Suchkriterien mit Hilfe von Auswahlmenüs

   Auswahl eines Suchkriteriums

Sie können einen oder mehrere Artikeltypen auswählen, indem Sie in dem
Auswahlkästchen einen Haken setzen. Im Beispiel wurde der Artikeltyp
»Bild« ausgewählt, woraufhin in der Vorschau die Treffer
angezeigt werden, die zu dem ausgewählten Suchkriterium passen (siehe
Abb.: :ref:`fig_kollektion-vorschau`).

.. _fig_kollektion-vorschau:

.. figure::
   ../images/kollektion-vorschau.*
   :alt: Die Vorschau zeigt sofort die gefundenen Treffer an

   Vorschau der Treffer

Es sind folgende Kombinationen möglich:

.. todo:: Neue Tabelle als Bild einfügen


.. _fig_kollektion-kriterien-tabelle:

.. figure::
   ../images/kollektion-kriterien-tabelle.*
   :alt: Tabelle mit den Kombinationsmöglichkeiten

   Tabelle der Kombinationsmöglichkeiten

Experimentieren Sie mit den Einstellmöglichkeiten. In der Vorschau sehen Sie
das Ergebnis Ihrer Auswahl. Die Eingabemöglichkeiten sind in Tabelle
:ref:`fig_kollektion-kriterien-tabelle` aufgeführt. 

Tage
  Geben Sie die Anzahl der Tage als positive oder negative Zahl
  ein. *Innerhalb der letzten* **6** *days* führt zum gleichen Ergebnis wie
  *In den nächsten* **-6** *days*. 
Datum
  Geben Sie ein Datum im Format TT/MM/YYYY ein. Sobald Sie in das
  Textfeld klicken, öffnet sich ein Datumsmenü, mit dem Sie das Datum
  bequem eingeben können (siehe Abb.:
  :ref:`fig_kollektion-suchkriterium-between-dates`). 

  .. _fig_kollektion-suchkriterium-between-dates:

  .. figure::
     ../images/kollektion-suchkriterium-between-dates.*
     :alt: Auswahl eines Datums mit Hilfe eines Widgets

     Bequeme Datumsauswahl

Textfeld
    Geben Sie eine Zeichenfolge ein. Geben Sie ein oder mehrere Wörter
    ein, die im durchsuchten Feld enthalten sein sollen. Die
    Reihenfolge mehrerer Wörter wird nur berücksichtigt, wenn Sie die
    Wortfolge in Anführungszeichen setzen. Sie können auch nach
    Wortbestandteilen suchen, indem Sie ähnlich wie bei der
    Website-Suche Platzhalter benutzen (siehe Abschnitt
    :ref:`sec_suche`).

    Wenn Sie einen relativen Pfad zu einem Ort in der Website
    eintragen wollen, so müssen Sie sich an eine bestimmte Konvention
    halten. Wählen Sie eine der folgenden Schreibweisen:

    * ›..‹ für den Ordner, in dem sich die Kollektion befindet

    * ›../..‹ für den Ordner über dem Ordner, in dem sich die Kollektion
      befindet. Diese Zeichenkette lässt sich bis zum Wurzelordner der Website
      verlängern, zum Beispiel: ›../../../‹

    * ›../ordnername‹ für den Ordner ›ordnername‹, der sich mit der Kollektion
      im gleichen Ordner befindet.


Auswahlmenü
  Bei vielen Kriterien hilft Ihnen ein Auswahlmenü bei der Eingabe des
  Wertes. 

Wenn Sie mehrere Suchparameter eingeben, so wird die Suche nach und
nach eingegrenzt (siehe Abb.:
:ref:`fig_kollektion-mehrere-suchkriterien`). Die Anzahl der
gefundenden Artikel wird ganz rechts angegeben. In dem Beispiel wird
mit Hilfe des ersten Suchkriteriums vier Artikel, durch Hinzunahme des
zweiten nur noch ein Artikel gefunden.

.. _fig_kollektion-mehrere-suchkriterien:

.. figure::
   ../images/kollektion-mehrere-suchkriterien.*
   :alt: Mehrere Suchkriterien grenzen die Treffer ein

   Mehrere Suchkriterien grenzen die Treffer ein

Wenn Sie mehrmals einen Suchparameter der gleichen Klasse, also zum
Beispiel »Searchable Text«, hinzufügen, wirkt sich nur der letzte
Parameter in der Reihe aus.

Durch Betätigung des Links :guilabel:`Entferne Zeile` entfernen Sie das
Suchkriterium in der entsprechenden Zeile.

Im letzten Abschnitt des Formulars bestimmen Sie die Reihenfolge, in
der die zur Kollektion passenden Artikel angezeigt werden. Wählen Sie
im Auswahlmenü :guilabel:`Sortiere nach` eine Artikeleigenschaft, nach der
sortiert werden soll. Die Sortierung erfolgt in der Regel
aufsteigend. Wenn Sie eine absteigende Sortierung wünschen, setzen Sie
das Häkchen bei :guilabel:`Umgekehrte Reihenfolge`. 

Weitere Bearbeitungsmöglichkeiten
=================================

In der unteren Hälfte des Bearbeitungsformulars eine Kollektion können
Sie einen Text eingeben, die Zahl der Suchresulate begrenzen und
festlegen, welche Informationen in der Tabellenansicht der Kollektion
aufgeführt werden sollen (siehe Abb.:
:ref:`fig_kollektion-bearbeiten-unten`).

.. _fig_kollektion-bearbeiten-unten:

.. figure:: ../images/kollektion-bearbeiten-unten.*
   :alt: Die untere Hälfte des Bearbeitungsformulars

   Bearbeitungsansicht einer Kollektion (unterer Teil)


Per Voreinstellung werden in der Tabellenansicht Titel, Ersteller,
Artikeltyp und Änderungsdatum angezeigt; der Titel dient auch als
Verweis zum Artikel.

Um eine weitere Spalte hinzuzufügen, wählen Sie im linken Fenster den
entsprechenden Eintrag aus und klicken Sie auf :guilabel:`>>`. Der
Eintrag wird daraufhin in das rechte Fenster übernommen. Möchten Sie
einen Eintrag aus der Anzeige entfernen, wählen Sie ihn im rechten
Fenster aus und klicken auf :guilabel:`<<`. Speichern Sie Ihre
Eingaben und wählen Sie anschließend in der Anzeige die
Darstellungsoption :guilabel:`Tabelle` aus. Die Kollektion wird nun
als Tabelle mit den von Ihnen festgelegten Spalten angezeigt. 


RSS-Feed der Kollektion
=======================

Plone erstellt von jeder Kollektion einen RSS-Feed. Dieser wird vom
Browser automatisch erkannt und zumeist in der Adresszeile angezeigt
(siehe dazu auch Abschnitt :ref:`sec_syndizierung`).

.. _sec_kollektionsportlet:

Kollektionsportlet
==================

Die Ergebnisse einer Kollektion können in einem Portlet angezeigt
werden. Abbildung :ref:`fig_portlet-kollektion` zeigt ein Beispiel. 

.. _fig_portlet-kollektion:

.. figure::
   ../images/portlet-kollektion.*
   :width: 40%
   
   Das Kollektionsportlet

Die Verweise im Kollektionsportlet führen in der Regel zur
Anzeigeansicht des Artikels. Bei Bilder führen die Verweise zu einer
Vollbildansicht des Bildes, bei Links zur Zieladresse. 

Um Portlets hinzufügen zu können, benötigen Sie
Verwaltungsrechte. Wenn Sie diese besitzen, finden Sie in der linken
und rechten Spalte die Schaltfläche :guilabel:`Portleteinstellungen`,
über die Sie in die Portletverwaltung gelangen. Details hierzu finden
Sie in Kapitel :ref:`sec_portlets`.

Hinzufügen eines Kollektionsportlets
------------------------------------

Rufen Sie in dem Ordner, in dem Sie ein Kollektionsportlet hinzufügen möchten,
die Portletverwaltung auf und wählen Sie im Auswahlmenü :guilabel:`Portlet
hinzufügen` den Menüpunkt :guilabel:`Kollektionsportlet` aus. Sie gelangen
dadurch in ein Formular (siehe Abbildung
:ref:`fig_kollektionsportlet-hinzufuegen`), in dem Sie die notwendigen
Einstellungen vornehmen können.

.. _fig_kollektionsportlet-hinzufuegen:

.. figure::
   ../images/kollektionsportlet-hinzufuegen.*
   :width: 100%

   Das Formular zur Konfiguration eines Kollektionsportlets

Kopfzeile des Portlets
    Geben Sie hier den Titel des Portlets ein. Er erscheint in der
    Kopfzeile des Portlets.

Zielkollektion
    Hier bestimmen Sie, welche Kollektion in Ihrer Website als Portlet
    angezeigt werden soll. Es handelt sich um ein Suchfeld, in das Sie
    einen Suchbegriff eingeben können. Betätigen Sie anschließend die
    Schaltfläche :guilabel:`Suche`. 

    Daraufhin werden unterhalb des Suchfeldes Suchergebnisse
    angezeigt (siehe Abbildung :ref:`fig_zielkollektion-auswaehlen`). 

    .. _fig_zielkollektion-auswaehlen:

    .. figure::
       ../images/zielkollektion-auswaehlen.*
       :width: 100%

       Suche zur Auswahl der Zielkollektion

    Markieren Sie die gewünschte Kollektion und betätigen Sie die
    Schaltfläche :guilabel:`Aktualisieren`. Die ausgewählte Kollektion
    wird daraufhin als Zielkollektion eingetragen (siehe Abbildung
    :ref:`fig_zielkollektion-ausgewaehlt`) 

    .. _fig_zielkollektion-ausgewaehlt:

    .. figure::
       ../images/zielkollektion-ausgewaehlt.*
       :width: 100%

       Ausgewählte Zielkollektion

    Wenn Sie in den Suchergebnissen nicht die gesuchte Kollektion
    finden, können Sie über die Schaltfläche :guilabel:`Übergeordneter
    Artikel` in die Ebene darüber wechseln oder mit der Schaltfläche
    :guilabel:`Durchsuchen` in den Suchergebnissen nach weiteren
    Kollektionen suchen. In dem in Abbildung
    :ref:`fig_zielkollektion-auswaehlen` gezeigten Beispiel führt ein
    Klick auf die Schaltfläche :guilabel:`Durchsuchen` hinter dem
    ersten Ergebnis dazu, dass auch die Unterkollektion »Teilnehmer«
    aufgelistet wird, die das Suchwort »Kochseminar« nicht enthalten
    hat und daher vorher nicht gefunden wurde (siehe Abbildung
    :ref:`fig_zielkollektion-weitere-gefunden`)

    .. _fig_zielkollektion-weitere-gefunden:

    .. figure::
       ../images/zielkollektion-weitere-gefunden.*
       :width: 100%

       Im ersten Suchresultat wurde eine Unterkollektion gefunden

    Wenn Sie die Zielkollektion eines Kollektionsportlets austauschen
    möchten, starten Sie einfach einen Suchlauf nach der gewünschten
    Kollektion. Markieren Sie die gewünschte Kollektion und klicken
    Sie auf :guilabel:`Aktualisieren`.  

Beschränkung 
    Sie können die Zahl der angezeigten Artikel begrenzen. Tragen Sie
    hier die gewünschte Anzahl ein. 

Artikel zufällig auswählen
    Normalerweise werden die Artikel im Kollektionsportlet in der
    gleichen Reihenfolge aufgelistet wie in der Kollektion
    selbst. Wenn Sie diese Option aktivieren, wird die Reihenfolge der
    Artikel zufällig bestimmt.

Zeige "Weiter..."-Verweis
    Wenn diese Option aktiviert ist, wird in der Fußzeile des Portlets
    ein Verweis zur Kollektion eingefügt. Dies ist vor allem dann
    sinnvoll, wenn das Portlet nur einige wenige Artikel auflistet.

Änderungsdatum zeigen
    Wenn unter dem Titel der aufgeführten Artikel das Datum der
    letzten Änderung erscheinen soll, aktivieren Sie diese Option. 

.. todo:: Übersetzung nachziehen, dort steht Freigabedatum
   https://dev.plone.org/ticket/13595
