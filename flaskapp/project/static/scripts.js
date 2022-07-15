
let $userTable = $('#userTable');

$(document).on("click", "#loadUsersButton", function(event){
    $.ajax({
        url: "/get-users/users.json",
        type: 'GET',
        contentType: "application/json",
        success: function(data) {
            $userTable.bootstrapTable("destroy");
            $userTable.bootstrapTable({data: data});
        },
        error: function(error) {
            console.log(error);
        }
    });
});