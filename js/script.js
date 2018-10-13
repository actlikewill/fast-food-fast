
let your_order = []
let theMenu;
let order_json;

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

  console.log(getCookie("role"));

window.onload = function getMenu() {       

    const url = `http://localhost:5000/api/v2/menu`

    document.getElementById("username").innerHTML = getCookie("user");

    if (getCookie("role") == "admin") {
        document.getElementById("admin-link").style.display = "block";
    }

    fetch(url)
    .then(function(response) {
        return response.json()
    })
    .then(function(data) {
        let menu = data['Menu'];
        let itemList = ``;
        theMenu = menu;

        console.log(menu);
        for(var i in menu)
        {
            itemList += `   <div id="${menu[i]['menu_item'].toLowerCase()}" class="menu-item" onclick="addItem(this.id)">
                            <div class="menu-img">
                            <img src="img/${menu[i]['menu_item'].toLowerCase()}.svg" alt="">
                            </div>
                            <div  class="menu-text">
                            <h4>${menu[i]['menu_item']}</h4>
                            </div>
                            <div  class="menu-price">
                            <h4>${menu[i]['price']}</h4>
                            </div>                            
                            </div>
                        `           
        }
        
        document.getElementById('MyMenu').innerHTML = itemList;     
    })
    .catch(function(error) {           

        console.log(error)
    })
}

function addItem(clicked_id) {
    var ul = document.getElementById("order-list");
    var item = event.target.id;
    var li = document.createElement("li");
    var order_item = document.getElementById(clicked_id).childNodes[3].innerText;
    var price = document.getElementById(clicked_id).childNodes[5].innerText;
    var listitem = `${order_item} --- ${price}`;
    li.appendChild(document.createTextNode(listitem));
    ul.appendChild(li);
    your_order.push(order_item.slice(0, -1));    
}


function getOrder(order) {
   let processed_order = {};
   let copy = order.slice(0);

   for (let i = 0; i < order.length; i++) {
       let count = 0;
       for (let j = 0; j < copy.length; j++) {
           if (order[i] == copy[j]) {
               count++;
               delete copy[j]
           }
       }
       if (count > 0) {                  
           processed_order[order[i]] = count;
       }
   }
   order_json = JSON.stringify(processed_order);
   
   return processed_order;  
}

let modal = document.getElementById("modal");
let placeOrderButton = document.getElementById("place-order-button");
let span = document.getElementsByClassName('close')[0];
span.onclick = function() {
    modal.style.display = "none";
}

placeOrderButton.onclick = function() {
    let theOrder = getOrder(your_order);
    let orderList = Object.keys(theOrder);
    let total = 0;
    let orderSummary = ` <table class="table modal-table">
                            <tr>
                                <th>Item</th>
                                <th>Quantity</th>
                                <th>Price</th>
                            </tr>`;

    for (let item in orderList) {

        let price = theMenu.find(x => x.menu_item == orderList[item]).price;
        let cost = price * theOrder[orderList[item]];
        total += cost;
        orderSummary += `
                            
                            <tr>
                                <td>${orderList[item]}</td>
                                <td>${theOrder[orderList[item]]}</td>
                                <td>${cost}</td>
                            </tr>
                        `;
    }
    orderSummary += `   
                    <tr>
                        <td>Total</td>
                        <td></td>
                        <td>${total}</td>
                    </tr>                            
                    </table>
                    `;

    document.getElementById("order-summary").innerHTML = orderSummary;

    modal.style.display = "block";
       
}

let confirmOrderButton = document.getElementById("confirm-order");
let successMessage =  document.getElementById("success-message");
let failMessage =  document.getElementById("fail-message");
let confirmButton = document.getElementById("confirm-order");

confirmOrderButton.onclick = function () {
    
    const url = `http://localhost:5000/api/v2/users/orders`
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type":"application/json",
            "Authorization":`Bearer ${getCookie("token")}`
        },
        body: order_json
    })
    .then(function(response) {
        if (response.status == 201) {
            confirmButton.style.display = "none";
            successMessage.style.display = "block";
        } else {
            confirmButton.style.display = "none";
            failMessage.style.display = "block";
        }
        
    })
    .then(function(data) {
        // res = data;
        // console.log(data);
        
    })
    .catch(function(error) {
        console.log(error)
        confirmButton.style.display = "none";
        failMessage.style.display = "block";
    })     
}

let backButton = document.getElementById("back");
let backButton2 = document.getElementById("back2")
let clearOrder = document.getElementById("clear")

backButton.onclick = function() {
    location.reload();
}
backButton2.onclick = function() {
    location.reload();
}
clearOrder.onclick = function() {
    location.reload();
}

