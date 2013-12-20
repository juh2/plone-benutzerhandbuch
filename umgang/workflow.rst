.. _sec_workflow:

================
 Arbeitsabläufe
================

Während Sie einen Artikel erstellen, möchten Sie in der Regel nicht,
dass der unfertige Text öffentlich eingesehen werden kann. Im
Gegenteil: er soll nur Ihnen persönlich oder einer kleinen Gruppe
zugänglich sein. Erst nach der Fertigstellung soll er durch Sie oder
eine andere dazu berechtigte Person veröffentlicht werden.

Ihre Website kann so konfiguriert sein, dass Sie einen
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

Status
======

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

.. table:: Farbliche Kennzeichnung des Revisionsstatus

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

Nicht jeder Übergang eines Artikels von einem Status in einen anderen ist
sinnvoll. Der Arbeitsablauf gibt daher nicht nur die Status, sondern auch die
möglichen Statusänderungen vor. Beispielsweise gibt es eine Statusänderung
»veröffentlichen«, bei der ein Artikel vom Status »privat« in den Status
»veröffentlicht« versetzt wird (siehe Abb.: :ref:`fig-status-statusaenderung`).
Statuswechsel entsprechen den Tätigkeiten, die neben der eigentlichen
inhaltlichen Bearbeitung von Artikeln die redaktionelle Arbeit ausmachen.

.. _fig-status-statusaenderung:

.. figure:: ../images/status-statusaenderung.*
   :width: 70%
   
   Status und Statusänderung

Der Arbeitsablauf regelt auch, unter welchen Bedingungen man eine
Statusänderung vornehmen darf. So darf man beispielsweise einen
Artikel nur dann veröffentlichen, wenn man in dem Ordner, in dem sich
der Artikel befindet, das Recht zum Veröffentlichen hat. In Abschnitt
:ref:`sec_ansicht-freigabe` wird beschrieben, wie diese Rechte
in einzelnen Ordnern zugewiesen werden können. Wenn Sie also in einem
Ordner veröffentlichen dürfen, können Sie dort die im Folgenden
beschriebenen Aufgaben eines Redakteurs wahrnehmen.

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

Der Standardarbeitsablauf von Plone wird als einfacher Arbeitsablauf
bezeichnet.  Anonyme und angemeldete Besucher können auf Artikel, die
diesem Arbeitsablauf unterworfen sind, erst dann zugreifen, wenn sie
veröffentlicht wurden. Siehe Abbildung :ref:`fig_workflow-einfach`.

.. _fig_workflow-einfach:

.. figure:: ../images/workflow-einfach.*
   :width: 50%

   Einfacher Arbeitsablauf

Es können für ausgewählte Benutzer und Benutzergruppen Ausnahmen
eingerichtet werden, indem man ihnen die Inhalte in bestimmten Ordnern
zur Ansicht oder zur Bearbeitung freigibt. Näheres hierzu erfahren Sie
in Kapitel :ref:`sec_ansicht-freigabe`.   

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
  Übergang vom Status »privat« in den Status »zur Redaktion
  eingereicht«. Der Übergang kann vom Besitzer des Artikels, aber auch
  von einem Redakteur oder dem Administrator ausgelöst werden.

Veröffentlichen
  Übergang vom Status »privat« oder »zur Redaktion
  eingereicht« in den Status »veröffentlicht«. Ein Redakteur oder ein
  Administrator ändert den Status des Artikels in »veröffentlicht« und
  macht ihn damit für alle Besucher der Website sichtbar. 

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
mehr sichtbar sein soll, muss er von der Website gelöscht werden. 

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
  Anfangsstatus (grün); ein neu hinzugefügter Artikel wird als
  öffentlicher Entwurf behandelt. Das heißt, jeder Besucher der
  Website kann den Artikel einsehen. Er taucht in der Navigation auf
  und kann über die Suche gefunden werden. Ein öffentlicher Entwurf
  kann jedoch nur von seinem Besitzer oder einem Redakteur bearbeitet
  werden.

Privat
  (rot) In diesem Status ist ein Artikel nur von seinem Besitzer
  sowie von Administratoren einsehbar.

Zur Redaktion eingereicht
  (orange) Siehe Abschnitt :ref:`sec_einf-publ`.

Veröffentlicht
  (blau) Ein Artikel in diesem Status ist allen Benutzern
  zugänglich. Er kann nicht mehr von seinem Besitzer oder von
  Redakteuren, sondern nur noch von Administratoren bearbeitet werden.


Die entsprechenden Statusänderungen heißen:

Privat schalten
  Übergang vom Status »öffentlicher Entwurf« in den Status
  »privat«. Der Besitzer versteckt dabei einen Artikel vor der
  Allgemeinheit, zum Beispiel um ihn in Ruhe zu bearbeiten.

Als Entwurf zeigen
  Übergang vom Status »privat« in den Status »öffentlicher
  Entwurf«. Der Besitzer macht damit einen privaten Artikel für die
  Allgemeinheit verfügbar.

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
  Anfangsstatus (grün); ein neu angelegter Artikel ist für alle
  angemeldeten Benutzer sichtbar. Anonyme Besucher der Website haben
  keinen Zugriff.

Privat
 (rot) Siehe Abschnitt :ref:`sec_comm-arbe`.

Zur Redaktion eingereicht
 (orange) Siehe Abschnitt :ref:`sec_einf-publ`.

Intern veröffentlicht
  (blau) Ein Artikel in diesem Status ist allen angemeldeten Benutzern
  zugänglich. Er kann nicht mehr von seinem Besitzer oder von
  Redakteuren, sondern nur noch von Administratoren bearbeitet werden.

Extern sichtbar
  (blau) Ein Artikel in diesem Status ist allen Besuchern der Website
  zugänglich. Er kann ebenfalls nur noch von Administratoren
  bearbeitet werden.

Die entsprechenden Statusänderungen lauten:

Privat schalten
  Übergang vom Status »interner Entwurf« in den Status »privat«. Der
  Besitzer versteckt dabei einen Artikel vor der Allgemeinheit, zum
  Beispiel um ihn in Ruhe zu bearbeiten.

Intern zeigen
  Übergang vom Status »privat« in den Status »interner Entwurf«. Der
  Besitzer macht den Artikel damit allen angemeldeten Besuchern
  zugänglich.

Zur Veröffentlichung einreichen
  Siehe Abschnitt :ref:`sec_einf-publ`.

Intern veröffentlichen
  Übergang vom Status »interner Entwurf« oder »zur Redaktion
  eingereicht« in den Status »intern veröffentlicht«. Ein Redakteur
  macht den Artikel für angemeldete Benutzer zugänglich.

Extern veröffentlichen
  Übergang vom Status »zur Redaktion eingereicht« oder »intern
  veröffentlicht« in den Status »extern sichtbar«. Ein Redakteur macht
  den Artikel auch anonymen Besuchern der Website zugänglich.

Zurückweisen
  Übergang vom Status »zur Redaktion eingereicht« oder »intern
  veröffentlicht« in den Status »interner Entwurf«. Ein Redakteur
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

Das wichtigste Bedienelement des Arbeitsablaufs ist das Statusmenü
(siehe Abbildung :ref:`fig_workflow`).

.. _fig_workflow:

.. figure:: ../images/workflow.*
   :width: 30%

   Statusmenü

Es gehört zu den Ausklappmenüs, die sich in der grünen Leiste über
der Artikelanzeige befinden.

Der Titel des Menüs gibt stets den aktuellen Status des betrachteten Artikels
wieder. Das Menü enthält Einträge für die jeweils möglichen Statuswechsel und
einen Eintrag mit der Bezeichnung :guilabel:`Erweitert`.

Wählen Sie einen der Statuswechsel, so wird der Status des Artikels
unmittelbar geändert, und die Änderung wird in der folgenden Statusmeldung
bestätigt. Die Einträge im Statusmenü haben sich infolge des Statuswechsels
geändert: es sind nun die Tätigkeiten aufgeführt, die Sie mit dem Artikel in
seinem neuen Revisionsstatus ausführen können.

Um zusätzlich zum Statuswechsel das Freigabe- und Ablaufdatum
einzustellen oder einen Kommentar zu speichern, wählen Sie den Eintrag
:guilabel:`Erweitert`. Sie gelangen damit zu dem Formular, das in
Abschnitt :ref:`sec_batch-publishing` beschrieben wird.

Historie der Statusänderungen
-----------------------------

Plone protokolliert für jeden Artikel die Statusänderungen mit den Kommentaren
der Benutzer in der Historie (siehe Abbildung :ref:`fig_workflow-historie`).

.. _fig_workflow-historie:

.. figure:: ../images/workflow-historie.*
   :width: 100%

   Historie der Statusänderungen eines Artikels

Die Tabelle enthält für jeden Protokolleintrag folgende Angaben (siehe
Abbildung :ref:`fig_workflow-historie`):

* Bezeichnung des Statuswechsels (Zur Veröffentlichung einreichen,
  Zurückweisen, Veröffentlichen)
* Name des Benutzers, der den Statuswechsel vorgenommen hat
* Datum und Uhrzeit des Statuswechsels
* Kommentar

Dabei ist der Name des Benutzers ein Verweis auf sein Profil in der Website.

.. _sec_revisionsliste:

Revisionsliste
--------------

Die Revisionsliste ist ein Portlet, das Redakteuren eine Liste aller zur
Veröffentlichung eingereichten Artikel anzeigt (siehe
Abbildung :ref:`fig_portlet-revlist`). Es wird Redakteuren per
Voreinstellung auf ihrer persönlichen Seite angezeigt. 

.. _fig_portlet-revlist:

.. figure:: ../images/portlet-revlist.*
   :width: 60%

   Portlet »Revisionsliste«


So haben Redakteure einen Überblick über die anstehende Arbeit und können die
zu prüfenden Artikeln direkt aufrufen.

Jeder zu prüfende Artikel ist mit Titel, Autor und Datum der letzten
Änderung aufgeführt. Der Titel ist ein Verweis zum Artikel
selbst. Wenn Sie den Mauszeiger über den Titel halten, sehen Sie
zusätzlich die Beschreibung des Artikels.

Die Liste ist nach dem Einreichungsdatum sortiert und beginnt mit dem
Artikel, der bereits am längsten auf die Prüfung wartet.


.. _sec_batch-publishing:

Gleichzeitige Statusänderung mehrerer Artikel
=============================================

Um Zeit zu sparen, möchte man manchmal den Status mehrerer Artikel
gleichzeitig verändern. Sofern sich die Artikel in einem Ordner
befinden, können Sie dies in Plone tun. Wählen Sie dazu zunächst in
der Inhaltsansicht des Ordners die betreffenden Artikel aus und
betätigen Sie dann bei den Ordneraktionen unterhalb der
Artikelauflistung die Schaltfläche :guilabel:`Status ändern`
(siehe Abbildung :ref:`fig_ordnerinhalt`). Sie gelangen daraufhin zum
Formular für die gemeinsame Statusänderung.

.. _fig_publikationsprozess-1:

.. figure:: ../images/publikationsprozess-1.*
   :width: 100%

   Formular für den Arbeitsablauf, oben

Im ersten Formularfeld (siehe Abbildung
:ref:`fig_publikationsprozess-1`) sind die Artikel aufgelistet, die
Sie vorher in der Inhaltsansicht ausgewählt haben. Wenn Sie Ihre
Meinung ändern und Artikel von der Statusänderung ausnehmen wollen,
entfernen Sie einfach das Häkchen neben dem entsprechenden Artikel.

Falls sich in der Liste mindestens ein Ordner befindet, können Sie
unterhalb der Liste ein Häkchen setzen und die Statusänderung »auf
alle Artikel im Ordner anwenden«. Daraufhin wird der Status aller
Artikel geändert, die in den enthaltenen Ordnern und ihren
Unterordnern liegen. Falls in der Liste kein Ordner ist, wird diese
Option nicht angeboten.

Falls Sie über den Eintrag :guilabel:`Erweitert` im Statusmenü eines
einzelnen Artikels zu diesem Formular gelangt sind, enthält die Liste
der betroffenen Artikel nur einen einzigen Eintrag.

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
versetzt werden. Wählen Sie ein Ablaufdatum, so werden die Artikel unabhängig
von ihrem Status ab jenem Zeitpunkt nicht mehr als veröffentlicht
behandelt.

Nach den beiden Fristen folgt ein Formularfeld für einen Kommentar,
der in die Historie der Artikel eingefügt wird.

Schließlich bietet dieses Formular eine Auswahl möglicher
Statuswechsel an.  Wenn Sie einen Statuswechsel auswählen, der für
einige der Artikel nicht möglich ist, so wird er auf die anderen
dennoch angewandt. Sie können jedoch auch die Status aller Artikel
beibehalten, wenn Sie nur die Fristen bearbeiten wollen.
