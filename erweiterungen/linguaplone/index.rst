=============
 LinguaPlone
=============

Mehrsprachige Inhalte lesen
===========================

Wenn auf der Plone-Website die Erweiterung LinguaPlone installiert
wurde, ist es möglich, Inhalte in verschiedenen Sprachen anzubieten.
Sie finden zur Auswahl der gewünschten Sprachversion oben rechts
Verweise mit den möglichen Sprachen
(siehe Abbildung :ref:`fig_sprache-auswaehlen`), in denen Inhalte
vorliegen können. Dabei kann es sich je nach Konfiguration der Website
um reine Textverweise oder um kleine Fähnchen handeln.

.. _fig_sprache-auswaehlen:

.. figure:: 
   ./images/sprache-auswaehlen.*
   :width: 100%
   :alt: Links mit der Bezeichnung English, Français, Deutsch

   Auswahl der Sprachversion

Wenn Sie einem dieser Verweise folgen, erscheint die gesamte Website
in der ausgewählten Sprache: die Bedienungselemente der
Benutzeroberfläche ebenso wie der Inhalt des Artikels, auf dem Sie sich
befunden haben, als Sie die Sprache wechselten.

Falls der Artikel nicht in der Sprache vorliegt, die Sie gewählt
haben, werden Sie stattdessen zur Startseite der Website oder zum
nächst höher gelegenen Ordner in der gewünschten Sprache
weitergeleitet. Von dort aus können Sie sich anhand der Navigation neu
orientieren.

Mehrsprachige Inhalte erstellen
===============================

Beim Aufbau einer mehrsprachige Website sind folgende Punkte zu
beachten.

#. Die Benutzeroberfläche der Website muss in alle Zielsprachen
   übersetzt werden. Diese Arbeit hat Ihnen die Plone-Community bereits
   abgenommen. Das Content-Management-System Plone unterstützt mehr
   als 50 Sprachen. Falls Sie Veränderungen an der Übersetzung der
   Benutzeroberfläche vornehmen möchten, informieren Sie sich auf
   http://plone.org über das Thema Internationalization_.

#. Es muss für jede Sprachversion ein entsprechender Navigationsbaum,
   also eine eigene Ordner-Hierarchie aufgebaut werden, damit sich die
   Besucher in ihrer Muttersprache auf der Website zurechtfinden. Wie
   Sie dies machen, wird in diesem Kapitel beschrieben.

#. Und schließlich müssen die Inhalte selbst in den gewünschten
   Sprachen vorliegen. Die Arbeitsschritte, die hierfür notwendig
   sind, werden ebenfalls in diesem Kapitel beschrieben.

Aufbau einer mehrsprachigen Navigation
======================================

Um eine mehrsprachige Navigation aufzubauen, müssen die Ordner,
mit denen eine Ordnerhierarchie aufgebaut wurde, übersetzt
werden. Soll die gesamte Website mehrsprachig aufgebaut werden, müssen
bereits die Ordner im Wurzelverzeichnis von Plone dabei einbezogen
werden. Der Aufbau einer mehrsprachigen Navigation muss daher in der
Regel von einem Administrator durchgeführt werden.

Sobald LinguaPlone installiert ist, finden Sie im Konfigurationsmenü
:guilabel:`Sprache` ein zusätzliches Auswahlmenü, in dem Sie festlegen können,
in welche Sprachen Inhalte übersetzt werden sollen (siehe Abbildung
:ref:`fig_konfiguration-sprache-linguaplone`). Das Konfigurationsmenü für die
Spracheinstellungen wird in Kapitel :ref:`sec_konfiguration-sprache`
beschrieben. 

.. _fig_konfiguration-sprache-linguaplone:

.. figure::
   ./images/konfiguration-sprache-linguaplone.*
   :width: 100%
   :alt: Das Konfigurationsmenüs »Sprache« mit zusätzlichem Auswahlmenü

   Die Spracheinstellungen

Um mehrere Sprachen auszuwählen, halten Sie die Command-Taste gedrückt, während
Sie die Sprache anklicken.

Gemeinsame oder sprachspezifische Startseite 
--------------------------------------------

Beim Aufbau einer mehrsprachigen Navigation können Sie mehrere Strategien
verfolgen. 

#. Sie für alle Sprachversionen Ihre Website eine gemeinsame Startseite
   einrichten, von wo aus die Besucher die einzelnen Sprachversionen erreichen
   können. Dies ist der in LinguaPlone nach der Installation voreingestellte
   Weg.  Der Eintrag :guilabel:`Startseite` in der Hauptnavigation führt in
   diesem Falle immer zurück auf die gemeinsame Startseite.

#. Wenn Sie für jede Sprachversion eine eigene Startseite einrichten möchten,
   müssen Sie Plone dafür entsprechend konfigurieren. Bei dieser Strategie wird
   für jede Sprachversion ein eigener Ordner eingerichtet, sodass eine
   vollständig getrennte Navigation entsteht. 
   
Bei letzterer Strategie werden Besucher, die in ihrem Browser »Deutsch« als
Standardsprache eingestellt haben, automatisch in den deutschen Sprachordner
weitergeleitet::
   
   http://localhost:8080/Plone/de

Besucher mit englischer oder französischer Voreinstellung werden entsprechend
in ihre Sprachordner weitergeleitet::   
   
   http://localhost:8080/Plone/en
   http://localhost:8080/Plone/fr

Der Menüeintrag :guilabel:`Startseite` beziehungsweise :guilabel:`Home` oder
:guilabel:`Accueil` führt dann je nach Sprache zu der Startseite in den
entsprechenden Sprachordnern. 

Damit haben Sie eine durchgehend mehrsprachige Website mit sprachspezifisch
getrennter Navigation. Dies betrifft übrigens auch die Suche, die immer nur
Ergebnisse aus der jeweiligen Sprachversion findet.  

Um Plone für mehrere sprachspezifische Startseiten zu konfigurieren, müssen Sie
den View @@language-setup-folders aufrufen, wenn Sie als Administrator in Plone
angemeldet sind::

    http://localhost:8080/Plone/@@language-setup-folders

Plone nimmt daraufhin sämtliche Konfigurationen automatisch vor und erzeugt für
jede Sprachversion einen Sprachordner (siehe Abbildung
:ref:`fig_language-setup-folders`).

.. _fig_language-setup-folders:

.. figure::
   ./images/language-setup-folders.*
   :width: 100%
   :alt: Das Protokoll des Aufrufs von @@language-setup-folders

   Protokoll des Aufrufs von @@language-setup-folders

In dem Beispiel hat Plone für die Sprachen Deutsch, Englisch und Französisch
drei Ordner mit den IDs »de«, »en« und »fr« erzeugt und mit Hilfe des
:term:`Interfaces <Interface>` »INavigationRoot« als Wurzelverzeichnis für die
entsprechende Sprachversion
gekennzeichnet. 

Sprachspezifische und sprachunabhängige Inhalte
-----------------------------------------------

Sobald eine Website mehrsprachige Inhalte verwaltet, bekommt die Zuordnung von
Artikeln zu einer bestimmten Sprache eine wichtige Bedeutung. Es werden nämlich
nur solche Artikel von der Erweiterung LinguaPlone als Sprachversion erkannt,
die nicht :term:`sprachunabhängig` sind. Wenn Sie beispielsweise die englische
Sprachversion der Website betrachten, werden alle Inhalte, die einer anderen
Sprache angehören unterdrückt und nicht angezeigt. Im Umkehrschluss bedeutet
dies, dass nur sprachunabhängige Inhalte in allen Sprachen zur Verfügung
stehen. 

Wenn Sie einen Artikel übersetzen möchten, gehen Sie daher zunächst
ins Teilformular »Kategorisierung« (siehe Kapitel
:ref:`sec_teilf-kateg`) des Artikels. Kontrollieren Sie dort die
Stellung des Auswahlmenüs :guilabel:`Sprache`. Wenn
»Sprachunabhängig (voreinstellt)« auswählt ist, wird der Artikel nicht
als eine bestimmte Sprachversion erkannt. Bei Bildern mag dies
sinnvoll sein, bei Artikeln, die übersetzt werden, sollte immer eine
Sprache gesetzt werden. Ordnen Sie also den Artikel vor der
Übersetzung der Ausgangssprache zu. In unserem Beispiel ist dies »Deutsch«.

Sobald Sie LinguaPlone installiert haben, erfolgt beim Anlegen neuer
Inhalte automatisch eine Zuordnung des Artikels zu der aktuell
ausgewählten Sprache, in der die Website betrachtet wird. Wenn Sie
sprachunabhängige Inhalte erstellen wollen, müssen Sie die
Voreinstellung entsprechend ändern.


Übersetzung eines Ordners
-------------------------

Wenn LinguaPlone installiert ist und Sie Artikel in der Website
bearbeiten dürfen, finden Sie im grünen Rahmen das Menü
:guilabel:`Übersetzen in...`. Wenn Sie das Menü aufklappen, sehen Sie
die Sprachen, in die Artikel der Website übersetzt werden können. In
unserem Beispiel in Abbildung :ref:`fig_ordner-uebersetzen` ist dies
Englisch und Französisch. 

.. _fig_ordner-uebersetzen:

.. figure::
   ./images/ordner-uebersetzen.*
   :width: 100%
   :alt: Anzeige eines Ordners mit geöffnetem Auswahlmenü

   Auswahlmenü zur Übersetzung

Wenn Sie eine der verfügbaren Sprachen auswählen, gelangen Sie zu
einem Bearbeitungsformular (siehe Abbildung
:ref:`fig_uebersetzen-ordner`), das auf der linken Seite den Ordner in
der Originalsprache (Deutsch) zeigt und auf der rechten Seiten die
entsprechenden Bearbeitungsfelder für die Übersetzung anbietet. Im
Übrigen ist das Formular genauso aufgebaut wie die Bearbeitungsansicht
eines Ordners. Sie haben wie in der normalen Bearbeitungsansicht in
verschiedenen Teilformularen die Möglichkeiten den Ordner mit Metadaten zu
kategorisieren. Geöffnet ist das Teilformular »Standard«, auf dem Sie den Titel
und die Beschreibung des Ordners eingeben können. Wenn Sie ins Englische
übersetzen, befinden Sie sich in der englischen Sprachversion eines Artikels.
Die Benutzeroberfläche von Plone erscheint entsprechend in Englisch.

.. _fig_uebersetzen-ordner:

.. figure::
   ./images/uebersetzen-ordner.*
   :width: 100%
   :alt: Zweigeteilte Bearbeitungsansicht des Ordners Kochseminar: links in
         Deutsch, rechts sind Formularfelder zur Eingabe der Übersetzung.

   Zweigeteilte Bearbeitungsansicht des Ordners »Kochseminar«

Geben Sie die Übersetzung für Titel und Beschreibung ein und betätigen
Sie die Schaltfläche :guilabel:`Save`. Sie gelangen danach zur Anzeige
des Ordners.

Der Ordner ist zunächst leer. LinguaPlone merkt sich, vom welchem
deutschsprachigen Ordner der Ordner eine Übersetzung darstellt. Wenn
Sie Artikel in dem Ursprungsordner übersetzen, werden die
Übersetzungen automatisch in dem richtigen Ordner der Zielsprache
gespeichert. 

Wechseln Sie daher zurück in den deutschsprachigen Originalordner,
indem Sie in der Sprachauswahl den Verweis (Textlink oder Fähnchen)
zur deutschen Sprachversion anklicken. Sie befinden sich dann wieder
im deutschen Ordner. 

Sie werden feststellen, dass der Kurzname des Ordners von LinguaPlone
automatische geändert wurde, indem der Original-ID ein »-en« angehängt
wurde. Aus :file:`kochseminar` wurde :file:`kochseminar-en`. Dies ist
nicht immer wünschenswert. Schalten Sie also gegebenenfalls die
Bearbeitung von Kurznamen ein, sodass Sie gleich bei der Übersetzung
auch einen passenden Kurznamen festlegen können oder ändern Sie nach
der Übersetzung die Kurznamen der übersetzten Artikel in sinnvoller
Weise über das Menü :guilabel:`Aktionen` oder in der Inhaltsansicht
der Ordner.

Der Status des übersetzten Ordners entspricht dem allgemeinen Anfangsstatus von
Ordnern auf der Website. In der Voreinstellung ist dies der Status »privat«.
Die Arbeitsabläufe der einzelnen Übersetzungen sind voneinander unabhängig.

Ebenso unabhängig vom Originalartikel ist die Historie des übersetzten
Artikels. 

Übersetzung einer Kollektion
----------------------------

Neben Ordnern sind Kollektionen wichtige Gliederungselemente einer
Plone-Website. Auch sie lassen sich mit LinguaPlone übersetzen. Die
Übersetzung erfolgt – wie bei Ordnern und allen anderen Artikeln – in
einer zweigeteilten Bearbeitungsansicht (siehe Abbildung
:ref:`fig_uebersetzen-kollektion`). 

.. _fig_uebersetzen-kollektion:

.. figure::
   ./images/uebersetzen-kollektion.*
   :width: 80%
   :alt: Zweigeteilte Bearbeitungsansicht einer Kollektion

   Zweigeteilte Bearbeitungsansicht einer Kollektion

Auf der linken Seite des Bearbeitungsformulars sehen Sie die Version
der Ausgangssprache, auf der rechten Seite können Sie die Übersetzung
eingeben. Dies gilt für alle Teilformulare der Bearbeitungsansicht. 

Bei der Einstellung der Kriterien gibt es keine zweigeteilte
Ansicht. Bedenken Sie, dass es in der Voreinstellung kein
Suchkriterium »Sprache« bei Kollektionen gibt. Ein solches Kriterium
kann jedoch im Konfigurationsmenü für Kollektionen (siehe Kapitel
:ref:`sec_konfiguration-kollektionen`) hinzugefügt werden. 

Der Status der übersetzten Kollektion entspricht dem Anfangsstatus von
Kollektionen auf der Website, in diesem Falle »privat«.

Übersetzung von Artikeln
========================

Die Übersetzung der anderen Artikeltypen erfolgt in gleicher Weise. Um einen
Artikel zu übersetzen, rufen Sie ihn zunächst in der Originalsprache auf.
Wählen Sie im Auswahlmenü :guilabel:`Übersetzen in...` die gewünschte Sprache
aus und füllen Sie die Felder in der zweigeteilten Bearbeitungsansicht
entsprechend aus.

Einige Formularfelder stehen Ihnen in der Bearbeitungsansicht einer
Übersetzung nicht zur Verfügung. So lässt sich das Freigabe- und
Ablaufdatum einer Übersetzung nicht verändern (siehe Abbildung
:ref:`fig_uebersetzen-teilf-dates`)

.. _fig_uebersetzen-teilf-dates:

.. figure::
   ./images/uebersetzen-teilf-dates.*
   :width: 100%
   :alt: Das Teilformular »Datum« in einer Übersetzung

   Das Teilformular »Datum« in einer Übersetzung

Man kann Übersetzungen auch nicht unabhängig vom Original von der
Navigation ausschließen (siehe :ref:`fig_uebersetzen-teilf-settings`).

.. _fig_uebersetzen-teilf-settings:

.. figure::
   ./images/uebersetzen-teilf-settings.*
   :width: 100%
   :alt: Das Teilformular »Einstellungen in einer Übersetzung

   Das Teilformular »Einstellungen« in einer Übersetzung

Folgende weitere Einschränkungen sollten Sie bei der Übersetzung
beachten:

Seite
   Beim Artikeltyp »Seite« werden im Teilformular »Einstellungen« die
   Vorgaben des Originals beim »Präsentationsmodus« und dem
   »Inhaltsverzeichnis« übernommen und können in Übersetzungen nicht
   geändert werden.

Nachricht
   In der Übersetzung einer Nachricht wird das Titelbild des Originals
   übernommen und kann nicht ausgetauscht werden.

Termin
   Datum und Uhrzeit eines Termins, die Teilnehmer und der
   Veranstaltungstyp werden vom Original unveränderbar übernommen.

Datei
   Beim Artikeltyp »Datei« können nur Titel, Beschreibung und die
   übrigen Metadaten verändert werden, die Datei selbst ist nicht austauschbar. 

Bild
   Das Bild im Artikeltyp »Bild« kann ebenfalls in Übersetzungen nicht
   ausgetauscht werden.

Verwaltung mehrsprachiger Inhalte
=================================

Das Menü :guilabel:`Übersetzen in...` besitzt unterhalb der Liste der
verfügbaren Sprachen den Eintrag :guilabel:`Übersetzungen
verwalten`. Sie gelangen über diesen Verweis zu einem Formular (siehe
Abbildung :ref:`fig_uebersetzungen-verwalten`) mit dem Sie

* die Sprachzuordnung einer Übersetzung verändern können

* beliebige Artikel in der Website als Übersetzung des aktuellen
  Artikels auswählen können und 

* Übersetzungen löschen können.

.. _fig_uebersetzungen-verwalten:

.. figure::
   ./images/uebersetzungen-verwalten.*
   :width: 100%
   :alt: Formular zur Verwaltung von Übersetzungen

   Verwaltung von Übersetzungen

Sprache ändern
--------------

Wenn der angezeigte Artikel irrtümlicherweise als englische
Übersetzung deklariert wurde, in Wirklichkeit aber die französische
Übersetzung ist, können Sie hier die Sprachzuordnung ändern.

Wählen Sie die gewünschte Sprache aus und betätigen Sie die
Schaltfläche :guilabel:`Sprache ändern`.

Übersetzung verknüpfen
----------------------

Wenn Sie bei der Planung Ihrer Website die einzelnen Sprachversionen
anders verwalten möchten als LinguaPlone dies vorgibt oder wenn
Inhalte ohne die Zuhilfenahme von LinguaPlone bereits übersetzt worden
sind, können Sie unter dieser Überschrift den Original-Artikeln die
entsprechenden Übersetzungen zuordnen.

Wählen Sie zunächst die Zielsprache aus und betätigen Sie die
Schaltfläche :guilabel:`Durchsuchen`, um den Artikel, der als
Übersetzung dienen soll, in der Website zu suchen. Es öffnet sich ein
Auswahlformular (siehe Abbildung :ref:`fig_uebersetzung-verknuepfen`),
das genau so zu bedienen ist, wie das im Kapitel
:ref:`sec_teilf-kateg` beschriebene Formular zur Auswahl eines
Verweises.

.. todo:: Screenshot noch aus alter Version, da ein Bug in 4.0.1

.. _fig_uebersetzung-verknuepfen:

.. figure::
   ./images/uebersetzung-verknuepfen.*
   :width: 100%
   :alt: Auswahlformular

   Formular zur Auswahl und Suche eines Artikels

Übersetzungen entfernen
-----------------------

Wenn Sie Übersetzungen entfernen möchten, markieren Sie unter der Überschrift
»Übersetzungen entfernen« die Sprachversion, die entfernt werden soll.
Anschließend haben Sie die Möglichkeit den Artikel, der die Übersetzung
enthält, endgültig zu löschen oder nur die Verknüpfung als Übersetzung zu
lösen. Zum Löschen betätigen Sie die Schaltfläche :guilabel:`Löschen`, um die
Verknüpfung als Übersetzung zu lösen :guilabel:`Unlink`.

.. attention:: Wenn Sie auf :guilabel:`Löschen` klicken, wird der
   Artikel, der als Übersetzung fungiert, in der Website tatsächlich
   gelöscht.

Das Formular zur Verwaltung von Übersetzungen steht nur dann
vollständig zur Verfügung, wenn es von dem Artikel in der
Ursprungssprache aus aufgerufen wird. Wenn Sie das Formular von einer
Übersetzung aus aufrufen, stehen Ihnen aus Sicherheitsgründen nicht
alle Verwaltungsmöglichkeiten zur Verfügung (siehe Abbildung
:ref:`fig_nicht-kanonische-sprache`). Die Ursprungssprache wird
auch als :term:`kanonische Sprache` bezeichnet, da nur in ihr
sämtliche Bearbeitungs- und Verwaltungsmöglichkeiten zur Verfügung
stehen, bei den abgeleiteten Übersetzungen jedoch nicht. 

.. _fig_nicht-kanonische-sprache:

.. figure::
   ./images/nicht-kanonische-sprache.*
   :width: 100%
   :alt: Eingeschränktes Formular zur Verwaltung von Übersetzungen

   Eingeschränktes Formular

Wenn Sie alle Verwaltungsmöglichkeiten zur Verfügung haben wollen,
müssen Sie zur kanonischen Sprache wechseln. Ein entsprechender
Verweis befindet sich unten auf dem Formular.

.. _Internationalization: http://plone.org/documentation/manual/plone-community-developer-documentation/i18n/
