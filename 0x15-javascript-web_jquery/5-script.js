$('DIV#add_item').click(() => {
  const val = '<li>Item</li>';
  $('UL.my_list').append(val);
});
