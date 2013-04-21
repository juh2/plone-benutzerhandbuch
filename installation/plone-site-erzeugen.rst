.. _sec_erzeugung-plone-site:

Erzeugung einer Plone-Site
==========================

Wenn Sie nach der Installation von Plone die Adresse http://localhost:8080 in
Ihren Browser eingeben, erscheint eine Seite, die Sie darüber informiert, dass
Plone läuft, aber noch keine Plone-Website erzeugt wurde (siehe Abbildung
:ref:`fig_plone-site-noch-nicht-erzeugt`)

.. _fig_plone-site-noch-nicht-erzeugt:

.. figure::
   ../images/plone-site-noch-nicht-erzeugt.*
   :width: 100%

   Der Startbildschirm nach erfolgreicher Installation

Vom diesem Startbildschirm aus haben Sie die Möglichkeit, ein Formular
aufzurufen, mit dem Sie eine Plone-Site anlegen können (siehe Abbildung
:ref:`fig_erzeuge-eine-plone-site`). Klicken Sie dazu auf
:menuselection:`Erzeuge eine Plone-Site`. Darüber hinaus können Sie das
:term:`Zope-Management-Interface` oder die Homepage des Plone-Projekts
http://plone.org aufrufen.

.. todo:: Screenshot gelegentlich erneuern

.. _fig_erzeuge-eine-plone-site:

.. figure::
   ../images/erzeuge-eine-plone-site.*
   :width: 100%

   Das Formular zum Anlegen einer Plone-Site

Bei der Erzeugung einer Plone-Site haben Sie folgende Optionen:

Pfadkennung
    Das Formularfeld ist vorausgefüllt mit dem Begriff Plone. Es handelt sich
    hierbei um die ID der Website, die später zu einem Teil der URL wird. 

Titel
    Der Titel ist der Name der Website. Er wird in der Titelzeile der Browser
    angezeigt. 

Sprache
    Mit dem Auswahlmenü legen Sie fest, in welcher Sprache die
    Benutzeroberfläche von Plone angezeigt werden soll. Voreingestellt ist
    ›Deutsch‹.

Erweiterungen
    In diesem Feld können Sie die verfügbaren Erweiterungen installieren. Hier
    tauchen diejenigen Erweiterungen auf, die Sie installiert haben. Wie Sie
    Erweiterungen installieren, erfahren Sie in Kapitel
    :ref:`sec_konfiguration-erweiterungen`.

Klicken Sie abschließend auf :menuselection:`Erzeuge Plone-Site`, um die
Plone-Site in der gewünschten Konfiguration zu erzeugen. 

Abschließend können Sie Ihre neue Plone-Site unter der Adresse
http://localhost:8080/Plone aufrufen, falls Sie im Formular die ID ›Plone‹
vergeben haben. Ihre Plone-Site sieht aus, wie in Abbildung
:ref:`fig_neue-plone-site` zu sehen.

.. _fig_neue-plone-site:

.. figure::
   ../images/neue-plone-site.*
   :width: 80 %

   Eine neu erzeugte Plone-Site

Lesen Sie sich den Text auf der Willkommens-Seite aufmerksam durch. Er enthält
zahlreiche Verweise auf weitere Informationsquellen.
