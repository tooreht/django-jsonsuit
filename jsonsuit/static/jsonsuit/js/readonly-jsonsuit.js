;(function(window, document) {
    function setup() {
        const widgets = document.querySelectorAll('*[class="jsonsuit readonly"][data-jsonsuit]');
        for (let i = 0; i < widgets.length; i++) {
            let code = widgets[i].querySelector('.suit code'),
                prettyJSON = JSON.stringify(JSON.parse(code.dataset.raw), null, 2),
                prettyHTML = Prism.highlight(prettyJSON, Prism.languages.json);

            code.innerHTML = prettyHTML;
        }
    }

    function DOMReady(a,b,c){b=document,c='addEventListener';b[c]?b[c]('DOMContentLoaded',a):window.attachEvent('onload',a)}
    DOMReady(setup);
}(window, document));
