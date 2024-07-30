object.onclick = function(){myFunction};

function myFunction() {

    var posts = document.getElementById('post_commentaries')

    if (posts.style.display == "none"){
        posts.style.display = "block"
    }else{
        posts.style.display = "none"
    }

  } 