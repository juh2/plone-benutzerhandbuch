.. _sec_konfiguration-textauszeichnung: 

================
Textauszeichnung
================

Das Standardformat bei Texteingaben ist HTML. Der Benutzer gibt
HTML-formatierten Text in der Regel mit Hilfe des Texteditors TinyMCE (siehe
Kapitel :ref:`sec_tinymce`) ein, sodass ihm oft nicht bewusst ist, dass Plone
HTML verarbeitet und speichert. Der Benutzer kann jedoch auch direkt
HTML-formatierten Text eingeben. Der Texteditor bietet ihm dazu eine passende
Funktion an. 

Im Bereich :guilabel:`Textauszeichnung` der Website-Konfiguration (siehe
Abbildung :ref:`fig_konfiguration-textauszeichnung`) können Sie ein anderes
Standardformat auswählen, alternative Formate zur Eingabe anbieten und
Funktionen einschalten, die aus Wikis bekannt sind. 

.. _fig_konfiguration-textauszeichnung:

.. figure::
   ../images/konfiguration-textauszeichnung.*
   :width: 100%
   :alt: Auswahl der Formate zur Texteingabe

   Einstellungen für Textauszeichnung


Teilformular »Textauszeichnung«
===============================

Im Teilformular »Textauszeichnung« legen Sie fest, in welchen Formaten Text eingegeben werden kann.  Als Formate stehen Ihnen zur Verfügung:

text/html
   HTML Auszeichnungssprache (in der Voreinstellung aktiviert)

text/plain
   Einfacher Text ohne Formatierungen

text/plain-pre
   Einfacher Text, der in ein <pre>-Tag für :term:`Preformatted Text` gepackt
   wird.

text/restructured
   :term:`Restructured Text` ist eine vereinfachte Markup-Sprache. 

text/structured
   :term:`Structured Text` ist eine vereinfachte Markup-Sprache.

text/x-python
   Für Python-Code. Eingegebener Code wird syntaktisch eingefärbt.

text/x-rst
   Zur Eingabe von :term:`Restructured Text`. 

text/x-web-intelligent
   Zur Eingabe von einfachem Text. Einrückungen und Absätze bleiben erhalten.
   Webadressen und E-Mail-Adresse werden so umgewandelt, dass sie zu
   anklickbaren Links werden.

text/x-web-markdown
   :term:`Markdown` ist eine vereinfachte Markup-Sprache. Um Markdown nutzen zu
   können, ist die Installation des Python-Moduls Markdown_ erforderlich.
  
text/x-web-textile
   :term:`Textile` ist eine vereinfachte Markup-Sprache. Um Textile nutzen zu
   können, ist die Installation des Python-Moduls Textile_ erforderlich. 


.. _Markdown: http://pypi.python.org/pypi/Markdown/2.0.3

.. _Textile: http://pypi.python.org/pypi/textile/2.1.4


Teilformular »Wiki-Verhalten«
=============================

.. _fig_konfiguration-wikiverhalten:

.. figure:: ../images/konfiguration-wikiverhalten.*
   :width: 80%
   :alt: Konfiguration des Wikiverhaltens

   Konfiguration des Wiki-Verhaltens


In diesem Teilformular (siehe Abbildung :ref:`fig_konfiguration-wikiverhalten`) können Sie für die Artikeltypen Seite, Termin und Nachricht das so genannte Wiki-Verhalten einschalten (siehe dazu Kapitel :ref:`sec_hinzufugen-mit-wiki` und :ref:`Wiki-Verweise <sec_wiki-verweise>`. 
