$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  dataType: 'json'
}).done((content) => {
  for (const list of content.results) {
    $('UL#list_movies').append('<li>' + list.title + '</li>');
  }
});
