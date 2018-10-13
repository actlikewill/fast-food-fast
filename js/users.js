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

let historyErrorMessage = document.getElementById("history-error")

window.onload = function getUserHistory() {
    document.getElementById("user").innerHTML = getCookie("user");

    const url =`http://localhost:5000/api/v2/users/orders`

    fetch(url, {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${getCookie("token")}`
        }        
    })
    .then(function(response) {
        
        if(response.status == 500) {
            historyErrorMessage.style.display = "block" 
        } 
        return response.json()
    
    })
    .then(function(data) {
        let orderHistory = data['Orders'];
        let orderTable = `  
                            <tr>
                            <th class="narrow">Date</th>
                            <th>You Bought:</th>
                            <th class="narrow">You Paid (Ksh):</th> 
                            <th class="narrow">Status</th>                                                       
                            </tr>
                        `;
        console.log(orderHistory);

        for (let i in orderHistory)
        {
            orderTable += `
                            <tr>
                            <td>${orderHistory[i]["date"]}</td>
                            <td>${orderHistory[i]["details"]}</td>
                            <td>${orderHistory[i]["cost"]}</td> 
                            <td>${orderHistory[i]["status"]}</td> 
                            </tr>            
                        `
        }

        document.getElementById("history-table").innerHTML = orderTable;


    })
    .catch(function(error) {
        
       console.log(error);
    })
}