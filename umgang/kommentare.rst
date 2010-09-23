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
   :width: 100%

   Kommentare

Antworten auf einen Kommentar werden direkt unterhalb des Kommentars
angezeigt und eingerückt. So kann sich eine verzweigte Diskussion
entwickeln.


An Diskussionen teilnehmen
==========================

Falls der Verfasser des Artikels Kommentare erlaubt hat, können Sie
den Artikel kommentieren. Um einen Kommentar hinzufügen zu können,
müssen Sie aber in der Regel an der Website angemeldet sein. Als nicht
angemeldeter Benutzer sehen Sie in diesem Fall einen Verweis zur
Anmeldung mit der Bezeichnung »Zum Kommentieren müssen Sie sich
anmelden«.

Nach der Anmeldung sehen Sie unterhalb des Artikels die Schaltfläche
:guilabel:`Kommentieren` und am Ende jedes einzelnen Kommentars die Schaltfläche
:guilabel`Antworten`q. Die Schaltflächen führen Sie zu einem Formular, in dem Sie
einen Kommentar zum Artikel oder eine Antwort auf einen Diskussionsbeitrag
verfassen können (siehe Abbildung :ref:`fig_kommentieren`).

.. _fig_kommentieren:

.. figure:: ../images/kommentieren.*
   :width: 100%

   Eingabeformular für einen Kommentar

Oberhalb des Formulars wird der Artikel angezeigt. Antworten Sie auf einen
anderen Diskussionsbeitrag, so sehen Sie außerdem alle Kommentare, die Ihrer
Antwort in der Diskussion vorangingen. So haben Sie beim Schreiben all das im
Blick, worauf Sie sich beziehen möchten.

Im Kommentarformular geben Sie einen Betreff und Ihren Kommentar ein. Sie
müssen beide Formularfelder ausfüllen. Der Kommentar ist einfacher Text, den
Sie nicht formatieren können. Wenn Sie das Formular speichern, gelangen Sie
wieder zur Anzeige des Artikels. Dort ist Ihr Beitrag sofort sichtbar.


Konfiguration
=============

Als Besitzer eines Artikels können Sie bestimmen, ob er kommentiert
werden darf. Jeder Besucher, der den Artikel einsehen darf, kann auch
alle Kommentare vollständig lesen. 

.. Ihr Administrator kann für die gesamte Website einstellen, ob
   unangemeldete Besucher Beiträge verfassen dürfen.

Um Kommentare zu erlauben, wechseln Sie in der Bearbeitungsansicht des
Artikels ins Teilformular »Einstellungen«. Dort können Sie die
Kommentarfunktion ein- und ausschalten, indem Sie das Häkchen bei der Option
»Kommentare erlauben« setzen oder entfernen (siehe
Abbildung :ref:`fig_kommentare-erlauben`).

.. _fig_kommentare-erlauben:

.. figure:: ../images/kommentare-erlauben.*
   :width: 100%

   Kommentare zu einem Artikel erlauben

Im Konfigurationsmenü kann der Administrator für jeden Artikeltyp
voreinstellen, ob Kommentare erlaubt sind (siehe Kapitel
:ref:`sec_konfiguration-artikeltypen`).


Beiträge löschen
================

Als Administrator eines Artikels können Sie einzelne Kommentare oder
auch ganze Diskussionsstränge löschen. Dafür besitzt jeder Kommentar
neben der Schaltfläche :guilabel:`Antworten` eine, die mit
:guilabel:`Löschen` beschriftet ist (siehe Abbildung
:ref:`fig_kommentare-loeschen`). Löschen Sie einen Diskussionsbeitrag,
auf den bereits geantwortet wurde, so werden auch alle Antworten auf
ihn entfernt. 

.. warning:: 
   Beachten Sie, dass beim Löschen von Kommentaren keine
   weitere Nachfrage erfolgt.

.. _fig_kommentare-loeschen:

.. figure::
   ../images/kommentare-loeschen.*
   :width: 100%

   Zusätzliche Schaltfläche zum Löschen von Kommentaren
