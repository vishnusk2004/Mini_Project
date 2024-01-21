function LocomotiveScrollpage(){
    const scroll = new LocomotiveScroll({
        el: document.querySelector('.main-container'),
        smooth: true
    });
}

function loadingtitle() {
    gsap.from(".right-text h1", {
        y: 100,
        opacity:0,
        delay:0.3,
        stagger:0.5
     });
}

function loadingtitle_mini(){
    gsap.from(".nav-title h1", {
        x:-1000,
        opacity:0
    })
}

LocomotiveScrollpage()
loadingtitle()
loadingtitle_mini()
