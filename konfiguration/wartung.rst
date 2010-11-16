.. _sec_konfiguration-wartung:

=========
 Wartung
=========

In diesem Bereich können vom admin-user Wartungsarbeiten vorgenommen werden.
Normale Benutzer, die die Funktion »Verwalten« besitzen, können auf diesen
Bereich nicht zugreifen. 

.. _fig_konfiguration-wartung:

.. figure::
   ../images/konfiguration-wartung.*
   :width: 100%
   :alt: Wartungsroutinen

   Wartungsroutinen

Zope Server herunterfahren oder neu starten
===========================================

Betätigen Sie die Schaltfläche :guilabel:`Herunterfahren`, wenn Sie den
Zope-Server stoppen wollen und :guilabel:`Neu starten`, wenn Sie den Server neu
starten möchten.  

Zope-Datenbank packen
=====================

Wenn ein Objekt in der Zope Object Database (ZODB) verändert wird, wird die
alte Version nicht gelöscht, sondern eine neue Version des Objekts an das Ende
der Datenbankdatei geschrieben. Dadurch wächst die ZODB kontinuierlich an. Der
Vorteil ist, dass alte Zustände der Datenbank durch die Undo-Funktion im ZMI
wieder herstellbar sind. 

Wenn Sie alte Objektversionen und gelöschte Objekte aus der Datenbankdatei
entfernen möchten, damit diese kleiner wird, müssen Sie die ZODB packen. Dabei
haben Sie die Möglichkeit zu bestimmen für wie viele Tage Sie die Undo-Historie
behalten wollen. Voreingestellt ist ein Wert von sieben Tagen. 

Betätigen Sie die Schaltfläche :guilabel:`Packe Datenbank jetzt`, wenn Sie die
ZODB packen möchten. 
