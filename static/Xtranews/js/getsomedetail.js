$('body').on( "click", function(e) {
  if($("#news-info-large").hasClass("d-block"))
  {
    $("#news-info-large").removeClass("d-block");
    $("#news-info-large").addClass("d-none");
    window.history.pushState("BackToNormal", "Url_Is_Back", currentUrl);
    $('#descriptionProgressBarContainer').removeClass("d-none");
  }
});

$("#clickkk").on( "click", function(e) {
    e.stopPropagation();
});

function getNewsInformation(title){
  var category = getCategory();
  var data = '';
  $.ajax({
      type: 'GET',
      url: window.location.origin + '/api/getnews/' + category + '/post/' + title,
      data: data,
      datatype: 'json',
      success: function (data) {
          var obj = JSON.parse(data)[0].fields; 
          $("#news-info-large").removeClass("d-none");
          $("#news-info-large").addClass("d-block");
          $("#ToTheOriginalArticle").addClass("link")
          $("#news-info-large-title").html(obj.title);
          $('#news-info-large-image').css('background-image', 'url(' + obj.image + ')');
          $("#news-info-large-subtitle").html(obj.pubDate);
          $("#news-info-large-description").html(obj.description);
          $("#news-publisher-name").html(obj.publisher);
          $("#ToTheOriginalArticle").attr("link", obj.link);
          getFullDescription(obj.shortedUrl);
      }
      });

}

function getFullDescription(link){
  var category = getCategory();
  var data = '';
 var timerData = 10;
  var timerID = setInterval(function() {
    if(timerData <= 70)
      timerData += 10 ;
    $('#descriptionProgressBar').css('width',timerData + '%');
    
}, 500); 



  $.ajax({
      type: 'GET',
      url: window.location.origin + '/api/getnews/' + category + '/post/detail/' + link,
      data: data,
      datatype: 'HTML',
      success: function (data) {
          $('#descriptionProgressBar').css('width','100%');
          clearInterval(timerID);
          timerData = 10;
          $("#news-info-large-description").html(data);
          $('#descriptionProgressBarContainer').addClass('d-none');
          $('#descriptionProgressBar').css('width','0%');
      },
      error: function(data) {
        $('#descriptionProgressBar').css('width','100%');
        clearInterval(timerID);
        timerData = 10;
        $('#descriptionProgressBarContainer').addClass('d-none');
        $('#descriptionProgressBar').css('width','0%');
      }
      });
      
      
}
$("#ToTheOriginalArticle").on("click",function(e) {          
  query = $(this).attr("link");
  window.open(query);
})

