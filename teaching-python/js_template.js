javascript:
function translate() {
  progress = $(".lesson__show-checkpoints").text();
  current = parseInt(progress.split("/")[0]);
  $(".block-label--light-blue").text("說明");
  content = $(".article__inner")[1];
  instructions = $(".article__inner")[3];
  if(current == 1) {
    $(content).replaceWith("");
    $(instructions).replaceWith("");
  }
  if(current == 2) {
    $(content).replaceWith("");
    $(instructions).replaceWith("");    
  }
  if(current == 3) {
    $(content).replaceWith("");
    $(instructions).replaceWith("");
  }
  if(current == 4) {
    $(content).replaceWith("");
    $(instructions).replaceWith("");
  }
  if(current == 5) {
    $(content).replaceWith("");
    $(instructions).replaceWith("");
  }
  if(current == 6) {
    $(content).replaceWith("");
    $(instructions).replaceWith("");
  }
  if(current == 7) {
    $(content).replaceWith("");
    $(instructions).replaceWith("");
  }
  if(current == 8) {
    $(content).replaceWith("");
    $(instructions).replaceWith("");
  }
  if(current == 9) {
    $(content).replaceWith("");
    $(instructions).replaceWith("");
  }
  if(current == 10) {
    $(content).replaceWith("");
    $(instructions).replaceWith("");
  }
  if(current == 11) {
    $(content).replaceWith("");
    $(instructions).replaceWith("");
  }
  if(current == 12) {
    $(content).replaceWith("");
    $(instructions).replaceWith("");
  }
  if(current == 13) {
    $(content).replaceWith("");
    $(instructions).replaceWith("");
  }
  if(current == 14) {
    $(content).replaceWith("");
    $(instructions).replaceWith("");
  }
  if(current == 15) {
    $(content).replaceWith("");
    $(instructions).replaceWith("");
  }
  if(current == 16) {
    $(content).replaceWith("");
    $(instructions).replaceWith("");
  }
  $(".is-hidden-if-is-expanded").replaceWith("<span class='is-hidden-if-is-expanded'><b>卡關了嗎?</b> 暗示!</span>");
  $(".is-shown-if-is-expanded--inline").replaceWith("<span class='is-shown-if-is-expanded--inline'><b>暗示</b></span>");  
  $(".lesson__course-name.one-line-text.js-course-name").text("Python Syntax(語法)");   
  $("p").css("font-family", "Meiryo");
  $("<style type='text/css'> body.composer{ font-family: 'Meiryo', 'Open Sans','Hevetica Neue','Helvetica',sans-serif; position: relative; overflow: hidden; width: auto; font-size: 17px; line-height: 30px;} </style>").appendTo("head");  
}

translate();
var text = document.querySelector(".lesson-left-bar");
var observer = new MutationObserver(function(mutations){
  observer.disconnect();
  translate();
  observer.observe(text, {childList: true, characterData: false, characterDataOldValue: false, subtree: true});
});
observer.observe(text, {childList: true, characterData: false, characterDataOldValue: false, subtree: true});


