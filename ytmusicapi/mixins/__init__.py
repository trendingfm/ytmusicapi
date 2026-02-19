"""
Mixins for YTMusic class.
"""

from ._protocol import MixinProtocol
from .browsing import BrowsingMixin
from .explore import ExploreMixin
from .genre import GenreMixin
from .library import LibraryMixin
from .playlists import PlaylistsMixin
from .podcasts import PodcastsMixin
from .search import SearchMixin
from .uploads import UploadsMixin
from .watch import WatchMixin

__all__ = [
    "MixinProtocol",
    "BrowsingMixin",
    "ExploreMixin",
    "GenreMixin",
    "LibraryMixin",
    "PlaylistsMixin",
    "PodcastsMixin",
    "SearchMixin",
    "UploadsMixin",
    "WatchMixin",
]
