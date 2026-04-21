# core/account/login.py
"""
🔐 LOGIN v2.0 — вход на Avito с сохранением куки и сессии
"""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from playwright.async_api import Page
    from core.avito.navigator import AvitoNavigator
    from services.logger import Logger
    from services.notifier import TelegramNotifier
    from core.browser.launcher import BrowserLauncher


async def login_with_session(
    page: Page,
    acc_id: str,
    navigator: AvitoNavigator,
    logger: Logger
) -> bool:
    """✅ ПРОВЕРКА ТОЛЬКО COOKIES - БЕЗ GOTO()"""
    
    try:
        logger.info(acc_id, "🔑 Checking saved session...")
        
        # ✅ ТОЛЬКО cookies - БЕЗ page.goto() и БЕЗ navigator.goto_main()!
        cookies = await page.context.cookies()
        
        avito_cookies = [
            c for c in cookies
            if "avito" in c.get("domain", "") and c.get("name") in {
                "sessid", "auth", "u", "buyer_laas_target_id", "buyer_local_priority_v2", "luri"
            }
        ]
        
        if len(avito_cookies) >= 2 and len(cookies) > 100:
            logger.success(acc_id, f"✅ AUTHENTICATED ({len(cookies)} cookies)")
            return True
        elif len(cookies) > 50:
            logger.success(acc_id, f"✅ AUTHENTICATED ({len(cookies)} cookies)")
            return True
        else:
            logger.warning(acc_id, f"❌ NOT AUTHENTICATED ({len(cookies)} cookies)")
            return False
    
    except Exception as e:
        logger.warning(acc_id, f"❌ Session check failed: {e}")
        return False


async def login_with_sms(
    page: Page,
    acc_id: str,
    phone: str,
    navigator: AvitoNavigator,
    logger: Logger,
    notifier: Optional[TelegramNotifier] = None,
    fingerprint = None,
    launcher: Optional[BrowserLauncher] = None
) -> bool:
    """📱 ВХОД ЧЕРЕЗ SMS"""
    
    try:
        logger.info(acc_id, f"🔐 Starting SMS login for {phone}")
        
        success = await navigator.goto_login(page, acc_id)
        if not success:
            logger.error(acc_id, "❌ Failed to load login page", severity="HIGH")
            return False
        
        await page.wait_for_load_state("networkidle", timeout=10000)
        await asyncio.sleep(1)
        logger.info(acc_id, "✅ On login page")
        
        logger.info(acc_id, f"📝 Entering phone: {phone}")
        
        try:
            phone_input = await page.query_selector('input[type="tel"]')
            if phone_input:
                await phone_input.fill(phone)
                await page.wait_for_timeout(500)
                
                continue_btn = await page.query_selector('button[type="submit"]')
                if continue_btn:
                    await continue_btn.click()
                    await page.wait_for_timeout(2000)
            else:
                logger.warning(acc_id, "⚠️ Phone input not found")
                return False
        
        except Exception as e:
            logger.error(acc_id, f"Error entering phone: {e}", severity="MEDIUM")
            return False
        
        logger.info(acc_id, "⏳ Waiting for SMS code...")
        logger.warning(acc_id, "🔔 SMS CODE NEEDED — waiting for code input...")
        
        if notifier:
            try:
                await notifier.notify_sms_needed(acc_id, phone)
            except Exception:
                pass
        
        sms_code = None
        max_attempts = 300
        
        for attempt in range(max_attempts):
            try:
                code_input = await page.query_selector('input[inputmode="numeric"]')
                
                if code_input:
                    code_value = await code_input.input_value()
                    if code_value and len(code_value) == 4:
                        sms_code = code_value
                        logger.success(acc_id, f"✅ SMS code received: {sms_code}")
                        break
                
                if attempt % 10 == 0:
                    logger.info(acc_id, f"⏳ Still waiting for SMS... ({attempt}s)")
                
                await page.wait_for_timeout(1000)
            
            except Exception:
                pass
        
        if not sms_code:
            logger.error(acc_id, "❌ SMS code timeout (5 minutes)", severity="HIGH")
            return False
        
        logger.info(acc_id, "⏳ Verifying login...")
        
        try:
            await page.wait_for_load_state("networkidle", timeout=10000)
            await asyncio.sleep(2)
        except Exception:
            pass
        
        is_auth = await page.evaluate("""
            () => {
                const profile = document.querySelector('[data-marker="account-menu-button"]');
                const userLink = document.querySelector('a[href*="/user/"]');
                const accountButton = document.querySelector('[data-marker="header/profile"]');
                return !!(profile || userLink || accountButton);
            }
        """)
        
        if not is_auth:
            logger.error(acc_id, "❌ Login verification failed", severity="HIGH")
            return False
        
        logger.success(acc_id, "✅ AUTHENTICATED VIA SMS")
        
        if launcher:
            try:
                logger.info(acc_id, "💾 Saving cookies and storage...")
                cookies_saved = await launcher.save_cookies(acc_id)
                storage_saved = await launcher.save_storage_state(acc_id)
                
                if cookies_saved or storage_saved:
                    logger.success(acc_id, "✅ Session saved for future logins (cookies + storage)")
                else:
                    logger.warning(acc_id, "⚠️ Failed to save some session data")
            
            except Exception as e:
                logger.warning(acc_id, f"⚠️ Error saving session: {e}")
        
        if notifier:
            try:
                await notifier.notify_login_success(acc_id, phone, "sms")
            except Exception:
                pass
        
        return True
    
    except Exception as e:
        logger.error(acc_id, f"❌ SMS login failed: {e}", severity="HIGH")
        
        if notifier:
            try:
                await notifier.notify_login_failed(acc_id, phone)
            except Exception:
                pass
        
        return False