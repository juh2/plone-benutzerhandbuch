.. _sec_portlets:

==========
 Portlets
==========

Zum Inhalt einer Plone"=Seite trägt nicht nur der aktuelle Artikel
bei. Jede Seite enthält auch eine Anzahl von Portlets, die links und
rechts neben der Artikelansicht angeordnet sind. Portlets fassen
Inhalte der Website zusammen, bieten Zugriff auf ihre Funktionen oder
stellen andere Informationen bereit.

Dieses Buch beschreibt die Details der einzelnen Portlets dort, wo ihre
Funktion besprochen wird (siehe Tabelle :ref:`tab_portlets`).

.. _tab_portlets:

+-------------------+----------------------------------+
| Titel             | siehe                            |
|                   |                                  |
+-------------------+----------------------------------+
| Anmelden          | :ref:`sec_anmelden`              |
+-------------------+----------------------------------+
| Navigation        | :ref:`sec_navigation-portlet`    |
|                   |                                  |
|                   |                                  |
+-------------------+----------------------------------+
| Aktuelle          | :ref:`sec_nutz-von-metad-3`      |
| Änderungen        |                                  |
|                   |                                  |
+-------------------+----------------------------------+
| Meine             | :ref:`sec_navigation-lesezeichen`|
| Lesezeichen       |                                  |
|                   |                                  |
+-------------------+----------------------------------+
| Suche             | :ref:`sec_suchportlet`           |
+-------------------+----------------------------------+
| Kollektionsportlet| :ref:`sec_kollektionsportlet`    |
|                   |                                  |
+-------------------+----------------------------------+
| Revisionsliste    | :ref:`sec_revisionsliste`        |
|                   |                                  |
+-------------------+----------------------------------+
| Nachrichten       | :ref:`sec_nachricht`             |
+-------------------+----------------------------------+
| Termine           | :ref:`sec_termin`                |
+-------------------+----------------------------------+
| Kalender          | :ref:`sec_termin`                |
+-------------------+----------------------------------+
| RSS-Feed          | :ref:`sec_rss`                   |
+-------------------+----------------------------------+
| Statisches        | :ref:`sec_statisches-portlet`    |
| Portlet           |                                  |
+-------------------+----------------------------------+
  
Portlets in der linken und rechten Spalte


Portlets werden ausgeblendet, wenn sie leer sind. Falls es
beispielsweise keine Nachrichten anzuzeigen gibt, hat das
Nachrichtenportlet keinen Inhalt und wird daher gar nicht
eingeblendet. Ferner erscheint per Voreinstellung auf der Startseite
kein Navigationsportlet, da sein Inhalt erst mit Unterordnern beginnt
(siehe Abschnitt :ref:`sec_navigation-portlet`).

Viele der Portlets enthalten eine Liste bestimmter Artikel der
Website, beispielsweise der neuesten Nachrichten. Solche Listen
umfassen aus Platzgründen nur wenige Einträge. Sie enden jedoch mit
einem Verweis, der Sie zu einer vollständigen Übersicht der zum
Portlet passenden Artikel führt. Das könnte etwa eine Liste aller
Nachrichten auf der Website sein.

.. _sec_statisches-portlet:

Statisches Portlet
==================

Im Gegensatz zu den meisten anderen Portlets wird der Inhalt eines statischen
Portlets nicht bei jeder Anzeige neu bestimmt. Stattdessen handelt es sich um
einen frei formatierbaren Text, der bei der Konfiguration des Portlets
bearbeitet und bei der Anzeige unverändert wiedergegeben wird (siehe
Abbildung :ref:`fig_statisches-portlet`).

.. _fig_statisches-portlet:

.. figure:: ../images/portlet-static.png

   Statisches Portlet

Außerdem kann jedes statische Portlet einen Verweis auf weiterführende
Informationen anzeigen.

Nicht nur der Inhalt statischer Portlets ist frei wählbar, sondern auch ihre
Gestaltung: Jedes statische Portlet hat einen eigenen Text in Kopf- und
Fußzeile, wobei die Fußzeile gar nicht angezeigt wird, wenn sie leer gelassen
wurde. Weiterhin müssen statische Portlets nicht unbedingt mit einem Rahmen
dargestellt werden.

Die Konfiguration eines statischen Portlets wird in
Abschnitt :ref:`sec_statisches-portlet-hinzufuegen` erläutert.
