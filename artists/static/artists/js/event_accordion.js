let accordions = document.getElementsByClassName('accordion-button');

for (let i=0; i < accordions.length; i++) {
    accordions[i].onclick = function() {
        this.classList.toggle('open');

        let accordionContent = this.nextElementSibling;
        let accordionArrow = this.lastElementChild;

        if(accordionContent.style.display) {
            accordionContent.style.display = null;
            accordionArrow.style.display = null;
        } else {
            accordionContent.style.display = "block";
            accordionArrow.style.display = "none";
        }
    }
}