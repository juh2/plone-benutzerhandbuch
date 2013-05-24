.. _sec_syndizierung:

==============
 Syndizierung
==============

Syndizierung oder Syndikation bedeutet, dass Inhalte einer Website
an anderer Stelle weiterverwendet werden, etwa auf anderen Websites oder in
einem Nachrichtenticker auf Ihrem Rechner. So kann man aktuelle
Veröffentlichungen auf einer Website verfolgen, ohne die Website selbst
regelmäßig besuchen zu müssen.

.. _sec_rss:

Feed-Formate
============

Per Syndizierung zu verbreitende Informationen werden in maschinenlesbarer Form
als sogenannter Feed zur Verfügung gestellt. Es gibt verschiedene Formate, die
dafür benutzt werden, zum Beispiel RSS 1.0 und RSS 2.0 sowie das Atom
Syndication Format. RSS steht für »Rich Site Summary« oder »Really Simple
Syndication«. Ein Feed ist eine Textdatei, die unter einer
bestimmten Internetadresse abrufbar ist. Diese Datei wird ständig erneuert,
etwa wenn eine neue Nachricht hinzukommt. Andere Websites oder Programme auf
Ihrem Rechner rufen sie in regelmäßigen Abständen ab.

Der Feed enthält eine begrenzte Anzahl von Artikeln
in einem standardisierten Textformat. Das Programm, welches die Artikel
verarbeiten will, kann die Datei zerlegen und zu jedem Artikel
den Titel, die Zusammenfassung, eine Internetadresse und andere
Angaben entnehmen. Diese Informationen werden dann beispielsweise in einer
Artikelliste auf einer anderen Website angezeigt.

Außerdem enthält ein Feed Metadaten wie Titel, Beschreibung,
Internetadresse und vielleicht ein Logo. Man bezeichnet Feeds auch als
Nachrichtenkanäle; ein Nachrichtenticker kann beispielsweise Nachrichten aus
mehreren Kanälen gleichzeitig anzeigen und die Kanäle dabei dem Titel nach
unterscheiden.

RSS-Portlet
===========

In Plone gibt es ein Portlet, das die neuesten Artikel eines beliebigen
RSS-Feeds aus dem Web anzeigt (siehe Abbildung :ref:`fig_portlet-rss`).

.. _fig_portlet-rss:

.. figure:: ../images/portlet-rss.png
   :width: 40%
   :alt: RSS-Portlet mit drei englischen Plone-Nachrichten

   RSS-Portlet

Das Portlet enthält eine Liste von Titeln, die jeweils Verweise zum
Artikeltext sind. Der Titel des Portlets zeigt den Kanaltitel, und
gegebenenfalls enthält die Fußzeile des Portlets einen Verweis zu einer Liste
aller Artikel des Kanals. Die Internetadresse des RSS-Feeds, die Anzahl
der im Portlet aufgelisteten Artikel und das Abrufintervall für den
RSS-Feed können Sie in den Einstellungen des Portlets festlegen.

Von Plone veröffentlichte Feeds
===============================


Plone kann Feeds nicht nur abrufen und darstellen, sondern für Ordner,
Kollektionen und Suchen auch eigene Feeds veröffentlichen.
Der Feed für einen Ordner listet die zuletzt geänderten Artikel im Ordner
auf, Feeds für Kollektionen und Suchen enthalten die jeweils zuerst
aufgeführten passenden Artikel oder Suchergebnisse. So könnten Sie
beispielsweise auf Ihrem Rechner in einem Nachrichtenticker einen Feed
Ihrer Website abonnieren, der Sie über Änderungen und neue Artikel auf der
Website informiert. 

Plone erzeugt Feeds in den Formaten RSS 1.0, RSS 2.0, Atom sowie im
iTunes-Format. 

Feeds von Kollektionen
----------------------


Plone erzeugt für jede Kollektion automatisch die einzelnen Feeds. Der Feed im
Format RSS 1.0 ist erreichbar, indem Sie an die Internetadresse der Kollektion
den Pfad :code:`/RSS` anhängen. Den RSS-2.0-Feed erreichen Sie unter
:code:`/rss.xml` und den Atom-Feed unter :code:`/atom.xml`. 

Die Internetadresse der Kollektion, die neue Nachrichten in einer
Plone-Site auflistet, lautet bei einer Standardinstallation::

   http://localhost:8080/Plone/news/aggregator

Den RSS-1.0-Feed dieser Kollektion erreichen Sie folglich über die
Internetadresse:: 

   http://localhost:8080/Plone/news/aggregator/RSS

Den Feed im Format RSS 2.0 erreichen Sie unter ::

   http://localhost:8080/Plone/news/aggregator/rss.xml

Und den Atom-Feed finden Sie unter ::

   http://localhost:8080/Plone/news/aggregator/atom.xml

RSS-Feeds von Ordnern
---------------------

Von einem Ordner werden in einer Standardinstallation keine RSS-Feeds erzeugt.
Sie können aber die Syndizierung für einen Ordner aktivieren, indem Sie in die
Ansicht :guilabel:`Syndizierung` wechseln und die Syndizierung einschalten
(siehe Abb.: :ref:`fig_syndizierung-einschalten`). Der Reiter ist in der
Voreinstellung nicht sichtbar. Sie können zu dem Formular aber auch gelangen,
wenn Sie an die Internetadresse des Ordners den Pfad :code:`/synPropertiesForm`
anhängen.

Um die Syndizierung für den Ordner::

   http://localhost:8080/Plone/veranstaltungen/

einzuschalten, geben Sie in der Adresszeile Ihres Browsers den Pfad::

   http://localhost:8080/Plone/veranstaltungen/synPropertiesForm

ein. Sie werden dann zur Artikelansicht »Syndizierung« geleitet (siehe
Abb.: :ref:`fig_syndizierung-einschalten`).

.. todo:: Neuer Screenshot

.. _fig_syndizierung-einschalten:

.. figure::
   ../images/syndizierung-einschalten.*
   :width: 100%
   :alt: Die Artikelansicht Syndizierung mit Konfigurationsmöglichkeiten«

   Artikelansicht Syndizierung

.. todo:: Neu formulieren, da anders in 4.3 

Durch Betätigung des Schalters :guilabel:`Syndizierung erlauben`
schalten Sie die Syndizierung für den Ordner ein. Die Anzeige wechselt
und Sie sehen die Standardeinstellungen für die Syndizierung, die Sie
anpassen können (siehe Abb. :ref:`fig_syndizierung`).

.. _fig_syndizierung:

.. figure:: ../images/syndizierung.*
   :width: 100%
   :alt: Die Ansicht zur Konfiguration der Syndizierung

   Syndizierungsansicht

Zuoberst finden Sie eine Schaltfläche, mit der Sie die Syndizierung
für diesen Ordner jederzeit wieder ausschalten können. Beachten Sie,
dass alle Syndizierungseinstellungen für diesen Ordner danach verloren
sind.

Als nächstes folgen der Kanaltitel und die Kanalbeschreibung des RSS-Feeds.
Dabei handelt es sich um den Titel und die Beschreibung des Ordners oder der
Kollektion. Um diese Angaben zu ändern, müssen Sie den Titel und die
Beschreibung des Ordners oder der Kollektion selbst anpassen.

Mit den folgenden drei Angaben teilen Sie den Anzeigeprogrammen mit,
wann und wie oft sie den Feed abrufen sollten. 

Periode aktualisieren
  Mit dem Auswahlmenü legen Sie fest, ob der RSS-Feed in einem
  stündlichen, täglichen, wöchentlichen, monatlichen oder jährlichem
  Rhythmus aktualisiert werden soll.

Frequenz aktualisieren
  Durch Eingabe einer Zahl legen Sie die Frequenz der Aktualisierung
  fest. Wenn Sie oben beispielsweise :guilabel:`hourly` als stündlich
  ausgewählt haben, können Sie durch Eingabe einer Zahl hier
  festlegen, ob der RSS-Feed jede Stunde (1) oder nur jede zweite Stunde (2)
  aktualisiert werden soll.

Datenbasis aktualisieren
  Der Rhythmus der Aktualisierung muss irgendwann starten. Mit den
  Auswahlmenüs können Sie hierfür ein Datum und eine Uhrzeit
  festlegen.

Höchstgrenzen Artikel
  Mit der eingegebenen Zahl legen Sie fest, wie viele Artikel der
  RSS-Feed anhalten soll. Voreingestellt sind 15 Artikel.


Die RSS-Feeds von Ordnern und Kollektionen sind bei jedem Abruf auf
dem jeweils aktuellen Stand. Wird ein Feed zu oft abgerufen, dann
belastet das den Webserver unnötig; liest man einen Kanal jedoch zu
selten, so verpasst man Meldungen. Welche Häufigkeit der
Aktualisierung sinnvoll ist, hängt von Ihrem Anwendungsfall ab und
muss für jeden Ordner und jede Kollektion einzeln abgeschätzt werden.

Für den RSS-Feed eines Ordners oder einer Kollektion werden als Titel und
Beschreibung die Metadaten des Ordners oder der Kollektion selbst verwendet.
Jeder Hinweis auf einen Artikel enthält neben Titel, Beschreibung und der
Internetadresse auch Angaben über den Herausgeber, den Autor, die
Nutzungsbedingungen und das Veröffentlichungsdatum. Diese Informationen werden
den Eigenschaften und Metadaten der Artikel entnommen.

In RSS-Feeds von Ordnern und Kollektionen ist der Inhalt von
Unterordnern nicht enthalten: wenn für sie die Syndizierung aktiviert
ist, haben sie ihre eigenen RSS-Feeds.

Wenn Sie die Syndizierungseinstellungen einer Kollektion ändern
wollen, erreichen Sie die Artikelansicht »Syndizierung«, indem Sie an
die Internetadresse der Kollektion den Pfad :code:`/synPropertiesForm`
anhängen. Die Ansicht ist genauso wie bei einem Ordner aufgebaut.

RSS-Feed einer Suche
--------------------

Wenn Sie eine Suche ausführen, so befindet sich am Anfang der Ergebnisliste
der Verweis »Abonnieren Sie einen stets aktuellen RSS-Feed aus diesen
Suchresultaten«. Dieser Verweis zeigt auf die Internetadresse eines
RSS-Feeds, der stets die aktuelle Ergebnisliste zu dieser Suchanfrage
enthält.


