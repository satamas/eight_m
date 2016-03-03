var $ = require('jquery');

var EVENTS = {
    fight: 1,
    light: 10,
    lego: 5,
    force: 5
};


$(document).ready(function() {
    getResultsAndUpdate();
});


function getResultsAndUpdate () {
    var bgLight = $('.layout__bg');

    var counters = {
        light: {
            el: $('#light-counter'),
            result: 0
        },
        dark: {
            el: $('#dark-counter'),
            result: 0
        }
    };


    $.ajax({
      method: "GET",
      url: "/stats"
    })
    .done(function(response) {
        if (response) {

            // cycle through the sides in response
            for (var side in response) {
                var events = response[side];
                var i = events.length;

                // set result values for counters
                while (i--) {
                    counters[side].result += EVENTS[events[i]];
                }

                // rendering results to counters
                counters[side].el.html(counters[side].result);
            }
        }

        // update light background position
        var percentage = (counters.dark.result - counters.light.result)*10;
        bgLight.css({transform: 'translateX(' + percentage + 'px)'});

        setTimeout(getResultsAndUpdate, 1000);
    })
    .fail(function(message) {
        console.error(message);
    });
}

