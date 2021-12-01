var rooturl="/"

jQuery(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
    });

function save(url1,url2,index='') {
    // body...
    //console.log($('#form').serialize())

    $.ajax({
        type: "POST",
        dataType: "json",//服务器返回的数据类型
        contentType: "application/x-www-form-urlencoded",//post请求的信息格式
        url: rooturl+url1 ,
        data: $('#form'+index).serialize(),
        success: function (result) {
            console.log($('#form').serialize());

            console.log(result);//在浏览器中打印服务端返回的数据(调试用)
            if(result['success']=='no')
                alert(result['why']);
            else if(result['success']=='yes'){
                //alert("SUCCESS");
                window.location=url2;
            }
        },
        error : function() {
            alert("异常！");
        }
    });
}
function seach(url1,text){
           console.log('seach')
             $.get(rooturl+url1+"?text="+text,function(ret){
            			gridData.rows=ret;
            			initComplete();
					})
            }
function update(){

}

function getbaseinfo(url,name) {
    // body...
    //console.log($('#form').serialize())
    name = document.getElementById(name).value
    $.ajax({
        type: "POST",
        dataType: "json",//服务器返回的数据类型
        contentType: "application/x-www-form-urlencoded",//post请求的信息格式
        url: rooturl+url ,
        data: {"name":name} ,
        success: function (result) {
            //console.log($('#form').serialize());

            //console.log(result);//在浏览器中打印服务端返回的数据(调试用)

            for(key in result){
                temp = document.getElementById(key);
                if(temp != null)
                    temp.value=result[key]
                if(key == 'sex')
                    console.log()
            }
        },
        error : function() {
            alert("异常！");
        }
    });
}
