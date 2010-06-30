.. _sec_tutorium-dokumente:

===================
 Umgang mit Seiten
===================


In diesem Tutorium lernen Sie, wie Sie eine Seite auf der Website anlegen,
bearbeiten und löschen.

Seite anlegen
=============

Wir gehen im Folgenden davon aus, dass Ihr Administrator in der Website einen
Ordner mit dem Namen »Veranstaltungen« eingerichtet hat. Diesen Ordner sollten
Sie nutzen, wenn Sie die nachfolgenden Tutorien durcharbeiten. Sie erreichen
ihn über einen Eintrag in der Hauptnavigation.

* Begeben Sie sich in den Ordner »Veranstaltungen«, indem Sie dem Verweis
  :guilabel:`Veranstaltungen` in der Hauptnavigation folgen.

Sie werden bemerken, dass die Anzeigeansicht des Ordners eine grüne Leiste
besitzt, auf dem sich Reiter und Ausklappmenüs befinden. Über die Reiter im
linken Bereich der Leiste gelangen Sie zum Beispiel zur Bearbeitungsansicht des
Ordners. Im rechten Bereich der Leiste befinden sich die Ausklappmenüs :guilabel:`Aktionen`, :guilabel:`Darstellung`, :guilabel:`Hinzufügen` und :guilabel:`Status: Veröffentlicht` (siehe Abbildung :ref:`fig_add-menu-seite`).

.. _fig_add-menu-seite:
   
.. figure::
   ../images/add-menu-seite.png
   :width: 100%
   :alt: Bildschirmfoto des Menüs zum Anlegen von Artikeln

   Menü zum Anlegen von Artikeln

* Klappen Sie das Menü »Hinzufügen« auf und wählen Sie »Seite« aus.


Falls Sie Javascript ausgeschaltet haben, sind alle Ausklappmenüs von Anfang an
geöffnet (siehe Abbildung :ref:`fig_add-menu-seite-ohne-js`). Sie sind jedoch alle
funktionsfähig.

.. _fig_add-menu-seite-ohne-js:
.. figure::
   ../images/add-menu-seite-ohne-js.*
   :width: 100%

   Aufgeklappte Menüs

Nachdem Sie eine neue Seite angelegt haben, sehen Sie ein Bearbeitungsformular
(siehe Abbildung :ref:`fig_homepage-edit-1`).

.. _fig_homepage-edit-1:
.. figure::
   ../images/homepage-edit-1.*
   :width: 100%
   :alt: Das Formular zum Anlegen und Bearbeiten einer Seite

   Bearbeitungsformular einer Seite


Seite bearbeiten
================

Das Bearbeitungsformular ist in fünf Teile untergliedert:

* Standard
* Kategorisierung
* Datum
* Urheber
* Einstellungen


Zunächst ist das Teilformular »Standard« geöffnet. Die übrigen Teilformulare
erreichen Sie über die Navigation direkt unterhalb der Überschrift »Seite
hinzufügen«.

Falls Sie in Ihrem Webbrowser Javascript ausgeschaltet haben, zeigt Ihnen die
Bearbeitungsansicht alle fünf Teilformulare untereinander an. Der vollständige
Funktionsumfang aller Teilformulare wird in Abschnitt :ref:`sec_bearbeiten`
erklärt.

In diesem Tutorium beschränken wir uns auf den Teil »Standard« des
Bearbeitungsformulars. Er enthält vier Felder (siehe
Abbildung :ref:`fig_homepage-edit-1`):

* Titel
* Zusammenfassung
* Haupttext
* Änderungsnotiz

Titel und Beschreibung
----------------------

Zunächst müssen Sie im ersten Feld den Titel der Seite angeben. Dies ist
zwingend erforderlich. Sie erkennen Formularfelder, die unbedingt ausgefüllt
werden müssen, an dem roten Quadrat rechts neben der Feldbezeichnung. Wenn Sie
versuchen, ein Formular mit einem unausgefüllten Pflichtfeld zu speichern,
erhalten Sie eine Fehlermeldung.

Beobachten Sie, wie Plone auf unausgefüllte Pflichtfelder reagiert, bevor Sie
Ihrer Seite einen neuen Titel geben:


* Wechseln Sie mit dem Cursor in das Feld »Zusammenfassung«, ohne einen
  Titel eingetragen zu haben.


Das Formularfeld »Titel« wird rot hinterlegt und Sie werden daran
erinnert, einen Titel einzugeben.


* Betätigen Sie die Schaltfläche »Speichern« am Ende des Formulars, ohne
  einen Titel einzugeben.


Plone hat die Seite nicht gespeichert, sondern zeigt das Bearbeitungsformular
erneut an. Das Titelfeld ist hervorgehoben und mit dem Hinweis versehen, dass
es ausgefüllt werden muss (siehe Abbildung :ref:`fig_homepage-edit-no-title`).

.. _fig_homepage-edit-no-title:

.. figure::
   ../images/homepage-edit-no-title.*
   :width: 100%

   Fehlermeldung wegen unausgefüllten Pflichtfelds


* Tragen Sie nun einen Titel für Ihre Seite in das Titelfeld ein, etwa
  »Das Kochseminar«.


Das zweite Feld erlaubt die Eingabe einer Zusammenfassung des Inhalts.  Diese
Zusammenfassung wird in automatisch erzeugten Übersichtslisten und als
Einleitung des Textes verwendet.  Sie soll dem Leser die Entscheidung
erleichtern, ob die Seite für ihn interessant ist oder nicht. Die Eingabe einer
Zusammenfassung empfiehlt sich daher in den meisten Fällen.

* Geben Sie in das Formularfeld »Zusammenfassung« einen kurzen
  beschreibenden Text ein.


Haupttext
---------

Das Feld »Haupttext« sieht etwas anders aus. Oberhalb des Textfelds finden
Sie eine Leiste mit Bedienungselementen des Texteditors TinMCE vor (siehe
Abbildung :ref:`fig_homepage-edit-2`).

.. _fig_homepage-edit-2:

.. figure::
   ../images/homepage-edit-2.*
   :width: 100%

   TinyMCE im Bearbeitungsformular einer Seite

Falls die Bearbeitungsleiste fehlt, haben Sie den Texteditor TinyMCE in Ihren
persönlichen Einstellungen möglicherweise nicht ausgewählt, oder Sie haben
Javascript deaktiviert. Siehe dazu das erste Tutorium :ref:`sec_tut-profil`.

TinyMCE lässt Sie den eingegebenen Text formatieren. Sie können unter anderem
Überschriften auszeichnen, Textstellen fett oder kursiv setzen und Absätze
links- oder rechtsbündig ausrichten. Eine ausführliche Beschreibung von TinyMCE
finden Sie in Abschnitt :ref:`sec_TinyMCE`.

* Geben Sie etwas Text in das Formularfeld »Haupttext« ein.
* Gehen Sie mit dem Cursor in eine Zeile, die zu einer Überschrift werden
  soll und wählen Sie aus dem Auswahlmenü den Stil »Heading« aus.
* Geben Sie etwas Text in einer neuen Zeile ein und markieren Sie mit Hilfe
  des Listensymbols diese Zeile als Liste.
* Beobachten Sie, wie neue Zeilen zu weiteren Listenpunkten werden, wenn Sie
  die Eingabetaste betätigen.
* Probieren Sie die anderen Formatierungen aus der Werkzeugleiste aus.

Beachten Sie das der Text, den Sie eingeben, sofort im Stil der Website
dargestellt wird. So erhalten Sie sofort einen Eindruck vom Ergebnis.

Änderungsnotiz
--------------

Kommentieren Sie in der Änderungsnotiz, was Sie auf der Seite geändert haben.
Da Plone auch die älteren Versionen eines Artikels speichert, kann man später
anhand dieser Notizen herausfinden, warum bestimmte Änderungen gemacht wurden.

Eingaben sichern
----------------

Sichern Sie Ihre Eingaben, wenn Sie mit ihnen zufrieden sind.

* Betätigen Sie die Schaltfläche :guilabel:`Speichern` am Ende des
  Formulars.

Akzeptiert Plone Ihre Änderungen, so zeigt es Ihnen die bearbeitete
Seite an (siehe Abbildung :ref:`fig_homepage-edited`).

.. _fig_homepage-edited:

.. figure::
   ../images/homepage-edited.*
   :width: 80%

   Die Seite nach der Bearbeitung

Sie werden dann durch eine Statusmeldung darüber informiert, dass die Seite
gespeichert wurde.

Ihre Eingaben werden nun in der Anzeige der Seite dargestellt. Die
Seitenüberschrift ist der von Ihnen eingegebene Titel. Gleich darauf folgt
visuell hervorgehoben Ihre Beschreibung und dann der Haupttext der Seite.

Wenn es beim Speichern ein Problem gab, verbleiben Sie in der
Bearbeitungsansicht.  Lesen Sie in diesem Fall die angezeigte Fehlermeldung
und korrigieren Sie Ihre Eingaben entsprechend.


Die Seite als Teil der Website
------------------------------

* Rufen Sie nun erneut den Ordner »Veranstaltungen« in der Hauptnavigation
  auf. 

In der Anzeige des Ordners erscheint ein neuer Eintrag für die Seite,
die Sie gerade angelegt haben (siehe Abbildung :ref:`fig_homefolder+page`).

.. _fig_homefolder+page:

.. figure::
   ../images/homefolder+page.*
   :width: 100%

   Die Seite in Ihrem Ordner und im Navigationsportlet

In der linken Seitenspalte ist außerdem das Navigationsportlet erschienen, in
dem sich die neu angelegte Seite als einziger Eintrag befindet. 

Ältere Versionen anzeigen
=========================

Plone sichert alte Versionen von Artikeln. Sie können auf diese älteren
Versionen zugreifen. 

Um diese Funktion ausprobieren zu können, müssen Sie zunächst die von Ihnen
angelegte Seite verändern. Rufen Sie dazu erneut die Bearbeitungsansicht auf
und ändern Sie den Titel beispielsweise in »Das Kochseminar – aktuelle
Informationen«. Vermerken Sie als Änderungsnotiz, dass Sie den Titel geändert
haben, und speichern Sie die Änderung.

Direkt unterhalb der Überschrift finden Sie in der Anzeige der Seite die so
genannte Verfasserzeile. Sie enthält den Namen des Verfassers, das Datum der
letzten Veränderung und einen Verweis auf die Historie des Artikels (siehe
Abbildung :ref:`fig_link-historie`).

.. _fig_link-historie:

.. figure::
   ../images/link-historie.*
   :width: 100%

   Die Verfasserzeile

* Rufen Sie die Historie über den Verweis in der Verfasserzeile auf (siehe
  Abbildung :ref:`fig_historie-tutorium`).

.. _fig_historie-tutorium:

.. figure::
   ../images/historie-tutorium.*
   :width: 100%

   Liste der Versionen eines Artikels

Sie enthält eine Liste aller bisherigen Versionen der Seite. Die oberste
Version ist die jeweils aktuelle. Sie können die aktuelle Version mit einer
älteren Version vergleichen oder eine ältere Version anzeigen. Sie können eine
ältere Version wieder zur aktuellen machen, indem Sie die Schaltfläche
:guilabel:`Durch diese Version ersetzen` betätigen. 

* Lassen Sie sich einen Vergleich zwischen den beiden Versionen anzeigen, indem
  Sie dem Verweis :guilabel:`Vergleichen` zwischen den beiden Versionen folgen. 

Sie sehen nun eine Ansicht, auf der die Versionen verglichen werden (siehe
Abbildung :ref:`fig_historie-tutorium-vergleich`). Die Ansicht enthält
Informationen über die Versionen und zeigt ganz unten die Unterschiede an. In
unserem Fall wurde nur der Titel verändert. Der alte Titel ist durchgestrichen,
daneben steht der neue Titel.  

.. _fig_historie-tutorium-vergleich:

.. figure::
   ../images/historie-tutorium-vergleich.*
   :width: 100%

   Vergleich zwischen zwei Versionen

* Gehen Sie anschließend zurück in die normale Anzeige der Seite, indem Sie in
  der grünen Leiste den Reiter :guilabel:`Anzeigen` anklicken.

* Rufen Sie erneut die Historie auf.

* Betätigen Sie nun die Schaltfläche :guilabel:`Durch diese Version ersetzen`.
  Sofort wird die Seite mit dem alten Titel angezeigt.

* Schauen Sie in der Historie nach, was passiert ist. Sie sehen nun ganz oben
  den Eintrag »Zurückgekehrt zu Version 0« Das heißt die Ursprungsversion
  (mit der Nummer 0) wurde zur aktuellen Version. Darunter werden die anderen
  beiden Versionen angezeigt. 

Machen Sie sich mit der Arbeitsweise der Historie vertraut, indem Sie an der
Seite weitere Änderungen vornehmen und die Historie aufrufen, um die Änderungen
anzeigen zu lassen. Denken Sie dabei daran, in den Änderungsnotizen zu
vermerken, was sie geändert haben oder warum sie etwas geändert haben.   

Seite löschen
=============

Nicht mehr benötigte Artikel können Sie von der Website entfernen. Löschen Sie
nun die Seite, die Sie gerade angelegt haben.

* Rufen Sie die Anzeigeansicht der Seite auf. 

* Öffnen Sie das Menü »Aktionen« und wählen Sie den Eintrag »Löschen«
  aus (siehe Abbildung :ref:`fig_aktionen-loeschen`).

.. _fig_aktionen-loeschen:

.. figure::
   ../images/aktionen-loeschen.png
   :width: 100%

   Aktionsmenü

Plone fragt vorsichtshalber nach, ob Sie die Seite wirklich löschen wollen,
bevor die Aktion ausgeführt wird, um ein versehentliches Löschen von Artikeln
zu vermeiden. Sie können die Löschaktion an diesem Punkt abbrechen oder
mit der Schaltfläche :guilabel:`Löschen` bestätigen. Nach dem Löschen wird der
Ordner aufgerufen, in dem sich die Seite befand. 

Andere Artikeltypen
===================

Sie haben in diesem Tutorium den Artikeltyp »Seite« kennengelernt. Probieren
Sie nun andere Artikeltypen aus. Legen Sie beispielsweise einen Termin oder
eine Nachricht an, bearbeiten und löschen Sie diese Artikel, und verfolgen Sie
die Änderungen in der Historie.
