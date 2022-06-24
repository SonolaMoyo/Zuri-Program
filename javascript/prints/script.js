function myFunction () {
    let text;
    let name = prompt("Enter your Name");
    let height = prompt("Enter your Height");
    let country = prompt("Enter your Country name");

    if(name == null || name == "" || height == null || height == "" || country == null || country == "") {
        text = "Please enter the details";
    }
    else {
        text = "Your Name: " + name + "<br>" +
               "Your Height: " + height + "<br>" +
               "Your Country: " + country + "<br>";
    }

    document.getElementById("demo").innerHTML = text;
}