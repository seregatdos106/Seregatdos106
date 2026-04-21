# core/avito/selectors.py
"""
🎯 SELECTORS v2.0 — селекторы и URL для Avito
✅ CSS селекторы для элементов
✅ URL'ы для навигации
✅ Data markers для Avito
"""

from enum import Enum


class AvitoUrls:
    """URL'ы для навигации на Avito"""
    
    MAIN = "https://www.avito.ru"
    LOGIN = "https://www.avito.ru/auth"
    FAVORITES = "https://www.avito.ru/favorites"
    PROFILE = "https://www.avito.ru/profile"
    MESSAGES = "https://www.avito.ru/messages"
    MY_ITEMS = "https://www.avito.ru/my"
    SEARCH_TEMPLATE = "https://www.avito.ru?p=1&q={query}"


class AvitoSelectors:
    """CSS селекторы для элементов на Avito"""
    
    # ═══════════════════════════════════════════════════════════════
    # ПОИСК
    # ═══════════════════════════════════════════════════════════════
    
    SEARCH_INPUT = 'input[data-marker="search-form/suggest"]'
    SEARCH_SUBMIT = 'button[data-marker="search-form/submit"]'
    SEARCH_RESULTS = '[data-marker="item"]'
    
    # ═══════════════════════════════════════════════════════════════
    # КАРТОЧКА ТОВАРА
    # ═══════════════════════════════════════════════════════════════
    
    ITEM_TITLE = '[data-marker="item-title"]'
    ITEM_PRICE = '[data-marker="item-price"]'
    ITEM_DESCRIPTION = '[data-marker="item-description"]'
    ITEM_PHOTOS = '[data-marker="photo"]'
    ITEM_CHARACTERISTICS = '[data-marker="item-params"]'
    ITEM_REVIEWS = '[data-marker="item-reviews"]'
    
    # ═══════════════════════════════════════════════════════════════
    # ИЗБРАННОЕ
    # ═══════════════════════════════════════════════════════════════
    
    FAVORITES_BUTTON = '[data-marker="item-add-to-favorites"]'
    FAVORITES_HEART = '[data-icon="heart"]'
    
    # ═══════════════════════════════════════════════════════════════
    # ПРОФИЛЬ ПРОДАВЦА
    # ═══════════════════════════════════════════════════════════════
    
    SELLER_LINK = 'a[href*="/user/"]'
    SELLER_NAME = '[data-marker="seller-name"]'
    SELLER_RATING = '[data-marker="seller-rating"]'
    SELLER_ITEMS = '[data-marker="seller-items"]'
    
    # ═══════════════════════════════════════════════════════════════
    # МЕНЮ И НАВИГАЦИЯ
    # ═══════════════════════════════════════════════════════════════
    
    PROFILE_MENU = '[data-marker="account-menu-button"]'
    USER_PROFILE = '[data-marker="header/profile"]'
    MESSAGES_LINK = '[data-marker="header/messages"]'
    FAVORITES_LINK = '[data-marker="header/favorites"]'
    
    # ═══════════════════════════════════════════════════════════════
    # МОИ ОБЪЯВЛЕНИЯ
    # ═══════════════════════════════════════════════════════════════
    
    MY_ITEMS_LIST = '[data-marker="my-items/item"]'
    ACTIVE_ITEMS = '[data-marker="my-items/active"]'
    SOLD_ITEMS = '[data-marker="my-items/sold"]'
    
    # ═══════════════════════════════════════════════════════════════
    # ОТЗЫВЫ
    # ═══════════════════════════════════════════════════════════════
    
    REVIEW_ITEM = '[data-marker="review-item"]'
    REVIEW_TEXT = '[data-marker="review-text"]'
    REVIEW_RATING = '[data-marker="review-rating"]'
    
    # ═══════════════════════════════════════════════════════════════
    # АВТОРИЗАЦИЯ
    # ═══════════════════════════════════════════════════════════════
    
    PHONE_INPUT = 'input[type="tel"]'
    SMS_CODE_INPUT = 'input[inputmode="numeric"]'
    SUBMIT_BUTTON = 'button[type="submit"]'
    
    # ═══════════════════════════════════════════════════════════════
    # ДРУГОЕ
    # ═══════════════════════════════════════════════════════════════
    
    LOADING_SPINNER = '[data-marker="loading"]'
    ERROR_MESSAGE = '[data-marker="error"]'
    BACK_BUTTON = 'button[aria-label*="Назад"]'


class ThreatType(Enum):
    """Типы угроз / срабатываний антибота"""
    
    CAPTCHA = "captcha"
    RATE_LIMIT = "rate_limit"
    IP_BLOCKED = "ip_blocked"
    CLOUDFLARE = "cloudflare"
    BOT_DETECTED = "bot_detected"
    UNKNOWN = "unknown"


class ThreatInfo:
    """Информация об обнаруженной угрозе"""
    
    def __init__(
        self,
        threat_type: ThreatType,
        message: str,
        is_safe: bool = False,
        score: int = 0
    ):
        """
        Args:
            threat_type: Тип угрозы
            message: Описа��ие
            is_safe: Безопасна ли страница
            score: Score угрозы (0-100)
        """
        
        self.type = threat_type
        self.message = message
        self.is_safe = is_safe
        self.score = score