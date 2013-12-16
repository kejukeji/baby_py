$(function(){
           var brand = $("#brand li .iradio")
           var divDisplayObj = $("#div-display")
           brand.bind("click", function(){
               var brandVal = $(this).parent().find("label").html()
               if (brandVal == "其他"){
                   divDisplayObj.hide()
               }else{
                   divDisplayObj.show()
               }
           })
})