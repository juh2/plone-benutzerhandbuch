.. _sec_konfiguration-erweiterungen:

================
 Zusatzprodukte
================

Im Bereich :guilabel:`Zusatzprodukte` (siehe Abbildung :ref:`fig_zusatzprodukte-installieren` können Sie Erweiterungen installieren. Dies ist sehr einfach zu bewerkstelligen.  

.. _fig_zusatzprodukte-installieren:

.. figure::
   ../images/zusatzprodukte-installieren.*
   :width: 80%
   :alt: Das Formular zur Installation eines Zusatzproduktes

   Formular zur Installation eines Zusatzproduktes

Auf der Seite finden Sie zwei Listen: die Aufstellung der installierbaren und der installierten Produkte. Wenn Sie eine Erweiterung in der Website nutzen möchten, markieren Sie es in der Liste der installierbaren Produkte und betätigen die Schaltfläche :guilabel:`Installieren`. 

Das installierte Produkte wechselt daraufhin in die Liste der installierten Produkte.

Falls die Erweiterung konfiguriert werden kann, finden Sie in der Website-Konfiguration unter der Überschrift »Konfiguration von Zusatzprodukten« einen entsprechenden Eintrag (siehe Abbildung :ref:`fig_konfiguration-zusatzprodukt`), der Sie zum Konfigurationsmenü des Zusatzproduktes führt. 

.. _fig_konfiguration-zusatzprodukt:

.. figure::
   ../images/konfiguration-zusatzprodukt.*
   :width: 80%
   :alt: Menüpunkt zur Konfiguration eines Zusatzproduktes

   Menüpunkt zur Konfiguration eines Zusatzproduktes

Im Bereich :guilabel:`Zusatzprodukte` der Website-Konfiguration tauchen nur die Erweiterungen auf, die bereits in der Instanz installiert wurden. Diese Installation erfolgt mit :term:`Buildout` und wird in Kapitel :ref:`sec_erweiterungen` beschrieben.

.. warning:: 
   Auch wenn die Installation von Erweiterungen sehr einfach vonstatten geht,
   sollten Sie nur die Zusatzprodukte installieren, die Sie wirklich benötigen
   und die von Ihnen in einer Testinstanz getestet wurden. Die Aktualisierung
   einer Plone-Instanz auf eine neuere Version kann durch Zusatzprodukte
   beträchtlich erschwert werden. Außerdem lassen sich einige Zusatzprodukte
   nicht sauber deinstallieren, das heißt sie hinterlassen teilweise
   Konfigurationen, die mühsam mit der Hand entfernt werden müssen. Nutzen Sie
   daher in jedem Fall eine Testinstanz, wenn Sie ein Zusatzprodukt
   ausprobieren möchten.  
