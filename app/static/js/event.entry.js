var $ = require('jquery');
var EVENTS = require('./events');
var API = require('./api');
var getResults = require('./getResults');

$(document).ready(function() {
    var event = location.href.substr(location.href.lastIndexOf('/') + 1);

    if (typeof EVENTS[event]) {
        initEvent(event);
    } else {
        console.error('Event is not defined', event);
    }

    getResults();
});

function initEvent (event) {
    var forceButtons = $('.force__button');
    var forceRate = $('.force__rate-number');
    var rateInput = $('.settings__rate');

    if (event == 'force') {
        rateInput.show();
    }

    forceButtons.on('click', function(e) {
        var button = $(this);
        var side = button.attr('data-side');
        var rateBlock = forceRate.filter("[data-side='" + side + "']");
        var customRate = rateInput.val();
        var value = customRate || EVENTS[event];

        button.hide();
        rateBlock.show().html(value);

        $.ajax({
          type: "GET",
          url: API.set,
          data: "side=" + side + "&eventName=" + event + (customRate ? "&rate=" + customRate : ""),
          success: function (message) {
              setTimeout(function() {
                  button.show();
                  rateBlock.hide();
              }, 2000);
          }
        });
    });
}