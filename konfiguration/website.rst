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

Dublin Core Metadaten einbinden
   Die Metadaten von Plone können nicht nur innerhalb des Systems verwendet
   werden. Da sie dem Dublin-Core-Schema entsprechen, können Sie auch als
   :term:`Metatags <Metatag>` in den HTML-Code eingebunden werden, sodass
   externe Systeme darauf zugreifen können. Markieren Sie diese Option, wenn
   Sie Dublin-Core-Metadaten in den HTML-Code Ihrer Seiten einbinden möchten.
   Mehr über die Dublin-Core-Elemente erfahren Sie in Kapitel
   :ref:`sec_exkurs-metadaten`. 

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


.. _sitemaps.org: http://sitemaps.org/

.. _`Webmaster Tools`: https://www.google.com/webmasters/tools/

.. _`Google Analytics`: http://www.google.com/intl/de/analytics/

.. [#] Vgl. hierzu zum Beispiel: http://de.wikipedia.org/wiki/Google_Analytics
