Title: Angular Seed Project with LoopBack
Date: 2017-05-04 15:44
Tags: Angular, JavaScript, LoopBack
Image: /images/planstack.svg
Twitter: https://twitter.com/legocoder/status/860146224397262848

Around a month ago I published a post about
[my Angular Seed Project with Firebase]({filename}20170328-angular-seed-project-with-firebase.md).
Since then I tried to promote this seed to a couple of friends in Germany, who
were not really happy to host their data on Firebase. So I started to refactor
the back-end to [LoopBack](http://loopback.io/), which is an awesome JavaScript
framework for rapid back-end development based on
[Express](http://expressjs.com). I used LoopBack for my latest major consulting
project and think that the development experience is awesome. There is a great
[client SDK for Angular](http://loopback.io/doc/en/lb3/AngularJS-JavaScript-SDK.html),
which makes connecting an Angular front-end super easy. Both AngularJS and
Angular are supported, so I could just attach my Angular front-end and replace
the Firebase `AuthService` with a LoopBack version. It even supports
Firebase-like real-time communication via the
[FireLoop platform](http://fireloop.io/). 

Meanwhile I also decided to replace MongoDB with a PostgreSQL database. I know
that document data stores are nowadays quite popular, but the explicit schemas
of relational databases have advantages in the long run, in my opinion. They
make sure that you have to think about migrations whenever you change the data
and forces some kind of versioning of data and API, which reduces the risks of
complex errors when your app grows.
[This great blog post](https://blog.scottnonnenberg.com/hard-won-lessons-five-years-with-node-js/#data-apis-and-versions)
of Scott Nonnenberg was quite inspiring and it gives a good overview of best
practices for future-proof JavaScript back-ends.

Finally, I am now running on a stack of PostgreSQL + LoopBack + Angular +
Node.js, which I call the "PLAN stack" 😃.
[Though I am not the first one](https://radialspark.github.io/PLAN-App-Accelerator/architecture.html)
who came up with the idea. I still think the new seed project for my PLAN stack
is a good starting point for modern web applications:

[https://github.com/ng-lisbon/angular-loopback-seed](https://github.com/ng-lisbon/angular-loopback-seed)

Check out [our trainings at ng-lisbon](http://www.ng-lisbon.com) if
you want to learn more about Angular and the PLAN stack!

I am happy to get any feedback, let me know what you think about the seed. Is
it useful, and what could be improved?