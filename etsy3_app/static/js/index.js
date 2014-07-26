/**
 * Created by joaquincunanan on 7/24/14.
 */

$(document).ready(function() {

    var apiKey = 'celykjw2r776vs5zbayaivn7';
    var favoriteArray=[];

    var itemarray=[];

    $('#getsale').on('click', function () {
        $.ajax({
//            url: 'https://openapi.etsy.com/v2/listings/active?api_key=' + apiKey,
//            url: 'https://openapi.etsy.com/v2/users/jcunanan1.js?callback=getData&api_key='+apiKey,
//            url: 'https://openapi.etsy.com/v2/listings/active?callback=getData&api_key='+apiKey,
            url: 'https://openapi.etsy.com/v2/listings/active.js?&limit=12&includes=Images:1&api_key='+apiKey,
            method: 'GET',
            dataType: 'jsonp',
            success: function (response) {


                etsy_response=response;
                for (var i=0; i<12;i++){
                    var itemarray=[];
                    item.title=etsy_response.results[i].title;
                    item.price=etsy_response.results[i].price;
//                    $('#forSale').append(item.title,"  ",item.price,"<br>");
                    console.log(item.title+" "+item.price);
                    itemarray.push(item);

                }

                console.log("array: "+itemarray);
                console.log(response)
            },
            error: function (response) {
                console.log(response)
            }

        });

    });

    $('#getshop').on('click', function () {
        var shop_name=$("input").val();
        $.ajax({

            url: 'https://openapi.etsy.com/v2/shops/'+shop_name+'/listings/active.js?&api_key='+apiKey,
            method: 'GET',
            dataType: 'jsonp',
            success: function (response) {


                etsy_response=response;
                for (var i=0; i<(response.results).length;i++){
                    var item={};


                    item.title=etsy_response.results[i].title;
                    item.description=etsy_response.results[i].description;
                    item.price=etsy_response.results[i].price;
                    item.listing_id=parseInt(etsy_response.results[i].listing_id);

                    console.log(item.title+" "+item.price+" "+item.listing_id);
                    itemarray.push(item);

                }
                for (var j=0; j<(itemarray).length;j++) {
                    console.log("array: " + itemarray[j].listing_id);
                }
                console.log(response);

            },
            error: function (response) {
                console.log(response)
            }
        });
    });
    $('#showShop').on('click', function () {
         console.log('showShop click');
         console.log("show " + itemarray[0].listing_id);
         var shopObject={};
         shopObject.searchResults=itemarray;
         shopObject = JSON.stringify(shopObject);

        console.log(shopObject);
         $.ajax({
             url: '/show_shop/',
             type: 'POST',
             dataType: 'HTML',
             data: shopObject,
             success: function (response) {
                 console.log(response);
                 $("#listingInfo").html(response);
             },
             error: function (error_response) {
                 console.log(error_response);
             }
         });
        $( document ).ajaxComplete(function() {
            $('#accordion').accordion({active: 1});
//            $('.listingInfo').accordion({active: 1});
        });
     });
    $(document).on('click','#favorite',function(){
        console.log("clicked favorite");
        var listObject={};
//        listObject.id = parseInt($(this).parent().find('#listID').text());
        listObject.title = $(this).parent().prev().find('#listTitle').text();
        console.log("favorite "+listObject.title,listObject.id);
        favoriteArray.push(listObject);
        console.log(favoriteArray);
    });

    $('#showFavorites').on('click', function () {
         console.log('showFavorites click');
         console.log(favoriteArray);
         var shopObject={};
         shopObject.searchResults=favoriteArray;
         shopObject = JSON.stringify(shopObject);

        console.log(shopObject);
         $.ajax({
             url: '/show_faves/',
             type: 'POST',
             dataType: 'HTML',
             data: shopObject,
             success: function (response) {
                 console.log(response);
                 $("#listingInfo").html(response);
             },
             error: function (error_response) {
                 console.log(error_response);
             }
         });
     });


});









