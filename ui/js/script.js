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

function addItem(clicked_id) {
    var ul = document.getElementById("order-list");
    var item = event.target.id;
    var li = document.createElement("li");
    var order_item = document.getElementById(clicked_id).childNodes[3].innerText;
    var price = document.getElementById(clicked_id).childNodes[5].innerText;
    var listitem = `${order_item} --- ${price}`
    li.appendChild(document.createTextNode(listitem));
    ul.appendChild(li);
}


function myFunction() {
  document.getElementById("demo").innerHTML = "Hello World";
}

