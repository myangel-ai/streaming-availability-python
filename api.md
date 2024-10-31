# Countries

Types:

```python
from streaming_availability.types import CountryRetrieveResponse, CountryListResponse
```

Methods:

- <code title="get /countries/{country-code}">client.countries.<a href="./src/streaming_availability/resources/countries.py">retrieve</a>(country_code, \*\*<a href="src/streaming_availability/types/country_retrieve_params.py">params</a>) -> <a href="./src/streaming_availability/types/country_retrieve_response.py">CountryRetrieveResponse</a></code>
- <code title="get /countries">client.countries.<a href="./src/streaming_availability/resources/countries.py">list</a>(\*\*<a href="src/streaming_availability/types/country_list_params.py">params</a>) -> <a href="./src/streaming_availability/types/country_list_response.py">CountryListResponse</a></code>

# Genres

Types:

```python
from streaming_availability.types import GenreListResponse
```

Methods:

- <code title="get /genres">client.genres.<a href="./src/streaming_availability/resources/genres.py">list</a>(\*\*<a href="src/streaming_availability/types/genre_list_params.py">params</a>) -> <a href="./src/streaming_availability/types/genre_list_response.py">GenreListResponse</a></code>

# Shows

Types:

```python
from streaming_availability.types import (
    ShowRetrieveResponse,
    ShowSearchFiltersResponse,
    ShowSearchTitleResponse,
    ShowTopResponse,
)
```

Methods:

- <code title="get /shows/{id}">client.shows.<a href="./src/streaming_availability/resources/shows.py">retrieve</a>(id, \*\*<a href="src/streaming_availability/types/show_retrieve_params.py">params</a>) -> <a href="./src/streaming_availability/types/show_retrieve_response.py">ShowRetrieveResponse</a></code>
- <code title="get /shows/search/filters">client.shows.<a href="./src/streaming_availability/resources/shows.py">search_filters</a>(\*\*<a href="src/streaming_availability/types/show_search_filters_params.py">params</a>) -> <a href="./src/streaming_availability/types/show_search_filters_response.py">ShowSearchFiltersResponse</a></code>
- <code title="get /shows/search/title">client.shows.<a href="./src/streaming_availability/resources/shows.py">search_title</a>(\*\*<a href="src/streaming_availability/types/show_search_title_params.py">params</a>) -> <a href="./src/streaming_availability/types/show_search_title_response.py">ShowSearchTitleResponse</a></code>
- <code title="get /shows/top">client.shows.<a href="./src/streaming_availability/resources/shows.py">top</a>(\*\*<a href="src/streaming_availability/types/show_top_params.py">params</a>) -> <a href="./src/streaming_availability/types/show_top_response.py">ShowTopResponse</a></code>

# Changes

Types:

```python
from streaming_availability.types import ChangeListResponse
```

Methods:

- <code title="get /changes">client.changes.<a href="./src/streaming_availability/resources/changes.py">list</a>(\*\*<a href="src/streaming_availability/types/change_list_params.py">params</a>) -> <a href="./src/streaming_availability/types/change_list_response.py">ChangeListResponse</a></code>
