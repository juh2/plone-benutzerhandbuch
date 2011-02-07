Installation unter Windows
==========================

Laden Sie von der Website plone.org den Windows-Installer in der
jeweils aktuellen Version herunter. Sie können dazu auch direkt den
Link zur Download-Datei in die Adresszeile Ihres Browsers
eingeben. Für die Version 4.0.2 lautet der Link:
``http://launchpad.net/plone/4.0/4.0.2/+download/Plone-4.0.2.exe``.

Wenn Sie nach dem Laden den Installer starten, sehen Sie die in
Abbildung :ref:`fig_win-installer-1` abgebildete Begrüßungsnachricht.

.. _fig_win-installer-1:

.. figure::
   ../images/win-installer-1.*
   :width: 80%
   
   Startbildschirm des Windows-Installers

Klicken auf :menuselection:`Next`, um das Installationsprogramm zu
starten. 

Im nächsten Schritt wählen Sie den Ordner aus, in dem Plone installiert
werden soll (siehe Abbildung :ref:`fig_win-installer-2`). In der Regel
können Sie den Vorschlag des Installationsprogramms übernehmen. 

.. _fig_win-installer-2:

.. figure::
   ../images/win-installer-2.*
   :width: 80%

   Auswahl des Installationsordners


Wenn Sie den Vorschlag des Installationsprogramms übernehmen,
installieren Sie Plone systemweit. Sie können Plone auch in Ihrem
Heimverzeichnis installieren, falls Sie das System lediglich
ausprobieren möchten. Klicken Sie auf :menuselection:`Next`, um in der
Installation fortzufahren.

Im nächsten Schritt legen Sie das Benutzerkonto für den Administrator
fest (siehe Abbildung :ref:`fig_win-installer-3`). Sie können den
vorgeschlagenen Benutzername ``admin`` übernehmen oder einen anderen
Namen festlegen. Um das Passwort zu setzen, müssen Sie es zweimal
eingeben. Sie benötigen den Benutzernamen und das Passwort, um
sich als Systemadministrator in Plone anzumelden.

.. _fig_win-installer-3:

.. figure::
   ../images/win-installer-3.*
   :width: 80%

   Anlage des Administratorkontos

Im folgenden Schritt listet Ihnen das Installationsprogramm zur
Kontrolle in einer Übersicht den Installationspfad auf (siehe
Abbildung :ref:`fig_win-installer-4`. Klicken Sie nun auf
:menuselection:`Installieren`, um Plone zu installieren.

.. _fig_win-installer-4:

.. figure::
   ../images/win-installer-4.*
   :width: 80%

   Übersicht der Installationsoptionen


Während der Installation informiert Sie ein Fortschrittsbalken (siehe Abbildung :ref:`fig_win-installer-5` über den Fortgang der Installation. 

.. _fig_win-installer-5:

.. figure::
   ../images/win-installer-5.*
   :width: 80%

   Fortschrittsbalken

Falls Plone an der Stelle, wo Sie es installieren wollen, bereits installiert
ist, bricht die Installation mit einer entsprechenden Meldung ab (siehe
jbbildung :ref:`fig_win-installer-6`) 


.. _fig_win-installer-6:

.. figure::
   ../images/win-installer-6.*
   :width: 80%

   Meldung über den Abbruch der Installation

Verschieben Sie die alte Installation an einen anderen Ort, wenn Sie die Daten
noch benötigen, oder löschen Sie die alte Installation und starten Sie erneut
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
