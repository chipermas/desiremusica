/* $(document).ready(function(){
    function ajax_login(){
        $.ajax({
            type: "POST",
            url: "/ajax-login",
            data: $('form').serialize(),
            
            success: function (response) {
                console.log(response)                
            },
            error: function(error) {
                console.log(error)
            }
        });
    }

    $('#login-form').submit(function (e) { 
        e.preventDefault();
        ajax_login();        
    });
}); */

window.onload = function(){
    $('#preloader').fadeOut();
    $('body').removeClass('hidden');    
    $('#mainNav').addClass('fixed-top');
}
$( document ).ready(function() {
    $('#exampleModal').modal('toggle')    
});
/* Funcion para pausar videos al cerrar modales*/
$('body').on('hidden.bs.modal', '.modal', function () {
    $('video').trigger('pause');
    });

function mostrarPassword(){
    var cambio = document.getElementById("password");
    if(cambio.type == "password"){
        cambio.type = "text";
        $('.icon').removeClass('fa fa-eye-slash').addClass('fa fa-eye');
    }else{
        cambio.type = "password";
        $('.icon').removeClass('fa fa-eye').addClass('fa fa-eye-slash');
    }
} 