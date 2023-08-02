class MapMagic:
    __map_open = "I solemnly swear that I am up to no good."
    __map_close = "Mischief managed."


class MarauderMap(MapMagic):
    __films_titles = {
        "results": [
            {
                "imdb_id": "tt1201607",
                "title": "Harry Potter and the Deathly Hallows: Part 2"
            },
            {
                "imdb_id": "tt0241527",
                "title": "Harry Potter and the Sorcerer's Stone"
            },
            {
                "imdb_id": "tt0926084",
                "title": "Harry Potter and the Deathly Hallows: Part 1"
            },
            {
                "imdb_id": "tt0304141",
                "title": "Harry Potter and the Prisoner of Azkaban"
            },
            {
                "imdb_id": "tt0417741",
                "title": "Harry Potter and the Half-Blood Prince"
            },
            {
                "imdb_id": "tt0295297",
                "title": "Harry Potter and the Chamber of Secrets"
            },
            {
                "imdb_id": "tt0330373",
                "title": "Harry Potter and the Goblet of Fire"
            },
            {
                "imdb_id": "tt0373889",
                "title": "Harry Potter and the Order of the Phoenix"
            }
        ]
    }

    def __init__(self, path='json_file.json'):
        self.path = path
        self.__create_json()

    def __create_json(self):
        import json
        from vars import films_awards
        json_data = json.dumps(films_awards, indent=4)
        with open(self.path, 'w') as json_file:
            json_file.write(json_data)

    def map_generator(self):
        import json
        from pprint import pprint
        print(MapMagic._MapMagic__map_open)

        with open(self.path, 'r') as json_file:
            films_titles_dict = json.load(json_file)

        films = films_titles_dict
        film_titles = self.__films_titles['results']

        films_list = []

        for film_title in film_titles:
            movie_title = film_title['title'].replace(":", "")
            movie_awards = []
            for film in films:
                for result in film['results']:
                    if result['movie']['imdb_id'] == film_title['imdb_id']:
                        award_dict = {
                            'type': result['type'],
                            'award_name': result['award_name'],
                            'award': result['award']
                        }
                        movie_awards.append(award_dict)
            sorted_movie_awards = sorted(movie_awards, key=lambda x: x['award_name'])
            films_list.append({movie_title: sorted_movie_awards})

        pprint(films_list)

        print(MapMagic._MapMagic__map_close)
