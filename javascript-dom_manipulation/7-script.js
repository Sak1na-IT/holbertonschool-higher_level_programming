fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    const movies = data.results;
    const listMovies = document.querySelector('#list_movies');
    
    movies.forEach(function (movie) {
      const li = document.createElement('li');
      li.textContent = movie.title;
      listMovies.appendChild(li);
    });
  });
