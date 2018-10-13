function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }

window.onload = function getName () {
    document.getElementById("admin-name").innerHTML = getCookie("user");
}
let addItemForm = document.forms["add-item-form"];
let addSuccessMessage = document.getElementById("add-success");
let addFailMessage = document.getElementById("add-fail");

addItemForm.addEventListener("submit", (e) => {
    e.preventDefault();

    let formData = new FormData(e.target);
    let menu_item = formData.get("menu_item");
    let description = formData.get("description");
    let price = formData.get("price");

    let newMenuItem = {
        menu_item:menu_item,
        description:description,
        price:price
    }

    const url = `http://localhost:5000/api/v2/menu`;

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type":"application/json",
            "Authorization": `Bearer ${getCookie("token")}`
        },
        body: JSON.stringify(newMenuItem)
    })
    .then(function(response) {
        if (response.status == 201) {
            addSuccessMessage.style.display = "block";
            addFailMessage.style.display = "none"

        } else {
            addFailMessage.style.display = "block"
            addSuccessMessage.style.display = "none";


        }
        return response.json()
    })
    .then(function(data) {
        console.log(data)
    })
    .catch(function(error) {
        console.log(error)
    })

    console.log(JSON.stringify(newMenuItem));

})