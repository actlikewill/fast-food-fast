function openTab(evt, tabName) {
    var i, tabcontent, tablinks;

    tabcontent = document.getElementsByClassName("tabcontent");
    for (i=0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    tablinks = document.getElementsByClassName("tablinks");
    for (i=0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace("active", "");
    }

    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}


let loginForm = document.forms["loginForm"];
let loginSuccessMessage = document.getElementById("login-success");
let loginFailMessage = document.getElementById("login-fail");

loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    let formData = new FormData(e.target);
    let username = formData.get("username");
    let password = formData.get("password");

    let loginData = {
        username: username,
        password:password
    }

    console.log(JSON.stringify(loginData));

    const url = `https://actlikewill-fastfoodfast.herokuapp.com/auth/login`;

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type":"application/json"
        },
        body: JSON.stringify(loginData)
    })
    .then(function(response) {
        console.log(response.status);
        if (response.status == 200) {
          loginSuccessMessage.style.display = "block";
          loginFailMessage.style.display = "none";           
           
        } else {
            loginFailMessage.style.display = "block";
        }         
        return response.json() 
    })
    .then(function(data) {
        console.log(data);        
        if (data["msg"] == "Login Successful")  {
        let token = data['token'];
        let user = data['user']; 
        let role = data['role'];       
        document.cookie=`token=${token};path=/`;
        document.cookie=`user=${user};path=/`;
        document.cookie=`role=${role};path=/`;
        if (role == "user") {
        let domain = window.location.hostname;
        setTimeout(() => {window.location.replace(`${domain}/fast-food-fast/index.html`)}, 2000) 
        } else {
        setTimeout(() => {window.location.replace(`${domain}fast-food-fast/admin.html`)}, 2000)
        } 
    }     
    })
    .catch(function(error) {
        console.log(error);
    })
});

function showCookie() {
    console.log(document.cookie);
}

let signUpForm = document.forms["signUpForm"];
let signUpFailMessage = document.getElementById("signUp-fail");
let signUpSuccessMessage = document.getElementById("signUp-success");
let signUpEmptyMessage = document.getElementById("signUp-empty");
let signUpDuplicateMessage = document.getElementById("signUp-duplicate");
signUpForm.addEventListener("submit", (e) => {
    e.preventDefault();

    let formData = new FormData(e.target);
    let username = formData.get("username");
    let email = formData.get("email");
    let password = formData.get("password");
    let confirmPassword = formData.get("confirm-password")

    let signUpData = {
        username: username,
        email: email,
        password:password,        
    }

    if (username == "" || email == "" || password == "" || confirmPassword == "") {
        signUpEmptyMessage.style.display = "block";
        signUpFailMessage.style.display = "none";
    } else if (password != confirmPassword) {
        signUpFailMessage.style.display = "block";
        signUpEmptyMessage.style.display = "none";
    } else {
        signUpDuplicateMessage.style.display = "none";        
        signUpEmptyMessage.style.display = "none";
        signUpFailMessage.style.display = "none";

        const url = `https://actlikewill-fastfoodfast.herokuapp.com/auth/users`;

        fetch(url, {
            method: "POST",
            headers: {
                "Content-Type":"application/json"
            },
            body: JSON.stringify(signUpData)
        })
        .then(function(response) {
            console.log(response.status)
            if (response.status == 401) {
                signUpDuplicateMessage.style.display = "block";
            } else if (response.status == 201) {
                signUpSuccessMessage.style.display = "block";
                
            }
            return response.json()
        })
        .then(function(data) {
            console.log(data);
        })
    } 

    console.log(signUpData);
});


