.. _sec_konfiguration-erweiterungen:

===============
 Erweiterungen
===============

Im Bereich :guilabel:`Erweiterungen` (siehe Abbildung
:ref:`fig_zusatzprodukte-installieren` können Sie Software-Pakete
installieren, mit denen die Funktionen von Plone erweitert
werden. 

.. _fig_zusatzprodukte-installieren:

.. figure::
   ../images/zusatzprodukte-installieren.*
   :width: 80%
   :alt: Das Formular zur Installation einer Erweiterung

   Formular zur Aktivierung einer Erweiterung

Auf der Seite finden Sie zwei Listen: die Aufstellung der verfügbaren und der
aktivierten Erweiterungen. Wenn Sie eine Erweiterung in der Website nutzen
möchten, markieren Sie sie in der Liste der verfügbaren Erweiterungen und
betätigen die Schaltfläche :guilabel:`Aktivieren`.  Die Erweiterung 
wird nun in der Liste der aktivierten Erweiterungen aufgeführt.

Falls die Erweiterung konfiguriert werden kann, finden Sie in der
Website-Konfiguration unter der Überschrift »Konfiguration von Erweiterungen«
einen entsprechenden Eintrag (siehe Abbildung
:ref:`fig_konfiguration-zusatzprodukt`), der Sie zum Konfigurationsmenü der
Erweiterung führt. 

.. _fig_konfiguration-zusatzprodukt:

.. figure::
   ../images/konfiguration-zusatzprodukt.*
   :width: 40%
   :alt: Menüpunkt zur Konfiguration einer Erweiterung

   Menüpunkt zur Konfiguration einer Erweiterung

Im Bereich :guilabel:`Erweiterungen` der Website-Konfiguration tauchen nur die
Erweiterungen auf, die bereits in der Instanz installiert wurden. Diese
Installation erfolgt mit :term:`Buildout` und wird in Kapitel
:ref:`sec_erweiterungen` beschrieben.

.. warning:: 
   Auch wenn die Installation von Erweiterungen sehr einfach vonstatten geht,
   sollten Sie nur die Erweiterungen installieren, die Sie wirklich benötigen
   und die von Ihnen in einer Testinstanz getestet wurden. Die Aktualisierung
   einer Plone-Instanz auf eine neuere Version kann durch Erweiterungen
   beträchtlich erschwert werden.
