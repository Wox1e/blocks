let offset = 10;
const limit = 10;



window.onscroll = function () {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        loadMoreContent();
    }
};

function loadMoreContent() {
    offset += limit;
    const url = "/api/load_more/";
    const params = "?offset=" + offset + "&limit=" + limit;
    fetch(url + params)
        .then(response => response.json())
        .then(data => {
            data.forEach(post => {
            createPostElement(post);
        });
    });
}

function createPostElement(post) {

    if (post.is_liked){
        post_html_code = `<div class="card-body" id = "post:${post.id}"> <div class="media"> <img src="${post.image}" alt="user image" width="60px" height="60px" class="rounded-circle mr-3"> <div class="media-body"> <a href="/profile/u/${post.username}" class = "username_text">${post.username}</a> <p class="text-justify">${post.text}</p> <div class = "user_actions"> <form class = "commentary_input" metod = "GET" action = "/publish/commentary/"> <div class = "custom_commentary_text"> <div class = "like_counter"> <p>${post.likes}<p> </div> <div class = "like"> <a href="/publish/post_unlike/?id=${post.id}" class="like_button"> <img src = "static/main/like_button/red_heart.svg" height = 30px, width = 30px> </a> </div> <input type="text" name="message" id="message" placeholder="Commentary" class="commentary_input_text"> <input type="hidden" name="post_id" value="${post.id}"> <script> function myFunction(id) { var posts = document.getElementById('post_commentaries' + id) if (posts.style.display == "none"){ posts.style.display = "block" }else{ posts.style.display = "none" } } </script> <form> <button type = "button" class = "comment_button" onclick="myFunction(${post.id})"> <img src = "static/main/comment_button/comment-solid.svg" height = 30px, width = 30px> </button> </form> </div> </form> </div> </div> <small>${post.posting_time}</small> </div> </div> <hr>`;
    }
    else{
        post_html_code = `<div class="card-body" id = "post:${post.id}"> <div class="media"> <img src="${post.image}" alt="user image" width="60px" height="60px" class="rounded-circle mr-3"> <div class="media-body"> <a href="/profile/u/${post.username}" class = "username_text">${post.username}</a> <p class="text-justify">${post.text}</p> <div class = "user_actions"> <form class = "commentary_input" metod = "GET" action = "/publish/commentary/"> <div class = "custom_commentary_text"> <div class = "like_counter"> <p>${post.likes}<p> </div> <div class = "like"> <a href="/publish/post_unlike/?id=${post.id}" class="like_button"> <img src = "static/main/like_button/black_heart.svg" height = 30px, width = 30px> </a> </div> <input type="text" name="message" id="message" placeholder="Commentary" class="commentary_input_text"> <input type="hidden" name="post_id" value="${post.id}"> <script> function myFunction(id) { var posts = document.getElementById('post_commentaries' + id) if (posts.style.display == "none"){ posts.style.display = "block" }else{ posts.style.display = "none" } } </script> <form> <button type = "button" class = "comment_button" onclick="myFunction(${post.id})"> <img src = "static/main/comment_button/comment-solid.svg" height = 30px, width = 30px> </button> </form> </div> </form> </div> </div> <small>${post.posting_time}</small> </div> </div> <hr>`;
    }

    document.getElementById('card').innerHTML += post_html_code;
}