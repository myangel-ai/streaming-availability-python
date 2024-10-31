# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ShowSearchTitleResponse",
    "ShowSearchTitleResponseItem",
    "ShowSearchTitleResponseItemGenre",
    "ShowSearchTitleResponseItemImageSet",
    "ShowSearchTitleResponseItemImageSetHorizontalPoster",
    "ShowSearchTitleResponseItemImageSetVerticalPoster",
    "ShowSearchTitleResponseItemImageSetHorizontalBackdrop",
    "ShowSearchTitleResponseItemImageSetVerticalBackdrop",
    "ShowSearchTitleResponseItemStreamingOption",
    "ShowSearchTitleResponseItemStreamingOptionAudio",
    "ShowSearchTitleResponseItemStreamingOptionService",
    "ShowSearchTitleResponseItemStreamingOptionServiceImageSet",
    "ShowSearchTitleResponseItemStreamingOptionSubtitle",
    "ShowSearchTitleResponseItemStreamingOptionSubtitleLocale",
    "ShowSearchTitleResponseItemStreamingOptionAddon",
    "ShowSearchTitleResponseItemStreamingOptionAddonImageSet",
    "ShowSearchTitleResponseItemStreamingOptionPrice",
    "ShowSearchTitleResponseItemSeason",
    "ShowSearchTitleResponseItemSeasonStreamingOption",
    "ShowSearchTitleResponseItemSeasonStreamingOptionAudio",
    "ShowSearchTitleResponseItemSeasonStreamingOptionService",
    "ShowSearchTitleResponseItemSeasonStreamingOptionServiceImageSet",
    "ShowSearchTitleResponseItemSeasonStreamingOptionSubtitle",
    "ShowSearchTitleResponseItemSeasonStreamingOptionSubtitleLocale",
    "ShowSearchTitleResponseItemSeasonStreamingOptionAddon",
    "ShowSearchTitleResponseItemSeasonStreamingOptionAddonImageSet",
    "ShowSearchTitleResponseItemSeasonStreamingOptionPrice",
    "ShowSearchTitleResponseItemSeasonEpisode",
    "ShowSearchTitleResponseItemSeasonEpisodeStreamingOption",
    "ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionAudio",
    "ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionService",
    "ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionServiceImageSet",
    "ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionSubtitle",
    "ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionSubtitleLocale",
    "ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionAddon",
    "ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionAddonImageSet",
    "ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionPrice",
]


class ShowSearchTitleResponseItemGenre(BaseModel):
    id: str
    """Id of the genre"""

    name: str
    """Name of the genre"""


class ShowSearchTitleResponseItemImageSetHorizontalPoster(BaseModel):
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


class ShowSearchTitleResponseItemImageSetVerticalPoster(BaseModel):
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


class ShowSearchTitleResponseItemImageSetHorizontalBackdrop(BaseModel):
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


class ShowSearchTitleResponseItemImageSetVerticalBackdrop(BaseModel):
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


class ShowSearchTitleResponseItemImageSet(BaseModel):
    horizontal_poster: ShowSearchTitleResponseItemImageSetHorizontalPoster = FieldInfo(alias="horizontalPoster")
    """Horizontal poster of the show."""

    vertical_poster: ShowSearchTitleResponseItemImageSetVerticalPoster = FieldInfo(alias="verticalPoster")
    """Vertical poster of the show."""

    horizontal_backdrop: Optional[ShowSearchTitleResponseItemImageSetHorizontalBackdrop] = FieldInfo(
        alias="horizontalBackdrop", default=None
    )
    """Horizontal backdrop of the show."""

    vertical_backdrop: Optional[ShowSearchTitleResponseItemImageSetVerticalBackdrop] = FieldInfo(
        alias="verticalBackdrop", default=None
    )
    """Vertical backdrop of the show."""


class ShowSearchTitleResponseItemStreamingOptionAudio(BaseModel):
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


class ShowSearchTitleResponseItemStreamingOptionServiceImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class ShowSearchTitleResponseItemStreamingOptionService(BaseModel):
    id: str
    """Id of the service."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the service."""

    image_set: ShowSearchTitleResponseItemStreamingOptionServiceImageSet = FieldInfo(alias="imageSet")
    """Image set of the service."""

    name: str
    """Name of the service."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the service."""


class ShowSearchTitleResponseItemStreamingOptionSubtitleLocale(BaseModel):
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


class ShowSearchTitleResponseItemStreamingOptionSubtitle(BaseModel):
    closed_captions: bool = FieldInfo(alias="closedCaptions")
    """Whether closed captions are available for the subtitle."""

    locale: ShowSearchTitleResponseItemStreamingOptionSubtitleLocale
    """A language and optionally an associated region."""


class ShowSearchTitleResponseItemStreamingOptionAddonImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class ShowSearchTitleResponseItemStreamingOptionAddon(BaseModel):
    id: str
    """Id of the addon."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the addon."""

    image_set: ShowSearchTitleResponseItemStreamingOptionAddonImageSet = FieldInfo(alias="imageSet")
    """Image set of the addon."""

    name: str
    """Name of the addon."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the addon."""


class ShowSearchTitleResponseItemStreamingOptionPrice(BaseModel):
    amount: str
    """Numerical amount of the price."""

    currency: str
    """
    [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) alphabetic code of the
    currency.
    """

    formatted: str
    """Formatted price, including both the amount and the currency."""


class ShowSearchTitleResponseItemStreamingOption(BaseModel):
    audios: List[ShowSearchTitleResponseItemStreamingOptionAudio]
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

    service: ShowSearchTitleResponseItemStreamingOptionService
    """Details of the streaming service localized according to the parent country."""

    subtitles: List[ShowSearchTitleResponseItemStreamingOptionSubtitle]
    """Array of the available subtitles."""

    type: Literal["free", "subscription", "buy", "rent", "addon"]
    """Type of the streaming option."""

    addon: Optional[ShowSearchTitleResponseItemStreamingOptionAddon] = None
    """
    Addon that the streaming option is available through. Omitted if the streaming
    option is not available through an addon.
    """

    expires_on: Optional[int] = FieldInfo(alias="expiresOn", default=None)
    """
    [Unix Time Stamp](https://www.unixtimestamp.com/) of the date that the streaming
    option is expiring. In other words, last day to watch.
    """

    price: Optional[ShowSearchTitleResponseItemStreamingOptionPrice] = None
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


class ShowSearchTitleResponseItemSeasonStreamingOptionAudio(BaseModel):
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


class ShowSearchTitleResponseItemSeasonStreamingOptionServiceImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class ShowSearchTitleResponseItemSeasonStreamingOptionService(BaseModel):
    id: str
    """Id of the service."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the service."""

    image_set: ShowSearchTitleResponseItemSeasonStreamingOptionServiceImageSet = FieldInfo(alias="imageSet")
    """Image set of the service."""

    name: str
    """Name of the service."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the service."""


class ShowSearchTitleResponseItemSeasonStreamingOptionSubtitleLocale(BaseModel):
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


class ShowSearchTitleResponseItemSeasonStreamingOptionSubtitle(BaseModel):
    closed_captions: bool = FieldInfo(alias="closedCaptions")
    """Whether closed captions are available for the subtitle."""

    locale: ShowSearchTitleResponseItemSeasonStreamingOptionSubtitleLocale
    """A language and optionally an associated region."""


class ShowSearchTitleResponseItemSeasonStreamingOptionAddonImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class ShowSearchTitleResponseItemSeasonStreamingOptionAddon(BaseModel):
    id: str
    """Id of the addon."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the addon."""

    image_set: ShowSearchTitleResponseItemSeasonStreamingOptionAddonImageSet = FieldInfo(alias="imageSet")
    """Image set of the addon."""

    name: str
    """Name of the addon."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the addon."""


class ShowSearchTitleResponseItemSeasonStreamingOptionPrice(BaseModel):
    amount: str
    """Numerical amount of the price."""

    currency: str
    """
    [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) alphabetic code of the
    currency.
    """

    formatted: str
    """Formatted price, including both the amount and the currency."""


class ShowSearchTitleResponseItemSeasonStreamingOption(BaseModel):
    audios: List[ShowSearchTitleResponseItemSeasonStreamingOptionAudio]
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

    service: ShowSearchTitleResponseItemSeasonStreamingOptionService
    """Details of the streaming service localized according to the parent country."""

    subtitles: List[ShowSearchTitleResponseItemSeasonStreamingOptionSubtitle]
    """Array of the available subtitles."""

    type: Literal["free", "subscription", "buy", "rent", "addon"]
    """Type of the streaming option."""

    addon: Optional[ShowSearchTitleResponseItemSeasonStreamingOptionAddon] = None
    """
    Addon that the streaming option is available through. Omitted if the streaming
    option is not available through an addon.
    """

    expires_on: Optional[int] = FieldInfo(alias="expiresOn", default=None)
    """
    [Unix Time Stamp](https://www.unixtimestamp.com/) of the date that the streaming
    option is expiring. In other words, last day to watch.
    """

    price: Optional[ShowSearchTitleResponseItemSeasonStreamingOptionPrice] = None
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


class ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionAudio(BaseModel):
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


class ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionServiceImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionService(BaseModel):
    id: str
    """Id of the service."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the service."""

    image_set: ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionServiceImageSet = FieldInfo(alias="imageSet")
    """Image set of the service."""

    name: str
    """Name of the service."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the service."""


class ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionSubtitleLocale(BaseModel):
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


class ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionSubtitle(BaseModel):
    closed_captions: bool = FieldInfo(alias="closedCaptions")
    """Whether closed captions are available for the subtitle."""

    locale: ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionSubtitleLocale
    """A language and optionally an associated region."""


class ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionAddonImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionAddon(BaseModel):
    id: str
    """Id of the addon."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the addon."""

    image_set: ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionAddonImageSet = FieldInfo(alias="imageSet")
    """Image set of the addon."""

    name: str
    """Name of the addon."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the addon."""


class ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionPrice(BaseModel):
    amount: str
    """Numerical amount of the price."""

    currency: str
    """
    [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) alphabetic code of the
    currency.
    """

    formatted: str
    """Formatted price, including both the amount and the currency."""


class ShowSearchTitleResponseItemSeasonEpisodeStreamingOption(BaseModel):
    audios: List[ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionAudio]
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

    service: ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionService
    """Details of the streaming service localized according to the parent country."""

    subtitles: List[ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionSubtitle]
    """Array of the available subtitles."""

    type: Literal["free", "subscription", "buy", "rent", "addon"]
    """Type of the streaming option."""

    addon: Optional[ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionAddon] = None
    """
    Addon that the streaming option is available through. Omitted if the streaming
    option is not available through an addon.
    """

    expires_on: Optional[int] = FieldInfo(alias="expiresOn", default=None)
    """
    [Unix Time Stamp](https://www.unixtimestamp.com/) of the date that the streaming
    option is expiring. In other words, last day to watch.
    """

    price: Optional[ShowSearchTitleResponseItemSeasonEpisodeStreamingOptionPrice] = None
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


class ShowSearchTitleResponseItemSeasonEpisode(BaseModel):
    air_year: int = FieldInfo(alias="airYear")
    """The year that the episode aired."""

    item_type: Literal["episode"] = FieldInfo(alias="itemType")
    """Type of the item. Always episode."""

    streaming_options: Dict[str, List[ShowSearchTitleResponseItemSeasonEpisodeStreamingOption]] = FieldInfo(
        alias="streamingOptions"
    )
    """Map of the streaming options by the country code."""

    title: str
    """Title of the episode."""

    overview: Optional[str] = None
    """A brief overview of the plot of the episode."""


class ShowSearchTitleResponseItemSeason(BaseModel):
    first_air_year: int = FieldInfo(alias="firstAirYear")
    """The first year that the season aired."""

    item_type: Literal["season"] = FieldInfo(alias="itemType")
    """Type of the item. Always season."""

    last_air_year: int = FieldInfo(alias="lastAirYear")
    """The last year that the season aired."""

    streaming_options: Dict[str, List[ShowSearchTitleResponseItemSeasonStreamingOption]] = FieldInfo(
        alias="streamingOptions"
    )
    """Map of the streaming options by the country code."""

    title: str
    """Title of the season."""

    episodes: Optional[List[ShowSearchTitleResponseItemSeasonEpisode]] = None
    """Array of the episodes belong to the season."""


class ShowSearchTitleResponseItem(BaseModel):
    id: str
    """Id of the show."""

    cast: List[str]
    """Array of the cast of the show."""

    genres: List[ShowSearchTitleResponseItemGenre]
    """Array of the genres of the show."""

    image_set: ShowSearchTitleResponseItemImageSet = FieldInfo(alias="imageSet")
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

    streaming_options: Dict[str, List[ShowSearchTitleResponseItemStreamingOption]] = FieldInfo(alias="streamingOptions")
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

    seasons: Optional[List[ShowSearchTitleResponseItemSeason]] = None
    """Array of the seasons belong to the series."""


ShowSearchTitleResponse: TypeAlias = List[ShowSearchTitleResponseItem]
