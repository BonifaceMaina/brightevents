$('#submit').click(function(event) {
    event.preventDefault();
    $.post(url, data=$('#eventform').serialize(), function(data) {
      if (data.status == 'ok') {
        $('#modal').modal('hide');
        location.reload();
      }
      else {
        $('#modal .modal-content').html(data);
      }
    });
  })