;(function(window, document) {
    function setup() {
        var widgets = document.querySelectorAll('*[class="jsonsuit"][data-jsonsuit]');

        for (var i = 0; i < widgets.length; i++) {
            var name = widgets[i].dataset.jsonsuit,
                textarea = document.getElementById('id_' + name),
                prettyJSON = JSON.stringify(JSON.parse(textarea.value), null, 2),
                prettyHTML = Prism.highlight(prettyJSON, Prism.languages.json),
                suit = widgets[i].querySelector('.suit'),
                code = suit.querySelector('code'),
                button = widgets[i].querySelector('button.toggle');

            textarea.value = prettyJSON;
            code.innerHTML = prettyHTML;
            button.textarea = textarea;
            button.suit = suit;
            button.addEventListener("click", toggle, false);
        }
    }

    function toggle(e) {
        e.preventDefault();
        if (e.target.suit.classList.contains('hidden')) {
            e.target.innerHTML = e.target.dataset.raw;
        } else {
            e.target.innerHTML = e.target.dataset.suit;
        }
        e.target.textarea.classList.toggle('hidden');
        e.target.suit.classList.toggle('hidden');
    }

    function DOMReady(a,b,c){b=document,c='addEventListener';b[c]?b[c]('DOMContentLoaded',a):window.attachEvent('onload',a)}
    DOMReady(setup);
}(window, document));
