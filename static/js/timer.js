var currSeconds = 0;
$( document ).ready(function() {      
    /* Increment the idle time
        counter every second */
        let idleInterval = setInterval(timerIncrement, 1000);  
    /* Zero the idle timer
        on mouse movement */
    $(this).mousemove(resetTimer);
    $(this).keypress(resetTimer);
    
});
function resetTimer() {  
    /* Hide the timer text */                 
    currSeconds = 0;
}  
function timerIncrement() {
    currSeconds = currSeconds + 1;    
    if (currSeconds > 120) {
        window.location.assign('/logout')
    }   
}