.. _sec_diskussionen:

============
 Kommentare
============

Plone verfügt über eine Kommentarfunktion, die es den Besuchern einer
Website erlaubt, sich mit den Autoren und anderen Besuchern über
einzelne Artikel auszutauschen.

Ist für einen Artikel die Kommentarfunktion eingeschaltet, so enthält seine
Anzeige am Seitenende die Schaltfläche »Kommentieren« sowie die bisherigen
Kommentare (siehe Abbildung :ref:`fig_kommentare`).

.. _fig_kommentare:

.. figure:: ../images/kommentare.*

   Kommentare

Antworten auf einen Kommentar werden direkt unterhalb des Kommentars
angezeigt und eingerückt. So kann sich eine verzweigte Diskussion
entwickeln.


Artikel kommentieren
====================

Falls der Verfasser des Artikels Kommentare erlaubt hat, können Sie
den Artikel kommentieren. Um einen Kommentar hinzufügen zu können,
müssen Sie möglicherweise an der Website angemeldet sein. Als nicht
angemeldeter Benutzer sehen Sie in diesem Fall einen Verweis zur
Anmeldung mit der Bezeichnung »Zum Kommentieren müssen Sie sich
anmelden«.

Falls nicht angemeldete Besucher der Website kommentieren dürfen,
besteht das Kommentarformular aus zwei Feldern. Im oberen Feld können
Sie Ihren Namen eintragen und im unteren Ihren Kommentar.

Die Kommentierungsmöglichkeit befindet sich unterhalb des
Artikels. Sie ist durch eine Linie mit der Bezeichnung »Kommentieren«
vom Artikel abgetrennt. In der Beschriftung oberhalb des eigentlichen
Kommentarfeldes werden Ihnen Hinweise auf Formatierungsmöglichkeiten
gegeben. Zur Verfügung stehen jeweils folgende Optionen:

Einfacher Text
    Bei dieser Option lässt sich der Text nicht formatieren.

Markdown
    Markdown ist eine vereinfachte Auszeichnungssprache, die von Plone
    intern in HTML-Syntax umgewandelt wird. Eine Einführung in
    Markdown finden Sie auf dieser Website_.

Erkennung von Web- und E-Mailadressen 
    Falls der Administrator die Option »Intelligent text« gewählt hat,
    werden URLs und E-Mailadressen in Links umgewandelt. Ansonsten
    stehen keine Formatierungsmöglichkeiten zur Verfügung.

Durch die Betätigung der Schaltfläche :guilabel:`Kommentieren` wird
der Kommentar gespeichert.

Falls Ihr Kommentar nicht sofort sichtbar wird, finden Sie über dem
Artikel den Hinweis, dass Ihr Kommentar noch vom Moderator freigegeben
werden muss.

Captchas
--------

Mit einem Captcha kann man verhindern, dass Kommentare von einem
Skript eingetragen werden. Dabei muss der Benutzer eine verzerrt
dargestellte Zeichenfolge in ein besonderes Feld eingeben. Die
Zeichenfolgen können nur mit erheblichem Aufwand mit Hilfe von
Computern erkannt werden. Sie bieten einen Schutz vor Spammern, sind
allerdings alles andere als benutzerfreundlich, da sie zusätzliche
Hürden beim Kommentieren einbauen. Ihr Einsatz muss daher abgewogen
werden. 

Kommentare moderieren
=====================

Wenn die Kommentarfunktion entsprechend konfiguriert ist, müssen
Kommentare von einem Moderator freigeschaltet werden. Kommentare
können von Redakteuren und Administratoren moderiert werden.

Kommentare im Artikel selbst moderieren
---------------------------------------

Ein Redakteur kann Kommentare direkt im Artikel moderieren (siehe
Abb. :ref:`fig_kommentare-freischalten`). 

.. todo:: Neuer Screenshot wg. Übersetzung

.. _fig_kommentare-freischalten:

.. figure::
   ../images/kommentare-freischalten.*
   :alt: Noch nicht freigeschaltete Kommentare unterhalb eines
   	 Artikels

   Kommentare im Artikel moderieren

Noch nicht freigeschaltete Artikel erscheinen in gelber Schrift. Dem
Moderator stehen zwei Schaltflächen zur Moderation zur Verfügung:
:guilabel:`Löschen`, um den Kommentar zu löschen, und
:guilabel:`Veröffentlichen`, um ihn freizuschalten.


.. warning::
   Beim Löschen werden Kommentare ohne Nachfrage entfernt.

Kommentare global moderieren
----------------------------

Administratoren können Kommentare auch global moderieren. Sie finden
in ihrem Benutzermenü den Eintrag :guilabel:`Kommentare moderieren`
(siehe Abb. :ref:`fig_benutzermenue-kommentare-moderieren`).

.. _fig_benutzermenue-kommentare-moderieren:

.. figure::
   ../images/benutzermenue-kommentare-moderieren.*
   :width: 50%
   :alt: Benutzermenü mit Link zur Kommentarmoderation

   Benutzermenü mit Link zur Moderation

Über diesen Eintrag gelangt man auf die Moderationsseite, auf der alle
offenen Kommentare aufgelistet sind (siehe Abb.:
:ref:`fig_kommentare-moderieren`)

.. _fig_kommentare-moderieren:

.. figure::
   ../images/kommentare-moderieren.*
   :alt: Auflistung aller Kommentare, die noch moderiert werden müssen

   Kommentare global moderieren

Die Tabelle enthält Spalten 

* für den Autor, der den Kommentar verfasst hat
* für das Datum und die Uhrzeit, wann der Kommentar geschrieben wurde
* für den Artikel, auf den sich der Kommentar bezieht,
* für den Wortlaut des Kommentars
* für Aktionen, die der Moderator ausführen kann. Diese sind
  :guilabel:`Veröffentlichen` und :guilabel:`Löschen`.

Kommentare per E-Mail-Benachrichtigung moderieren
-------------------------------------------------

Moderatoren können per E-Mail darüber informiert werden, dass ein
neuer Kommentar abgegeben wurde und moderiert werden muss. 

.. _fig_kommentare-moderator-email:

.. figure::
   ../images/kommentare-moderator-email.*
   :alt: Wortlaut der E-Mail an Moderatoren

   E-Mail-Benachrichtigung

Die E-Mail enthält drei Links sowie den Wortlaut des Kommentars. Der
erste Link führt zu dem Kommentar. Mit den beiden anderen Links kann
der Moderator den Kommentar freigeben oder löschen.

Löschen bereits freigeschalteter Kommentare
===========================================

Als Administrator können Sie bereits veröffentlichte Kommentare oder auch ganze
Diskussionsstränge durch Betätigung der Schaltfläche :guilabel:`Löschen` wieder
entfernen (siehe Abbildung :ref:`fig_kommentare-loeschen`). Löschen Sie einen
Diskussionsbeitrag, auf den bereits geantwortet wurde, so werden auch alle
Antworten auf ihn entfernt.

.. _fig_kommentare-loeschen:

.. figure::
   ../images/kommentare-loeschen.*

   Schaltfläche zum Löschen von Kommentaren

.. warning:: 
   Kommentare werden ohne Nachfrage gelöscht.


Kommentare als Autor erlauben
=============================

Als Besitzer eines Artikels können Sie bestimmen, ob er kommentiert
werden darf. Jeder Besucher, der den Artikel einsehen darf, kann auch
alle Kommentare vollständig lesen. 

Um Kommentare zu erlauben, wechseln Sie in der Bearbeitungsansicht des
Artikels ins Teilformular »Einstellungen«. Dort können Sie die
Kommentarfunktion ein- und ausschalten, indem Sie das Häkchen bei der Option
»Kommentare erlauben« setzen oder entfernen (siehe
Abbildung :ref:`fig_kommentare-erlauben`).

.. _fig_kommentare-erlauben:

.. figure:: ../images/kommentare-erlauben.*
   :alt: Untermenü »Einstellungen« mit der Option »Kommentare
   	 erlauben«

   Kommentare zu einem Artikel erlauben

Im Konfigurationsmenü kann der Administrator für jeden Artikeltyp
voreinstellen, ob Kommentare erlaubt sind (siehe Kapitel
:ref:`sec_konfiguration-artikeltypen`).

Viele der hier vorgestellten Funktionen müssen zentral konfiguriert
werden. Mehr dazu in Kapitel :ref:`sec_kommentierungseinstellungen`.


.. _Website: http://daringfireball.net/projects/markdown/
