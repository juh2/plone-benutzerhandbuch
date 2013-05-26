.. _sec_konfiguration-benutzer-gruppen:

======================
 Benutzer und Gruppen
======================

Die Benutzerverwaltung in Plone sowie die Möglichkeit, mehrere
Benutzer zu Gruppen zusammenzufassen und Gruppen als Untergruppen
einer übergreifenden Gruppe zuzuordnen, gehören zu den
herausragendsten Leistungsmerkmalen des CMS Plone. Innerhalb des CMS
lassen sich so sehr flexibel Hierarchien, Abteilungen und
Arbeitsgruppen von Unternehmen und Organisationen abbilden.

Zuweisung von Funktionen an Benutzer und Gruppen
================================================

Funktionen können zunächst einzelnen Benutzern zugewiesen werden. Man kann
beispielsweise Benutzer A die Funktion »Ansehen« zuweisen und Benutzer B die
Funktion »Bearbeiten«. Dadurch wäre Benutzer B in der Lage, einen Inhalt zu
verändern, den Benutzer A lediglich ansehen kann (siehe Abb.: :ref:`fig_funktion-zuweisen-benutzer`).

.. _fig_funktion-zuweisen-benutzer:

.. figure:: 
   ../images/funktion-zuweisen-benutzer.*
   :width: 50%
   :alt: Grafische Darstellung der Zuweisung

   Zuweisung an Benutzer

Die Funktionen können auch Gruppen zugewiesen werden. In einem CMS mit vielen
Benutzern wird die Zuordnung von Funktionen zu einzelnen Benutzern schnell
unübersichtlich. Daher kann man in Plone die Funktionen auch ganzen Gruppen
zuweisen. Benutzer, die Mitglied einer Gruppe sind, können alle Funktionen
ausüben, die der Gruppe zugewiesen wurden. Da Benutzer verschiedenen Gruppen
angehören können, erhöht die Zuweisung von Funktionen an Gruppen die
Flexibilität des Systems, ohne dass dabei der Überblick verloren
geht (siehe Abb.: :ref:`fig_funktion-zuweisen-gruppe`).

.. _fig_funktion-zuweisen-gruppe:

.. figure::
   ../images/funktion-zuweisen-gruppe.*
   :width: 50%
   :alt: Grafische Darstellung der Zuweisung

   Zuweisung an Gruppe
        
In Plone können Gruppen Mitglied einer Gruppe sein (siehe Abb.:
:ref:`fig_verschachtelte-gruppe`). Dadurch wird das Zugriffsmanagement noch
flexibler und es wird möglich, Organisationshierarchien realistisch in Plone
abzubilden. Es lassen sich Arbeitsbereiche und Zuständigkeiten für Abteilungen
und ihre Unterabteilungen mit fein justierten Zugriffsrechten bilden. Spontan
zusammengestellte Teams können wahlweise aus einzelnen Benutzern oder ganzen
organisatorischen Einheiten gebildet werden.

.. _fig_verschachtelte-gruppe:

.. figure::
   ../images/verschachtelte-gruppe.*
   :width: 50%
   :alt: Grafische Darstellung einer verschachtelten Gruppe

   Verschachtelte Gruppen

In der Benutzer- und Gruppenkonfiguration weisen Sie Funktionen global zu. Sie
können die Funktionen aber auch ordnerweise zuweisen. So kann beispielsweise
die Gruppe A im Ordner A Inhalte ansehen, während Gruppe B diese bearbeiten
kann. Im Ordner B kann dies genau umgekehrt sein (siehe Abb.:
:ref:`fig_funktion-ordnerweise-zuweisen`). Lesen Sie dazu Kapitel
:ref:`sec_ansicht-freigabe`.

.. _fig_funktion-ordnerweise-zuweisen:

.. figure::
   ../images/funktion-ordnerweise-zuweisen.*
   :width: 50%
   :alt: Grafische Darstellung der ordnerweisen Zuweisung

   Funktionen ordnerweise zuweisen

Die Zuweisung von Funktionen an Gruppen oder Benutzer kann also sowohl global,
das heißt für die gesamte Website, erfolgen, als auch lokal für einzelne
Bereiche. So ist es möglich, dass eine Gruppe bzw. ein Benutzer in
verschiedenen Bereichen einer Website unterschiedliche Funktionen ausübt. Die
Abbildung :ref:`fig_konfiguration-benutzer-gruppen-benutzeruebersicht` zeigt
wie man die Zugriffsrechte global bequem zuweisen kann.

Benutzerübersicht
=================

Über den Verweis :guilabel:`Benutzer und Gruppen` im
Konfigurationsmenü gelangt man zunächst zur Benutzerübersicht (siehe
Abbildung :ref:`fig_konfiguration-benutzer-gruppen-benutzeruebersicht`).

.. _fig_konfiguration-benutzer-gruppen-benutzeruebersicht:

.. figure::
   ../images/konfiguration-benutzer-gruppen-benutzeruebersicht.*
   :width: 100%
   :alt: Übersicht über alle registrierten Benutzer

   Benutzerübersicht

Die Übersicht besteht aus einer Liste, in der alle Benutzer der
Website in alphabetischer Reihenfolge aufgeführt werden. Die
Sortierung orientiert sich dabei am vollständigen Namen, nicht am
Benutzernamen. Da Plone Vor- und Nachnamen nicht gesondert speichert,
muss man den Nachnamen vor dem Vornamen eingeben, falls man eine
Sortierung nach Nachname wünscht. Ansonsten werden die Benutzer nach
dem Vornamen sortiert.   

Benutzersuche 
   Mit Hilfe der Suche kann man die Liste eingrenzen oder
   wenn keine Benutzerliste angezeigt wird, gezielt nach Benutzern
   suchen (vgl. dazu Abschnitt
   :ref:`sec_konfiguration-benutzer-gruppen-einstellungen`)

Funktionen
   Die Liste zeigt die Funktionen der Benutzer an, die diese global
   auf der gesamten Website ausüben. Änderungen, die hier vorgenommen
   werden, wirken sich auf der gesamten Website aus. Markieren Sie
   dazu die Funktion, die Sie dem jeweiligen Benutzer zuweisen
   möchten, und betätigen Sie die Schaltfläche :guilabel:`Änderungen
   anwenden`. Wenn Sie
   Benutzern in einzelnen Bereichen der Website Funktionen zuordnen
   möchten, nutzen Sie die in Kapitel :ref:`sec_ansicht-freigabe`
   beschriebene Artikelansicht :guilabel:`Freigabe`.

Passwort zurücksetzen
   Wenn Sie in der Spalte :guilabel:`Passwort zurücksetzen` ein
   Häkchen setzen und :guilabel:`Änderungen anwenden` klicken, erhält
   der entsprechende Benutzer eine E-Mail mit einem Link zu einer
   Seite, auf der er sein Passwort neu eingeben kann.

Benutzer löschen
   Wenn Sie in dieser Spalte eine Markierung setzen und
   :guilabel:`Änderungen anwenden` klicken, wird der Benutzer
   gelöscht.

   .. warning:: Das Löschen eines Benutzers erfolgt ohne Nachfrage und
      		kann mit der Undo-Funktion im ZMI nicht immer
      		rückgängig gemacht werden.  

Einzelne Benutzer verwalten
===========================

Klickt man in der Benutzerübersicht auf einen Benutzernamen, gelangt man
zu drei Formularen, mit denen man den ausgewählten Benutzer verwalten kann. 

Persönliche Informationen
   Dieses Formular entspricht dem Formular, das der jeweilige Benutzer
   selbst einsehen und bearbeiten kann (vgl. dazu Kapitel
   :ref:`sec_profil`) 

Persönliche Einstellungen
   Dieses Formular entspricht dem Formular ›Meine Einstellungen‹, das
   der jeweilige Benutzer einsehen und bearbeiten kann (vgl. dazu
   Kapitel :ref:`sec_meine-einstellungen`)

Gruppenmitgliedschaften
   Mit Hilfe dieses Formulars (Abbildung
   :ref:`fig_konfiguration-benutzer-gruppen-gruppenmitgliedschaften`) können
   Sie einzelne Benutzer Gruppen zuordnen. 

   .. _fig_konfiguration-benutzer-gruppen-gruppenmitgliedschaften:

   .. figure::
      ../images/konfiguration-benutzer-gruppen-gruppenmitgliedschaften.*
      :width: 100%
      :alt: Verwaltung der Gruppenmitgliedschaften eines Benutzers

      Gruppenmitgliedschaften eines Benutzers

   Das Formular ist zweigeteilt:

   Aktuelle Gruppenmitgliedschaften
      Im oberen Teil des Formulars sind die Gruppen aufgelistet, in
      denen der Benutzer Mitglied ist. Wenn Sie den Benutzer aus einer
      Gruppe entfernen wollen, setzen Sie in der Spalte ›Entfernen‹
      ein Häkchen und klicken Sie auf die Schaltfläche
      :guilabel:`Mitgliedschaft in der ausgewählten Gruppe beenden`. 
  
   Gruppenzuweisung
      Im unteren Teil des Formulars können Sie den Benutzer einer
      neuen Gruppe zuweisen. Markieren Sie dazu die gewünschte Gruppe
      und klicken Sie auf die Schaltfläche :guilabel:`Füge den
      Benutzer der ausgewählten Gruppe hinzu`. 

      Nach der Zuweisung erscheint die neue Gruppe im oberen Teil des
      Formulars (Abbildung
      :ref:`fig_konfiguration-benutzer-gruppen-benuzer-zur-gruppe-hinzugefuegt`). In
      unserem Beispiel wurde der Benutzer ›Anton Autor‹ Mitglied der
      Gruppe ›Redakteure Kochkurse‹.

      .. _fig_konfiguration-benutzer-gruppen-benuzer-zur-gruppe-hinzugefuegt:
      
      .. figure::
      	 ../images/konfiguration-benutzer-gruppen-benuzer-zur-gruppe-hinzugefuegt.*
	 :width: 100%
	 :alt: Neue Gruppenmitgliedschaft
	 
	 Neue Gruppenmitgliedschaft

.. _sec_konfiguration-benutzer-gruppen-gruppenuebersicht:

Gruppenübersicht
================

Über den Reiter :guilabel:`Gruppen` gelangen Sie zur Gruppenübersicht
(Abbildung
:ref:`fig_konfiguration-benutzer-gruppen-gruppenuebersicht`). Sie ist
wie die Benutzerübersicht aufgebaut.

.. _fig_konfiguration-benutzer-gruppen-gruppenuebersicht:

.. figure::
   ../images/konfiguration-benutzer-gruppen-gruppenuebersicht.*
   :width: 100%
   :alt: Übersicht über die Gruppen der Website

   Gruppenübersicht

Standardgruppen
---------------

Folgende Gruppen werden bei der Installation von Plone automatisch
angelegt:

Administrators (Administrators)
   Benutzer, die dieser Gruppe angehören, können die Website
   verwalten. Das heißt, sie können überall auf der Website Ordner und
   Kollektionen hinzufügen, sie haben Zugriff auf die
   Einstellungsmöglichkeiten in der Konfiguration, sie können Benutzer
   und Gruppen hinzufügen und diesen auf der gesamten Website
   Funktionen zuordnen. Sie haben jedoch keinen Zugriff auf die
   Funktionen im Konfigurationsbereich :guilabel:`Wartung`. 

Authenticated Users (Virtual Group) (AuthenticatedUsers)
   Jeder Benutzer ist automatisch Mitglied in der Gruppe der
   authentifizierten Benutzer. Mit Hilfe dieser Gruppe kann man
   allen registrierten Benutzern Funktionen zuweisen. Wenn
   registrierte Benutzer beispielsweise einen privaten Ordner einsehen
   sollen, kann man dieser Gruppe in dem privaten Ordner über die
   Artikelansicht :guilabel:`Freigabe` die Funktion ›Kann
   ansehen‹ zuweisen. 

Reviewers (Reviewers)
   Mitglieder dieser Gruppe können Artikel auf der Website veröffentlichen.

Site Administrators (Site Administrators)
   Diese Gruppe hat umfassende Verwaltungsrechte und kann auch auf den
   Konfigurationsbereich :guilabel:`Wartung` zugreifen.  

Einzelne Gruppe verwalten
=========================

Klickt man in der Gruppenübersicht auf einen Gruppennamen, gelangt man
zu vier Formularen, mit denen man die ausgewählte Gruppe verwalten kann.

Gruppenmitglieder
-----------------

Zunächst ist die Übersicht über die Gruppenmitglieder geöffnet (siehe
Abbildung
:ref:`fig_konfiguration-benutzer-gruppen-gruppenmitglieder`). Mit
Hilfe dieses Formulars können Sie Benutzer und Gruppen der jeweiligen
Gruppe hinzufügen oder bestehende Gruppenmitglieder aus der Gruppe entfernen.

.. _fig_konfiguration-benutzer-gruppen-gruppenmitglieder:

.. figure::
   ../images/konfiguration-benutzer-gruppen-gruppenmitglieder.*
   :width: 100%
   :alt: Liste aller Mitglieder einer Gruppe

   Liste der Gruppenmitglieder

In der Überschrift ist die ausgewählte Gruppe namentlich
aufgeführt. Das Formular ist in zwei Teile geteilt:

Aktuelle Gruppenmitglieder
   Unter dieser Überschrift sind die Mitglieder der Gruppe mit ihren
   E-Mail-Adressen aufgelistet. Wenn Sie einen Benutzer aus der Gruppe
   entfernen möchten, markieren Sie den Benutzer und betätigen Sie die
   Schaltfläche :guilabel:`Lösche ausgewählte Benutzer/Gruppen`.

Suche nach neuen Gruppenmitgliedern
   Wenn Sie einen neuen Benutzer zur Gruppe hinzufügen möchten, suchen
   Sie ihn zunächst über die Benutzersuche (siehe Abbildung
   :ref:`fig_konfiguration-benutzer-gruppen-benutzer-gesucht`) 

   .. _fig_konfiguration-benutzer-gruppen-benutzer-gesucht:

   .. figure:: 
      ../images/konfiguration-benutzer-gruppen-benutzer-gesucht.*
      :width: 80%
      :alt: Benutzer wurde gefunden

      Gefundener Benutzer

   Sie können anschließend einen oder mehrere Benutzer oder Gruppen auswählen und
   der Gruppe hinzufügen, indem Sie die Benutzer oder Gruppen
   markieren und auf :guilabel:`Füge die ausgewählten Benutzer oder
   Gruppen dieser Gruppe hinzu` klicken. Wenn alle Benutzer für die
   Auswahl aufgelistet werden sollen, betätigen Sie :guilabel:`Zeige
   alle`. 

Gruppeneinstellungen
--------------------

In den Gruppeneinstellungen (Abbildung
:ref:`fig_konfiguration-benutzer-gruppen-gruppeneinstellungen`) können Sie
den Titel und die Beschreibung der Gruppe verändern.

.. _fig_konfiguration-benutzer-gruppen-gruppeneinstellungen:

.. figure::
   ../images/konfiguration-benutzer-gruppen-gruppeneinstellungen.*
   :width: 100%
   :alt: Gruppeneinstellungen

   Gruppeneinstellungen


Gruppenportlets
---------------

In der linken und rechten Spalte können Gruppenportlets konfiguriert
werden. Sie werden nur Benutzern angezeigt, die Mitglied der
entsprechenden Gruppe sind. Mit Hilfe des Formulars ›Gruppenportlets‹
können Sie diese Portlets verwalten (siehe Abbildung
:ref:`fig_konfiguration-benutzer-gruppen-gruppenportlets`). 

.. _fig_konfiguration-benutzer-gruppen-gruppenportlets:

.. figure:: 
   ../images/konfiguration-benutzer-gruppen-gruppenportlets.*
   :width: 100%
   :alt: Verwaltung gruppenspezifischer Portlets

   Gruppenportlets

Über das Auswahlmenü :guilabel:`Portlet hinzufügen` können Sie ein
neues Portlet hinzufügen. Neu hinzugefügte Portlets werden in der
entsprechenden Spalte aufgeführt (siehe Abbildung
:ref:`fig_konfiguration-benutzer-gruppen-gruppenportlet-hinzugefuegt`).

.. _fig_konfiguration-benutzer-gruppen-gruppenportlet-hinzugefuegt:

.. figure::
   ../images/konfiguration-benutzer-gruppen-gruppenportlet-hinzugefuegt.*
   :width: 100%
   :alt: Neu hinzugefügtes Gruppenportlet

   Neu hinzugefügtes Gruppenportlet

Weitere Details zur Verwaltung von Portlets finden Sie in Kapitel
:ref:`sec_portlets-hinzufuegen`.
 
Gruppenseite
------------

Auf der persönlichen Seite eines Benutzers (vgl. Kapitel
:ref:`sec_personliche-seite-1`) können gruppenspezifische Portlets
angezeigt werden. Ein Benutzer sieht dann auf seiner persönlichen
Seite Informationen, die ihn betreffen, weil er Mitglied einer
bestimmten Gruppe ist. 

.. _fig_konfiguration-benutzer-gruppen-gruppenseite:

.. figure::
   ../images/konfiguration-benutzer-gruppen-gruppenseite.*
   :width: 100%
   :alt: Konfigurierung der Gruppenseite

   Gruppenseite

.. _sec_konfiguration-benutzer-gruppen-benutzer-anlegen:

Mit Hilfe des Formulars ›Gruppenseite‹ können Sie die Portlets
definieren, die auf der persönlichen Seite von Mitgliedern der Gruppe 
angezeigt werden sollen. Die Gruppenportlets werden zusätzlich zu den
Portlets auf der persönlichen Seite angezeigt, die der Benutzer selbst
definiert. 

Weitere Details zur Verwaltung von Portlets finden Sie in Kapitel
:ref:`sec_portlets-hinzufuegen`.

Neuen Benutzer anlegen
======================

Wenn Sie einen neuen Benutzer anlegen möchten, betätigen Sie in der
Benutzerübersicht die Schaltfläche :guilabel:`Neuen Benutzer
hinzufügen`. Es öffnet sich daraufhin das Registrierungsformular
(siehe Abbildung
:ref:`fig_konfiguration-benutzer-gruppen-benutzer-anlegen`). 

.. _fig_konfiguration-benutzer-gruppen-benutzer-anlegen:

.. figure::
   ../images/konfiguration-benutzer-gruppen-benutzer-anlegen.*
   :width: 100%
   :alt: Das Registrierungsformular

   Das Formular zur Registrierung neuer Benutzer

Das Registrierungsformular kann je nach Konfiguration unterschiedliche
Eingabefelder besitzen (vgl. dazu Abschnitt
:ref:`sec_konfiguration-benutzer-gruppen-einstellungen`). Nach der
Installation enthält es folgende Formularfelder:

* Vor- und Nachname
* Benutzername
* E-Mail
* Passwort
* Passwort bestätigen
* Den folgenden Gruppen hinzufügen

  - Hiermit können gleich bei der Registrierung die Gruppen ausgewählt
    werden, in denen der Benutzer Mitglied sein soll.

Mögliche weitere Felder sind:

* Homepage
* Biografie
* Ort 
* Porträt
* Porträt löschen

Die Felder entsprechen den möglichen Angaben, die ein Benutzer über
sich in seinen ›Persönlichen Informationen‹ machen kann (vgl. dazu Kapitel
:ref:`sec_profil`).

.. _sec_konfiguration-benutzer-gruppen-einstellungen:

Benutzer- und Gruppeneinstellungen
==================================

Über den Reiter :guilabel:`Einstellungen` gelangen Sie zu den
Benutzer- und Gruppeneinstellungen. Dahinter verbergen sich zwei
Optionen, die Plone für große Websites optimieren (Abbildung
:ref:`fig_konfiguration-benutzer-gruppen-einstellungen`).

.. _fig_konfiguration-benutzer-gruppen-einstellungen:

.. figure::
   ../images/konfiguration-benutzer-gruppen-einstellungen.*
   :width: 100%
   :alt: Besondere Einstellungen für große Websites

   Einstellungen für große Websites

Wenn auf einer Website sehr viele Benutzer registriert sind, kann der Aufruf
der Benutzerübersicht viel Zeit in Anspruch nehmen, da vor der Anzeige die
Informationen aller Benutzer ausgewertet werden. Sie können in einem solchen
Fall die Option :guilabel:`Viele Benutzer?` aktivieren. Auf der
Benutzerübersicht wird dann statt der Liste ein Suchfeld angezeigt, über das
sie nach Benutzern suchen können. Geben Sie dazu in das Suchfeld den gesuchten
Benutzernamen oder den Vor- oder Nachnamen des gesuchten Benutzers in die
Suche ein und klicken Sie auf :guilabel:`Suche`.

Auf Websites mit sehr vielen Gruppen verfahren Sie
entsprechend und aktivieren die Option :guilabel:`Viele Gruppen?`.

.. _sec_konfiguration-benutzer-gruppen-registrierungseinstellungen:

Registrierungseinstellungen
===========================

Über den Reiter :guilabel:`Registrierungseinstellungen` gelangen Sie
zu einem Formular, wo Sie bestimmen können, welche Felder im
Registrierungsformular auftauchen (siehe Abbildung
:ref:`fig_konfiguration-benutzer-gruppen-felder-registrierung`).

.. _fig_konfiguration-benutzer-gruppen-felder-registrierung:

.. figure::
   ../images/konfiguration-benutzer-gruppen-felder-registrierung.*
   :width: 100%
   :alt: Konfiguration des Registrierungsformulars

   Konfiguration des Registrierungsformulars

Die Felder in der rechten Spalte werden auf dem Registrierungsformular
angezeigt, die Felder in der linken nicht. Benutzen Sie die
Pfeiltasten, um Felder in die linke oder rechte Spalte zu
verschieben. Mit den senkrechten Pfeilen können Sie die Sortierung der
Felder auf dem Formular beeinflussen.

E-Mail-Adresse statt Benutzername
---------------------------------

Wenn sich Ihre Benutzer mit einer E-Mail-Adresse statt mit einem
Benutzernamen anmelden sollen, müssen Sie die entsprechende Option in
den ›Sicherheitseinstellungen‹ aktivieren. Lesen Sie dazu Kapitel
:ref:`sec_konfiguration-sicherheit`.


