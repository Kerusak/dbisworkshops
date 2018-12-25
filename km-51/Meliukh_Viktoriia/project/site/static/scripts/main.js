(function (){
            $.ajax({
                url: 'gethousingnumbers',
                type: 'GET',
                contentType: "application/json",
                success: function (response) {
                     var data =  JSON.parse(response);
                     var html ='';
                     for(var i =0; i < data.length; i++){
                        html += '<option value="' + data[i].number + '"> Housing ' + data[i].number + '</option>'
                     }
                     $('#housing').append(html);
                }
            });
            $.ajax({
                url: 'getnumberofseats',
                type: 'GET',
                contentType: "application/json",
                success: function (response) {
                     var data =  JSON.parse(response);
                     var html ='';
                     for(var i =0; i < data.length; i++){
                        html += '<option value="' + data[i].number + '"> ' + data[i].number + ' seats</option>'
                     }
                     $('#seats').append(html)
                }
            });
            $.ajax({
                url: 'lessonsdata',
                type: 'GET',
                contentType: "application/json",
                success: function (response) {
                     var data =  JSON.parse(response);
                     var html ='';
                     for(var i =0; i < data.length; i++){
                        html += '<option value="' + data[i].lessonnumber + '"> ' + data[i].etime + ' - ' + data[i].btime + ' (' +  data[i].lessonnumber + ' lesson)</option>'
                     }
                     $('#lessons').append(html)
                }
            });


            $('#submit').click(function(){
                $('#label').css('display', 'none');
                var form = $('#form')[0];
                console.log($(form))
                var validate = true;
                var mult = form[4].checked ? 1 : 0;
                var lessons;
                for(var i = 0; i < 4; i++){
                    if(!form[i].value  || form[i].value == 0 ){
                        validate = false;
                    }
                }
                if(validate){
                    lessons = form[3].selectedOptions[0]["label"]
                   $.ajax({
                        url: 'findclassrooms?h_num=' + form[1].value + '&seats=' + form[2].value + '&mult=' + mult + "&date=" + form[0].value + '&l_num=' + form[3].value,
                        type: 'GET',
                        contentType: "application/json",
                        success: function (response) {
                            console.log(response)
                            document.location.href='/displaysearchresult?h_num=' + form[1].value + '&seats=' + form[2].value + '&mult=' + mult + "&date=" + form[0].value + '&l_num=' + form[3].value + '&lsn=' + lessons
                        }
                    });
                }
                else {
                    $('#label').css('display', 'inline')
                }


            })

            $(".select-btn").click(function(e){
                var el = $(e.target)[0];
                var data = el.dataset;
                document.location.href='/bookingconfirm?c_num=' + data.classroomnum +  '&c_id=' + data.id + '&h_num=' + data.housingnumber + '&seats=' + data.numberofseats + '&mult=' + data.multimedia + '&lsn=' + data.lsn + '&date=' + data.date

            })

            $("#confirm").click(function(e){
                e.preventDefault();
                var el = $(e.target)[0];
                var data = el.dataset;
                console.log(data)
                var temp = data.lsn;
                var re = /\(/;
                var index = temp.match(re);
                var l_num = temp[index.index + 1];

                $.ajax({
                    url: 'book?c_id=' + data.c_id + '&b_date=' + data.bdate + '&l_num=' + l_num,
                    type: 'GET',
                    contentType: "application/json",
                    success: function (response) {
                        document.location.href='/confirmsuccess'
                    }
                });
            })

            $(".delete").click(function(e){
                var conf = confirm("Delete booking?");
                if(conf){
                    var el = $(e.target)[0];
                    var data = el.dataset;



                    $.ajax({
                        url: 'deletebooking?id=' + data.id,
                        type: 'GET',
                        contentType: "application/json",
                        success: function (response) {
                         var item = $(el).parent().parent();
                            if(item){
                                item.remove()
                            }
                        }
                    });
                }
            })

            $(".checkUser").click(function(e){
                var el = $(e.target)[0];
                var data = el.dataset;

                $.ajax({
                    url: 'checkuser?id=' + data.id,
                    type: 'GET',
                    contentType: "application/json",
                    success: function (response) {
                        var item = $(el).parent();
                        item.css('display', 'none');
                    }
                });
            })
            $(".deleteUser").click(function(e){
                var el = $(e.target)[0];
                var data = el.dataset;

                $.ajax({
                    url: 'deleteuser?id=' + data.id,
                    type: 'GET',
                    contentType: "application/json",
                    success: function (response) {
                            var item = $(el).parent().parent();
                            if(item){
                                item.remove()
                            }

                    }
                });
            })


})()
