$(document).ready(function(){

// if city, Region and Country are not detected show some texts
var cityName = $("#mycity").html();
if(cityName === ""){
   $("#mycity").html("City");
} 
// for Region
var regionName = $("#myregion").html();
if(regionName === ""){
   $("#myregion").html("Region");
}

// for Country
var countryName = $("#mycountry").html();
if(countryName === ""){
   $("#mycountry").html("Country");
}

// submit search form 
$("#search-form").submit(function(){
  var keyword = $("#search-input").val();
  var country = $("#country").val();
  var region =  $("#state").val();
  var city = $("#city").val();
  if(keyword === ""){
    $("#alert").attr("class","alert alert-danger text-info").show().text("Enter a keyword").delay(700).hide(400);
  }
  if(country === ""){
      $("#alert").attr("class","alert alert-danger text-info").show().text("Country not selected").delay(700).hide(400);
  }
  if(region === ""){
      $("#alert").attr("class","alert alert-danger text-info").show().text("Region not selected").delay(700).hide(400);
  }
  if(city === ""){
    $("#alert").attr("class","alert alert-danger text-info").show().text("City not selected").delay(700).hide(400);
  }
  else if(city !=="" && region !=="" && country !=="" && keyword !==""){
    $.ajax(
      {
        url:"/ajax/keyword_search/",
        data:{
          "keyword": keyword,
          "country": country,
          "region": region,
          "city": city
        },
        dataType: "json",
        success: function(data){
          $("#search-result-size").html(" ");
          if(data.services.length == 0){ // if service array is zero 
              var $searchResult = $("#js-search-result");
              ($searchResult).html("");
              ($searchResult).append('<q>'+keyword+'</q>'+' not found');
          }
          else{
            $("#search-result-size").html("<span class='badge badge-pill badge-success'>"+data.services.length+"</span> ").append(" Results");
            var $searchResult = $("#js-search-result");
            ($searchResult).html("");
            $.each(data.services, function(index){
              // create service items
              var $cardTitle = $("<h6 class='card-title text-dark font-weight-bold'></h6>").html(data.services[index].business_name);
              $cardTitle.append("<hr>");
              var $address = $("<li class='fa fa-map-marker text-info'></li>").text(" "+data.services[index].street_address);
              var $price = $("<p class='text-warning'></p>");
              $price.text(data.services[index].price+" "+data.services[index].currency);
              var $detailButton = $('<a class="btn btn-primary card-link stretched-link" href="/servicedetails/'+data.services[index].id+'/'+'">More...</a>');
              var $cardBody = $("<div class='card-body'></div");
              var $col = $("<div class='col-xl-3 col-lg-3 col-sm-6'></div>");
              ($cardTitle).append($address).append($price).append($detailButton);
              $cardBody.html($cardTitle);
              var $card = $("<div class='card'></div>");
              var $cardImage = $("<img src='"+"https://smartcity090.s3.amazonaws.com/media/"+data.services[index].picture+"' class='card-img-top rounded-circle' alt='photo'>");
              $card.html($cardImage).append($cardBody);
              $col.html($card);
              ($searchResult).html($col);
            });
          }
        },
        error: function(data){
          $("#alert").attr("class","alert alert-danger text-info").show().text("Unknown Error occured.").delay(700).hide(400);
        },
      }
    );
  }
  return false;
});
  // get states for the selected country 
  $("#country, #id_country").change(function(){
      var country = $(this).val();
      if(country !==''){
        $.ajax(
          {
            url:"/ajax/states/",
            data:{
              "country":country,
            },
            dataType: 'json',
            success:function(data){
              $("#state, #id_region").html('');
              for(var i = 0; i < data.regions.length; i++){
                $("#state, #id_region").append('<option id="selected-state" value="'+ data.regions[i]['id'] +'">'+ data.regions[i]['name'] +'</option>');
              }
            }
          }
        );
      }
      else{
        $("#alert").attr("class","alert alert-danger text-info").show().text("Select a country.").delay(700).hide(400);
      }
      
  });

// get cities for the selected state
$("#state, #id_region").change(function(){
  var state = $(this).val();
  $.ajax(
    {
      url:"/ajax/cities/",
      data:{
        "state":state,
      },
      dataType:"json",
      success:function(data){
        $("#city, #id_city").html("");
        for(var i = 0; i < data.cities.length; i++){
          $("#city, #id_city").append('<option id="selected-city" value="'+ data.cities[i]['id'] +'">'+ data.cities[i]['city'] +'</option>');
        }
      },
      error: function(data){
        $("#alert").attr("class","alert alert-success text-danger").show().text("Failed to load cities.").delay(700).hide(400);
      }
    }
  );
});
});