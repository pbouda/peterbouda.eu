Title: Migration einer App von Angular 1 nach Angular 2
Date: 2016-06-07 14:05
Tags: Angular, Javascript
Image: https://cloud.peterbouda.eu/index.php/s/ppol6Io9rSYC8sj/download
Imagewidth: 500

Vor zwei Wochen habe ich in Lissabon einen Vortrag über [die Migration von Angular 1 nach Angular 2](http://www.meetup.com/AngularJS-Portugal/events/230723687/) gehalten. Dazu habe ich eine kleine App portiert, die ich vor einiger Zeit schon als Fingerübung als Grundgerüst einer Angular-App in purer ES6-Syntax entwickelt habe. Das Hauptziel war eben jener Minimalismus, also ein möglichst kleiner gulp-Prozess und möglichst wenige Laufzeitabhängigkeiten. Diese App findet ihr hier:

[https://github.com/pbouda/angular-es6-boilerplate](https://github.com/pbouda/angular-es6-boilerplate)

 Die App ist ein kleiner RSS-Feedreader, der aber letztendlich gar kein RSS lädt sondern schon eine geparste JSON-Version... Also ein JSON-Feedreader :-)

Der Angular-2-Port war dann die nächste Herausforderung, weil ich weiterhin bei ES6 bleiben und nicht noch TypeScript zum Projekt hinzufügen wollte. Letztendlich blieb es dann auch bei kleineren Änderungen für die ersten Schritte hin zu Angular 2, wobei die Nachforschung teilweise doch zeitintensiv war, weil viele der Online-Tutorials eben auf TyeScript setzen.

Die ersten Schritte bei der Portierung werden am Besten im Vergleich der Branches des git-Repositories sichtbar. Hier nur ein schneller Überblick, mehr Details werde ich dann in kommenden Posts veröffentlichen.

Als Erstes habe ich einfach alle Angular-2-Abhängigkeiten zum Projekt hinzugefügt, und die App per `UpgradeAdapter` initialisiert:

[https://github.com/pbouda/angular-es6-boilerplate/compare/master...step1/addangular2](https://github.com/pbouda/angular-es6-boilerplate/compare/master...step1/addangular2)

Im Zweiten Schritt habe ich dann die Komponente `RssFeedListComponent` nach Angular 2 portiert und das entsprechende Template angepasst. Da Angular 2 bestimmte Syntax-Features kommender JavaScript- bzw. eben derzeitiger TypeScript-Versionen benutzt (wie [Dekatoren](https://medium.com/google-developers/exploring-es7-decorators-76ecb65fb841#.v0nqw1gyr)), musste ich außerdem das preset `anguar2` zu meinen babelify-Setup hinzufügen:

[https://github.com/pbouda/angular-es6-boilerplate/compare/step1/addangular2...step2/upgradecomponent](https://github.com/pbouda/angular-es6-boilerplate/compare/step1/addangular2...step2/upgradecomponent)

Dabei habe ich auch jshint erst einmal entfernt, um die Sache nicht zu verkomplizieren. Alternativ hätte ich auch die Dekoratoren u.a. für jshint ausklammern können. Ich plane aber dann in Zukunft [eslint](http://eslint.org/) zu benutzen, da es sich besser an den eigenen Stil anpassen lässt.

Als besondere Stolperstelle erwies sich die "Rückportierung" der Komponente von `component` nach `directive`. Der ansonsten sehr nützliche [Angular-2-Upgrade-Guide](https://angular.io/docs/ts/latest/guide/upgrade.html) empfiehlt zunächst, möglichst alle Direktiven in `component`-Aufrufe umzuwandeln. Jedoch lassen sich diese dann *nicht* per `upgradeAdapter.downgradeNg2Component` füttern, diese Downgrades basieren weiterhin auf Direktiven. Allein damit habe ich einige Stunden verbracht, bis ich herausgefunden haben, warum meine Komponente partout nicht funktionieren wollte...

Am Ende lief die App dann aber als Hybrid-Applikation sowohl mit Angular 1 als auch Angular 2, und wenn man die Problemstellen kennt bleiben die Anpassungsarbeiten bei einer solch kleinen App auch im Rahmen. Ich werde demnächst die Portierung einer Produktivanwendung in Angriff nehmen, dann werde ich sicher weitere Erkenntnisse gewinnen und euch hier mitteilen.
