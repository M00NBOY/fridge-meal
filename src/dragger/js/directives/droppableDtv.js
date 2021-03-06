class droppableDtv{
    constructor(){
        this.restrict = 'A';
    }
    link(scope, elem, attrs){
        const el = elem[0];

        elem.on(
            'drop',
            e => {
                const item = document.querySelector('#' + e.dataTransfer.getData('text'));

                el.classList.remove('dropping');

                if (e.stopPropagation) {
                    e.stopPropagation();
                };

                scope.vm.match(item, el);

                return false;
            }
        );

        elem.on(
            'dragover',
            e => {
                e.dataTransfer.dropEffect = 'move';
                e.preventDefault();

                el.classList.add('dropping');

                return false;
            }
        );

        elem.on(
            'dragenter',
            e => {
                el.classList.add('dropping');
                return false;
            }
        );

        elem.on(
            'dragleave',
            e => {
                el.classList.remove('dropping');

                return false;
            }
        );
    }
}

export default droppableDtv;
