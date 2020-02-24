let replacetoBR = function(text) {
    return text.replace(/\r?\n/g, "<br>");
}

let replacetoRN = function(text) {
    return text.replace(/<br>/g, '\r\n');
}

$(document).ready(function() {
});

function addComment(post_id) {
        let param = $('form[name=commentForm]').serialize();
        $.ajax({
            type: 'POST',
            url: '/addcomment/'+post_id,
            data : param,
            datatype: 'json',

            success: function(res) {
                let text = Array();
                res.forEach(function(e) {
                    pk = e.pk;
                    user = e.fields.author[0];
                    star = e.fields['star'];
                    content = e.fields['content'];
                    if (current_user == user) {
                        tmp = user +'<a href="/deletecomment/'+ pk +'"> 삭제 </a><a id="'+ pk +'" href="javascript:" onclick="commentEdit(this)"> 수정 </a><div>'+ e.fields['star'].toFixed(1) +'<div class="content">'+ e.fields['content'] +'</div><hr>'
                    } else {
                        tmp = user +'<div>'+ e.fields['star'].toFixed(1) +'<div>'+ e.fields['content'] +'</div><hr>'
                    }
                    text.push(tmp);
                });
                $('#comment-box').html(text);
            },
            error: function(req, status, err) {
                console.log(err);
                console.log(status);
            }

        })
}


function commentEdit(e) {
    console.log(e);
    let target = $(e).parent();
    let content = target.children('.content').text();
    console.log(content);
    let tm = replacetoRN(content);   
    let form = '<form id="'+ e.id +'" name="commentEditForm">'+ csrf_input + '<textarea cols="40" rows="4" style="resize:none;" name="content">'+ tm +'</textarea><input type="button" value="수정" onclick="return editFormSubmit(this)"><input pk="'+ e.id +'" type="button" value="취소" onclick="getComment(this)"></form>';

    target.html(form);
}

function commentEditSubmit(e) {
    let param = $('form[name=commentEditForm]').serialize();
        $.ajax({
            type: 'POST',
            url: '/updatecomment/'+$('form[name=commentEditForm]').id,
            data : param,
            datatype: 'json',

            success: function(res) {
                 console.log(res);
            },
            error: function(req, status, err) {
                console.log(err);
                console.log(status);
            }

        })
}

function getComment(e) {
    $.ajax({
        type: 'GET',
        url: '/getcomment/'+$(e).attr('pk'),
        datatype: 'json',

        success: function(res) {
            console.log(res);
            let text =Array();
            let pk = res[0].pk;
            let content = res[0].fields['content'];
            let star = res[0].fields['star'];
            let user = res[0].fields.author[0];
            if (current_user == user) {
                tmp = user +'<a href="/deletecomment/'+ pk +'"> 삭제 </a><a id="'+ pk +'" href="javascript:" onclick="commentEdit(this)"> 수정 </a><div>'+ star.toFixed(1) +'</div><div class="content">'+ content +'</div>'
            } else {
                tmp = user +'<div>'+ star.toFixed(1) +'</div><div class="content">'+ content +'</div><hr>'
            }
            text.push(tmp);
            console.log(text);
            $(e).parent().parent().html(text);
        },
        error: function(req, err) {
            console.log(err);
        }

    })
}