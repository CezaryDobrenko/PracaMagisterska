# Django auth user model must be first
from scrapper.models.user import User
from scrapper.models.user import Test
from scrapper.models.folder import Folder
from scrapper.models.api_key import ApiKey
from scrapper.models.collected_data import CollectedData
from scrapper.models.selectors import Selector
from scrapper.models.selector_type import SelectorType
from scrapper.models.website import Website