# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ShowRetrieveResponse",
    "Genre",
    "ImageSet",
    "ImageSetHorizontalPoster",
    "ImageSetVerticalPoster",
    "ImageSetHorizontalBackdrop",
    "ImageSetVerticalBackdrop",
    "StreamingOption",
    "StreamingOptionAudio",
    "StreamingOptionService",
    "StreamingOptionServiceImageSet",
    "StreamingOptionSubtitle",
    "StreamingOptionSubtitleLocale",
    "StreamingOptionAddon",
    "StreamingOptionAddonImageSet",
    "StreamingOptionPrice",
    "Season",
    "SeasonStreamingOption",
    "SeasonStreamingOptionAudio",
    "SeasonStreamingOptionService",
    "SeasonStreamingOptionServiceImageSet",
    "SeasonStreamingOptionSubtitle",
    "SeasonStreamingOptionSubtitleLocale",
    "SeasonStreamingOptionAddon",
    "SeasonStreamingOptionAddonImageSet",
    "SeasonStreamingOptionPrice",
    "SeasonEpisode",
    "SeasonEpisodeStreamingOption",
    "SeasonEpisodeStreamingOptionAudio",
    "SeasonEpisodeStreamingOptionService",
    "SeasonEpisodeStreamingOptionServiceImageSet",
    "SeasonEpisodeStreamingOptionSubtitle",
    "SeasonEpisodeStreamingOptionSubtitleLocale",
    "SeasonEpisodeStreamingOptionAddon",
    "SeasonEpisodeStreamingOptionAddonImageSet",
    "SeasonEpisodeStreamingOptionPrice",
]


class Genre(BaseModel):
    id: str
    """Id of the genre"""

    name: str
    """Name of the genre"""


class ImageSetHorizontalPoster(BaseModel):
    w1080: str
    """Link to the 1080px wide version of the image."""

    w1440: str
    """Link to the 1440px wide version of the image."""

    w360: str
    """Link to the 360px wide version of the image."""

    w480: str
    """Link to the 480px wide version of the image."""

    w720: str
    """Link to the 720px wide version of the image."""


class ImageSetVerticalPoster(BaseModel):
    w240: str
    """Link to the 240px wide version of the image."""

    w360: str
    """Link to the 360px wide version of the image."""

    w480: str
    """Link to the 480px wide version of the image."""

    w600: str
    """Link to the 600px wide version of the image."""

    w720: str
    """Link to the 720px wide version of the image."""


class ImageSetHorizontalBackdrop(BaseModel):
    w1080: str
    """Link to the 1080px wide version of the image."""

    w1440: str
    """Link to the 1440px wide version of the image."""

    w360: str
    """Link to the 360px wide version of the image."""

    w480: str
    """Link to the 480px wide version of the image."""

    w720: str
    """Link to the 720px wide version of the image."""


class ImageSetVerticalBackdrop(BaseModel):
    w240: str
    """Link to the 240px wide version of the image."""

    w360: str
    """Link to the 360px wide version of the image."""

    w480: str
    """Link to the 480px wide version of the image."""

    w600: str
    """Link to the 600px wide version of the image."""

    w720: str
    """Link to the 720px wide version of the image."""


class ImageSet(BaseModel):
    horizontal_poster: ImageSetHorizontalPoster = FieldInfo(alias="horizontalPoster")
    """Horizontal poster of the show."""

    vertical_poster: ImageSetVerticalPoster = FieldInfo(alias="verticalPoster")
    """Vertical poster of the show."""

    horizontal_backdrop: Optional[ImageSetHorizontalBackdrop] = FieldInfo(alias="horizontalBackdrop", default=None)
    """Horizontal backdrop of the show."""

    vertical_backdrop: Optional[ImageSetVerticalBackdrop] = FieldInfo(alias="verticalBackdrop", default=None)
    """Vertical backdrop of the show."""


class StreamingOptionAudio(BaseModel):
    language: str
    """
    [ISO 639-2](https://en.wikipedia.org/wiki/ISO_639-2) code of the associated
    language with the locale.
    """

    region: Optional[str] = None
    """
    [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of
    the country, or [UN M49](https://en.wikipedia.org/wiki/UN_M49) code of the area
    associated with the locale.
    """


class StreamingOptionServiceImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class StreamingOptionService(BaseModel):
    id: str
    """Id of the service."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the service."""

    image_set: StreamingOptionServiceImageSet = FieldInfo(alias="imageSet")
    """Image set of the service."""

    name: str
    """Name of the service."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the service."""


class StreamingOptionSubtitleLocale(BaseModel):
    language: str
    """
    [ISO 639-2](https://en.wikipedia.org/wiki/ISO_639-2) code of the associated
    language with the locale.
    """

    region: Optional[str] = None
    """
    [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of
    the country, or [UN M49](https://en.wikipedia.org/wiki/UN_M49) code of the area
    associated with the locale.
    """


class StreamingOptionSubtitle(BaseModel):
    closed_captions: bool = FieldInfo(alias="closedCaptions")
    """Whether closed captions are available for the subtitle."""

    locale: StreamingOptionSubtitleLocale
    """A language and optionally an associated region."""


class StreamingOptionAddonImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class StreamingOptionAddon(BaseModel):
    id: str
    """Id of the addon."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the addon."""

    image_set: StreamingOptionAddonImageSet = FieldInfo(alias="imageSet")
    """Image set of the addon."""

    name: str
    """Name of the addon."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the addon."""


class StreamingOptionPrice(BaseModel):
    amount: str
    """Numerical amount of the price."""

    currency: str
    """
    [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) alphabetic code of the
    currency.
    """

    formatted: str
    """Formatted price, including both the amount and the currency."""


class StreamingOption(BaseModel):
    audios: List[StreamingOptionAudio]
    """Array of the available audios."""

    available_since: int = FieldInfo(alias="availableSince")
    """
    [Unix Time Stamp](https://www.unixtimestamp.com/) of the date that this
    streaming option was detected.
    """

    expires_soon: bool = FieldInfo(alias="expiresSoon")
    """Whether the streaming option expires within a month."""

    link: str
    """
    Deep link to the streaming option's page in the web app of the streaming
    service. Unlike videoLink, this field is guaranteed to be populated.
    """

    service: StreamingOptionService
    """Details of the streaming service localized according to the parent country."""

    subtitles: List[StreamingOptionSubtitle]
    """Array of the available subtitles."""

    type: Literal["free", "subscription", "buy", "rent", "addon"]
    """Type of the streaming option."""

    addon: Optional[StreamingOptionAddon] = None
    """
    Addon that the streaming option is available through. Omitted if the streaming
    option is not available through an addon.
    """

    expires_on: Optional[int] = FieldInfo(alias="expiresOn", default=None)
    """
    [Unix Time Stamp](https://www.unixtimestamp.com/) of the date that the streaming
    option is expiring. In other words, last day to watch.
    """

    price: Optional[StreamingOptionPrice] = None
    """Price of the renting or buying the item.

    A movie and an episode that is available to buy or rent will always have a
    price.

    A series or a season that is available to buy or rent may have a price or not.
    If the price is available, that means the entire series or the season can be
    bought or rented as a whole for the given price. If the price is null, that
    means sub-items of the series or the season are available to buy or rent, but it
    is not possible to buy or rent the entire series or the season as a whole at
    once. In this case, the price of the sub-items can be found in the episodes or
    seasons array.
    """

    quality: Optional[Literal["sd", "hd", "qhd", "uhd"]] = None
    """Maximum supported video quality of the streaming option."""

    video_link: Optional[str] = FieldInfo(alias="videoLink", default=None)
    """
    Deep link to the video associated with the streaming option. Omitted if there's
    no direct link to the video. Might have the same value as link.
    """


class SeasonStreamingOptionAudio(BaseModel):
    language: str
    """
    [ISO 639-2](https://en.wikipedia.org/wiki/ISO_639-2) code of the associated
    language with the locale.
    """

    region: Optional[str] = None
    """
    [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of
    the country, or [UN M49](https://en.wikipedia.org/wiki/UN_M49) code of the area
    associated with the locale.
    """


class SeasonStreamingOptionServiceImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class SeasonStreamingOptionService(BaseModel):
    id: str
    """Id of the service."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the service."""

    image_set: SeasonStreamingOptionServiceImageSet = FieldInfo(alias="imageSet")
    """Image set of the service."""

    name: str
    """Name of the service."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the service."""


class SeasonStreamingOptionSubtitleLocale(BaseModel):
    language: str
    """
    [ISO 639-2](https://en.wikipedia.org/wiki/ISO_639-2) code of the associated
    language with the locale.
    """

    region: Optional[str] = None
    """
    [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of
    the country, or [UN M49](https://en.wikipedia.org/wiki/UN_M49) code of the area
    associated with the locale.
    """


class SeasonStreamingOptionSubtitle(BaseModel):
    closed_captions: bool = FieldInfo(alias="closedCaptions")
    """Whether closed captions are available for the subtitle."""

    locale: SeasonStreamingOptionSubtitleLocale
    """A language and optionally an associated region."""


class SeasonStreamingOptionAddonImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class SeasonStreamingOptionAddon(BaseModel):
    id: str
    """Id of the addon."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the addon."""

    image_set: SeasonStreamingOptionAddonImageSet = FieldInfo(alias="imageSet")
    """Image set of the addon."""

    name: str
    """Name of the addon."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the addon."""


class SeasonStreamingOptionPrice(BaseModel):
    amount: str
    """Numerical amount of the price."""

    currency: str
    """
    [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) alphabetic code of the
    currency.
    """

    formatted: str
    """Formatted price, including both the amount and the currency."""


class SeasonStreamingOption(BaseModel):
    audios: List[SeasonStreamingOptionAudio]
    """Array of the available audios."""

    available_since: int = FieldInfo(alias="availableSince")
    """
    [Unix Time Stamp](https://www.unixtimestamp.com/) of the date that this
    streaming option was detected.
    """

    expires_soon: bool = FieldInfo(alias="expiresSoon")
    """Whether the streaming option expires within a month."""

    link: str
    """
    Deep link to the streaming option's page in the web app of the streaming
    service. Unlike videoLink, this field is guaranteed to be populated.
    """

    service: SeasonStreamingOptionService
    """Details of the streaming service localized according to the parent country."""

    subtitles: List[SeasonStreamingOptionSubtitle]
    """Array of the available subtitles."""

    type: Literal["free", "subscription", "buy", "rent", "addon"]
    """Type of the streaming option."""

    addon: Optional[SeasonStreamingOptionAddon] = None
    """
    Addon that the streaming option is available through. Omitted if the streaming
    option is not available through an addon.
    """

    expires_on: Optional[int] = FieldInfo(alias="expiresOn", default=None)
    """
    [Unix Time Stamp](https://www.unixtimestamp.com/) of the date that the streaming
    option is expiring. In other words, last day to watch.
    """

    price: Optional[SeasonStreamingOptionPrice] = None
    """Price of the renting or buying the item.

    A movie and an episode that is available to buy or rent will always have a
    price.

    A series or a season that is available to buy or rent may have a price or not.
    If the price is available, that means the entire series or the season can be
    bought or rented as a whole for the given price. If the price is null, that
    means sub-items of the series or the season are available to buy or rent, but it
    is not possible to buy or rent the entire series or the season as a whole at
    once. In this case, the price of the sub-items can be found in the episodes or
    seasons array.
    """

    quality: Optional[Literal["sd", "hd", "qhd", "uhd"]] = None
    """Maximum supported video quality of the streaming option."""

    video_link: Optional[str] = FieldInfo(alias="videoLink", default=None)
    """
    Deep link to the video associated with the streaming option. Omitted if there's
    no direct link to the video. Might have the same value as link.
    """


class SeasonEpisodeStreamingOptionAudio(BaseModel):
    language: str
    """
    [ISO 639-2](https://en.wikipedia.org/wiki/ISO_639-2) code of the associated
    language with the locale.
    """

    region: Optional[str] = None
    """
    [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of
    the country, or [UN M49](https://en.wikipedia.org/wiki/UN_M49) code of the area
    associated with the locale.
    """


class SeasonEpisodeStreamingOptionServiceImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class SeasonEpisodeStreamingOptionService(BaseModel):
    id: str
    """Id of the service."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the service."""

    image_set: SeasonEpisodeStreamingOptionServiceImageSet = FieldInfo(alias="imageSet")
    """Image set of the service."""

    name: str
    """Name of the service."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the service."""


class SeasonEpisodeStreamingOptionSubtitleLocale(BaseModel):
    language: str
    """
    [ISO 639-2](https://en.wikipedia.org/wiki/ISO_639-2) code of the associated
    language with the locale.
    """

    region: Optional[str] = None
    """
    [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of
    the country, or [UN M49](https://en.wikipedia.org/wiki/UN_M49) code of the area
    associated with the locale.
    """


class SeasonEpisodeStreamingOptionSubtitle(BaseModel):
    closed_captions: bool = FieldInfo(alias="closedCaptions")
    """Whether closed captions are available for the subtitle."""

    locale: SeasonEpisodeStreamingOptionSubtitleLocale
    """A language and optionally an associated region."""


class SeasonEpisodeStreamingOptionAddonImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class SeasonEpisodeStreamingOptionAddon(BaseModel):
    id: str
    """Id of the addon."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the addon."""

    image_set: SeasonEpisodeStreamingOptionAddonImageSet = FieldInfo(alias="imageSet")
    """Image set of the addon."""

    name: str
    """Name of the addon."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the addon."""


class SeasonEpisodeStreamingOptionPrice(BaseModel):
    amount: str
    """Numerical amount of the price."""

    currency: str
    """
    [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) alphabetic code of the
    currency.
    """

    formatted: str
    """Formatted price, including both the amount and the currency."""


class SeasonEpisodeStreamingOption(BaseModel):
    audios: List[SeasonEpisodeStreamingOptionAudio]
    """Array of the available audios."""

    available_since: int = FieldInfo(alias="availableSince")
    """
    [Unix Time Stamp](https://www.unixtimestamp.com/) of the date that this
    streaming option was detected.
    """

    expires_soon: bool = FieldInfo(alias="expiresSoon")
    """Whether the streaming option expires within a month."""

    link: str
    """
    Deep link to the streaming option's page in the web app of the streaming
    service. Unlike videoLink, this field is guaranteed to be populated.
    """

    service: SeasonEpisodeStreamingOptionService
    """Details of the streaming service localized according to the parent country."""

    subtitles: List[SeasonEpisodeStreamingOptionSubtitle]
    """Array of the available subtitles."""

    type: Literal["free", "subscription", "buy", "rent", "addon"]
    """Type of the streaming option."""

    addon: Optional[SeasonEpisodeStreamingOptionAddon] = None
    """
    Addon that the streaming option is available through. Omitted if the streaming
    option is not available through an addon.
    """

    expires_on: Optional[int] = FieldInfo(alias="expiresOn", default=None)
    """
    [Unix Time Stamp](https://www.unixtimestamp.com/) of the date that the streaming
    option is expiring. In other words, last day to watch.
    """

    price: Optional[SeasonEpisodeStreamingOptionPrice] = None
    """Price of the renting or buying the item.

    A movie and an episode that is available to buy or rent will always have a
    price.

    A series or a season that is available to buy or rent may have a price or not.
    If the price is available, that means the entire series or the season can be
    bought or rented as a whole for the given price. If the price is null, that
    means sub-items of the series or the season are available to buy or rent, but it
    is not possible to buy or rent the entire series or the season as a whole at
    once. In this case, the price of the sub-items can be found in the episodes or
    seasons array.
    """

    quality: Optional[Literal["sd", "hd", "qhd", "uhd"]] = None
    """Maximum supported video quality of the streaming option."""

    video_link: Optional[str] = FieldInfo(alias="videoLink", default=None)
    """
    Deep link to the video associated with the streaming option. Omitted if there's
    no direct link to the video. Might have the same value as link.
    """


class SeasonEpisode(BaseModel):
    air_year: int = FieldInfo(alias="airYear")
    """The year that the episode aired."""

    item_type: Literal["episode"] = FieldInfo(alias="itemType")
    """Type of the item. Always episode."""

    streaming_options: Dict[str, List[SeasonEpisodeStreamingOption]] = FieldInfo(alias="streamingOptions")
    """Map of the streaming options by the country code."""

    title: str
    """Title of the episode."""

    overview: Optional[str] = None
    """A brief overview of the plot of the episode."""


class Season(BaseModel):
    first_air_year: int = FieldInfo(alias="firstAirYear")
    """The first year that the season aired."""

    item_type: Literal["season"] = FieldInfo(alias="itemType")
    """Type of the item. Always season."""

    last_air_year: int = FieldInfo(alias="lastAirYear")
    """The last year that the season aired."""

    streaming_options: Dict[str, List[SeasonStreamingOption]] = FieldInfo(alias="streamingOptions")
    """Map of the streaming options by the country code."""

    title: str
    """Title of the season."""

    episodes: Optional[List[SeasonEpisode]] = None
    """Array of the episodes belong to the season."""


class ShowRetrieveResponse(BaseModel):
    id: str
    """Id of the show."""

    cast: List[str]
    """Array of the cast of the show."""

    genres: List[Genre]
    """Array of the genres of the show."""

    image_set: ImageSet = FieldInfo(alias="imageSet")
    """Image set of the show."""

    imdb_id: str = FieldInfo(alias="imdbId")
    """[IMDb](https://www.imdb.com/) id of the show."""

    item_type: Literal["show"] = FieldInfo(alias="itemType")
    """Type of the item. Always show."""

    original_title: str = FieldInfo(alias="originalTitle")
    """Original title of the show."""

    overview: str
    """A brief overview of the overall plot of the show."""

    rating: int
    """Rating of the show.

    This is calculated by taking the average of ratings found online from multiple
    sources.
    """

    show_type: Literal["movie", "series"] = FieldInfo(alias="showType")
    """Type of the show. Based on the type, some properties might be omitted."""

    streaming_options: Dict[str, List[StreamingOption]] = FieldInfo(alias="streamingOptions")
    """Map of the streaming options by the country code."""

    title: str
    """Title of the show."""

    tmdb_id: str = FieldInfo(alias="tmdbId")
    """[TMDB](https://www.themoviedb.org/) id of the show."""

    creators: Optional[List[str]] = None
    """Array of the creators of the series."""

    directors: Optional[List[str]] = None
    """Array of the directors of the movie."""

    episode_count: Optional[int] = FieldInfo(alias="episodeCount", default=None)
    """Number of episodes that are either aired or announced for a series."""

    first_air_year: Optional[int] = FieldInfo(alias="firstAirYear", default=None)
    """The first year that the series aired."""

    last_air_year: Optional[int] = FieldInfo(alias="lastAirYear", default=None)
    """The last year that the series aired."""

    release_year: Optional[int] = FieldInfo(alias="releaseYear", default=None)
    """The year that the movie was released."""

    runtime: Optional[int] = None
    """Runtime of the movie in minutes."""

    season_count: Optional[int] = FieldInfo(alias="seasonCount", default=None)
    """Number of seasons that are either aired or announced for a series."""

    seasons: Optional[List[Season]] = None
    """Array of the seasons belong to the series."""
