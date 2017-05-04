Title: Angular Seed Project with Firebase
Date: 2017-03-28 16:44
Tags: Angular, JavaScript, Firebase
Image: /images/angular.png
Twitter: https://twitter.com/legocoder/status/846753559844716544

To learn more about [Firebase](https://github.com/angular/angularfire2), and
specifically how to connect an Angular application to it, I started to
implement a
[little seed project](https://github.com/pbouda/angular-firebase-seed) that
provides basic functionality to register users via e-mail/password combination
and let them login to a profile page. Registered and confirmed users can
currently change their mail address in their password in the profile. I used
the [ng-bootstrap module](https://ng-bootstrap.github.io) for the UI, which was
a great opportunity to learn some basics about Bootrap 4 also.

The usage of the angularfire2 module was a bit tricky, some functionality is
not (yet) available in the module and one has to use the JavaScript firebase
SDK, which is fortunately part of the angularfire2 module. Have a look at the
[AuthService](https://github.com/pbouda/angular-firebase-seed/blob/master/src/app/shared/auth.service.ts)
class to sees some details.

I hope that this project serves well as the basis of my next web projects, I
also plan to update it regularly whenever I learn something or when new
versions of Angular and the CLI are published. Currently it uses Angular 4.0.0
and version 1.0.0 of the CLI, so everything is shiny new :) The project is
available on Github:

[https://github.com/ng-lisbon/angular-firebase-seed](https://github.com/ng-lisbon/angular-firebase-seed)

I am happy to get any feedback, let me know what you think about the seed. Is
it useful, and what could be improved?