.. _sec_workflow:

================
 Arbeitsabläufe
================

Während Sie einen Artikel erstellen, möchten Sie in der Regel nicht,
dass der unfertige Artikel öffentlich eingesehen werden kann. So lange
er nicht fertig ist, soll er nur Ihnen persönlich oder einer kleinen
Gruppe zugänglich sein. Erst nach der Fertigstellung soll er
durch Sie oder eine andere dazu berechtigte Person veröffentlicht werden.

Ihre Website kann nämlich auch so konfiguriert sein, dass Sie einen
Artikel nicht unmittelbar selbst veröffentlichen können, sondern eine
andere Person Ihren Artikel vor der Veröffentlichung begutachten
muss. Wir bezeichnen eine solche Person im Folgenden als Redakteur.

Von der Idee bis zur Fertigstellung durchläuft ein Artikel in diesen Fällen
einen Arbeitsablauf, der die einzelnen Schritte im Zusammenspiel zwischen
Autoren und Redakteuren regelt. Plone stellt verschiedene Arbeitsabläufe zur
Verfügung, die sich für unterschiedliche Szenarien eignen.

Ein Arbeitsablauf in Plone besteht aus einer bestimmten Anzahl von Zuständen,
in denen sich ein Artikel befinden kann, und einer Reihe von Übergängen
zwischen diesen Zuständen. Man spricht auch von Status und Statusänderungen.

.. _sec_status:

========
 Status
========

Der Arbeitsablauf steuert, wer unter welchen Bedingungen Artikel einer
Website einsehen darf. Er unterscheidet beispielsweise Artikel, die
nur ihr Besitzer sehen darf, von solchen, die den angemeldeten
Benutzern oder jedem beliebigen Besucher der Website angezeigt werden.

Der Status eines Artikels bestimmt, wer den Artikel einsehen
darf. Jeder Artikel, der einem Arbeitsablauf unterworfen ist, besitzt
einen Status, und im Arbeitsablauf kann dieser Status von Autoren und
Redakteuren verändert werden.

Wenn Sie an der Website angemeldet sind, stellt Plone die Verweise auf
Artikel in Ordnerübersichten und Portlets farbig dar. Die Farbe zeigt
dabei den Status an (siehe Tabelle :ref:`tab_status-farben`).

.. _tab_status-farben:

.. table:: Farbliche Kennzeichnung der Revisionsstatus

   ======    =========================
   Farbe     Status
   ======    =========================
   rot	     privat
   grün	     öffentlicher Entwurf
   orange    zur Redaktion eingereicht
   blau	     veröffentlicht
   ======    =========================

Navigationselemente wie die Reiter in der Hauptnavigation, Verweise in
Portlets oder die Nachrichten- und Terminübersicht sind in der
Voreinstellung so konfiguriert, dass sie nur veröffentlichte Artikel
anzeigen.

Statusänderung
==============

Nicht jeder Übergang eines Artikels von einem Status in einen anderen
ist sinnvoll. Der Arbeitsablauf gibt daher nicht nur die Status,
sondern auch die möglichen Statusänderungen vor. Beispielsweise gibt
es eine Statusänderung »veröffentlichen«, bei der ein Artikel vom
Status »privat« in den Status »veröffentlicht« versetzt
wird. Statuswechsel entsprechen den Tätigkeiten, die neben der
eigentlichen inhaltlichen Bearbeitung von Artikeln die redaktionelle
Arbeit ausmachen.

Der Arbeitsablauf regelt auch, unter welchen Bedingungen man eine
Statusänderung vornehmen darf. So darf man beispielsweise einen Artikel nur
dann veröffentlichen, wenn man in dem Ordner, in dem sich der Artikel
befindet, das Recht zum Veröffentlichen hat. In
Abschnitt :ref:`sec_zugriffsrechte-ansicht` wird beschrieben, wie diese
Rechte in einzelnen Ordnern zugewiesen werden können. Wenn Sie also in einem
Ordner veröffentlichen dürfen, können Sie dort die im Folgenden beschriebenen
Aufgaben eines Redakteurs wahrnehmen.

Plone kennt vier Arbeitsabläufe, die für ganz unterschiedliche
Anforderungen ausgelegt sind:

* Einfacher Arbeitsablauf
* Arbeitsablauf mit einem Status
* Community-Arbeitsablauf
* Intranet-Arbeitsablauf

Außerdem kann die Website so konfiguriert werden, dass die
Sichtbarkeit von Artikeln nicht durch einen Arbeitsablauf, sondern
durch den Status des Ordners bestimmt wird, in dem sie sich
befinden. Das ist per Voreinstellung bei Bildern und Dateien der
Fall. Solche Artikel besitzen keinen Status und kennen keine
Statusänderungen.

Es ist Sache des Administrators zu bestimmen, welcher Arbeitsablauf
für welche Artikeltypen einer Website angewendet wird. Es kann also
zum Beispiel der Fall eintreten, dass der Artikeltyp »Seite« einem
anderen Arbeitsablauf unterliegt als der Typ »Nachricht«.

.. _sec_einf-publ:

Einfacher Arbeitsablauf
=======================

Plones Standardarbeitsablauf wird als einfacher Arbeitsablauf
bezeichnet.  Nicht angemeldete Besucher können auf Artikel, die diesem
Arbeitsablauf unterworfen sind, erst dann zugreifen, wenn sie
veröffentlicht wurden. Siehe Abbildung :ref:`fig_workflow-einfach`.

.. _fig_workflow-einfach:

.. figure:: ../images/workflow-einfach.*
   :width: 50%

   Einfacher Arbeitsablauf



Der einfache Arbeitsablauf umfasst drei Status:

Privat
  Anfangsstatus (rot); neu angelegte Artikel befinden sich im Status
  »privat«. Ein privater Artikel darf nur von seinem Besitzer oder einem
  Administrator eingesehen und bearbeitet werden.

Zur Redaktion eingereicht
  (orange) Ein Artikel in diesem Status wurde zur Prüfung eingereicht,
  damit ihn ein Redakteur freigeben oder zurückweisen kann. Besitzer
  und Redakteure dürfen den Artikel einsehen, aber nur Redakteure
  dürfen ihn bearbeiten.  

Veröffentlicht 
  (blau) Jeder Besucher der Website darf veröffentlichte
  Artikel einsehen. Sie werden auch anonymen Besuchern in der
  Navigation angezeigt. Ein Artikel kann nach der Veröffentlichung von
  seinem Besitzer und von Redakteuren bearbeitet werden.

Die Statusänderungen entsprechen folgenden Tätigkeiten:


Zur Veröffentlichung einreichen
  Übergang vom Status
  »privat« in den Status »zur Redaktion eingereicht«. Der Übergang kann vom
  Besitzer des Artikels, aber auch von einem Redakteur oder dem Administrator
  ausgelöst werden.

Veröffentlichen
  Übergang vom Status »privat« oder »zur Redaktion
  eingereicht« in den Status »veröffentlicht«. Ein Redakteur oder ein
  Administrator ändert den Status des Artikels in »veröffentlicht« und weist
  den Artikel damit als offiziellen Inhalt der Website aus.

Zurückweisen
  Übergang vom Status »zur Redaktion eingereicht« oder
  »veröffentlicht« in den Status »privat«. Ein Redakteur lehnt damit die
  Veröffentlichung auf der Website ab. Der Autor kann den Artikel nach
  weiterer Bearbeitung erneut zur Prüfung einreichen. 

Zurückziehen
  Übergang vom Status »zur Redaktion eingereicht« oder
  »veröffentlicht« in den Status »privat«. Der Besitzer zieht einen
  Artikel aus dem veröffentlichten Inhalt der Website zurück,
  beispielsweise um ihn zu überarbeiten und später erneut zur
  Veröffentlichung einzureichen.


Arbeitsablauf mit einem Status
==============================

In diesem Arbeitsablauf befinden sich Artikel sofort im Status
»veröffentlicht«. Es gibt nur diesen einen Status und damit auch keine
Statusänderungen. Wenn ein Artikel, der diesem Arbeitsablauf unterliegt, nicht
mehr sichtbar sein soll, muss er von der Website gelöscht werden. Siehe
Abbildung :ref:`fig_workflow-ein-status`.

.. _fig_workflow-ein-status:

.. figure:: ../images/workflow-ein-status.*
   :width: 30%

   Arbeitsablauf mit einem Status

.. _sec_comm-arbe:

Community-Arbeitsablauf
=======================

Artikel im Community-Arbeitsablauf sind für alle Besucher der Website
sichtbar, sofern sie nicht ausdrücklich in den Status »privat« versetzt
wurden (siehe Abbildung :ref:`fig_workflow-community`).

.. _fig_workflow-community:

.. figure:: ../images/workflow-community.*
   :width: 50%

   Community-Arbeitsablauf

Es gibt folgende Status:


Öffentlicher Entwurf
  Anfangsstatus (grün); ein neu hinzugefügter
  Artikel wird als öffentlicher Entwurf behandelt. Das heißt, jeder Besucher
  der Website kann den Artikel einsehen. Er taucht in der Navigation auf und
  kann über die Suche gefunden werden. Ein öffentlicher Entwurf kann jedoch
  nur von seinem Besitzer oder einem Redakteur bearbeitet werden.

Privat
  (rot) In diesem Status ist ein Artikel nur von seinem Besitzer
  sowie von Administratoren einsehbar.

Zur Redaktion eingereicht
  (orange) Siehe Abschnitt :ref:`sec_einf-publ`.

Veröffentlicht
  (blau) Ein Artikel in diesem Status ist allen Benutzern
  zugänglich. Er kann nicht mehr von seinem Besitzer oder von Redakteuren,
  sondern nur noch von Administratoren bearbeitet werden.


Die entsprechenden Statusänderungen heißen:

Privat schalten
  Übergang vom Status »öffentlicher Entwurf« in den
  Status »privat«. Der Besitzer versteckt dabei einen Artikel vor der
  Allgemeinheit, zum Beispiel um ihn in Ruhe zu bearbeiten.

Als Entwurf zeigen
  Übergang vom Status »privat« in den Status
  »öffentlicher Entwurf«. Der Besitzer macht damit einen privaten Artikel
  für die Allgemeinheit verfügbar.

Zur Veröffentlichung einreichen
  Siehe Abschnitt :ref:`sec_einf-publ`.

Veröffentlichen
  Obwohl Artikel bereits als Entwurf für alle Besucher sichtbar sind,
  ist es sinnvoll, Artikel zu veröffentlichen. Je nach Konfiguration
  der Website werden sie beispielsweise erst dann in der Navigation
  angezeigt.

Zurückweisen
  Übergang vom Status »zur Redaktion eingereicht« in den
  Status »öffentlicher Entwurf«. Ein Redakteur lehnt eine Veröffentlichung
  des Artikels ab.

Zurückziehen
  Übergang vom Status »veröffentlicht« oder »zur Redaktion
  eingereicht« in den Status »öffentlicher Entwurf«. Der Besitzer
  zieht den Artikel von der Veröffentlichung zurück.

.. _sec_intr-arbe:

Intranet-Arbeitsablauf
======================

Der Intranet-Arbeitsablauf ist für Websites gedacht, die ganz oder teilweise
nur einer geschlossenen Benutzergruppe zugänglich sein sollen. Der wesentliche
Unterschied zum Community-Arbeitsablauf besteht darin, dass man Artikel
intern und extern veröffentlichen kann. Siehe
Abbildung :ref:`fig_workflow-intranet`.

.. _fig_workflow-intranet:

.. figure:: ../images/workflow-intranet.*
   :width: 70%

   Intranet-Arbeitsablauf

Es gibt folgende Status:

Interner Entwurf
  Anfangsstatus (grün); ein neu angelegter Artikel ist
  für alle angemeldeten Benutzer sichtbar. Anonyme Besucher der Website haben
  keinen Zugriff.

Privat
 (rot) Siehe Abschnitt :ref:`sec_comm-arbe`.

Zur Redaktion eingereicht
 (orange) Siehe Abschnitt :ref:`sec_einf-publ`.

Intern veröffentlicht
  (blau) Ein Artikel in diesem Status ist allen
  angemeldeten Benutzern zugänglich. Er kann nicht mehr von seinem Besitzer
  oder von Redakteuren, sondern nur noch von Administratoren bearbeitet
  werden.

Extern sichtbar
  (blau) Ein Artikel in diesem Status ist allen
  Besuchern der Website zugänglich. Er kann ebenfalls nur noch von
  Administratoren bearbeitet werden.

Die entsprechenden Statusänderungen lauten:

Privat schalten
  Übergang vom Status »interner Entwurf« in den
  Status »privat«. Der Besitzer versteckt dabei einen Artikel vor der
  Allgemeinheit, zum Beispiel um ihn in Ruhe zu bearbeiten.

Intern zeigen
  Übergang vom Status »privat« in den Status »interner
  Entwurf«. Der Besitzer macht den Artikel damit allen angemeldeten Besuchern
  zugänglich.

Zur Veröffentlichung einreichen
  Siehe Abschnitt :ref:`sec_einf-publ`.

Intern veröffentlichen
  Übergang vom Status »interner Entwurf« oder »zur
  Redaktion eingereicht« in den Status »intern veröffentlicht«. Ein Redakteur
  macht den Artikel für angemeldete Benutzer zugänglich.

Extern veröffentlichen
  Übergang vom Status »zur Redaktion eingereicht«
  oder »intern veröffentlicht« in den Status »extern sichtbar«. Ein Redakteur
  macht den Artikel auch anonymen Besuchern der Website zugänglich.

Zurückweisen
  Übergang vom Status »zur Redaktion eingereicht« oder
  »intern veröffentlicht« in den Status »interner Entwurf«. Ein Redakteur
  lehnt eine Veröffentlichung des Artikels ab.

Zurückziehen
  Übergang vom Status »zur Redaktion eingereicht«, »intern
  veröffentlicht« oder »extern sichtbar« in den Status »interner
  Entwurf«. Der Besitzer zieht den Artikel von der Veröffentlichung
  zurück.  

.. _sec_bedienelemente:

Bedienelemente
==============

Statusmenü
----------

Das wichtigste Bedienelement des Arbeitsablaufs
ist das Statusmenü (siehe Abbildung :ref:`fig_workflow`).

.. _fig_workflow:

.. figure:: ../images/workflow.*
   :width: 100%

   Statusmenü

Es gehört zu den Ausklappmenüs, die sich in dem grünen Rahmen um die
Artikelanzeige befinden.

Der Titel des Menüs gibt stets den aktuellen Status des betrachteten Artikels
wieder. Das Menü enthält Einträge für die jeweils möglichen Statuswechsel und
einen Eintrag mit der Bezeichnung »Erweitert«.

Wählen Sie einen der Statuswechsel, so wird der Status des Artikels
unmittelbar geändert, und die Änderung wird in der folgenden Statusmeldung
bestätigt. Die Einträge im Statusmenü haben sich infolge des Statuswechsels
geändert: es sind nun die Tätigkeiten aufgeführt, die Sie mit dem Artikel in
seinem neuen Revisionsstatus ausführen können.

Um zusätzlich zum Statuswechsel das Freigabe- und Ablaufdatum einzustellen
oder einen Kommentar zu speichern, wählen Sie den Eintrag »Erweitert«. Sie
gelangen damit zu dem Formular, das in Abschnitt :ref:`sec_batch-publishing`
beschrieben wird.

Historie der Statusänderungen
-----------------------------

Plone protokolliert für jeden Artikel die Statusänderungen mit den Kommentaren
der Benutzer. Sobald für einen Artikel wenigstens eine Statusänderung oder ein
Kommentar zum Arbeitsablauf vorliegt, können Sie das Protokoll einsehen. In
der Anzeige des Artikels finden Sie dann unten eine ausklappbare Tabelle mit
allen Protokolleinträgen, die mit »Historie« beschriftet ist
(siehe Abbildung :ref:`fig_workflow-historie-eingeklappt`).

.. _fig_workflow-historie-eingeklappt:

.. figure:: ../images/workflow-historie-eingeklappt.*
   :width: 100%

   Ausklappschalter für die Statushistorie

Die Tabelle enthält für jeden Protokolleintrag folgende Angaben (siehe
Abbildung :ref:`fig_workflow-historie`):

.. _fig_workflow-historie:

.. figure:: ../images/workflow-historie.*
   :width: 100%

   Historie der Statusänderungen eines Artikel	s


* Aktion: Bezeichnung des Statuswechsels
* Ausgeführt von: Name des Benutzers, der den Statuswechsel vorgenommen hat
* Datum und Uhrzeit des Statuswechsels
* Kommentar

Dabei ist der Name des Benutzers ein Verweis auf sein Profil in der Website.

.. _sec_revisionsliste:

Revisionsliste
--------------

Die Revisionsliste ist ein Portlet, das Redakteuren eine Liste aller zur
Veröffentlichung eingereichten Artikel anzeigt (siehe
Abbildung :ref:`fig_portlet-revlist`).

.. _fig_portlet-revlist:

.. figure:: ../images/portlet-revlist.*
   :width: 100%

   Portlet »Revisionsliste«


So haben Redakteure einen Überblick über die anstehende Arbeit und können die
zu prüfenden Artikeln direkt aufrufen.

Jeder zu prüfende Artikel ist mit Titel und Datum der letzten Änderung
aufgeführt. Der Titel ist ein Verweis zum Artikel selbst, und ein
Symbol zeigt den Artikeltyp an. Wenn Sie den Mauszeiger über den Titel
halten, sehen Sie zusätzlich die Beschreibung des Artikels.

Die Liste ist nach dem Einreichungsdatum sortiert und beginnt mit dem
Artikel, der bereits am längsten auf die Prüfung wartet.


.. _sec_batch-publishing:

Gleichzeitige Statusänderung mehrerer Artikel
=============================================

Gehören mehrere Artikel inhaltlich zusammen, kann es sinnvoll sein, ihren
Status gemeinsam in einem Arbeitsschritt zu verändern.  Das betrifft
beispielsweise eine Seite mit den darin verwendeten Bildern oder mehrere
Artikel, die gleichzeitig veröffentlicht oder aus dem öffentlichen Angebot
herausgenommen werden sollen.

Sie können in Plone gleichzeitig für mehrere Artikel in einem Ordner
Freigabedatum und Ablaufdatum bearbeiten, Kommentare anfügen und den Status
ändern. Wählen Sie dazu zunächst in der Inhaltsansicht des Ordners die
betreffenden Artikel aus. Unter den Ordneraktionen befindet sich eine mit der
Bezeichnung »Status ändern« (siehe Abbildung :ref:`fig_ordnerinhalt`). Sie
gelangen daraufhin zum Formular für die gemeinsame Statusänderung.

.. _fig_publikationsprozess-1:

.. figure:: ../images/publikationsprozess-1.*
   :width: 100%

   Formular für den Arbeitsablauf, oben

Das erste Formularfeld (siehe Abbildung
:ref:`fig_publikationsprozess-1`) enthält eine Liste mit einem Eintrag
für jeden angekreuzten Artikel. Zu Beginn sind alle Artikel
angekreuzt. Sie können die Menge der tatsächlich betroffenen Artikel
nochmals einschränken, indem Sie Markierungen aus der Liste entfernen.

Falls sich in der Liste mindestens ein Ordner befindet, können Sie
unterhalb der Liste ein Häkchen setzen und die Statusänderung »auf
alle Artikel im Ordner anwenden«. Daraufhin wird der Status aller
Artikel geändert, die in den enthaltenen Ordnern und ihren
Unterordnern liegen. Falls in der Liste kein Ordner ist, wird diese
Option nicht angeboten.

Falls Sie über den Eintrag »Erweitert« im Statusmenü eines einzelnen
Artikels zu diesem Formular gelangt sind, enthält die Liste der
betroffenen Artikel nur einen einzigen Eintrag.

.. _fig_publikationsprozess-2:

.. figure:: ../images/publikationsprozess-2.*
   :width: 100%

   Formular für den Arbeitsablauf, unten

Die nächsten beiden Formularfelder (siehe Abbildung
:ref:`fig_publikationsprozess-2`) dienen der Eingabe von Freigabedatum
und Ablaufdatum. In beiden Fällen können Sie Datum und Uhrzeit
wählen. Für die Auswahl des Datums steht Ihnen ein Kalender zur
Verfügung, den Sie über das Kalendersymbol rechts neben dem
Auswahlfeld für den Tag erreichen. Wenn Sie ein Freigabedatum angeben,
werden die Artikel frühestens ab diesem Zeitpunkt als veröffentlicht
behandelt, auch wenn sie bereits vorher in den Status »veröffentlicht«
gelangen. Wählen Sie ein Ablaufdatum, so werden die Artikel unabhängig
von ihrem Status ab jenem Zeitpunkt nicht mehr als veröffentlicht
behandelt.

Nach den beiden Fristen folgt ein Formularfeld für einen Kommentar,
der in die Statushistorie der Artikel eingefügt wird.

Schließlich bietet dieses Formular eine Auswahl möglicher
Statuswechsel an.  Wählen Sie einen Statuswechsel aus, der für einige
der Artikel nicht möglich ist, so wird er auf die anderen dennoch
angewandt. Sie können jedoch auch die Revisionsstatus aller Artikel
beibehalten, wenn Sie nur die Fristen bearbeiten oder einen Kommentar
eingeben wollen.
