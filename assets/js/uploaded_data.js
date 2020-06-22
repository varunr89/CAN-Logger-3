$( document ).ready(function() {
    $('#email').text(sessionStorage.getItem("email"));
    var access_token = window.sessionStorage.getItem('id_token');
    $.ajax({
      url: "https://47tzdaoo6k.execute-api.us-east-2.amazonaws.com/dev/list",
        method: "GET",
        crossDomain: true,
        dataType: 'json',
        headers: {
            'Authorization': "Bearer " + access_token,
            'Access-Control-Allow-Origin': "*"
        }
    })
    .done(function (data, textStatus, jqXHR) {
      console.log(data)
      for (const line in data['Items']) {
        // if (data.hasOwnProperty(line)) {

          var file_name = data['Items'][line]['filename'];
          console.log(file_name)
          var file_size = data['Items'][line]['filesize'];
          if (file_size === undefined) { file_size = 'Unknown' };
          var id = data['Items'][line]['serial_num'];
        var verify_status = data['Items'][line]['verify_status'];
          if (verify_status === undefined) { verify_status = 'Unknown' };
        var upload_time = data['Items'][line]['upload_date'];
          if (upload_time === undefined) { upload_time = 'Unknown' };
          $("#loggerID").append(
            '<tr id="row_' + id + '">' +
            "<td>" + file_name + "</td>" +
            "<td>" + id + '</td>' +
            '<td>' + file_size + "</td>" +
            '<td>' + upload_time + "</td>" +
            '<td>' + verify_status + "</td>" +
            "</tr>"
          );
        // }
      }
    })
    .fail(function (error_data){
        displayRibbon('There was an error when retrieving CAN Logger information.', 'danger');
        console.info(error_data)        
    });    
});

// https://www.w3schools.com/howto/howto_js_sort_table.asp
function sortTable(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("Uploaded_Data");
  switching = true;
  // Set the sorting direction to ascending:
  dir = "asc";
  /* Make a loop that will continue until
  no switching has been done: */
  while (switching) {
    // Start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /* Loop through all table rows (except the
    first, which contains table headers): */
    for (i = 1; i < (rows.length - 1); i++) {
      // Start by saying there should be no switching:
      shouldSwitch = false;
      /* Get the two elements you want to compare,
      one from current row and one from the next: */
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      /* Check if the two rows should switch place,
      based on the direction, asc or desc: */
      if (dir == "asc") {
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      } else if (dir == "desc") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /* If a switch has been marked, make the switch
      and mark that a switch has been done: */
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      // Each time a switch is done, increase this count by 1:
      switchcount ++;
    } else {
      /* If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again. */
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}