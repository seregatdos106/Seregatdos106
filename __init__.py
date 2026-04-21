# core/account/__init__.py
"""
📦 ACCOUNT PACKAGE — инициализация компонентов управления аккаунтом
"""

from __future__ import annotations

from core.account.manager import AccountManager, AccountState

__all__ = [
    "AccountManager",
    "AccountState",
]