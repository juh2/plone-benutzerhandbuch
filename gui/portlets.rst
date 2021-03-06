.. _sec_portlets:

==========
 Portlets
==========

Zum Inhalt einer Plone-Seite trägt nicht nur der aktuelle Artikel
bei. Jede Seite kann auch eine Reihe von Portlets enthalten, die links
und rechts neben der Artikelansicht angeordnet sind. Portlets fassen
Inhalte der Website zusammen, bieten Zugriff auf ihre Funktionen oder
stellen andere Informationen bereit.

Die Details der einzelnen Portlets werden in den Kapiteln erläutert,
in denen ihre Funktion besprochen wird (siehe Tabelle :ref:`Portlets
<tab_portlets>`).

.. _tab_portlets:

.. table:: Portlets in der linken und rechten Spalte

   +-------------------+----------------------------------+
   | Titel             | siehe                            |
   +===================+==================================+
   | Anmelden          | :ref:`sec_anmelden`              |
   +-------------------+----------------------------------+
   | Navigation        | :ref:`sec_navigation-portlet`    |
   +-------------------+----------------------------------+
   | Aktuelle          | :ref:`sec_nutz-von-metad-3`      |
   | Änderungen        |                                  |
   +-------------------+----------------------------------+
   | Suche             | :ref:`sec_suchportlet`           |
   +-------------------+----------------------------------+
   | Kollektionsportlet| :ref:`sec_kollektionsportlet`    |
   +-------------------+----------------------------------+
   | Revisionsliste    | :ref:`sec_revisionsliste`        |
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
Portlets nicht bei jeder Anzeige neu erzeugt. Sein Inhalt ist unveränderlich.
Er wird bei der Konfiguration des Portlets eingegeben (siehe Abbildung
:ref:`fig_statisches-portlet`).

.. _fig_statisches-portlet:

.. figure:: ../images/portlet-static.*
   :width: 40%

   Statisches Portlet

Außerdem können Kopf- und Fußzeile eines statischen Portlets auf weitere 
Informationen verweisen 

Nicht nur der Inhalt statischer Portlets ist frei wählbar, sondern
auch ihre Gestaltung: Jedes statische Portlet hat einen eigenen Text
in Kopf- und Fußzeile, wobei die Fußzeile nicht angezeigt wird, wenn
sie leer gelassen wurde. Ein statisches Portlet kann auch ganz ohne
Rahmen, Kopf- und Fußzeile dargestellt werden.

.. _sec_statisches-portlet-hinzufuegen:

Statisches Portlet hinzufügen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Einstellungsmöglichkeiten im Bearbeitungsformular für statische
Portlets (siehe Abbildung :ref:`fig_statisches-portlet-hinzufuegen`)

.. _fig_statisches-portlet-hinzufuegen:

.. figure:: ../images/statisches-portlet-hinzufuegen.png
   :width: 100%

   Hinzufügen des statischen Portlets

* Kopfzeile des Portlets
* Text 
* Rahmen des Portlets verbergen
* Fußzeile des Portlets
* Verweis auf weitere Informationen 

Ein statisches Portlet kann nur von einem Administrator hinzugefügt
werden.
