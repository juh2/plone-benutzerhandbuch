=========
 Adapter
=========

Adapter in einem Formular-Ordner sind dafür verantwortlich, die eingegebenen Formulardaten zu verarbeiten. 

.. _sec_mail-adapter:

Mail-Adapter
============ 

Der Mail-Adapter wird beim Anlegen eines Formular-Ordners automatisch
erzeugt. Er hat die Aufgabe, die eingegebenen Daten per E-Mail zu
versenden. Jedesmal wenn ein Benutzer das Formular absendet, werden
die eingegebenen Daten per E-Mail verschickt. 

Der Mail-Adapter kann sehr flexibel konfiguriert werden. Es können
mehrere Mail-Adapter in einem Formular-Ordner genutzt werden. Das
Formular zum Hinzufügen oder Bearbeiten eines Mail-Adapters ist in
mehrere Teilformulare gegliedert.

* Standard (siehe Abbildung :ref:`fig_mail-adapter-hinzufuegen`)
* Adressing (siehe Abbildung :ref:`fig_mailer-bearbeiten-adressing`)
* Message (siehe Abbildung :ref:`fig_mailer-bearbeiten-message`)
* Template (siehe Abbildung :ref:`fig_mailer-bearbeiten-template`)
* Encryption (siehe Abbildiung :ref:`fig_mailer-bearbeiten-encryption`)
* Overrides (selten benötigte Funktionen, deren Erklärung den Rahmen dieser
  Darstellung sprengen würde)

Teilformular »Standard«
-----------------------

.. _fig_mail-adapter-hinzufuegen:

.. figure:: 
   ./images/mail-adapter-hinzufuegen.*
   :width: 80%
   :alt: Formular zum Hinzufügen eines Mail-Adapters

   Formular zum Hinzufügen eines Mail-Adapters

Im Teilformular »Standard« können Sie den Titel des Mail-Adapters
sowie Namen und E-Mail-Adresse des Empfängers eingeben. An
die hier angegebene E-Mail-Adresse werden die E-Mails versendet.

Teilformular Adressing
----------------------

.. _fig_mailer-bearbeiten-adressing:

.. figure:: 
   ./images/mailer-bearbeiten-adressing.*
   :width: 80%
   :alt: Teilformular »Adressing«

   Teilformular »Adressing«

Häufig ist es nicht damit getan, die Formulardaten an einen Empfänger
zu versenden. Auf dem Teilformular »Adressing« können weitere Optionen
eingestellt werden (siehe Abbildung
:ref:`fig_mailer-bearbeiten-adressing`).

Empfänger herauslesen aus 
   Wenn Sie dem Benutzer, der das Formular ausfüllt, die Möglichkeit
   geben wollen, den Empfänger der E-Mail selbst zu bestimmen, können
   Sie im Formular-Ordner ein Auswahlfeld (siehe
   :ref:`sec_auswahl-feld` oder
   :ref:`sec_mehrfach-auswahl-feld`) mit den möglichen
   Empfängern anlegen und an dieser Stelle festlegen, dass die
   Empfängeradresse aus diesem Formularfeld ausgelesen werden
   soll. Die hier getroffene Angabe überschreibt die Empfängeradresse,
   die im Teilformular »Standard« eingegeben wurde. Beachten Sie, dass
   hier auch Formularfelder zur Auswahl aufgelistet sind, die nicht
   für diesen Zweck geeignet sind.

Kopie-Empfänger und Blindkopie-Empfänger
   In diesen beiden Feldern können Sie beliebig viele weitere
   E-Mail-Adressen eingetragen, an die die Formulardaten ebenfalls
   gesendet werden sollen.

Antwortadresse herauslesen aus
   Sie können dem Benutzer, der das Formular ausgefüllt hat, die
   Möglichkeit geben, eine Antwortadresse für Rückfragen
   einzutragen. Der Benutzer gibt die Adresse in einem Text-Feld
   (siehe :ref:`sec_text-feld`) ein, wo sie validiert werden
   kann. An dieser Stelle fügen Sie die Antwortadresse in die E-Mail
   ein, sodass der Empfänger mit dem Absender leichter Kontakt
   aufnehmen kann. Beachten Sie, dass
   hier auch Formularfelder zur Auswahl aufgelistet sind, die nicht
   für diesen Zweck geeignet sind.
    

Teilformular »Message«
----------------------

Spätestens dann, wenn ein Empfänger die Daten verschiedener Formulare
zugesendet bekommt, ist es sinnvoll, dem Empfänger Informationen
zukommen zu lassen, die ihm helfen, die Daten einzusortieren. Solche
Informationen können Sie im Teilformular »Message« eingeben (siehe
Abbildung :ref:`fig_mailer-bearbeiten-message`).

.. _fig_mailer-bearbeiten-message:

.. figure:: 
   ./images/mailer-bearbeiten-message.*
   :width: 70%
   :alt: Teilformular »Message«

   Teilformular »Message«

Betreff
   Hier können Sie die Betreff-Zeile der E-Mail festlegen. Wählen Sie
   ein aussagekräftiges Betreff, damit der Empfänger gleich sieht,
   worum es geht.

Betreff herauslesen aus
   Wenn Sie dem Benutzer die Möglichkeit geben wollen, die
   Betreff-Zeile selbst zu bestimmen, so können Sie hier das
   Formularfeld bestimmen, aus dem das Betreff ausgelesen werden
   soll. Wenn Sie dazu ein Auswahlfeld benutzen, können Sie
   entsprechende Betreffs vorgeben.

Körper (vorangestellt)
   In dieses Feld können Sie einen erklärenden Text schreiben. Er wird
   der Auflistung der Daten vorangestellt.

Körper (angehängt)
   Der Text, den Sie in dieses Feld eingeben, wird den gesendeten
   Formulardaten angehängt. Denkbar wären hier Verarbeitungshinweise
   für den Empfänger.

Körper (Signatur)
   In dieses Feld können Sie eine Signatur eintragen, die durch eine
   gestrichelte Linie von der eigentlichen E-Mail abgetrennt wird.

Alle Felder einbeziehen
   Falls Sie diese Option auswählen, werden die Daten aus allen Felder
   des Formulars in der E-Mail aufgeführt. Falls Sie dies nicht
   wollen, wählen Sie diese Option nicht aus. 

Antworten Zeigen
   Hier können Sie die Formularfelder auswählen, deren Daten per
   E-Mail verschickt werden sollen.

Leere Felder anzeigen
   Falls einige Formularfelder nicht ausgefüllt werden müssen und
   daher leer bleiben können, stellt sich die Frage, ob diese Felder
   überhaupt in die E-Mail übernommen werden sollen. Je nachdem wie
   die Daten ausgewertet werden, kann es sinnvoll sein, auch die Namen der
   nicht ausgefüllten Formularfelder aufzulisten. 

Teilformular »Template«
-----------------------

Im Teilformular »Template« (Abbildung
:ref:`fig_mailer-bearbeiten-template`) können Sie unter anderem
bestimmen, ob die E-Mail als HTML-Nachricht oder reine Textnachricht
versendet werden soll.

.. _fig_mailer-bearbeiten-template:

.. figure:: 
   ./images/mailer-bearbeiten-template.*
   :width: 80%
   :alt: Teilformular »Template«

   Teilformular »Template«

Mail-Körper-Template
   Sie können das Zope-Template, aus dem der Text der E-Mail erstellt
   wird, komplett ändern.

Typ des Mail-Körpers
   Hier bestimmen Sie, ob die E-Mail als HTML- oder reine
   Text-Nachricht formatiert werden soll.

HTTP-Header
   Sie können auswählen, welche HTTP-Header in die E-Mail
   eingeschlossen werden sollen. Es gibt eine sinnvolle
   Voreinstellung.

Zusätzliche Header
   Sie können weitere Header im RFC822 kompatiblem Format in die
   E-Mail einfügen. Dies kann zum Beispiel sinnvoll sein, wenn die E-Mails
   maschinell sortiert werden sollen.


Teilformular »Encryption«
-------------------------

Formulardaten enthalten häufig persönliche Daten, die geschützt werden
müssen. Daher bietet es sich an, die E-Mail verschlüsselt zu
versenden. Dazu benutzt Plone das Open-Source-Programm `GNU Privacy
Guard`_ (GnuPG). Es muss auf dem Server, auf dem Plone läuft,
installiert sein. Das Teilformular »Encryption« (siehe Abbildung
:ref:`fig_mailer-bearbeiten-encryption`) ist nur sichtbar, wenn Plone das
ausführbare Programm :program:`gpg` gefunden hat. 

.. _`GNU Privacy Guard`: http://www.gnupg.org/

.. _fig_mailer-bearbeiten-encryption:

.. figure:: 
   ./images/mailer-bearbeiten-encryption.*
   :width: 80%
   :alt: Teilformular »Encryption«

   Teilformular »Encryption«

Sie können in das Feld die ID eines :term:`öffentlichen Schlüssels
<öffentlicher Schlüssel>` oder die dazu gehörige E-Mail-Adresse
eingeben. Der öffentliche Schlüssel muss sich im :term:`Keyring` des
Benutzer befinden, unter dessen Benutzerkennung der Zope-Server läuft,
mit dem Plone betrieben wird. 

Anzeige aller Einstellungen
---------------------------

Die Anzeige des Mail-Adapters zeigt eine Übersicht über alle
vorgenommenen Einstellungen (siehe Abbildung
:ref:`fig_mailer-anzeigen`). 

.. _fig_mailer-anzeigen:

.. figure:: 
   ./images/mailer-anzeigen.*
   :width: 80%
   :alt: Übersicht über alle Einstellungen des Mail-Adapters

   Anzeige der Einstellungen des Mail-Adapters

.. _sec_daten-speicher-adapter:

Daten-Speicher-Adapter
====================== 

Die eingegebenen Formulardaten können mit Hilfe des
Daten-Speicher-Adapters in Plone gespeichert werden. 

.. _fig_daten-speicher-hinzufuegen:

.. figure::
   ./images/datenspeicher-hinzufuegen.*
   :width: 80%
   :alt: Formular zum Hinzufügen eines Datenspeichers

   Formular zum Hinzufügen eines Datenspeichers

Beim Hinzufügen oder Bearbeiten des Daten-Speicher-Adapters (siehe
Abbildung :ref:`fig_daten-speicher-hinzufuegen`) können
folgende Einstellungen vorgenommen werden:

Titel
   Name des Daten-Speicher-Adapters

Zusätzliche Daten
   Neben den reinen Formulardaten können weitere Daten gespeichert
   werden, die zur Identifizierung des Benutzers, der
   das Formular ausgefüllt hat, dienen können

Download-Format
   Sie können die Daten in zwei Formaten herunterladen. Die einzelnen
   Datenwerte sind entweder mit Komma oder mit Tabulator
   getrennt. Abbildung :ref:`fig_daten-speicher-download` zeigt mit
   Komma getrennte Werte.

.. _fig_daten-speicher-download:

.. figure::
   ./images/datenspeicher-download.*
   :width: 80%
   :alt: Download der Daten als CSV-Datei

   Download der CSV-Datei

Spaltennamen einbeziehen
   Zur Verbesserung der Übersicht können Sie in der ersten Zeile die
   Namen der Spalten einbeziehen. 

Das Herunterladen der Daten erfolgt über die Anzeige des Adapter
(siehe Abbildung :ref:`fig_daten-speicher-anzeige`).

.. _fig_daten-speicher-anzeige:

.. figure::
   ./images/datenspeicher-anzeige.*
   :width: 80%
   :alt: Anzeige des Datenspeichers

   Anzeige des Datenspeichers

Klicken Sie auf den Link :guilabel:`Hier klicken, um Ihre Eingaben zu
speichern`, um die gespeicherten Daten herunter zu laden. 

Um die von dem Adapter gespeicherten Daten zu löschen, betätigen Sie die Schaltfläche
:guilabel:`Die gespeicherten Eingaben löschen`. 

.. _sec_adapter-fuer-eigenes-skript:

Adapter für eigenes Skript
========================== 

.. _fig_adapter-eigenes-skript:

.. figure::
   ./images/adapter-eigenes-skript.*
   :width: 80%
   :alt: Adapter für eigenes Skript

   Adapter für eigenes Skript

Sie können das abgesendete Formular auch mit einem eigenen Pythonskript
weiterverarbeiten. Den Code können Sie dabei bequem im Browser eingeben (siehe
Abbildung :ref:`fig_adapter-eigenes-skript`). 
