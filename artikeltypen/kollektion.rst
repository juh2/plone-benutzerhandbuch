.. |close| image:: ../images/pb_close.png

.. _sec_kollektion:

============
 Kollektion
============

Oft möchte man Artikel, die sich in unterschiedlichen Ordnern einer Website
befinden an einem Ort zusammenfassen. Dies kann beispielsweise eine
Nachrichtenübersicht sein oder eine Liste aller Artikel, die sich einem
bestimmten Thema widmen.  Da jeder Artikel sich aber nur an einem Platz in der
Ordnerhierarchie der Website befinden kann, sind Ordner nicht geeignet, um
Artikel unter verschiedenen Gesichtspunkten zu gruppieren.

Stattdessen verwendet man Kollektionen, um beliebig viele verschiedene
Übersichten zu erstellen. Kollektionen sind unabhängig von der Ordnerstruktur
der Website, da es sich hierbei um die Auflistung von Artikeln handelt, die
bestimmten Suchkriterien entsprechen.  Eine Kollektion ist das Ergebnis einer
vorgefertigten Suche; Plone hält die Artikelauswahl anhand von Suchkriterien
stets aktuell.

Anzeige
=======

Nach außen verhalten sich Kollektionen wie Ordner. Sie kennen ebenso wie Ordner
verschiedene Darstellungen für die Anzeigeansicht, aus denen Sie im
Darstellungsmenü wählen können:

* Kurzfassung
* Gesamter Inhalt
* Tabelle
* Album
* Liste
* Kollektion

Als Beispiel zeigt Abbildung :ref:`fig_kollektion` die Darstellung als Liste.

.. _fig_kollektion:

.. figure:: ../images/kollektion.*
   :width: 100%
   
   Darstellung einer Kollektion als Liste

Die ersten fünf Darstellungsvarianten funktionieren so wie bei Ordnern. Die
letzte Variante, die Darstellung als »Kollektion« ist in der
Bearbeitungsansicht der Kollektion konfigurierbar. 

Kollektionen haben neben den Reitern :guilabel:`Inhalte`,
:guilabel:`Bearbeiten` und :guilabel:`Freigabe` einen weiteren Reiter mit Namen
:guilabel:`Kriterien`.  Dahinter verbirgt sich das Formular, mit dem Sie die
Kritieren festlegen, die darüber entscheiden, welche Artikel in der Kollektion
aufgeführt werden.  

Wie Ordner besitzen Kollektionen auch keinen eigenen redaktionellen Inhalt. 

.. _sec_kollektion-bearbeiten:

Bearbeitungsansicht
===================


.. _fig_kollektion-bearbeiten:

.. figure:: ../images/kollektion-bearbeiten.*
   :width: 100%

   Bearbeitungsansicht einer Kollektion

In der Bearbeitungsansicht können Sie Titel, Zusammenfassung und Haupttext
einer Kollektion (siehe Abbildung :ref:`fig_kollektion-bearbeiten`) bearbeiten.

Darunter können Sie einstellen, ob alle Artikel auf einer Seite angezeigt
werden sollen oder auf mehrere Seite verteilt. Kreuzen Sie dazu »Anzeige der
Suchresultate auf mehrere Seiten verteilen« an und geben Sie im Feld darunter
die Anzahl der Artikel ein, die auf einer Seite aufgelistet werden sollen.
Findet die Kollektion anhand der gewählten Suchkriterien mehr Artikel als dort
vermerkt, so wird die Liste auf mehrere Seiten verteilt. Unterhalb der
angezeigten Liste finden Sie dann Verweise auf die weiteren Seiten (siehe
Abbildung :ref:`fig_ergebnisse-auf-mehreren-seiten-anzeigen`).  

.. _fig_ergebnisse-auf-mehreren-seiten-anzeigen:

.. figure:: ../images/ergebnisse-auf-mehreren-seiten-anzeigen.*
   :width: 100%

   Navigationsleiste zu weiteren Artikeln

Wenn Sie die Option nicht aktivieren oder als Artikelanzahl 0
eingeben, werden alle passenden Artikel auf einer Seite
aufgeführt. Dies kann bei sehr vielen Artikeln zu
Geschwindigkeitsproblemen bei der Anzeige führen.

Sie haben in der Bearbeitungsansicht die Möglichkeit die tabellarische
Darstellung der Kollektion zu konfigurieren. Markieren Sie hierzu die
Option :guilabel:`Als Tabelle anzeigen` und legen Sie anschließend in
der Option :guilabel:`Tabellenspalten` fest, welche Informationen in
der Tabelle angezeigt werden sollen. Per Voreinstellung wird nur der
Titel angezeigt; er dient auch als Verweis zum Artikel. Wählen Sie
dazu einen Eintrag im linken Fenster aus und klicken Sie auf
:guilabel:`>>`. Der Eintrag wird daraufhin in das rechte Fenster
übernommen. Möchten Sie einen Eintrag aus der Anzeige entfernen,
wählen Sie ihn im rechten Fenster aus und klicken auf
:guilabel:`<<`. Speichern Sie Ihre Eingaben und wählen Sie
anschließend in der Anzeige die Darstellungsoption
:guilabel:`Kollektion` aus. Die Kollektion wird nun als Tabelle mit
den von Ihnen festgelegten Spalten angezeigt. Die Darstellungoption
:guilabel:`Tabelle` benutzt dagegen die in Plone vordefinierten
Tabellenspalten (Titel, Autor, Artikeltyp, Änderungsdatum).

Wenn Sie die Darstellungsoption :guilabel:`Kollektion` wählen und das Feld
:guilabel:`Als Tabelle anzeigen` nicht ankreuzen, werden die Artikel in einer
Liste aufgeführt. Eine solche Liste zeigt für jeden Eintrag den Titel, die
Beschreibung, einen Verweis auf das Profil des Erstellers und das Datum der
letzten Änderung. Der Titel dient dabei als Verweis auf den Artikel selbst.

RSS-Feed der Kollektion
=======================

Plone erstellt von jeder Kollektion einen RSS-Feed. Dieser wird vom
Browser automatisch erkannt und zumeist in der Adresszeile angezeigt
(siehe dazu auch Abschnitt :ref:`sec_syndizierung`).

Suchkriterien
=============

Die Artikel, die eine Kollektion anzeigt, werden durch einen Suchlauf bestimmt.
Eine Reihe von Metadaten und andere Eigenschaften von Artikeln können dabei als
Suchkriterien dienen.  Damit ein Artikel zur Kollektion passt, muss er alle
Kriterien gleichzeitig erfüllen.  (Die Kriterien werden bei der Suche mit »und«
verknüpft.) 

.. Für jede Artikeleigenschaft kann es in einer Kollektion höchstens ein Suchkriterium geben.

Abbildung :ref:`fig_kriterien` zeigt die Ansicht :guilabel:`Kriterien`, also
das Formular, in dem Sie festlegen, welche Felder in der Datenbank von Plone
durchsucht werden und welche Suchkriterien dabei zur Anwendung kommen.  Jedes
Feld bezieht sich dabei auf eine bestimmte Eigenschaft von Artikeln. In einer
Kollektion kann jedes Feld nur einmal berücksichtigt werden. Sie können jedoch
für manche Felder mehrere Suchkriterien festlegen.  
 
.. _fig_kriterien:

.. figure:: ../images/kriterien.*
   :width: 100%

   Kriterienansicht einer Kollektion

Die Ansicht :guilabel:`Kriterien` enthält:

* eine Tabelle der bereits vorhandenen Kriterien,
* ein Feld zum Anlegen eines neuen Kriteriums (:guilabel:`Neues Kriterium
  hinzufügen`) und
* ein Auswahlfeld für die Sortierreihenfolge (:guilabel:`Sortierreihenfolge
  festlegen`).

Die Tabelle der vorhandenen Kriterien nennt in der Spalte »Feld« das
Datenbankfeld, auf das sich das jeweilige Kriterium bezieht. Die
Spalte »Kriterium« zeigt die Art des Suchkriteriums an und enthält das
Eingabe- oder Auswahlfeld für seinen Wert, beispielsweise die Namen
der möglichen Artikeltypen.

Die Art der Suchkriterien richtet sich nach den durchsuchbaren
Artikeleigenschaften. Im Feld :guilabel:`Titel` kann man beispielsweise nach
einem Wort suchen, bei einem Datum will man dagegen feststellen, ob es vor oder
nach einem bestimmten Zeitpunkt liegt. Bei einigen Feldern kann ein Suchtext
frei eingegeben werden, bei anderen muss man aus vorgegebenen Begriffen
auswählen.

Tabelle :ref:`Suchkriterien für Kollektionen <tab_thema-feldnamen>` fasst
zusammen, welche Kriteriumstypen für jedes der Felder in Frage kommen.

.. tabularcolumns:: p{6cm}|p{6cm} 

.. _tab_thema-feldnamen:

+----------------------------+-----------------------------------------+
|Feldnamen                   | Kriteriumstypen                         |
+============================+=========================================+
| * Beschreibung             | * Text                                  |
| * Durchsuchbarer Text      |                                         |
| * Titel                    |                                         |
+----------------------------+-----------------------------------------+
| * Kurzname                 | * Text                                  |
|                            | * Werteliste                            |
+----------------------------+-----------------------------------------+
| * Ersteller                | * Wählen Sie Einträge aus der Liste     |
|                            | * Beschränke auf den aktuellen Benutzer |
|                            | * Text                                  |
|                            | * Werteliste                            |
+----------------------------+-----------------------------------------+
| * Status (Revisionsstatus) | * Wählen Sie Einträge aus der Liste     |
| * Stichwörter              | * Text                                  |
|                            | * Werteliste                            |
+----------------------------+-----------------------------------------+
| * Änderungsdatum           | * Relatives Datum                       |
| * Erstellungsdatum         | * Zeitspanne                            |
| * Anfangsdatum             |                                         |
| * Enddatum                 |                                         |
| * Freigabedatum            |                                         |
| * Ablaufdatum              |                                         |
+----------------------------+-----------------------------------------+
| * Artikeltyp               | * Artikeltypen auswählen                |
+----------------------------+-----------------------------------------+
| * Verweise zu              | * Artikel auswählen                     |
+----------------------------+-----------------------------------------+
| * Ort                      | * Ort in der Website                    |
|                            | * Ein Pfad zu einem Ort in der Website, |
|                            |   relativ zur aktuellen Position        |
+----------------------------+-----------------------------------------+



Es werden Ihnen für die einzelnen Felder nur passende Kriteriumstypen
zur Auswahl angeboten:

Text 
    Geben Sie ein oder mehrere Wörter ein, die im durchsuchten Feld
    enthalten sein sollen. Die Reihenfolge mehrerer Wörter wird nur
    berücksichtigt, wenn Sie die Wortfolge in Anführungszeichen
    setzen. Sie können auch nach Wortbestandteilen suchen, indem Sie
    ähnlich wie bei der Website-Suche Platzhalter benutzen (siehe
    Abschnitt :ref:`sec_suche`).

Werteliste 
    Sie können eine beliebige Anzahl von Werten eingeben; jeweils ein
    Wert pro Zeile. Das kann zum Beispiel eine Liste von Benutzernamen
    für das Feld »Ersteller« sein.

    Unterhalb der Werteliste befindet sich das Eingabefeld
    :guilabel:`Verknüpfungsoperation`. Falls Sie mehrere Werte eintragen, können
    Sie damit bestimmen, ob die gesuchten Artikel mit einem der
    eingegebenen Werte (»oder«) oder mit allen Werten (»und«)
    übereinstimmen müssen. Wenn Sie beispielsweise alle Artikel mit
    dem Ersteller »Adam« und alle mit dem Ersteller »Berta«
    zusammenfassen wollen, müssen Sie diese beiden Werte mit »oder«
    verknüpfen.

Wählen Sie Einträge aus der Liste
  Hier wählen Sie Werte aus einer vorgegebenen Liste aus,
  beispielweise aus den verfügbaren Stichworten. Auch hier gibt es die
  Verknüpfungen »und« und »oder«.

Relatives Datum
  Sie können verlangen, dass der Wert des Feldes vor,
  nach oder genau auf einen Stichtag fällt. Der Stichtag ist jedoch kein
  festes Datum, sondern bezieht sich auf den Zeitpunkt, zu dem
  die Kollektion angezeigt wird. Beispielsweise können Sie so eine ständig
  aktuelle Liste aller Artikel erzeugen, die jünger als eine Woche sind.

  Zur Konfiguration dieses Kriteriums gehören drei Angaben. Die ersten
  beiden bestimmen den Stichtag, der mit dem jeweils aktuellen Datum
  zusammenfallen (»Heute«) oder um eine auszuwählende Zeitspanne in
  der Vergangenheit oder Zukunft liegen kann. Im Eingabefeld
  :guilabel:`Mehr oder weniger` bestimmen Sie, ob das Datum im
  betreffenden Feld der durchsuchten Artikel auf den Stichtag fallen,
  näher als dieser am jeweils aktuellen Datum oder weiter davon
  entfernt liegen soll.

Zeitspanne
  Wählen Sie zwei Zeitpunkte (Anfang und Ende) aus, zwischen
  denen der Wert des Feldes liegen muss. Sie haben zwei Gruppen von
  Eingabefeldern, um für den Anfang und das Ende der Zeitspanne jeweils einen
  Kalendertag und eine Uhrzeit zu bestimmen. Das Kalendersymbol öffnet ein
  zusätzliches Fenster mit einem Kalender, in dem Sie bequem ein beliebiges
  Datum auswählen können.

Artikeltypen auswählen
  Wählen Sie beliebig viele Artikeltypen aus einer
  Liste aus. Es werden dann nur Artikel des gewählten Typs in der Kollektion
  angezeigt.

Artikel auswählen 
  Wählen Sie aus einer Liste aus, in der alle Artikel aufgeführt
  werden, auf die verwiesen wurde. Dies betrifft nur die Verweise, die
  im Teilformular :guilabel:`Kategorisierung` in der
  Bearbeitungsansicht eines Artikels hinzugefügt wurden (siehe Kapitel
  :ref:`sec_teilf-kateg`). Die Kollektion enthält dann nur
  Artikel, die auf alle ausgewählten Artikel verweisen.

Ort in der Website
  Schränken Sie die Suchergebnisse auf Artikel ein,
  die sich an bestimmten Stellen in der Ordnerhierarchie der Website befinden.
  Dabei können Sie sowohl einzelne Artikel zulassen als auch Ordner angeben,
  deren Inhalt einschließlich der Unterordner durchsucht werden soll.

  Um zu durchsuchende Artikel zusammenzustellen, betätigen Sie die
  Schaltfläche :guilabel:`Hinzufügen` unterhalb der Artikelliste. Daraufhin
  öffnet Ihr Webbrowser ein zweites Fenster, in dem Sie durch die Website
  navigieren und Artikel auswählen können. Markieren Sie den
  gewünschten Artikel, er wird sofort der Liste im Hauptfenster
  hinzugefügt. Wenn Sie Ihre Auswahl beendet haben, schließen Sie das
  Fenster, indem Sie oben link auf das Symbol |close| klicken.  

  Sie können Artikel wieder aus der Liste löschen, indem Sie im
  Hauptfenster das Häkchen vor den betreffenden Artikeln entfernen und
  das Formular speichern.

Ein Pfad zu einem Ort in der Website, relativ zur aktuellen Position
  Mit diesem Kriterium bestimmen sie einen zur Kollektion relativen
  Pfad. Tragen Sie dazu eine entsprechende Zeichenkombination in das
  Textfeld ein – zum Beispiel: 

  * ›..‹ für den Ordner, in dem sich die Kollektion befindet
  * ›../..‹ für den Ordner über dem Ordner, in dem sich die Kollektion
    befindet
  * ›../ordnername‹ für einen Ordner, der sich mit der Kollektion im
    gleichen Ordner befindet.

Beschränke auf aktuellen Benutzer 
  Dieses Kriterium ist nur für das Feld »Ersteller« vorhanden. Wenn es
  gesetzt wird, zeigt die Kollektion nur Artikel an, die von dem
  Benutzer erstellt wurden, der die Kollektion aufruft.


Um ein Kriterium zu löschen, kreuzen Sie es an und betätigen Sie die
Schaltfläche :guilabel:`Löschen` unterhalb der Tabelle.

Der Abschnitt »Neues Kriterium hinzufügen« bietet Ihnen im Eingabefeld
:guilabel:`Feldname` die durchsuchbaren Felder an, für die noch kein
Kriterium angelegt wurde. Das Eingabefeld :guilabel`Kriteriumstyp`
enthält nur Einträge, die zum gerade ausgewählten Feld passen. Sie
können nur ein neues Kriterium auf einmal hinzufügen.

Im letzten Abschnitt des Formulars bestimmen Sie die Reihenfolge, in der die
zur Kollektion passenden Artikel angezeigt werden. Wählen Sie eine
Artikeleigenschaft, nach der sortiert werden soll, und entscheiden Sie, ob
auf- oder absteigend sortiert wird.


Unterkollektionen
-----------------

Eine Kollektion kann Unterkollektionen besitzen, um die Suche mit
weiteren Kriterien zu verfeinern oder verwandte Kollektionen zu
gruppieren. Die Anzeige der Kollektion enthält dann in einigen
Darstellungsoptionen eine Liste der Unterkollektionen (siehe
Abbildung :ref:`fig_kollektion-mit-unterkollektionen`).

.. _fig_kollektion-mit-unterkollektionen:

.. figure:: ../images/kollektion-mit-unterkollektionen.png
   :width: 100%

   Anzeige einer Kollektion mit Unterkollektionen

In der Bearbeitungsansicht von Unterkollektionen können Sie entscheiden, ob
Kriterien von übergeordneten Kollektionen geerbt werden sollen. Kreuzen Sie
dazu in der Bearbeitungsansicht der Unterkollektion das Eingabefeld
:guilabel:`Kriterien erben` an.

Erbt eine Unterkollektion Kriterien, so verfeinert sie die Ergebnisse
der übergeordneten Kollektion. Sie enthält dann nur die Artikel aus
der übergeordneten Kollektion, die auch die Kriterien der
Unterkollektion erfüllen.

Enthält die Unterkollektion ein Feld, das bereits in der
übergeordneten Kollektion verwendet wird, so überschreiben die
Kriterien in der Unterkollektion die Kriteren in der übergeordneten
Kollektion. Auf diese Weise lassen sich einzelne Kriterien von der Vererbung
ausschließen.

Sie können Unterkollektionen wie andere Artikel kopieren und
verschieben. Rufen Sie dazu die Unterkollektion auf, wählen Sie aus
dem Menü :guilabel:`Aktionen` den gewünschten Vorgang auf und rufen
Sie dann den Ordner oder die Kollektion auf, in die Sie die
Unterkollektion verschieben oder kopieren möchten. 

Wenn Sie versuchen, andere Artikel als Kollektionen in eine
Kollektion einzufügen, erhalten Sie eine Fehlermeldung.

.. Die Ansicht »Unterkollektionen« einer Kollektion (siehe Abbildung
   :ref:`fig_unterthemen`) ist ähnlich der Inhaltsansicht eines
   Ordners aufgebaut (siehe Abschnitt :ref:`sec_ordner-aktionen`). In
   ihr können Sie mehrere Unterkollektionen auf einmal umbenennen,
   löschen oder veröffentlichen.

   .. _fig_unterthemen:

   .. figure:: ../images/unterthemen.png
      :width: 100%

      Ansicht »Unterkollektionen«

Wenn Sie eine Unterkollektion an einen anderen Ort auf der Website verschieben
oder kopieren, gehen ihr dabei geerbte Suchkriterien der ehemals
übergeordneten Kollektionen verloren. Falls Sie sie in
eine andere Kollektion verschieben, erbt sie deren Kriterien.

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
Verwaltungsrechte. Wenn Sie diese besitzen, finden Sie in der linke
und rechte Spalte die Schaltfläche :guilabel:`Portleteinstellungen`,
über die Sie in die Portletverwaltung gelangen. Details
hierzu finden Sie in Kapitel :ref:`sec_portlets`. 

Hinzufügen eines Kollektionsportlets
------------------------------------

Rufen Sie in dem Ordner, in dem Sie ein Kollektionsportlet hinzufügen
möchten, die Portletverwaltung auf und wählen Sie im Auswahlmenü
:guilabel:`Portlet hinzufügen` den Menüpunkt
:guilabel:`Kollektionsportlet` aus. Sie gelangen dadurch in ein
Formular (siehe Abbildung :ref:`fig_kollektionsportlet-hinzufuegen`), in dem Sie
die notwendigen Einstellungen vornehmen können.

.. _fig_portlet-hinzufuegen:

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
    finden, können über die Schaltfläche :guilabel:`Übergeordneter
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

    Beachten Sie, dass die Anzahl der im Portlet angezeigten Artikel
    auch durch die Option :guilabel:`Anzeige der Suchresultate auf
    mehrere Seiten verteilen` in der Bearbeitungsansicht der
    Kollektion beeinflusst wird. Die dort vorgenommene Einstellung
    geht immer vor. Wurde die Zahl der Artikel beispielsweise auf fünf
    begrenzt, können auch im Portlet nie mehr als fünf Artikel
    angezeigt werden (vgl. dazu Kapitel
    :ref:`sec_kollektion-bearbeiten`).

Artikel zufällig auswählen
    Normalerweise werden die Artikel im Kollektionsportlet in der
    gleichen Reihenfolge aufgelistet wie in der Kollektion
    selbst. Wenn Sie diese Option aktivieren, wird die Reihenfolge der
    Artikel zufällig bestimmt.

Zeige "Weiter..."-Verweis
    Wenn diese Option aktiviert ist, wird in der Fußzeile des Portlets
    ein Verweis zur Kollektion eingefügt. Dies ist vor allem dann
    sinnvoll, wenn das Portlet nur einige wenige Artikel auflistet.

Daten zeigen
    Wenn unter dem Titel der aufgeführten Artikel das Datum der
    letzten Änderung erscheinen soll, aktivieren Sie diese Option. 

