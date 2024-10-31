# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ChangeListResponse",
    "Change",
    "ChangeService",
    "ChangeServiceImageSet",
    "ChangeAddon",
    "ChangeAddonImageSet",
    "Shows",
    "ShowsGenre",
    "ShowsImageSet",
    "ShowsImageSetHorizontalPoster",
    "ShowsImageSetVerticalPoster",
    "ShowsImageSetHorizontalBackdrop",
    "ShowsImageSetVerticalBackdrop",
    "ShowsStreamingOption",
    "ShowsStreamingOptionAudio",
    "ShowsStreamingOptionService",
    "ShowsStreamingOptionServiceImageSet",
    "ShowsStreamingOptionSubtitle",
    "ShowsStreamingOptionSubtitleLocale",
    "ShowsStreamingOptionAddon",
    "ShowsStreamingOptionAddonImageSet",
    "ShowsStreamingOptionPrice",
    "ShowsSeason",
    "ShowsSeasonStreamingOption",
    "ShowsSeasonStreamingOptionAudio",
    "ShowsSeasonStreamingOptionService",
    "ShowsSeasonStreamingOptionServiceImageSet",
    "ShowsSeasonStreamingOptionSubtitle",
    "ShowsSeasonStreamingOptionSubtitleLocale",
    "ShowsSeasonStreamingOptionAddon",
    "ShowsSeasonStreamingOptionAddonImageSet",
    "ShowsSeasonStreamingOptionPrice",
    "ShowsSeasonEpisode",
    "ShowsSeasonEpisodeStreamingOption",
    "ShowsSeasonEpisodeStreamingOptionAudio",
    "ShowsSeasonEpisodeStreamingOptionService",
    "ShowsSeasonEpisodeStreamingOptionServiceImageSet",
    "ShowsSeasonEpisodeStreamingOptionSubtitle",
    "ShowsSeasonEpisodeStreamingOptionSubtitleLocale",
    "ShowsSeasonEpisodeStreamingOptionAddon",
    "ShowsSeasonEpisodeStreamingOptionAddonImageSet",
    "ShowsSeasonEpisodeStreamingOptionPrice",
]


class ChangeServiceImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class ChangeService(BaseModel):
    id: str
    """Id of the service."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the service."""

    image_set: ChangeServiceImageSet = FieldInfo(alias="imageSet")
    """Image set of the service."""

    name: str
    """Name of the service."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the service."""


class ChangeAddonImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class ChangeAddon(BaseModel):
    id: str
    """Id of the addon."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the addon."""

    image_set: ChangeAddonImageSet = FieldInfo(alias="imageSet")
    """Image set of the addon."""

    name: str
    """Name of the addon."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the addon."""


class Change(BaseModel):
    change_type: Literal["new", "removed", "updated", "expiring", "upcoming"] = FieldInfo(alias="changeType")
    """Type of the change."""

    item_type: Literal["show", "season", "episode"] = FieldInfo(alias="itemType")
    """Type of the item affected from the change."""

    service: ChangeService
    """Service affected from the change."""

    show_id: str = FieldInfo(alias="showId")
    """Id of the show affected from the change."""

    show_type: Literal["movie", "series"] = FieldInfo(alias="showType")
    """Type of the show affected from the change."""

    streaming_option_type: Literal["free", "subscription", "buy", "rent", "addon"] = FieldInfo(
        alias="streamingOptionType"
    )
    """Type of the streaming option."""

    addon: Optional[ChangeAddon] = None
    """Addon info, if the streamingOptionType is addon. Otherwise omitted."""

    episode: Optional[int] = None
    """Number of the episode affected from the change.

    Omitted if item_type is not episode.
    """

    link: Optional[str] = None
    """
    Deep link to the affected streaming option's page in the web app of the
    streaming service. This field is guaranteed to be populated when changeType is
    new, updated, expiring or removed. When changeType is upcoming, this field might
    be populated or null depending on if the link of the future streaming option is
    known.
    """

    season: Optional[int] = None
    """Number of the season affected from the change.

    Omitted if item_type is not seasonor episode.
    """

    timestamp: Optional[int] = None
    """
    [Unix Time Stamp](https://www.unixtimestamp.com/) of the change. Past changes
    (new, updated, removed) will always have a timestamp. Future changes (expiring,
    upcoming) will have a timestamp if the exact date is known. If not, timestamp
    will be omitted, e.g. a show is known to be expiring soon, but the exact date is
    not known.
    """


class ShowsGenre(BaseModel):
    id: str
    """Id of the genre"""

    name: str
    """Name of the genre"""


class ShowsImageSetHorizontalPoster(BaseModel):
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


class ShowsImageSetVerticalPoster(BaseModel):
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


class ShowsImageSetHorizontalBackdrop(BaseModel):
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


class ShowsImageSetVerticalBackdrop(BaseModel):
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


class ShowsImageSet(BaseModel):
    horizontal_poster: ShowsImageSetHorizontalPoster = FieldInfo(alias="horizontalPoster")
    """Horizontal poster of the show."""

    vertical_poster: ShowsImageSetVerticalPoster = FieldInfo(alias="verticalPoster")
    """Vertical poster of the show."""

    horizontal_backdrop: Optional[ShowsImageSetHorizontalBackdrop] = FieldInfo(alias="horizontalBackdrop", default=None)
    """Horizontal backdrop of the show."""

    vertical_backdrop: Optional[ShowsImageSetVerticalBackdrop] = FieldInfo(alias="verticalBackdrop", default=None)
    """Vertical backdrop of the show."""


class ShowsStreamingOptionAudio(BaseModel):
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


class ShowsStreamingOptionServiceImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class ShowsStreamingOptionService(BaseModel):
    id: str
    """Id of the service."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the service."""

    image_set: ShowsStreamingOptionServiceImageSet = FieldInfo(alias="imageSet")
    """Image set of the service."""

    name: str
    """Name of the service."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the service."""


class ShowsStreamingOptionSubtitleLocale(BaseModel):
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


class ShowsStreamingOptionSubtitle(BaseModel):
    closed_captions: bool = FieldInfo(alias="closedCaptions")
    """Whether closed captions are available for the subtitle."""

    locale: ShowsStreamingOptionSubtitleLocale
    """A language and optionally an associated region."""


class ShowsStreamingOptionAddonImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class ShowsStreamingOptionAddon(BaseModel):
    id: str
    """Id of the addon."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the addon."""

    image_set: ShowsStreamingOptionAddonImageSet = FieldInfo(alias="imageSet")
    """Image set of the addon."""

    name: str
    """Name of the addon."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the addon."""


class ShowsStreamingOptionPrice(BaseModel):
    amount: str
    """Numerical amount of the price."""

    currency: str
    """
    [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) alphabetic code of the
    currency.
    """

    formatted: str
    """Formatted price, including both the amount and the currency."""


class ShowsStreamingOption(BaseModel):
    audios: List[ShowsStreamingOptionAudio]
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

    service: ShowsStreamingOptionService
    """Details of the streaming service localized according to the parent country."""

    subtitles: List[ShowsStreamingOptionSubtitle]
    """Array of the available subtitles."""

    type: Literal["free", "subscription", "buy", "rent", "addon"]
    """Type of the streaming option."""

    addon: Optional[ShowsStreamingOptionAddon] = None
    """
    Addon that the streaming option is available through. Omitted if the streaming
    option is not available through an addon.
    """

    expires_on: Optional[int] = FieldInfo(alias="expiresOn", default=None)
    """
    [Unix Time Stamp](https://www.unixtimestamp.com/) of the date that the streaming
    option is expiring. In other words, last day to watch.
    """

    price: Optional[ShowsStreamingOptionPrice] = None
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


class ShowsSeasonStreamingOptionAudio(BaseModel):
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


class ShowsSeasonStreamingOptionServiceImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class ShowsSeasonStreamingOptionService(BaseModel):
    id: str
    """Id of the service."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the service."""

    image_set: ShowsSeasonStreamingOptionServiceImageSet = FieldInfo(alias="imageSet")
    """Image set of the service."""

    name: str
    """Name of the service."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the service."""


class ShowsSeasonStreamingOptionSubtitleLocale(BaseModel):
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


class ShowsSeasonStreamingOptionSubtitle(BaseModel):
    closed_captions: bool = FieldInfo(alias="closedCaptions")
    """Whether closed captions are available for the subtitle."""

    locale: ShowsSeasonStreamingOptionSubtitleLocale
    """A language and optionally an associated region."""


class ShowsSeasonStreamingOptionAddonImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class ShowsSeasonStreamingOptionAddon(BaseModel):
    id: str
    """Id of the addon."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the addon."""

    image_set: ShowsSeasonStreamingOptionAddonImageSet = FieldInfo(alias="imageSet")
    """Image set of the addon."""

    name: str
    """Name of the addon."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the addon."""


class ShowsSeasonStreamingOptionPrice(BaseModel):
    amount: str
    """Numerical amount of the price."""

    currency: str
    """
    [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) alphabetic code of the
    currency.
    """

    formatted: str
    """Formatted price, including both the amount and the currency."""


class ShowsSeasonStreamingOption(BaseModel):
    audios: List[ShowsSeasonStreamingOptionAudio]
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

    service: ShowsSeasonStreamingOptionService
    """Details of the streaming service localized according to the parent country."""

    subtitles: List[ShowsSeasonStreamingOptionSubtitle]
    """Array of the available subtitles."""

    type: Literal["free", "subscription", "buy", "rent", "addon"]
    """Type of the streaming option."""

    addon: Optional[ShowsSeasonStreamingOptionAddon] = None
    """
    Addon that the streaming option is available through. Omitted if the streaming
    option is not available through an addon.
    """

    expires_on: Optional[int] = FieldInfo(alias="expiresOn", default=None)
    """
    [Unix Time Stamp](https://www.unixtimestamp.com/) of the date that the streaming
    option is expiring. In other words, last day to watch.
    """

    price: Optional[ShowsSeasonStreamingOptionPrice] = None
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


class ShowsSeasonEpisodeStreamingOptionAudio(BaseModel):
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


class ShowsSeasonEpisodeStreamingOptionServiceImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class ShowsSeasonEpisodeStreamingOptionService(BaseModel):
    id: str
    """Id of the service."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the service."""

    image_set: ShowsSeasonEpisodeStreamingOptionServiceImageSet = FieldInfo(alias="imageSet")
    """Image set of the service."""

    name: str
    """Name of the service."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the service."""


class ShowsSeasonEpisodeStreamingOptionSubtitleLocale(BaseModel):
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


class ShowsSeasonEpisodeStreamingOptionSubtitle(BaseModel):
    closed_captions: bool = FieldInfo(alias="closedCaptions")
    """Whether closed captions are available for the subtitle."""

    locale: ShowsSeasonEpisodeStreamingOptionSubtitleLocale
    """A language and optionally an associated region."""


class ShowsSeasonEpisodeStreamingOptionAddonImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class ShowsSeasonEpisodeStreamingOptionAddon(BaseModel):
    id: str
    """Id of the addon."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the addon."""

    image_set: ShowsSeasonEpisodeStreamingOptionAddonImageSet = FieldInfo(alias="imageSet")
    """Image set of the addon."""

    name: str
    """Name of the addon."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the addon."""


class ShowsSeasonEpisodeStreamingOptionPrice(BaseModel):
    amount: str
    """Numerical amount of the price."""

    currency: str
    """
    [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) alphabetic code of the
    currency.
    """

    formatted: str
    """Formatted price, including both the amount and the currency."""


class ShowsSeasonEpisodeStreamingOption(BaseModel):
    audios: List[ShowsSeasonEpisodeStreamingOptionAudio]
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

    service: ShowsSeasonEpisodeStreamingOptionService
    """Details of the streaming service localized according to the parent country."""

    subtitles: List[ShowsSeasonEpisodeStreamingOptionSubtitle]
    """Array of the available subtitles."""

    type: Literal["free", "subscription", "buy", "rent", "addon"]
    """Type of the streaming option."""

    addon: Optional[ShowsSeasonEpisodeStreamingOptionAddon] = None
    """
    Addon that the streaming option is available through. Omitted if the streaming
    option is not available through an addon.
    """

    expires_on: Optional[int] = FieldInfo(alias="expiresOn", default=None)
    """
    [Unix Time Stamp](https://www.unixtimestamp.com/) of the date that the streaming
    option is expiring. In other words, last day to watch.
    """

    price: Optional[ShowsSeasonEpisodeStreamingOptionPrice] = None
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


class ShowsSeasonEpisode(BaseModel):
    air_year: int = FieldInfo(alias="airYear")
    """The year that the episode aired."""

    item_type: Literal["episode"] = FieldInfo(alias="itemType")
    """Type of the item. Always episode."""

    streaming_options: Dict[str, List[ShowsSeasonEpisodeStreamingOption]] = FieldInfo(alias="streamingOptions")
    """Map of the streaming options by the country code."""

    title: str
    """Title of the episode."""

    overview: Optional[str] = None
    """A brief overview of the plot of the episode."""


class ShowsSeason(BaseModel):
    first_air_year: int = FieldInfo(alias="firstAirYear")
    """The first year that the season aired."""

    item_type: Literal["season"] = FieldInfo(alias="itemType")
    """Type of the item. Always season."""

    last_air_year: int = FieldInfo(alias="lastAirYear")
    """The last year that the season aired."""

    streaming_options: Dict[str, List[ShowsSeasonStreamingOption]] = FieldInfo(alias="streamingOptions")
    """Map of the streaming options by the country code."""

    title: str
    """Title of the season."""

    episodes: Optional[List[ShowsSeasonEpisode]] = None
    """Array of the episodes belong to the season."""


class Shows(BaseModel):
    id: str
    """Id of the show."""

    cast: List[str]
    """Array of the cast of the show."""

    genres: List[ShowsGenre]
    """Array of the genres of the show."""

    image_set: ShowsImageSet = FieldInfo(alias="imageSet")
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

    streaming_options: Dict[str, List[ShowsStreamingOption]] = FieldInfo(alias="streamingOptions")
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

    seasons: Optional[List[ShowsSeason]] = None
    """Array of the seasons belong to the series."""


class ChangeListResponse(BaseModel):
    changes: List[Change]
    """Array of the changes."""

    has_more: bool = FieldInfo(alias="hasMore")
    """Whether there are more changes available."""

    shows: Dict[str, Shows]
    """Map of the shows affected by the changes."""

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """Cursor value to pass to get the next set of changes."""
