$(document).ready(function () {
  const list = '<li>Item</li>';
  $('DIV#add_item').click(function () {
    $('UL.my_list').append(list);
  });
  $('DIV#remove_item').click(function () {
    $('UL.my_list li').last().remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list li').remove();
  });
});
