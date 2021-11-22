const reply_comment_box = document.querySelector(".js-reply");
const reply_btn = document.querySelector(".js-btn");
const SHOWING = "showing";


function handleClick(event) {
    reply_comment_box.classList.add(SHOWING);
}

function loadReply() {
    console.log("hello");
    reply_btn.addEventListener("click", handleClick);
}

function init() {
    loadReply();
}

init();