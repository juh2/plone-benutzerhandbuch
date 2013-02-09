======================
 Angemeldete Benutzer
======================

Jeder registrierte Benutzer besitzt einen Benutzernamen, mit dem er
für die Website eindeutig identifizierbar ist. Jeder Benutzername darf
innerhalb einer Website daher nur einmal vergeben werden.

Nachdem Sie sich mit Ihrem Benutzernamen und Passwort an der Website
angemeldet haben, passt sich die Benutzungsoberfläche an Ihre
persönlichen Einstellungen an und bietet Ihnen zusätzliche
Funktionen. Dazu zählen die persönliche Seite, der persönliche Ordner
sowie die Möglichkeit, Webinhalte zu bearbeiten.

.. _sec_anmelden:

Anmelden
========

In diesem Buch gehen wir davon aus, dass Sie bereits auf Ihrer Website
registriert sind und Ihre Zugangsdaten, also Benutzernamen und
Passwort, kennen.  Falls Sie das Tutorium in Abschnitt
:ref:`sec_tutorium-rundgang` nachvollzogen haben, haben Sie Ihr
Passwort auch schon einmal geändert.

Sie können sich auf verschiedene Weise an der Website anmelden. Zum
einen gibt es das Anmeldeportlet, das Sie als anonymer Besucher auf
jeder Seite der Website sehen. Zum anderen enthält das Benutzermenü
für anonyme Besucher den Verweis »Anmelden«, der zu einem
Anmeldeformular führt.

Sowohl das Portlet als auch das Anmeldeformular enthalten Eingabefelder für
Ihren Benutzernamen und Ihr Passwort sowie eine Schaltfläche zum Anmelden
(siehe Abbildung :ref:`fig_portlet-login`).

.. _fig_portlet-login:

.. figure:: ../images/portlet-login.*
   :width: 80%
   :alt: Zwei Anmeldeportlets, links mit Feld für Benutzername, rechts
   	 für E-Mail-Adresse

   Anmeldeportlets (Benutzername/E-Mail-Adresse)

.. _fig_anmeldeformular:

.. figure:: ../images/anmeldeformular.*
   :width: 100%

   Anmeldeformular


Sie verweisen außerdem auf ein oder zwei Formulare:


* Unter »Passwort vergessen?« können sich registrierte Benutzer per
  E-Mail einen Link zuschicken lassen, der sie zu einer Seite führt, auf der
  sie ihr Passwort neu setzen können.
* Der Verweis »Neuer Benutzer?« erscheint nur, falls die Website so
  konfiguriert wurde, dass man sich selbst registrieren kann. Er führt
  dann zum Registrierungsformular.

.. _sec_benutzer-aktionen:

Benutzeraktionen
================

Nach Ihrer Anmeldung an der Website haben Sie im Benutzermenü Zugriff auf eine
Reihe von Aktionen (siehe Abbildung :ref:`fig_benutzermenue`):

.. _fig_benutzermenue:

.. figure:: ../images/benutzermenue.*

   Benutzermenü für einen angemeldeten Benutzer


Ihr Name/Ihre E-Mail-Adresse 
 Der oberste Eintrag dient als Titel des Benutzermenüs und ist Ihr
  Benutzername oder Ihre E-Mail-Adresse.  

Mein Ordner
  Hier gelangen Sie gegebenenfalls zu Ihrem persönlichen
  Ordner (siehe Abschnitt :ref:`sec_mitgliedsordner`).

Persönliche Seite
  Dieser Eintrag führt Sie zu Ihrer persönlichen Seite (siehe
  Abschnitt :ref:`sec_personliche-seite-1`).

Meine Einstellungen
  Über diesen Eintrag gelangen Sie zu einem Formular, auf dem Sie
  persönliche Einstellungen vornehmen können (siehe
  :ref:`sec_meine-einstellungen`).

Abmelden 
  Über diesen Verweis melden Sie sich von der Website ab und
  haben keinen Zugriff mehr auf die erweiterten Funktionen für
  angemeldete Benutzer.

.. _sec_personliche-seite-1:

Persönliche Seite
=================

Ihre persönliche Seite kann mehrere Portlets enthalten, die entweder
von Ihnen oder vom Administrator hinzugefügt wurden (siehe Abbildung
:ref:`fig_persoenliche-seite-redakteur`).

.. _fig_persoenliche-seite-redakteur:

.. figure::
   ../images/persoenliche-seite-redakteur.*
   :width: 100%
   :alt: Die persönliche Seite eines Redakteurs

   Die persönliche Seite eines Redakteurs
 

.. _sec_portlets-hinzufuegen:

Portlets hinzufügen
-------------------

Die Portlets auf Ihrer Seite sind in vier Spalten angeordnet. In der
Bearbeitungsansicht Ihrer Seite können Sie in jeder der Spalten
beliebige Portlets anlegen, umordnen, zeitweise verbergen und löschen
(siehe Abbildung :ref:`fig_persoenliche-seite-bearbeiten`). Einen
Überblick über Plones Portlets finden Sie in Abschnitt
:ref:`sec_portlets`.

.. _fig_persoenliche-seite-bearbeiten:

.. figure:: ../images/persoenliche-seite-bearbeiten.*
   :width: 100%
   :alt: Die Bearbeitungsansicht der persönlichen Seite

   Die Bearbeitungsansicht der persönlichen Seite

Sie finden folgende Bedienelemente in der Bearbeitungsansicht Ihrer
persönlichen Seite:

* Das Auswahlmenü :guilabel:`Portlet hinzufügen`. In diesem Menü
  finden Sie alle Portlets, die Sie auf Ihrer persönlichen Seite
  hinzufügen können.

* Die Liste der in jeder Spalte zugewiesenen Portlets mit dem Titel
  »Hier zugewiesene Portlets«.

* Die Einträge für jedes Portlet sind grau hinterlegt.

  * Der Name des Portlets ist ein Verweis auf seine
    Bearbeitungsansicht
  * Mit den Pfeilsymbolen können Sie die Reihenfolge der Portlets in
    der jeweiligen Spalte verändern.
  * Mit :guilabel:`Verbergen` machen Sie das Portlet unsichtbar, ohne
    es zu löschen. Dies ist praktisch, wenn Sie es nur zeitweise nicht
    auf Ihrer persönlichen Seite anzeigen wollen.
  * Mit dem Verweis :guilabel:`x` löschen Sie das Portlet komplett.

Um ein Portlet hinzuzufügen, wählen Sie es im Auswahlmenü aus. Viele
Portlets müssen Sie erst konfigurieren, bevor sie angezeigt werden
können. Dies geschieht im jeweiligen Bearbeitungsformular des
Portlets. Nachfolgend werden die Einstellungsmöglichkeiten in den
Bearbeitungsformularen der einzelnen Portlets aufgeführt.


RSS-Feed
~~~~~~~~

.. _fig_rss-feed-hinzufuegen:

.. figure:: ../images/rss-feed-portlet-hinzufuegen.*
   :width: 80%
   :alt: Bearbeitungsformular eines RSS-Portlets

   Hinzufügen des RSS-Portlets

Einstellungsmöglichkeiten im Bearbeitungsformular von RSS-Portlets
(siehe Abbildung :ref:`fig_rss-feed-hinzufuegen`):

* Titel des RSS-Portlets. Wenn Sie nichts eintragen, wird der Titel
  aus dem Feed selbst benutzt.
* Anzahl der Artikel, die im Portlet angezeigt werden sollen.
* URL des RSS-Feeds
* Aktualisierungsintervall: Anzahl der Minuten, nach denen der
  RSS-Feed erneuert werden soll

Suche
~~~~~

Einstellungsmöglichkeiten im Suchportlet (siehe Abbildung
:ref:`fig_suchportlet-hinzufuegen`).

.. _fig_suchportlet-hinzufuegen:

.. figure:: ../images/suchportlet-hinzufuegen.*
   :width: 80%
   :alt: Bearbeitungsformular eines Suchportlets

   Hinzufügen des Suchportlets

* Sofortsuche erlauben (siehe hierzu Abschnitt :ref:`sec_sofortsuche`)

Aktuelle Änderungen
~~~~~~~~~~~~~~~~~~~

Einstellungsmöglichkeiten im Portlet »Aktuelle Änderungen« (siehe
Abbildung :ref:`fig_aktuelle-artikel-portlet-hinzufuegen`).

.. _fig_aktuelle-artikel-portlet-hinzufuegen:

.. figure:: ../images/aktuelle-artikel-portlet-hinzufuegen.*
   :width: 80%
   :alt: Bearbeitungsformular des Portlets »Aktuelle Änderungen«

   Hinzufügen des Portlets »Aktuelle Änderungen«


* Anzahl der Artikel, die im Portlet angezeigt werden sollen.

Nachrichten
~~~~~~~~~~~

Einstellungsmöglichkeiten im Nachrichtenportlet (siehe Abbildung
:ref:`fig_nachrichten-portlet-hinzufuegen`)

.. _fig_nachrichten-portlet-hinzufuegen:

.. figure:: ../images/nachrichten-portlet-hinzufuegen.*
   :width: 80%
   :alt: Bearbeitungsformular eines Nachrichtenportlets

   Hinzufügen des Nachrichtenportlets


* Anzahl der Artikel, die im Portlet angezeigt werden sollen.
* zu berücksichtigende Status der Artikel

Welche Nachrichten angezeigt werden, richtet sich danach, ob sie die
Nachrichten im gewählten Status überhaupt sehen
dürfen. Veröffentlichte Nachrichten kann sich jeder Benutzer anzeigen
lassen. Nachrichten im Status »privat« können Sie nur unter bestimmten
Bedingungen – zumeist jedoch nicht – einsehen.

Termine
~~~~~~~

Einstellungsmöglichkeiten im Bearbeitungsformular von Terminportlets
(siehe Abbildung :ref:`fig_terminportlet-hinzufuegen`)

.. _fig_terminportlet-hinzufuegen:

.. figure:: ../images/terminportlet-hinzufuegen.*
   :width: 80%
   :alt: Bearbeitungsformular eines Terminportlets

   Hinzufügen des Terminportlets


* Anzahl der angezeigten Termine
* zu berücksichtigende Status (siehe die Erläuterung zum
  Nachrichtenportlet)

Klassisches Portlet
~~~~~~~~~~~~~~~~~~~

Unter einem klassischen Portlet versteht man ein Portlet, das für eine
frühere Version von Plone erstellt wurde. Ein solches Portlet können
Sie nicht direkt anlegen. Sie müssen im Auswahlmenü »Klassisches
Portlet« wählen und beim Bearbeiten angeben, wo Plone die Beschreibung
des Portlets finden kann.

Das einzige klassische Portlets, das Plone von Haus aus mitbringt, ist das
Portlet für Ihre Lesezeichen. Fragen Sie Ihren Administrator, ob es auf Ihrer
Website weitere klassische Portlets gibt.

.. _fig_klassisches-portlet-hinzufuegen:

.. figure:: ../images/klassisches-portlet-hinzufuegen.*
   :width: 80%
   :alt: Bearbeitungsformular zum Hinzufügen eines so genannten
   	 klassischen Portlets

   Hinzufügen des klassischen Portlets

Abbildung :ref:`fig_klassisches-portlet-hinzufuegen`
zeigt das Bearbeitungsformular für ein klassisches Portlet. Ein solches
Portlet wird durch ein Makro in einer Vorlage beschrieben; Sie müssen die
Namen der Vorlage und des Makros angeben. Da Portletmakros in der Regel den
Namen »portlet« hatten, ist das Formularfeld bereits mit diesem Namen
vorausgefüllt. Die Vorlage für das Lesezeichenportlet heißt
``portlet_favorites``.

.. _sec_meine-einstellungen:

Meine Einstellungen
===================

Wenn Sie dem Verweis :guilabel:`Meine Einstellungen` im Benutzermenü
folgen, gelangen Sie auf das Formular »Meine Einstellungen«, auf dem
Sie eine persönliche Konfiguration der Website vornehmen können (siehe
Abbildung :ref:`fig_meine-einstellungen`).

.. _fig_meine-einstellungen:

.. figure:: ../images/meine-einstellungen.*
   :width: 100%
   :alt: Formular mit benutzerspezifischen Konfigurationsmöglichkeiten 

   Persönliche Einstellungen

Folgende Konfigurationsmöglichkeiten stehen Ihnen zur Verfügung:

Texteditor
  Hier wählen Sie aus, mit welchem Texteditor
  Sie den Haupttext Ihrer Seiten bearbeiten wollen. Es gibt
  drei Möglichkeiten:
 
  * Standardeinstellung der Website übernehmen: Sie übernehmen damit
    die Einstellungen, die Ihr Administrator vorgesehen hat.

  * TinyMCE: Dies ist ein komfortabler, visueller Editor. Mit ihm können Sie Ihren
    Text bei der Eingabe direkt formatieren und sehen ihn dabei so, wie er
    später von Plone angezeigt wird. 

  * Keiner: Wenn Sie keinen Texteditor auswählen, erhalten Sie bei
    Textfeldern einfach ein mehrzeiliges Eingabefeld. Dies
    funktioniert in jedem Webbrowser. Sie können dann in die
    Eingabefelder neben einfachem Text und HTML möglicherweise auch
    andere Textauszeichnungssprachen eingeben.

Externen Editor erlauben
  Wenn diese Option aktiviert ist, können Sie Plone-Artikel mit Hilfe
  eines Editors bearbeiten, der lokal auf Ihrem Rechner installiert
  ist. Hierzu sind Zusatzprogramme notwendig, die gesondert
  installiert werden müssen (siehe dazu Kapitel
  :ref:`sec_externer-editor`) 

Aufgeführt in der Suche
  Falls diese Option aktiviert ist, können andere Benutzer Sie über
  die Benutzersuche finden. Weiter Informationen dazu finden Sie in
  Kapitel :ref:`sec_mitgliedersuche`. 

Bearbeitung der Kurznamen erlauben 
  Wenn Sie diese Option auswählen, können Sie in der
  Bearbeitungsansicht von Artikeln deren Kurznamen bearbeiten. Blenden
  Sie das Feld aus, wenn Sie eine aufgeräumtere Bearbeitungsansicht
  bevorzugen. Unabhängig davon können Sie die Kurznamen von Artikeln
  jederzeit in der Inhaltsansicht ihres jeweiligen Ordners bearbeiten.

  Diese Einstellung wirkt sich nur aus, wenn Ihr Administrator für die
  Website erlaubt hat, Kurznamen zu bearbeiten.

Sprache 
  Über das Auswahlmenü :guilabel:`Sprache` können Sie angeben,
  welche Sprache Sie bevorzugt sprechen. Diese Einstellung hat keine
  weitere Auswirkung.

Über Reiter in der grünen Leiste gelangen Sie zu weiteren Bereichen
Ihrer Einstellungen:

Persönliche Informationen
  Dieser Verweis führt Sie zu Ihrem Profil (siehe Abschnitt
  :ref:`sec_profil`).

Passwort
  Um ein neues Passwort für Ihr Benutzerkonto zu setzen, müssen Sie
  zunächst Ihr altes Passwort im ersten Formularfeld eingeben (siehe
  :ref:`fig_passwort-aendern`) und anschließend zweimal das neue Passwort
  eingeben. Betätigen Sie anschließend die Schaltfläche
  :guilabel:`Passwort ändern`.

  .. _fig_passwort-aendern:
  .. figure:: 
     ../images/passwort-aendern.*
     :width: 80%
     :alt: Formular zum Ändern des Passworts
     
     Formular zum Ändern des Passworts


.. _sec_profil:
     	       
Persönliche Informationen
-------------------------

Ihr Profil gibt anderen Benutzern der Website einen Überblick über
Ihre Person und Ihre Tätigkeit (siehe Abbildung :ref:`fig_profil`).

.. _fig_profil:

.. figure:: ../images/profil.*
   :width: 80%
   :alt: Formular zur Bearbeitung Ihrer persönlichen Informationen

   Formular zur Bearbeitung Ihrer persönlichen Informationen

Verweise auf Ihr Profil finden sich in Ihren Artikeln und einigen
automatisch erzeugten Übersichtslisten. 

Das Profil enthält folgende Informationen:

Vor- und Nachname
  Geben Sie hier Ihren vollständigen Namen ein. Mit
  diesem Namen werden Sie beispielsweise in der Anzeige Ihrer Artikel als
  Verfasser genannt.

E-Mail
 Geben Sie eine gültige E-Mail-Adresse ein, unter der
  Sie erreichbar sind. Dieses Feld müssen Sie ausfüllen.

Homepage
  Falls Sie eine eigene Website haben, so können Sie sie hier
  eintragen.  

Biographie
  Ein paar Sätze über Ihre Person und Ihre Arbeit. Mit diesem
  Text stellen Sie sich in Ihrem Profil vor. 

Ort
  Die Stadt oder das Land, wo Sie wohnen oder arbeiten.

Porträt
  Ein Foto von Ihnen, das in Ihrem Profil angezeigt wird. Wenn Sie ein
  zu großes Bild hochladen, wird es auf eine sinnvolle Größe skaliert.
  Um das Bild zu löschen, kreuzen Sie :guilabel:`Porträt löschen` an.

Einige Ihrer persönlichen Informationen werden auf der Website anderen
Benutzern zugänglich gemacht. So gelangen andere Benutzer
beispielsweise über einen Verweis in der Verfasserzeile eines Artikels
auf ein Formular (siehe Abbildung
:ref:`fig_rueckmeldung-an-autor`), über das sie mit Ihnen Kontakt aufnehmen
können. In diesem Formular werden der Benutzername, die Biographie,
und der Ort aus Ihren persönlichen Informationen angezeigt. 

.. _fig_rueckmeldung-an-autor:

.. figure::
   ../images/rueckmeldung-an-autor.*
   :width: 100%
   :alt: Das Formular, mit dem man dem Autor eine E-Mail senden kann

   Kontaktformular 
   
Das Formular verschickt Nachrichten an die E-Mail-Adresse, die Sie bei
der Anmeldung oder in den persönlichen Informationen angegeben haben,
sodass anonyme Besucher die Adresse nicht zu sehen bekommen. Die
Nachrichten bestehen aus Betreff und Text. Wenn Sie selbst Ihre
Profilseite betrachten, wird das Rückmeldeformular ausgeblendet.

Die Liste Ihrer aktuellen Artikel ist nach Artikeltypen sortiert und
enthält Titel und Änderungsdatum jedes aufgeführten Artikels. Darunter
finden Sie einen Verweis zu einer Liste aller von Ihnen verfassten
Artikel, beginnend mit dem neuesten.


.. _sec_mitgliedsordner:

Mein Ordner
===========

Falls Ihre Website entsprechend konfiguriert ist, erhält jeder Benutzer einen
persönlichen Ordner. Sie erreichen Ihren Ordner nach der Anmeldung über den
Verweis :guilabel:`Mein Ordner` im Benutzermenü. Wenn es auf Ihrer Website keine
persönlichen Ordner gibt, fehlt dieser Verweis.

In Ihrem Ordner können Sie nach eigenem Ermessen Artikel anlegen,
bearbeiten und löschen. An anderen Stellen der Website haben Sie diese
Möglichkeiten eventuell nicht oder nur eingeschränkt. 

Die persönlichen Ordner sind ebenso öffentlich einsehbar wie alle
anderen Inhalte der Website. Sie finden die Ordner anderer Benutzer
beispielsweise durch eine Suche im Benutzerbereich (siehe
Abschnitt :ref:`sec_mitgliedersuche`).

In Ihrem eigenen Ordner können Sie außer den öffentlich sichtbaren
auch solche Artikel sehen, die den Revisionsstatus
»privat« tragen, also vor anderen Benutzern und unangemeldeten
Besuchern versteckt sind.

.. todo:: Nachfragen ob es Favorites überhaupt noch gibt

.. Wenn Sie Lesezeichen anlegen, erzeugt Plone einen Lesezeichenordner
   in Ihrem persönlichen Ordner mit dem Titel »Favorites«. Für jedes
   Lesezeichen, das Sie auf der Website setzen, wird in diesem Ordner
   ein Lesezeichen-Artikel angelegt.

.. _sec_mitgliedersuche:

Benutzersuche
=============

Über den Eintrag :guilabel:`Benutzer` in der Hauptnavigation erreichen
Sie die Benutzersuche (siehe Abbildung :ref:`fig_benutzersuche`).

.. _fig_benutzersuche:

.. figure:: ../images/benutzersuche.*
   :width: 60%

   Benutzersuche

Sie können Benutzer Ihrer Website nach folgenden Kriterien suchen:

Name
  Geben Sie hier den Benutzernamen des gesuchten Benutzers
  ein. Sie können auch nach einem Teilwort suchen.

E-Mail
  Geben Sie die E-Mail-Adresse des gesuchten Benutzers ein.
  Auch hier können Sie nach einem Teil der Adresse suchen.

Vollständiger Name des Benutzers
  Geben Sie hier den Vor- oder Nachnamen
  des Benutzers ein. Sie können auch ein Teilwort oder den gesamten Namen
  eingeben.

Alle Suchkriterien werden gleichzeitig angewendet: Es werden nur Benutzer
gefunden, die alle Kriterien erfüllen. Nicht angegebene Kriterien
werden nicht beachtet.

Die Liste der Suchergebnisse enthält die Namen und Porträts der gefundenen
Benutzer. Sie sind gegebenenfalls Verweise auf die jeweiligen persönlichen
Ordner.

