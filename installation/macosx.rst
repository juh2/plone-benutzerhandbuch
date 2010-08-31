Installation unter Mac OS X
===========================

Wenn Sie von plone.org die Disk-Image-Datei mit dem Installationspaket für
Plone 4 heruntergeladen, aktiviert und gemountet haben, sehen Sie drei Objekte:
das Installationsprogramm, eine README-Datei im HTML-Format und einen Order
mit den Lizenzbestimmungen für alle Komponenten des Installationspakets. 

.. figure::
   ../images/mac-installer-1.*
   :width: 80%

   Der Inhalt des gemounteten Diskimages: Unified Installer, README und Lizenzen 

Starten Sie das Installationsprogramm mit einem Doppelklick auf das
Anwendungs-Icon und folgen Sie den Anweisungen. Zunächst öffnet sich die
Begrüßungsnachricht (siehe die Abbildung :ref:`fig_mac-installer-2`)

.. _fig_mac-installer-2:

.. figure::
   ../images/mac-installer-2.*
   :width: 80%

   Begrüßungsnachricht 

Wenn Sie Plone installieren möchten, klicken Sie auf
:menuselection:`Fortfahren`. Sie gelangen dadurch zur Laufwerksauswahl (siehe
Abbildung :ref:`fig_mac-installer-3`)

.. _fig_mac-installer-3:

.. figure::
   ../images/mac-installer-3.*
   :width: 80%

   Laufwerksauswahl


Sie können Plone systemweit oder in Ihrem Heimverzeichnis installieren. In
beiden Fällen landet Plone im Programm-Ordner.  Falls dieser in Ihrem
Heimverzeichnis noch nicht existiert, wird er bei der Installation erzeugt. Wählen Sie ein Laufwerk oder Ihren Heimordner als Installationsort aus und klicken Sie auf :menuselection:`Fortfahren`. Sie haben dann die Möglichkeit, den Installationstyp auszuwählen (siehe Abbildung :ref:`fig_mac-installer-4`)  


.. _fig_mac-installer-4:

.. figure::
   ../images/mac-installer-4.*
   :width: 80%

   Auswahl des Installationstyps 

Sie haben bei der Auswahl des Installationstyps folgende Möglichkeiten:

Stand-alone Installation
   Dies ist eine einfache Installation. Sie eignet sich zum Ausprobieren von
   Plone und für Entwicklungszwecke.

ZEO Cluster
   Die Installation von Plone in einem ZEO-Cluster ist für Produktivsysteme
   gedacht. Sie bietet die Möglichkeit zum Load-Balancing.


Klicken Sie auf :menuselection:`Fortfahren`, wenn Sie ihre Wahl getroffen
haben. Sie werden anschließend aufgefordert, mit der Installation zu beginnen
(siehe Abbildung :ref:`fig_mac-installer-5`). 

.. _fig_mac-installer-5:

.. figure::
   ../images/mac-installer-5.*
   :width: 80%

   Bestätigung der Installation 

Klicken Sie nun auf :menuselection:`Installieren`, um Plone zu installieren. 

Während der Installation müssen Sie für den Benutzer ›admin‹ ein Passwort
setzen (siehe Abbildung :ref:`fig_mac-installer-6`. Sie müssen das Passwort
zweimal eingeben.

.. _fig_mac-installer-6:

.. figure::
   ../images/mac-installer-6.*
   :width: 80%

   Aufforderung zur Festlegung eines Passworts

Sie benötigen das Passwort später, um sich als Systemadministrator in Plone
anzumelden. 

Ein Fortschrittsbalken (siehe Abbildung :ref:`fig_mac-installer-8` informiert
Sie über den Fortgang der Installation. 

.. _fig_mac-installer-8:

.. figure::
   ../images/mac-installer-8.*
   :width: 50%

   Fortschrittsbalken

Falls Plone an der Stelle, wo Sie es installieren wollen, bereits installiert
ist, bricht die Installation mit einer entsprechenden Meldung ab (siehe
jbbildung :ref:`fig_mac-installer-7`) 


.. _fig_mac-installer-7:

.. figure::
   ../images/mac-installer-7.*
   :width: 50%

   Meldung über den Abbruch der Installation

Verschieben Sie die alte Installation an einen anderen Ort, wenn Sie die Daten
noch benötigeni, oder löschen Sie die alte Installation und starten Sie erneut
das Installationsprogramm. 

Wenn Sie die alten Daten in der neuen Plone-Version benutzen möchten,
informieren Sie sich über die dafür notwendigen Migrationsschritte_. 


.. _Migrationsschritte: http://plone.org/documentation/manual/upgrade-guide

Nach erfolgreicher Installation wird automatisch die Datei
:file:`/Applications/Plone/zinstance/README.html` in Ihrem Browser geöffnet. 
Dort finden Sie Hinweise, wie Sie Plone starten und stoppen können. 

Sie können in :program:`Terminal` mit folgendem Befehl starten und stoppen.::

    /Applications/Plone/zinstance/bin/plonectl start
    /Applications/Plone/zinstance/bin/plonectl stop



Außerdem wird der
Finder im Ordner :file:`/Applications/Plone/zinstance` geöffnet. In diesem
Ordner finden Sie das Programm :program:`PloneController`, das Ihnen eine
grafische Benutzeroberfläche für das Starten und Stoppen von Plone zur
Verfügung stellt (siehe Abbildung :ref:`fig_plonecontroller`).  


.. _fig_plonecontroller:

.. figure::
   ../images/plonecontroller.*
   :width: 50%

   PloneController


Wenn Sie Plone gestartet haben, können Sie in :program:`PloneController` die
Anzeige Ihrer neu installierten Plone-Website aufrufen. Alternativ können Sie
in Ihrem Browser die Adresse http://localhost:8080/Plone eingeben.
