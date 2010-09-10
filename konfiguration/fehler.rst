.. _sec_konfiguration-fehler:

========
 Fehler
========

Wenn es in Plone zu einer Fehlfunktion kommt, schreibt das Programm ein Fehlerprotokoll, mit dem es möglich ist, die Ursache des Fehlers zu finden. Die jeweils jüngsten Protokolle werden hier aufgelistet (siehe Abbildung :ref:`konfiguration-fehler`).

.. _fig_konfiguration-fehler:

.. figure::
   ../images/konfiguration-fehler.*
   :width: 100%
   :alt: Bereich, in dem Fehler aufgelistet werden

   Auflistung der Fehler


Ganz oben auf der Seite finden Sie einen Link zur Fehlerreferenz auf der Website plone.org.

Unmittelbar darunter befindet sich ein Suchformular und diverse Schaltflächen. Unterhalb der Schaltflächen befindet sich die Liste mit ein Einträgen.  

Nach einem Fehlerreport suchen
   Geben Sie in das Formularfeld eine Fehlernummer ein und betätigen Sie die
   Schaltfläche :guilabel:`Suche`. Sie werden daraufhin direkt zu dem
   entsprechenden Fehler geführt. Plone zeigt dem Benutzer bie einer
   Fehlfunktion die entsprechende Fehlernummer an. 

Aktualisieren
   Wenn Sie diese Schaltfläche betätigen wird die Übersicht über die
   Fehlerprotokolle neu geladen. 

Angezeigte Einträge löschen
   Mit dieser Schaltfläche können Sie die Liste der Fehlerprotokolle löschen.
   Wenn Sie bereits gelöschte Fehlerprotokolle einsehen möchten, betätigen Sie
   die Schaltfläche :guilabel:`Alle Einträge anzeigen`. 

Alle Einträge anzeigen
   Wenn Sie diese Schaltfläche betätigen, werden alle Fehlerprotokolle
   aufgelistet, auch die, die vorher gelöscht wurden. 

Anzahl der Fehler, die gespeichert werden.
   Voreingestellt sind 20 Fehlermeldungen. Treten mehr Fehler auf, werden die
   ältesten Fehler gelöscht.  

Fehler ins Ereignisprotokoll kopieren
   In der Voreinstellung werden Fehler auch ins Ereignisprotokoll übernommen.
   Es handelt sich dabei um die Datei :file:`$INSTANCE/var/log/instance.log`.   

Zu ignorierende Fehlertypen
   Bestimmte Fehlermeldungen beziehen sich nicht unbedingt auf eine
   Fehlfunktion. Solche Fehlertypen können ignoriert werden. In der
   Voreinstellung werden die Fehlertypen »Unauthorized«, »NotFound« und
   «Redirect« nicht beachtet. 
