let hearts = document.getElementById('like-count');
let count = 0;

function like(){
    
    count+=1;
    hearts.innerHTML = count + 'likes';
}