var newsFrom = 12 ;
var IsEnough = false ;

$(function () {
  getNews(newsFrom);
});

var currentUrl =  window.location.href ;
function getNews(requiredNews) {
    var category = getCategory();
    var data = '';
    $.ajax({
        type: 'GET',
        url:  window.location.origin + '/api/getnews/' + category ,
        data: { 
            totalnews: requiredNews, 
          },
        datatype: 'json',
        success: function (data) {
            for (var i = 0; i < data.length; i++) {

                var myHtml = `
                    <div class="col-sm-6 col-md-6 col-lg-4 col-xl-3 align-self-center" style="margin-bottom: 5px;margin-top: 5px;">
                      <div class="card card-news" title="` + data[i].shortedUrl + `" style="cursor:pointer;" >
                       <div class="card-body text-left" style="padding: 0px;">
                        <div style="width: 100%;background: url('` + data[i].image + `') center / cover no-repeat;">
                          <div style="width: 100%;height: 200px;"></div>
                          <div class="d-flex d-lg-flex align-items-end align-items-lg-end" style="height: 100px;background: linear-gradient(180deg, rgba(255,255,255,0) 0%, black 67%);">
                             <h5 class="text-center" style="padding: 14px;font-size: 18px;color: rgb(255,255,255);margin: 0px;">` + data[i].title + `</h5>
                           </div>
                         </div>
                        </div>
                      </div>
                    </div>
                      `;

                $("#mynewsinfo").append(myHtml);

            }

            newsFrom = newsFrom +  12 ;
            
            if(data.length == 0){IsEnough = true ;}
              

            $(".card-news").on( "click", function(e) {
              // e.preventDefault();
              query = $(this).attr("title");
              // var urrrl = encodeURI(title);
              
              
              getNewsInformation(query);
              // window.location.href = location.origin + "/home/post/" + query;
              var nxtUrl = location.origin + "/home/post/" + query;
              window.history.pushState("ArticleLink", "Url_Changed", '/' + category + '/post/' + query);
             });
          
        }
    });

}

function getCategory(){
  var category = '';
  for(i=1;(window.location.pathname)[i] != '/' && i < (window.location.pathname).length;i++)
  category += window.location.pathname[i];
  return category ;
}


