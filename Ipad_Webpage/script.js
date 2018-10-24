function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('txt').innerHTML =
    h + ":" + m + ":" + s;
    var t = setTimeout(startTime, 500);
}
function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}

// function test(){
//     return "testingmore"
// }

function changeContent(){
    var x=document.getElementById('myTable').rows
    var y=x[0].cells
    y[0].innerHTML="NEW CONTENT"
    y[0].style.color="#fff"
}