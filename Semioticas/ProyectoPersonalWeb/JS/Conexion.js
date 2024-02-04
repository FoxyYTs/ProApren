function myFunction() {
    var inputValue = document.getElementById("user").value;
    var inputValue2 = document.getElementById("pss").value;
    if (inputValue == "Daza" && inputValue2 == "1234") {
        window.location.href = "index.html";
    } else {
        console.log("Error")
    }
}