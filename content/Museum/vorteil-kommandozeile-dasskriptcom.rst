Vorteil Kommandozeile
#####################
:date: 2010-06-04 10:19
:slug: vorteil-kommandozeile

Das N900 wird ja allgemein (noch?) nicht so sehr als **der** iPhone-
oder Android-Konkurrent wahrgenommen. Als halbwegs interessierter
Linux-Anwender oder gar -Entwickler ist aber schnell festzustellen, wo
ein offenes Betriebssystem einen Vorteil hat: es gibt die Kommandozeile,
also eine Shell :-). Zwei schöne Beispiel wurden dazu in den letzten
Wochen veröffentlicht, also zeigt die folgenden Sachen mal euren Kumpels
mit den Apfel-Handys. Sie werden zwar nicht kapieren worum es geht, aber
Hauptsache ihr selbst wisst den Vorteil auf eurer Seite.

Beim ersten Beispiel handelt es sich `um eine kleines Shell-Skript zum
Energiesparen`_. Dazu schaltet es einfach die Internetverbindung aus,
setzt das Netz auf 2G und schaltet den automatischen E-Mail-Abruf aus.
Genauso schnell lässts sich alles auch wieder aktiveren, drei bzw. vier
Zeilen Code reichen aus. Und weil es so elegant ist, hier das ganze
Skript::

   #!/bin/sh

   # Simple shell script created in order to preserve battery power in your N900

   # Actions taken:
   # 1. Sets internet connection mode 'Always ask' /(available under Settings -> Internet connections -> Connect automatically).
   # 2. Disconnects current internet connection.
   # 3. Switches cellular radio into 2G-only mode.
   # 4. Disables automatic email send&receive in Modest email client.

   # Created by Dawid Lorenz aka evad, http://adl.pl

   if [ "$1" == "off" ]
    then
     echo "Restoring power suckers..."
     gconftool-2 --set --type list --list-type string /system/osso/connectivity/network_type/auto_connect [*]
     gconftool-2 --set --type bool /apps/modest/auto_update true
     run-standalone.sh dbus-send --system --type=method_call --dest=com.nokia.phone.net /com/nokia/phone/net Phone.Net.set_selected_radio_access_technology byte:0
    else
     echo "Going into power saving mode..."
     gconftool-2 --set --type list --list-type string /system/osso/connectivity/network_type/auto_connect []
     gconftool-2 --set --type bool /apps/modest/auto_update false
     run-standalone.sh dbus-send --system --dest=com.nokia.icd /com/nokia/icd_ui com.nokia.icd_ui.disconnect boolean:true
     run-standalone.sh dbus-send --system --type=method_call --dest=com.nokia.phone.net /com/nokia/phone/net Phone.Net.set_selected_radio_access_technology byte:1
   fi

Einfach als "power-saver.sh" auf dem N900 ablegen, und dann per
"power-saver.sh" den Energiesparmodus aktivieren bzw. per
"power-saver.sh off" wieder deaktivieren.

Das zweite Beispiel ist wohl etwas allgemeinverständlicher: `Videos per
HTTP oder SSH vom N900 auf den Desktop streamen`_. Benutzt werden nur
auf dem Gerät vorinstallierte Programme. Dekodiert wird dabei alles auf
dem Desktop, so dass bei ausreichend potenter Netzverbindung sogar
HD-Videos gestreamt werden können. Da lacht das Linux-Anwender-Herz und
der Apfelfan schaut in die Röhre, wenigstens kurzzeitig.

.. _um eine kleines Shell-Skript zum Energiesparen: http://blog.adl.pl/saving-n900-battery-power-with-simple-shell-script/495
.. _Videos per HTTP oder SSH vom N900 auf den Desktop streamen: http://thpmaemo.blogspot.com/2010/06/streaming-video-to-big-screen.html
