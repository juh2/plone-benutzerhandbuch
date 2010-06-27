.. _sec_ordner:

========
 Ordner
========

Mit Ordnern geben Sie Ihrer Website eine inhaltliche Struktur. Sie können
verwandte und zusammengehörige Artikel in Ordnern zusammenfassen und mit Hilfe
von ineinander verschachtelten Ordnern komplexe Navigationsstrukturen aufbauen.

.. TODO: Hier später Verweis auf Admin-Tutorial einfügen.

Die Anzeigeansicht eines Ordners listet entweder den Inhalt des Ordners, also
die Artikel, die sich in ihm befinden, auf, oder sie verwendet einen
ausgewählten Artikel aus dem Ordner wie eine Art Titelblatt und zeigt diesen
Artikel an. Der Inhalt von Ordnern kann auf unterschiedliche Art und Weise
dargestellt werden.  Ordner haben dafür mehrere Vorlagen, aus denen Sie im Menü
:guilabel:`Darstellung` wählen können:

* Kurzfassung
* Gesamter Inhalt
* Tabelle
* Album
* Liste

.. _fig_ordner:

.. figure:: ../images/folder-order.png
   :width: 100%

   Der Inhalt eines Ordners als Kurzfassung

Kurzfassung

Tabelle

Liste

Album

Liste
Die Darstellung als Liste (siehe Abbildung :ref:`fig_ordner`) enthält
zu jedem Eintrag den Titel, die Beschreibung, einen Verweis auf das
Profil des Erstellers und das Datum der letzten Änderung. Der Titel
ist ein Verweis zum jeweiligen Artikel. Eine Ausnahme bilden Einträge
für Termine: bei ihnen werden anstelle des Änderungsdatums Ort und
Zeitraum des Termins angezeigt.

Artikel im Revisionsstatus »privat« werden in der Regel ausgeblendet. Sie
sehen nur die privaten Artikel, die Ihnen gehören oder sich in Ihrem
persönlichen Ordner befinden.

Wollen Sie für die Ordneranzeige einen Artikel aus dem Ordner benutzen, wählen
Sie im Darstellungsmenü den Punkt »Artikel aus dem Ordner.... Sie
gelangen so zu einem Formular, in dem Sie einen Artikel aus dem Ordner
markieren können. In der Anzeigeansicht des Ordners erscheint nun keine
Übersicht über seinen Inhalt, sondern der ausgewählte Artikel.

Plone kann für Ordner RSS-Feeds erzeugen. Dieser Vorgang wird Syndizierung
genannt. Jeder Ordner besitzt eine weitere Ansicht, in der Sie das
Syndizierungsverhalten steuern können (siehe
Abschnitt :ref:`sec_syndizierung-ansicht`).

.. _sec_bearbeitungsansicht-ordner:

Bearbeitungsansicht
===================

In der Bearbeitungsansicht eines Ordners gibt es im Teilformular
»Einstellungen« die Option »Vor- und Zurückblättern einschalten«
(siehe Abbildung :ref:`fig_ordner-bearbeiten`).

.. _fig_ordner-bearbeiten:

.. figure:: ../images/ordner-bearbeiten.png
   :width: 100%

   Das Teilformular »Einstellungen« bei Ordnern

Wenn diese Option eingeschaltet ist und sich in einem Ordner mehrere Artikel
befinden, so erscheinen in deren Anzeige Verweise zum jeweils
vorherigen und nächsten Artikel (siehe Abbildung :ref:`fig_vor-zurueck-navi`).

.. _fig_vor-zurueck-navi:

.. figure:: ../images/vor-zurueck-navi.png
   :width: 100%

   Vor- und Zurückblättern zwischen Artikeln

Damit lässt sich beispielsweise ein langer Text in kleinere
Abschnitte gliedern, durch die der Leser bequem blättern kann.

Inhaltsansicht
==============

Wenn Sie den Inhalt eines Ordners verwalten dürfen, erhalten Sie Zugriff auf
seine Inhaltsansicht (siehe Abbildung :ref:`fig_ordnerinhalt`).

.. _fig_ordnerinhalt:

.. figure:: ../images/ordnerinhalt.png
   :width: 100%

   Inhaltsansicht eines Ordners

Sie erreichen diese Ansicht über den Reiter »Inhalte«.

Die Inhaltsansicht eines Ordners zeigt eine Tabelle aller im Ordner
befindlichen Artikel mit ihren wichtigsten Eigenschaften. In dieser Ansicht
können Sie die Artikel unter anderem kopieren, verschieben und löschen.
Haben Sie einen Artikel aus dem Ordner als Ordneranzeige ausgewählt, so ist er
durch Fettschrift hervorgehoben.

Artikel liegen in einem Ordner in der Reihenfolge, in der sie hinzugefügt
wurden, und werden so auch in den Ordneransichten und der Navigation
angezeigt. Sie können die Reihenfolge jedoch verändern, indem Sie einzelne
Artikel an dem Symbol »::« in der Spalte »Reihenfolge« ganz rechts mit der
Maus »anfassen« und auf- oder abwärts
verschieben. Falls Sie Javascript ausgeschaltet haben, finden Sie in der
Spalte stattdessen Pfeilsymbole vor (siehe Abbildung :ref:`fig_umordnen`).

.. _fig_umordnen:

.. figure:: ../images/umordnen.png
   :width: 100%

   Artikel in einem Ordner umordnen]{Artikel in einem Ordner umordnen:
   mit Javascript (links) und ohne (rechts)}
