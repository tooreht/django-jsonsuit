;(function(window, document) {
    function setup() {
        const widgets = document.querySelectorAll('*[class="jsonsuit editable"][data-jsonsuit]');
        for (let i = 0; i < widgets.length; i++) {
            const name = widgets[i].dataset.jsonsuit,
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
            button.code = code;
            button.addEventListener("click", toggle, false);
        }
    }

    function toggle(e) {
        e.preventDefault();
        if (e.target.suit.classList.contains('hidden')) {
            e.target.innerHTML = e.target.dataset.raw;
            try {
                const prettyJSON = JSON.stringify(JSON.parse(e.target.textarea.value), null, 2);
                const prettyHTML = Prism.highlight(prettyJSON, Prism.languages.json);
                e.target.textarea.value = prettyJSON;
                e.target.code.innerHTML = prettyHTML;
            } catch (error) {
                console.error(error);
            }
        } else {
            e.target.innerHTML = e.target.dataset.suit;
        }
        e.target.textarea.classList.toggle('hidden');
        e.target.suit.classList.toggle('hidden');
    }

    document.addEventListener('DOMContentLoaded', _e => setup());
}(window, document));
