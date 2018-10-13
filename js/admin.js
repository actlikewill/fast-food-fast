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

function updateStatusComplete(orderNumber) {
    
    const url =`https://actlikewill-fastfoodfast.herokuapp.com/api/v2/orders/${orderNumber}`;
    let status = {status: "Complete"};
    fetch(url, {
        method:"PUT",
        headers: {
            "Content-Type":"application/json",
            "Authorization": `Bearer ${getCookie("token")}`
        },
        body: JSON.stringify(status)
    })
    .then(function(response) {
        if (response.status == 201) {
            setTimeout(location.reload(), 50000)
        }
        return response.json();
    })
    .then(function(data) {
        console.log(data)
    })    
}

function updateStatusDecline(orderNumber) {
    
    const url =`https://actlikewill-fastfoodfast.herokuapp.com/api/v2/orders/${orderNumber}`;
    let status = {status: "Declined"};
    fetch(url, {
        method:"PUT",
        headers: {
            "Content-Type":"application/json",
            "Authorization": `Bearer ${getCookie("token")}`
        },
        body: JSON.stringify(status)
    })
    .then(function(response) {
        if (response.status == 201) {
            setTimeout(location.reload(), 50000)
        }
        return response.json();
    })
    .then(function(data) {
        console.log(data)
    })    
}

function undoStatus(orderNumber) {
    
    const url =`https://actlikewill-fastfoodfast.herokuapp.com/api/v2/orders/${orderNumber}`;
    let status = {status: "pending"};
    fetch(url, {
        method:"PUT",
        headers: {
            "Content-Type":"application/json",
            "Authorization": `Bearer ${getCookie("token")}`
        },
        body: JSON.stringify(status)
    })
    .then(function(response) {
        if (response.status == 201) {
            setTimeout(location.reload(), 50000)
        }
        return response.json();
    })
    .then(function(data) {
        console.log(data)
    })    
}

let adminErrorMessage = document.getElementById("admin-error");

window.onload = function getOrders() {
    document.getElementById("admin").innerHTML = getCookie("user");
    const url =`https://actlikewill-fastfoodfast.herokuapp.com/api/v2/orders`

    this.fetch(url, {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${getCookie("token")}`
        }
    })
    .then(function(response) {
        if(response.status == 500) {
            adminErrorMessage.style.display = "block" 
        } 
        return response.json()        
    })
    .then(function(data) {        
        let allOrders = data['Orders'];
        let allOrdersTable = `      
                                <tr>
                                <th class="narrow">Order Number</th>
                                <th class="narrow">Date</th>
                                <th class="narrow">Ordered By</th>
                                <th>Details</th>
                                <th class="narrow">Amount Due (Ksh)</th>
                                <th>Actions</th> 
                                <th class="narrow">Order Status</th>
                                </tr>
                            `;
        console.log(allOrders);

        for (let i in allOrders)
        {
        let actionButtons;
        
        if (allOrders[i]['status'] == "Complete" || allOrders[i]['status'] == "Declined") {
            actionButtons = `<button class="undo order-button" onclick="undoStatus(${allOrders[i]['order_id']})">Undo Order</button>`
        } else if (allOrders[i]['status'] == "pending") {
            actionButtons = `
                                <button class="complete order-button" onclick="updateStatusComplete(${allOrders[i]['order_id']})">Complete Order</button>
                                <button class="decline order-button" onclick="updateStatusDecline(${allOrders[i]['order_id']})">Decline Order</button>
                            `
        }

        
            allOrdersTable += `
                                <tr>
                                <td>${allOrders[i]['order_id']}</td>
                                <td>${allOrders[i]['date_ordered']}</td>
                                <td>${allOrders[i]['ordered_by']}</td>
                                <td>${allOrders[i]['details']}</td> 
                                <td>${allOrders[i]['price']}</td>                            
                                <td>${actionButtons}</td>                                    
                                <td>${allOrders[i]['status']}</td>
                                </tr>
                            `
        }

        document.getElementById("all-orders-table").innerHTML = allOrdersTable;
    })
    
}