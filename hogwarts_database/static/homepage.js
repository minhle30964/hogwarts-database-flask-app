// Adding event listener for events in DOM (specifically for homepage) //
document.addEventListener("DOMContentLoaded", function () {
    // Creating variable for the Maurauders' Map button on the homepage of web application //
    let btn = document.querySelector("#spell");
    // Creating list of elements that should appear when the Maurauders' Map button on the homepage of web application is pressed //
    let invisible_elements = document.querySelectorAll(".appear");

    // Adding event listener to check for when button is clicked //
    btn.addEventListener("click", function () {
        // Changing jumbotron's background if button is clicked //
        document.getElementById("block").style.backgroundColor = "rgba(240, 240, 240, 0.8)";
        document.getElementById("block").style.backgroundImage = "none";
        // Making the hidden elements on the homepage visible when the button is clicked //
        for (let element of invisible_elements)
        {
            element.style.visibility = "visible";
        }
        // Hiding the Maurauders' Map button on the homepage of web application //
        btn.style.visibility = "hidden";
    });
});
