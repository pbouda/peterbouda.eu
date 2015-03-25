function reply(id)
{
    id = decodeURIComponent(id);
    $('#commentForm_replyto').val(id);
}

$(document).ready(function() {
    function generateMailToLink()
    {
        var user = 'pbouda'; //user@domain = your email address
        var domain = 'outlook.com';
        var subject = 'Comment for \'' + $('#commentForm_replytoSlug').val() + '\'' ;

        var d = new Date();
        var body = ''
            + 'Hey,\nI posted a new comment on ' + document.URL + '\n\nGreetings ' + $("#commentForm_inputName").val() + '\n\n\n'
            + 'Raw comment data:\n'
            + '----------------------------------------\n'
            + 'date: ' + d.getFullYear() + '-' + (d.getMonth()+1) + '-' + d.getDate() + ' ' + d.getHours() + ':' + d.getMinutes() + '\n'
            + 'author: ' + $("#commentForm_inputName").val() + '\n'
            + 'site: ' + $("#commentForm_inputSite").val() + '\n';

        var replyto = $('#commentForm_replyto').val();
        if (replyto.length != 0)
        {
            body += 'replyto: ' + replyto + '\n'
        }

        body += '\n'
            + $("#commentForm_inputText").val() + '\n'
            + '----------------------------------------\n';

        var link = 'mailto:' + user + '@' + domain + '?subject='
            + encodeURIComponent(subject)
            + "&body="
            + encodeURIComponent(body);
        return link;
    }


    $('#commentForm').on("submit",
        function( event )
        {
            event.preventDefault();
            $(location).attr('href', generateMailToLink());
        }
    );
});
