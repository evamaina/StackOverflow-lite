function validateForm() {

    //First name validation
    var fname = document.forms["signUp"]["Fname"].value;

    if (fname == "") {
        alert("First Name must be filled out");
        document.forms["signUp"]["Fname"].focus();
        return false;
    }

    //Last name validation
    var Lname = document.forms["signUp"]["Lname"].value;
    if (Lname == "") {
        alert("Last Name must be filled out");
        document.forms["signUp"]["Lname"].focus();
        return false;
    }

    //Username validation
    var Username = document.forms["signUp"]["username"].value;
    if (Username == "") {
        alert("Username Name must be filled out");
        document.forms["signUp"]["username"].focus();
        return false;
    }

    //Email validation
    var Email = document.forms["signUp"]["email"].value;
    if (Email == "") {
        alert("Email must be filled out");
        document.forms["signUp"]["email"].focus();
        return false;
    }

    //Password validation
    var Password = document.forms["signUp"]["password"].value;
    if (Password== "") {
        alert("Password must be filled out");
        document.forms["signUp"]["password"].focus();
        return false;
    }

    //confirm password validation
    var Confirm_password = document.forms["signUp"]["confirm_password"].value;
    if (Confirm_password == "") {
        alert("confirm password must be filled out");
        document.forms["signUp"]["confirm_password"].focus();
        return false;
    }

    if(Password!=Confirm_password){
        alert("Password mismatch");
        document.forms["signUp"]["confirm_password"].focus();
        return false;
    }

        //checkbox validation
    var checkbox = document.getElementById("checkbox").checked;

    if (checkbox== false){
        alert("accept terms");
        document.getElementById("checkbox").focus();
        return false;
    }
    
}

