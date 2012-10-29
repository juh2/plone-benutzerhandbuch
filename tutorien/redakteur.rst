.. _sec_veroff-von-artik:

=============================
Veröffentlichung von Artikeln
=============================

Dieses Tutorium erläutert die Arbeitsschritte, die notwendig sind, um einen
Artikel zu veröffentlichen.

Wenn Sie einen Artikel erstellen, ist er zunächst »privat«. Nur Sie selbst
haben Zugriff auf ihn. Andere Besucher der Website können den Artikel erst
einsehen, nachdem er veröffentlicht wurde. Wenn Sie Ihre Website
alleine betreiben, können Sie selbst darüber entscheiden, ob ein Artikel
veröffentlicht werden soll oder nicht. In vielen Fällen sind Sie jedoch
nicht allein für eine Website verantwortlich, sodass die Veröffentlichung von
Artikeln mit anderen Personen abgestimmt werden muss. Plone unterstützt solche
Abstimmungsprozeduren durch festgelegte Arbeitsabläufe (siehe
Abschnitt :ref:`sec_workflow`).

Artikel zu verfassen, zu redigieren und zu veröffentlichen bedeutet in der
Regel eine Arbeitsteilung zwischen Personen, die unterschiedliche
Funktionen ausüben. Die einen, die wir im Folgenden als Autoren
bezeichnen, verfassen Artikel, die anderen, die Redakteure, redigieren
und veröffentlichen sie.

In Plone haben Autoren und Redakteure unterschiedliche Rechte, sodass es
empfehlenswert ist, wenn Sie dieses Tutorium zu zweit an verschiedenen
Rechnern mit verteilten Rollen durcharbeiten. Falls Sie alleine arbeiten,
müssen Sie sich während des Tutoriums ab- und mit dem Benutzernamen eines
Redakteurs wieder anmelden.

.. _sec_veroff-von-artik-1:

Anmelden als Autor oder Redakteur
=================================

Wir gehen im Folgenden davon aus, dass in Ihrer Website ein Benutzer
registriert worden ist, der zusätzliche Rechte besitzt und im Ordner
»Veranstaltungen« Artikel veröffentlichen darf. Wir bezeichnen diesen Benutzer
im Folgenden als »Redakteur«. Wenn Sie die Redakteursfunktionen in diesem
Tutorium ausprobieren möchten, müssen Sie sich mit dem Benutzernamen des
Redakteurs bei Ihrer Website anmelden. Fragen Sie gegebenenfalls Ihren
Administrator nach den entsprechenden Zugangsdaten. Wenn Sie Autorenfunktionen
ausüben, können Sie sich mit Ihrem persönlichen Benutzernamen anmelden.


.. _sec_artik-zur-veroff:

Artikel zur Veröffentlichung einreichen
=======================================


.. _sec_veroff-von-artik-2:

Einen einzelnen Artikel zur Veröffentlichung einreichen
-------------------------------------------------------

* Melden Sie sich auf Ihrer Website mit Ihrem Benutzernamen an.
* Legen Sie im Ordner »Veranstaltungen« eine neue Seite an, bearbeiten Sie
  Titel, Beschreibung und Haupttext und speichern Sie Ihre Eingaben.
* Vergewissern Sie sich in der Ordnerübersicht, dass der Status des
  Artikels »privat« ist und der Eintrag für den Artikel rot dargestellt
  wird.
* Reichen Sie die Seite zur Veröffentlichung ein, indem Sie zur Anzeige des
  Artikels wechseln und im Statusmenü den Eintrag :guilabel:`Zur
  Veröffentlichung einreichen` wählen (siehe Abbildung
  :ref:`fig_auswahlmenu-zur-veroeffentlichung-einreichen`).

.. _fig_auswahlmenu-zur-veroeffentlichung-einreichen:

.. figure::
   ../images/zur-veroeffentlichung-einreichen.*
   :width: 100%

   Einen Artikel zur Veröffentlichung einreichen

* Achten Sie auf die Statusmeldung und darauf, dass der Artikel in der
  Ordnerübersicht nun als »zur Redaktion eingereicht« geführt und in
  Orange dargestellt wird.

.. _fig_zur-veroeffentlichung-eingereicht:

.. figure::
   ../images/zur-veroeffentlichung-eingereicht.*
   :width: 100%

   Statusmeldung nach Einreichung

.. _sec_veroff-von-artik-4:

Mehrere Artikel zur Veröffentlichung einreichen
-----------------------------------------------

Sie können mehrere Artikel gleichzeitig zur Veröffentlichung einreichen.

* Legen Sie mehrere Artikel im Ordner »Veranstaltungen« an.
* Wechseln Sie zur Inhaltsansicht des Ordners. Ihre neuen Artikel werden
  dort mit dem Status »privat« geführt und rot dargestellt.
* Wählen Sie in der Tabelle die Artikel aus, die Sie zur Veröffentlichung
  einreichen wollen.
* Betätigen Sie die Schaltfläche :guilabel:`Status ändern` unterhalb der
  Tabelle. Sie gelangen zu einem Formular (siehe Abbildung
  :ref:`fig_formular-arbeitsablauf`), mit dem Sie die ausgewählten Artikel zur
  Veröffentlichung einreichen können. Das Formular wird in Abschnitt
  :ref:`sec_batch-publishing` im Detail beschrieben.
* Geben Sie im Feld »Kommentare« eine Nachricht für Ihren Redakteur ein.
* Wählen Sie ganz unten auf dem Formular im Abschnitt »Statusänderung«
  :guilabel:`Zur Veröffentlichung einreichen` und speichern Sie.
* Achten Sie auf die Statusmeldung und darauf, dass alle eingereichten
  Artikel im Ordner nun den Status »zur Veröffentlichung eingereicht« tragen
  und in einer anderen Farbe (Orange) dargestellt werden.

.. _fig_formular-arbeitsablauf:

.. figure::
   ../images/formular-arbeitsablauf.*
   :width: 100%

   Das erweiterte Formular für den Arbeitsablauf

.. todo:: Formular erscheint als Popup. Prüfen!

Sie erreichen das Formular auch über den Menüeintrag »Erweitert...« im
Statusmenü eines Artikels. Sie werden vor allem dann das Formular benötigen,
wenn Sie Ihrem Redakteur Kommentare hinterlassen wollen.


.. _sec_artik-redig-und:

Artikel veröffentlichen und zurückweisen
========================================

Nachdem ein Artikel zur Veröffentlichung eingereicht wurde, kommt der
Redakteur ins Spiel. Übernehmen Sie deshalb jetzt  die Rolle des Redakteurs.

* Melden Sie sich mit Ihrem eigenen Benutzernamen ab.
* Melden Sie sich mit dem Benutzernamen des Redakteurs wieder an.
* Wechseln Sie zur persönlichen Seite des Redakteurs.


Auf der persönlichen Seite des Redakteurs erscheint ein Portlet mit der
Revisionsliste (siehe Abbildung :ref:`fig_revisionsliste-persoenliche-seite`).

.. _fig_revisionsliste-persoenliche-seite:

.. figure::
   ../images/revisionsliste-persoenliche-seite.*
   :width: 100%

   »Revisionsliste« auf persönlicher Seite


Die Liste enthält Artikel, die zur Veröffentlichung eingereicht wurden und die
Sie veröffentlichen dürfen.

.. _sec_artik-redig-veroff:

Artikel veröffentlichen
-----------------------

* Wählen Sie in der Revisionsliste einen Artikel aus.
* Lesen und bearbeiten Sie gegebenenfalls den Artikel.
* Veröffentlichen Sie den Artikel, indem Sie im Statusmenü den Eintrag
  »Veröffentlichen« (siehe Abbildung :ref:`fig_statusmenu-veroeffentlichen`)
  auswählen.
* Achten Sie auf die Statusmeldung und darauf, dass der Artikel in der
  Ordneransicht nun mit dem Status »veröffentlicht« angezeigt und in Blau
  dargestellt wird.

.. _fig_statusmenu-veroeffentlichen:

.. figure::
   ../images/veroeffentlichen.*
   :width: 100%

   Einen Artikel veröffentlichen

Der veröffentlichte Artikel ist nun auch für anonyme Besucher der Website
sichtbar.

.. _sec_artik-redig-und-1:

Historie des Arbeitsablaufs
===========================

Rufen Sie den veröffentlichten Artikel auf und gehen Sie zur Historie des
Artikels, indem Sie dem Verweis »Historie« unterhalb des Titels folgen. (siehe
Abbildung :ref:`fig_historie-arbeitsablauf`).

.. _fig_historie-arbeitsablauf:

.. figure::
   ../images/historie-arbeitsablauf.*
   :width: 100%

   Historie des Arbeitsablaufes

Dort können Sie nachschauen, wer den Artikel wann bearbeitet, zur
Veröffentlichung eingereicht oder veröffentlicht hat. Die Tabelle enthält eine
Liste aller Änderungen. 

.. _sec_artik-redig-veroff-1:

Artikel zurückweisen
--------------------

Falls Sie der Meinung sind, dass ein Artikel nicht veröffentlicht werden
sollte, können Sie ihn zurückweisen.

* Wählen Sie in der Revisionsliste einen Artikel aus.
* Lesen Sie den Artikel.
* Weisen Sie den Artikel zurück, indem Sie im Statusmenü den Eintrag
  :guilabel:`Zurückweisen` (siehe Abbildung :ref:`fig_statusmenu-veroeffentlichen`)
  auswählen.
* Achten Sie auf die Statusmeldung und darauf, dass der Artikel in der
  Ordnerübersicht nun den Status »privat« trägt und in Rot dargestellt wird.

Am Status »privat« erkennt der Verfasser, dass Sie den Artikel
zurückgewiesen haben.

Da eine Zurückweisung ohne Begründung für den Verfasser zumeist unbefriedigend
ist, sollten Sie das erweiterte Formular »Arbeitsablauf« benutzen, um ihm im
Kommentarfeld eine Begründung für die Zurückweisung zu hinterlassen. Der
Verfasser des Artikels kann diesen Kommentar in der Historie nachlesen und
seinen Artikel entsprechend überarbeiten.

Falls Sie zu zweit das Tutorium durcharbeiten, wechseln Sie nun die Rollen und
gehen Sie die Arbeitsschritte dieses Abschnitts erneut durch.

