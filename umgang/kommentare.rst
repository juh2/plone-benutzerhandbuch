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
Skript eingetragen werden. Dabei muss der Benutzer ein verzerrt
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


.. _fig_kommentare-freischalten:

.. figure::
   ../images/kommentare-freischalten.*
   :alt: Noch nicht freigeschaltete Kommentare unterhalb eines
   	 Artikels

   Kommentare im Artikel moderieren

Noch nicht freigeschaltete Artikel erscheinen in gelber Schrift. Dem
Moderator stehen zwei Schaltflächen zur Moderation zur Verfügung:
:guilabel:`Löschen`, um den Kommentar zu löschen, und
:guilabel:`Approve`, um ihn freizuschalten.

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

Als Administrator können Sie einzelne Kommentare oder auch ganze
Diskussionsstränge löschen. Dafür besitzt jeder Kommentar neben der
Schaltfläche :guilabel:`Antworten` eine, die mit :guilabel:`Löschen`
beschriftet ist (siehe Abbildung
:ref:`fig_kommentare-loeschen`). Löschen Sie einen Diskussionsbeitrag,
auf den bereits geantwortet wurde, so werden auch alle Antworten auf
ihn entfernt.

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




.. _sec_kommentierungseinstellungen:

Konfiguration der Kommentarfunktion
===================================

Die Kommentarfunktion lässt sich detailliert konfigurieren. Im
Konfigurationsmenü von Plone befindet sich ein Eintrag mit dem Namen
:guilabel:`Kommentare`. Über diesen Link gelangt man in das
Konfigurationsmenü für die Kommentarfunktion (siehe Abb.:
:ref:`fig_konfiguration-kommentare`). 


.. _fig_konfiguration-kommentare:

.. figure::
   ../images/konfiguration-kommentare.*
   :alt: Das Konfigurationsmenü für die Kommentarfunktion

   Das Konfigurationsmenü für die Kommentarfunktion

Folgende Optionen können eingestellt werden:

Kommentierungsfunktion generell einschalten
    Wenn hier ein Häkchen gesetzt ist, wird die Kommentierungsfunktion
    aktiviert. Wenn Kommentare generell nicht erwünscht sind,
    entfernen Sie das Häkchen. Die übrigen Optionen sind daraufhin
    nicht zugänglich.

Anonyme Kommentare
   Da Plone sehr differenziert als öffentliches Internetportal sowie
   als teilweise öffentliches oder geschlossenes Intranet betrieben
   werden kann, gibt es die Möglichkeit nicht angemeldeten Benutzern
   das Kommentieren zu erlauben.

Enable comment moderation
   Wenn man anonyme Kommentare erlaubt, ist es oftmals empfehlenswert,
   diese vor einer Veröffentlichung von einem Moderator sichten und
   freigeben lassen. Wenn dies der Fall ist, aktivieren Sie diese
   Option.

Text transformationen
   Eine Textauszeichnung (Formatierung) ist bei Kommentaren in der
   Regel nicht nötig. In der Voreinstellung wird daher die Texteingabe
   in reinen Text umgewandelt. Wenn Kommentare umfangreich formatiert werden
   sollen, können Sie den Benutzern die Eingabe von Markdown
   ermöglichen. Die dritte Eintellungsmöglichkeit ist »Intelligent
   text«. Bei dieser Option werden URLs und E-Mail-Adresse in Links
   konvertiert. Alle anderen Eingaben werden in reinen Text
   umgewandelt.

Captcha
   Um zu verhindern, dass durch Skripte automatisiert Kommentare
   erzeugt werden, können Captchs genutzt werden. Dazu müssen die
   angegebenen Erweiterungen installiert werden. Ansonsten kann hier
   keine Auswahl erfolgen.

Zeige das Portrait des Kommentators
   Wenn ein registrierter Benutzer kommentiert, erscheint sein
   Porträtfoto im Kommentar, wenn diese Option aktiviert ist.

Email-Benachrichtigungen für Moderatoren aktivieren
   Wenn diese Option aktiviert ist, erhält der Moderator eine E-Mail,
   wenn ein neuer Kommentar zu kontrollieren ist. Standardmäßig wird
   die E-Mail an die Adresse versendet, die in der E-Mail-Konfiguration
   angegeben wurde. Es kann im Feld darunter eine alternative
   Moderator E-Mail-Adresse angegeben werden.

Moderator Email Address
   Hier kann eine E-Mail-Adresse angegeben werden, an die die
   Benachrichtigungen geschickt werden.

E-Mail-Benachrichtigungen für Benutzer aktivieren
   Diese Option ist standardmäßig aktiviert. Leider funktioniert sie
   wegen eines Bugs nicht. In einer zukünftigen Version von Plone
   könnte dieser Bug beseitigt sein. Wenn diese Option aktiviert ist,
   kann sich der Benutzer über weitere Kommentare zu einem Artikel per
   E-Mail informieren lassen. 


.. _Website: http://daringfireball.net/projects/markdown/
