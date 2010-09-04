.. _sec_konfiguration-website:

=========
 Website
=========

Im Bereich :guilabel:`Website` des Konfigurationsmenüs (siehe Abbildung :ref:`fig_konfiguration-website`) können Sie eine Reihe von grundsätzlichen Einstellungen an Ihrer Website vornehmen. 

.. _fig_konfiguration-website:

.. figure::
   ../images/konfiguration-website.*
   :width: 100%
   :alt: Konfigurationsmenü »Website«

   Konfigurationsmenü »Website«

Titel der Website
   Beim Erzeugen der Plone-Site (siehe Kapitel :ref:`sec_erzeugung-plone-site`)
   wurde ein Titel vergeben. Er erscheint an dieser Stelle und kann jederzeit
   geändert werden. Der Titel der Website taucht in der Kopfzeile der Browser
   auf und wird von Suchmaschinen ausgewertet.

Beschreibung der Website
   Bei der Erzeugung der Plone-Site konnte eine Beschreibung der Website
   eingegeben werden. An dieser Stelle kann die Beschreibung geändert werden. 

Zeige Kurznamen der Artikel?
   An dieser Stelle können Sie die Anzeige der Kurznamen in der
   Bearbeitungsansicht grundsätzlich erlauben. Der Benutzer kann dann in seinen
   persönlichen Einstellungen die Option nutzen (siehe dazu Kapitel
   :ref:`sec_persoenliche-einstellungen`). 

Sofort-Bearbeitung einschalten
   Die Sofort-Bearbeitung wird in Kapitel :ref:`sec_bearbeiten` beschrieben.
   Die Möglichkeit kann hier ein- oder ausgeschaltet werden. 

Link-Integritätsprüfung aktivieren
   Die Link-Integritätsprüfung wird in Kapitel
   :ref:`sec_kopieren-verschieben-loeschen` beschrieben. Die Funktion kann hier
   ein- oder ausgeschaltet werden. 

Externen Editor aktivieren
   Es ist möglich, die Artikel in Plone mit Hilfe eines Texteditors auf dem
   lokalen Rechner zu bearbeiten. Hierfür muss der lokale Rechner entsprechend
   konfiguriert werden. Auf Seite der Website wird an dieser Stelle die
   Möglichkeit gewährt, einen solchen Editor zu benutzen. 

sitemap.xml.gz verfügbar machen
   Plone kann eine Übersicht über die Inhalte der Website nach dem Standard von
   sitemaps.org_ erstellen und ständig aktuell halten. Suchmaschinen nutzen
   diese Datei, um über Veränderungen zeitnah informiert zu sein. Bei Google
   kann man die Sitemap in den `Webmaster Tools`_  anmelden.  

Javascript für Web-Statistik-Unterstützung
   Wenn Sie beispielsweise `Google Analytics`_ mit Plone nutzen möchten, können
   Sie den  von Google zur Verfügung gestellten Javascript-Code in dieses Feld
   einfügen. Er wird am Ende jeder Webseite eingefügt. Selbstverständlich
   können Sie hier auch den Code für andere Statistik-Dienste einfügen.
   Beachten Sie, dass der Einsatz von Google Analytics in Deutschland
   umstritten ist. [#]_ 

Bearbeitungssperre für Bearbeitungen über die Plone-Bedienoberfläche einschalten
   Diese per Voreinstellung aktivierte Option verhindert, dass zwei Benutzer
   einen Artikel gleichzeitig bearbeiten können.

.. _sitemaps.org: http://sitemaps.org/

.. _`Webmaster Tools`: https://www.google.com/webmasters/tools/

.. _`Google Analytics`: http://www.google.com/intl/de/analytics/

.. [#] Vgl. hierzu zum Beispiel: http://de.wikipedia.org/wiki/Google_Analytics
