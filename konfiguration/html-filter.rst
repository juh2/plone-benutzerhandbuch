.. _sec_konfiguration-html-filter:

=============
 HTML-Filter
=============

Aus Sicherheitsgründen entfernt Plone bei der Speicherung von Artikeln :term:`HTML-Tags <HTML-Tag>`, die ein Sicherheitsrisiko darstellen können.  Darüber hinaus werden Tags entfernt, die nicht :term:`XHTML`-konform sind. Ein Benutzer kann also bei der Eingabe von Text bestimmte HTML-Elemente nicht benutzen. 

Der Filter kann in der Website-Konfiguration im Bereich :guilabel:`HTML-Filter` angepasst werden. Bevor man von der Voreinstellung abweicht, sollte man sich über mögliche Folgen im Klaren sein.  

.. _fig_konfiguration-html-filter-html-tags:

.. figure::
   ../images/konfiguration-html-filter-html-tags.*
   :width: 80%
   :alt: Menü zur Bestimmung von HTML-Tags, die gefiltert werden sollen

   Filterung von HTML-Tags

Das Formular (siehe Abbildung :ref:`fig_konfiguration-html-filter-html-tags`
besteht aus drei Teilformularen:

* HTML-Tags
* Attribute
* Style

Eine Übersicht über HTML-Tags, Attribute und Stile finden Sie unter anderem auf der Website SELFHTML_.

.. _SELFHTML: http://de.selfhtml.org/

Teilformular »HTML-Tags«
========================

Das Teilformular »HTML-Tags« listet die HTML-Tags auf, die herausgefiltert
werden sollen. Dabei werden die so genannten »fiesen Tags« mitsamt ihrem Inhalt
gelöscht. Bei den unter der Überschrift »Entfernte Tags« aufgeführten Elementen
bleibt der Inhalt erhalten, es werden lediglich die Tags selbst entfernt.  

Wenn Sie ein Tag aus der ersten Liste zulassen wollen, müssen Sie es aus der
Liste der fiesen Tags entfernen **und** in die Liste »Benutzerdefinierte Tags«
eintragen. Um ein Tag zu entfernen, markieren Sie es in der Liste, indem Sie in
der nebenstehenden Checkbox das Häkchen setzen und das Tag damit auswählen.
Betätigen Sie anschließend die Schaltfläche :guilabel:`Remove selected items`.

Um ein Tag hinzuzufügen, betätigen Sie die Schaltfläche :guilabel:`Nasty tags
hinzufügen`. Es erscheint daraufhin ein zusätzliches Eingabefeld, in das Sie
den Namen des Tags eintragen können.  In den beiden anderen Listen gehen Sie
bei Bedarf entsprechend vor. 

Vergessen Sie abschließend nicht, Ihre Eingaben zu speichern.

Teilformular »Attribute«
========================

Attribute sind Elemente, die innerhalb eines HTML-Tags gesetzt werden und diesem bestimmte Eigenschaften zuweisen. So verändert man bespielsweise mit dem Attribut »bgcolor« die Farbe des Hintergrundes in einem HTML-Tag. 

In einem CMS, bei dem auf ein einheitliches Aussehen aller Webseiten Wert gelegt wird, ist es nicht wünschenswert, dem Benutzer zu viele Freiheiten bei der Gestaltung zu geben. Daher werden diverse Attribute grundsätzlich oder in Kombination mit bestimmten HTML-Tags wie zum Beispiel »table«, »th« und »td« entfernt. 

Sie können die Voreinstellung verändern, indem Sie Attribute hinzufügen oder entfernen.

Teilformular »Style«
====================

Stilattribute in :term:`CSS`-Definitionen werden grundsätzlich entfernt. Lediglich die unter »Erlaubte Stile« aufgeführten Attribute können verwendet werden. 

:term:`CSS`-Klassen können dagegen weitgehend verwendet werden, da ihr Aussehen zentral festgelegt wird. Unter der Überschrift »Gefilterte Klassen« können Sie eine Liste von CSS-Klassen anlegen, die trotzdem gefiltert werden sollen. 
