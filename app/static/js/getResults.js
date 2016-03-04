var $ = require('jquery');
var EVENTS = require('./events');
var API = require('./api');

function getResultsAndUpdate () {
    var bgLight = $('.layout__bg');

    var counters = {
        light: {
            el: $('#counter-light'),
            result: 0
        },
        dark: {
            el: $('#counter-dark'),
            result: 0
        }
    };


    $.ajax({
      method: "GET",
      url: API.get
    })
    .done(function(response) {
        if (response) {

            // cycle through the sides in response
            for (var side in response) {
                var events = response[side];
                var i = events.length;

                // set result values for counters
                while (i--) {
                    counters[side].result += events[i].rate || EVENTS[events[i].event];
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

module.exports = getResultsAndUpdate;