Title: Making an Angular UI Bootstrap accordion scrolling to top when opening
Date: 2016-05-12 11:23
Tags: Angular, JavaScript
Image: https://cloud.peterbouda.eu/index.php/s/ppol6Io9rSYC8sj/download
Imagewidth: 500

I am using the [UI Bootstrap Angular directives](https://angular-ui.github.io/bootstrap/),
specifically the accordion directive, within one of our projects at MAJ Digital.
Now I was looking for a way to scroll to the top of the accordion content,
when it is too large to fit on a screen. By default, the directive will be opened
at the middle of the content, so the user does not see the top and bottom of the
panel. A compact solution requires jQuery, for example in a directive like
the following:

```javascript
( function() {
    'use strict';

    /**
     * Makes the `uib-accordion-group` element scroll to top on the
     * `shown.bs.collapse` event. We use it in bootstrap accordions, when the
     * user opens one of the accordion items this directive will scroll the
     * item to the top of the screen.
     */
    angular.module( 'app.shared' )
    .directive( 'scrollTop', scrollTop );

    function scrollTop() {
        return {
            restrict: 'A',
            link: link
        };
    }

    function link( scope, element ) {
        scope.collapsing = false;
        var jqElement = $( element) ;
        scope.$watch( function() {
            return jqElement.find( '.panel-collapse' ).hasClass( 'collapsing' );
        }, function( status ) {
            if ( scope.collapsing && !status ) {
                if ( jqElement.hasClass( 'panel-open' ) ) {
                    $( 'html,body' ).animate({
                        scrollTop: jqElement.offset().top - 20
                    }, 500 );
                }
            }
            scope.collapsing = status;
        } );
    }

} )();
```

You can then use the `scroll-top` directive on the `uib-accordion-group`, just like this:

    <uib-accordion-group is-open="status.openPanel" scroll-top>
    ...
    </uib-accordion-group>
