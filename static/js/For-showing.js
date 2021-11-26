const btn = document.getElementById("77");
const bio = document.getElementById("76");


function isOverflown() {
    bool = bio.scrollHeight > bio.clientHeight || bio.scrollWidth > bio.clientWidth;
    if (bool) {
        btn.classList.add("showing");
    }
}

function handleClick(event) {
    bio.classList.remove("takasa2");
    bio.classList.remove("overflow-hidden");
    bio.classList.add("takasa-auto");
}

function loadFunction() {
    isOverflown();
    btn.addEventListener("click", handleClick);
}
function init() {
    loadFunction();
}

init();