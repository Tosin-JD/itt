var imageTextArea = document.getElementById("image-text");
var heightLimit = 200; /* Maximum height: 200px */

var btnCopyImageText = document.getElementById("copy-image-text");


window.onload = function() {
//   textarea.style.height = ""; /* Reset the height*/
  imageTextArea.style.height = Math.min(imageTextArea.scrollHeight, heightLimit) + "px";
};



btnCopyImageText.onclick = function(){
  imageTextArea.select();
  document.execCommand('copy');
  
  btnCopyImageText.value = "Copied";
  setTimeout(
    function(){
      btnCopyImageText.value = "Copy";
    }, 1200);
}

