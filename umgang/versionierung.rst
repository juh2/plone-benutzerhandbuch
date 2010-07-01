.. _sec_versionierung:

===============
 Versionierung
===============

Es wird bei Ihrer Arbeit an der Website gelegentlich vorkommen, dass Sie
Änderungen zurücknehmen und zu einer früheren Version eines Artikels
zurückkehren möchten. Das ist in Plone mit Hilfe der Versionsverwaltung
möglich. Das CMS erstellt jedes Mal, wenn Sie einen Artikel verändern und
speichern, eine neue Version des Inhalts. Die alten Versionen des Artikels
werden dabei nicht überschrieben, sondern stehen weiterhin zur Verfügung.

Sie erreichen die älteren Versionen eines Artikels über den Link
:guilabel:`Historie` in der Verfasserzeile des Artikels. Wenn Sie ihn
anklicken, öffnet sich ein Fenster mit einer Übersicht über die
bereits gespeicherten Versionen des Artikels (siehe Abbildung :ref:`fig_historie`).

.. _fig_historie:

.. figure:: ../images/historie.*
   :width: 100%

   Die Historie eines Artikels

Dort finden Sie eine Übersicht vor, in der ganz oben die aktuelle
Arbeitskopie und darunter die vorherigen Versionen aufgelistet
sind. Ganz unten steht die erste Version. 

Jede Version wird mit einem grauen Rahmen versehen dargestellt. In der
breiten grauen Kopfleiste jeder Version finden Sie Informationen über
den Benutzer, der die Version abgespeichert hat, und Datum und Uhrzeit
der Speicherung. Rechts daneben befindet sich jeweils eine
Schaltfläche mit der Bezeichnung :guilabel:`Durch diese Version
ersetzen`. Wenn Sie die Schaltfläche betätigen, wird die aktuelle
Version durch diese Version ersetzt. Das bedeutet, dass die Besucher
Ihrer Website nun eine frühere Version zu Gesicht bekommen. Die alte
Arbeitskopie wird unter einer neuen Versionsnummer gespeichert.

In der Zeile unterhalb des grauen Balkens erscheint der Wortlaut der
Änderungsnotiz sowie ein Verweis zur Anzeige dieser Version. Folgen
Sie dem Link :guilabel:`Anzeigen`, wenn Sie sich die Version anschauen
möchten. Daneben finden Sie einen Verweis zu einem Vergleich zwischen
der jeweiligen Version und der gerade aktuellen Version. Folgen Sie
diesem Link, um einen Überblick über die vorgenommenen Veränderungen
zu erhalten (siehe Abbildung
:ref:`fig_versionsvergleich-metadaten`). Darüber hinaus befinden sich
jeweils zwischen den Versionen Verweise auf einen Vergleich der
jeweils benachbarten Versionen. Folgen Sie diesem Verweis, wenn Sie
sehen wollen, was jeweils von Version zu Version geändert wurde.


Versionsvergleich
=================

Beim Versionsvergleich werden nicht nur Änderungen am Inhalt des
Artikels aufgelistet, sondern auch Modifikationen an den Metadaten wie
den Kategorien oder dem Freigabe- oder Ablaufdatum und an den
sonstigen Einstellungen. Als einzige Ausnahme werden Verweise auf
andere Artikel von der Versionsverwaltung nicht erfasst.

.. Ist das ein Bug?

Bei den Metadaten bedeutet ein vorangestelltes Pluszeichen, dass der
folgende Eintrag oder Wert hinzugefügt wurde; ein Minuszeichen zeigt an,
welcher Eintrag oder Wert gelöscht wurde (siehe
Abbildung :ref:`fig_versionsvergleich-metadaten`).

.. _fig_versionsvergleich-metadaten:

.. figure:: ../images/versionsvergleich-metadaten.*
   :width: 100%

   Versionsvergleich geänderte Termindaten

.. _fig_versionsvergleich-zusammenfassung:

.. figure:: ../images/versionsvergleich-zusammenfassung.*
   :width: 100%

   Versionsvergleich geänderte Zusammenfassung

Bei Textfeldern, etwa der Beschreibung bzw. der Zusammenfassung,
werden die beiden Versionen hintereinander angezeigt. Die alte Fassung
ist dabei durchgestrichen (siehe Abbildung
:ref:`fig_versionsvergleich-zusammenfassung`).

Bei Änderungen im Haupttext wird hinzugefügter Text hellgrün
hervorgehoben, ersetzter und gelöschter Text hellrot (siehe Abbildung
:ref:`fig_versionsvergleich-haupttext`).

.. _fig_versionsvergleich-haupttext:

.. figure:: ../images/versionsvergleich-haupttext.*
   :width: 100%

   Versionsvergleich mit geändertem Haupttext

Für bestimmte Änderungen gibt es zwei Ansichten:

* im fortlaufenden Text
* als Code

Sie haben dann die Wahl, welche Ansicht Ihnen mehr zusagt. Wenn Sie
*im fortlaufenden Text* die Meldung sehen »Für dieses Feld gibt es
keine Vergleichsansicht« wechseln Sie einfach zur Darstellung *als
Code*.



