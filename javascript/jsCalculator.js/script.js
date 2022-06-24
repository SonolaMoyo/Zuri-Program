function myFunction () {
    let text;
    let ans = 0; //answer
    let a = Number(prompt("Enter first integer variable"));
    let b = Number(prompt("Enter second integer variable"));
    let opr = prompt("Enter operator"); //operator
    const operator = ["+", "-", "/", "*"];

    if( isNaN(a) || isNaN(b) || !operator.includes(opr)) {
        text = "Invalid input";
    } else {
        switch(opr){
            case "+":
                ans = a + b;
                break;

            case "-":
                ans = a - b;
                break;

            case "/":
                ans = a/b;
                break;

            case "*":
                ans = a * b;
                break;

            default:
                ans = 0;
        }
        text = a + " " + opr + " " + b + " = " + ans;
    }
    document.getElementById("demo").innerHTML = text;
    alert(text)
}

// 