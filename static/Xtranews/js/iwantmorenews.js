$(window).scroll(function() {
    
    if($(window).scrollTop() + $(window).height() == $(document).height()) {
        if(!IsEnough){
        if($.active < 1){
            getNews(newsFrom);
            console.log("News Wil COme Wait");
    } else {
            console.log("Already Request More News For U");
    }
}
else
    alert("IS ENOUGH FOR TODAY");
    }
 });