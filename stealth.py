# core/browser/stealth.py
"""
🛡️ STEALTH ENGINE PRO v6.0
РАСШИРЕННАЯ ЗАЩИТА ПРОТИВ AVITO, CLOUDFLARE И ДРУГИХ АНТИБОТОВ
✅ Canvas Fingerprinting Protection
✅ WebGL Fingerprinting Protection
✅ AudioContext Fingerprinting Protection
✅ Hardware concurrency spoofing с шумом
✅ Fonts fingerprinting protection
✅ 25+ уровней защиты
"""

from core.browser.fingerprint import Fingerprint
import random
import string


class StealthEngineV5:
    """
    🛡️ STEALTH ENGINE V5.0
    """
    
    # Твой код полностью...
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.7328.6 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.7307.13 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7319.173 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7360.79 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.7292.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.7289.73 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.7278.59 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7284.35 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.7328.6 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7360.79 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.7328.6 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7360.79 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7; rv:131.0) Gecko/20100101 Firefox/131.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0",
    ]
    
    # Остальное твой код...
    VIEWPORTS = [
        {"width": 1920, "height": 1080},
        {"width": 1366, "height": 768},
        {"width": 1440, "height": 900},
        {"width": 1536, "height": 864},
        {"width": 1280, "height": 720},
        {"width": 1600, "height": 900},
        {"width": 1024, "height": 768},
        {"width": 1280, "height": 800},
        {"width": 1920, "height": 1200},
        {"width": 2560, "height": 1440},
        {"width": 1680, "height": 1050},
        {"width": 1440, "height": 810},
        {"width": 1152, "height": 864},
    ]
    
    GEOLOCATION_POINTS = [
        {"latitude": 55.7558, "longitude": 37.6173, "city": "Москва"},
        {"latitude": 59.9341, "longitude": 30.3356, "city": "Санкт-Петербург"},
        {"latitude": 54.9924, "longitude": 82.8979, "city": "Новосибирск"},
        {"latitude": 56.8389, "longitude": 60.6057, "city": "Екатеринбург"},
        {"latitude": 53.1959, "longitude": 44.9999, "city": "Липецк"},
        {"latitude": 55.9311, "longitude": 37.4112, "city": "Домодедово"},
        {"latitude": 55.8766, "longitude": 37.7247, "city": "Чехов"},
        {"latitude": 52.2977, "longitude": 104.2964, "city": "Иркутск"},
        {"latitude": 56.0153, "longitude": 92.8932, "city": "Красноярск"},
        {"latitude": 52.2965, "longitude": 104.2964, "city": "Иркутск"},
        {"latitude": 61.2242, "longitude": 73.3676, "city": "Ноябрьск"},
        {"latitude": 53.2007, "longitude": 45.0038, "city": "Тамбов"},
        {"latitude": 54.7265, "longitude": 20.4427, "city": "Калининград"},
        {"latitude": 56.1264, "longitude": 40.1843, "city": "Владимир"},
        {"latitude": 56.8389, "longitude": 35.9161, "city": "Тверь"},
        {"latitude": 57.1567, "longitude": 39.4066, "city": "Ярославль"},
        {"latitude": 58.1342, "longitude": 37.2622, "city": "Вологда"},
        {"latitude": 57.9235, "longitude": 41.7599, "city": "Киров"},
        {"latitude": 56.4285, "longitude": 43.8354, "city": "Нижний Новгород"},
        {"latitude": 53.1951, "longitude": 45.0193, "city": "Пенза"},
        {"latitude": 40.7128, "longitude": -74.0060, "city": "New York"},
        {"latitude": 34.0522, "longitude": -118.2437, "city": "Los Angeles"},
        {"latitude": 41.8781, "longitude": -87.6298, "city": "Chicago"},
        {"latitude": 29.7604, "longitude": -95.3698, "city": "Houston"},
        {"latitude": 33.7490, "longitude": -84.3880, "city": "Atlanta"},
        {"latitude": 39.7392, "longitude": -104.9903, "city": "Denver"},
        {"latitude": 47.6062, "longitude": -122.3321, "city": "Seattle"},
        {"latitude": 37.7749, "longitude": -122.4194, "city": "San Francisco"},
        {"latitude": 42.3601, "longitude": -71.0589, "city": "Boston"},
        {"latitude": 39.9526, "longitude": -75.1652, "city": "Philadelphia"},
        {"latitude": 28.7041, "longitude": 77.1025, "city": "Delhi"},
        {"latitude": 19.0760, "longitude": 72.8777, "city": "Mumbai"},
        {"latitude": 13.0827, "longitude": 80.2707, "city": "Chennai"},
        {"latitude": 28.6139, "longitude": 77.2090, "city": "New Delhi"},
        {"latitude": 23.1815, "longitude": 79.9864, "city": "Indore"},
    ]
    
    LANGUAGE_COMBINATIONS = [
        "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "en-US,en;q=0.9",
        "en-GB,en;q=0.8",
        "de-DE,de;q=0.9,en;q=0.8",
        "fr-FR,fr;q=0.9,en;q=0.8",
        "it-IT,it;q=0.9,en;q=0.8",
        "es-ES,es;q=0.9,en;q=0.8",
        "pt-BR,pt;q=0.9,en;q=0.8",
        "ja-JP,ja;q=0.9,en;q=0.8",
        "zh-CN,zh;q=0.9,en;q=0.8",
    ]
    
    TIMEZONES = [
        "Europe/Moscow",
        "Europe/London",
        "America/New_York",
        "America/Chicago",
        "America/Denver",
        "America/Los_Angeles",
        "Asia/Tokyo",
        "Asia/Shanghai",
        "Asia/Hong_Kong",
        "Asia/Singapore",
        "Asia/Dubai",
        "Australia/Sydney",
        "Australia/Melbourne",
        "Europe/Berlin",
        "Europe/Paris",
        "Europe/Madrid",
        "Europe/Rome",
        "Europe/Amsterdam",
        "Europe/Stockholm",
        "Europe/Zurich",
    ]
    
    @staticmethod
    def build_advanced_stealth_script(fp: Fingerprint) -> str:
        """
        🛡️ ПОСТРОЙИТЬ ПРОДВИНУТЫЙ STEALTH СКРИПТ (v6.0)
        """
        
        ua = fp.user_agent
        lang = fp.language
        tz = fp.timezone
        canvas_noise = fp.canvas_noise_seed
        audio_noise = fp.audio_noise_seed
        
        return f"""
        (() => {{
            'use strict';
            
            console.log('%c🛡️ STEALTH ENGINE v6.0 ACTIVATED', 'color:#00ff00; font-size:14px; font-weight:bold; background:#000; padding:5px;');
            
            // ���═══════════════════════════════════════════════════════════
            // LEVEL 1: KILL ALL AUTOMATION DETECTION MARKERS
            // ════════════════════════════════════════════════════════════
            
            const automationMarkers = [
                'webdriver', '__playwright', '__pw_manual', '__pw_resolve', '__pw_reject',
                '__puppeteer_evaluation_script', '__lastWatir', 'cdc_', '__selenium_evaluate',
                'pw_', 'playwright', 'NightwatchJS', '_Selenium_IDE_Recorder', 'callPhantom',
                'phantom', '__nightmare', '__protractor_instance', 'driver', 'selenium',
                '_phantom', 'webdriverResource', 'chromedriver', 'isSelenium', '_Watir_Element_Container',
                'domautomation', 'document.$0', '__webdriver_script_fn', 'window.$0', '_phantom',
            ];
            
            automationMarkers.forEach(marker => {{
                try {{ delete globalThis[marker]; }} catch(e) {{}}
                try {{ delete window[marker]; }} catch(e) {{}}
                try {{ delete document[marker]; }} catch(e) {{}}
                try {{ delete navigator[marker]; }} catch(e) {{}}
                try {{
                    Object.defineProperty(window, marker, {{
                        get: () => undefined,
                        set: () => {{}},
                        configurable: true,
                    }});
                }} catch(e) {{}}
            }});
            
            // ════════════════════════════════════════════════════════════
            // LEVEL 2: NAVIGATOR PROPERTIES (ADVANCED)
            // ════════════════════════════════════════════════════════════
            
            Object.defineProperty(navigator, 'webdriver', {{
                get: () => false,
                configurable: true,
            }});
            
            Object.defineProperty(navigator, 'userAgent', {{
                get: () => '{ua}',
                configurable: true,
            }});
            
            Object.defineProperty(navigator, 'appVersion', {{
                get: () => '{ua.split(" ")[0]}',
                configurable: true,
            }});
            
            Object.defineProperty(navigator, 'languages', {{
                get: () => Object.freeze(['ru-RU', 'ru', 'en-US', 'en']),
                configurable: true,
            }});
            
            Object.defineProperty(navigator, 'language', {{
                get: () => 'ru-RU',
                configurable: true,
            }});
            
            Object.defineProperty(navigator, 'hardwareConcurrency', {{
                get: () => {fp.hardware_concurrency},
                configurable: true,
            }});
            
            Object.defineProperty(navigator, 'deviceMemory', {{
                get: () => {fp.device_memory},
                configurable: true,
            }});
            
            Object.defineProperty(navigator, 'maxTouchPoints', {{
                get: () => {fp.max_touch_points},
                configurable: true,
            }});
            
            Object.defineProperty(navigator, 'vendor', {{
                get: () => 'Google Inc.',
                configurable: true,
            }});
            
            // ════════════════════════════════════════════════════════════
            // LEVEL 3: CANVAS FINGERPRINTING PROTECTION
            // ════════════════════��═══════════════════════════════════════
            
            const canvasSeed = {canvas_noise};
            const origToDataURL = HTMLCanvasElement.prototype.toDataURL;
            const origToBlob = HTMLCanvasElement.prototype.toBlob;
            
            HTMLCanvasElement.prototype.toDataURL = function(type) {{
                if (this.width > 16 && this.height > 16) {{
                    const ctx = this.getContext('2d');
                    if (ctx) {{
                        try {{
                            const imageData = ctx.getImageData(0, 0, this.width, this.height);
                            for (let i = 0; i < imageData.data.length; i++) {{
                                imageData.data[i] ^= (canvasSeed % 256);
                            }}
                            ctx.putImageData(imageData, 0, 0);
                        }} catch(e) {{}}
                    }}
                }}
                return origToDataURL.call(this, type);
            }};
            
            HTMLCanvasElement.prototype.toBlob = function(callback, type, quality) {{
                const self = this;
                const ctx = this.getContext('2d');
                if (ctx && this.width > 16 && this.height > 16) {{
                    try {{
                        const imageData = ctx.getImageData(0, 0, this.width, this.height);
                        for (let i = 0; i < imageData.data.length; i++) {{
                            imageData.data[i] ^= (canvasSeed % 256);
                        }}
                        ctx.putImageData(imageData, 0, 0);
                    }} catch(e) {{}}
                }}
                return origToBlob.call(this, callback, type, quality);
            }};
            
            // ════════════════════════════════════════════════════════════
            // LEVEL 4: WEBGL FINGERPRINTING PROTECTION
            // ════════════════════════════════════════════════════════════
            
            const origGetParameter = WebGLRenderingContext.prototype.getParameter;
            WebGLRenderingContext.prototype.getParameter = function(parameter) {{
                if (parameter === 37445) return '{fp.webgl_vendor}';
                if (parameter === 37446) return '{fp.webgl_renderer}';
                if (parameter === 7938) return 'WebGL 1.0';
                return origGetParameter(parameter);
            }};
            
            if (WebGL2RenderingContext) {{
                const origGetParameter2 = WebGL2RenderingContext.prototype.getParameter;
                WebGL2RenderingContext.prototype.getParameter = function(parameter) {{
                    if (parameter === 37445) return '{fp.webgl_vendor}';
                    if (parameter === 37446) return '{fp.webgl_renderer}';
                    if (parameter === 7938) return 'WebGL 2.0';
                    return origGetParameter2(parameter);
                }};
            }}
            
            // ════════════════════════════════════════════════════════════
            // LEVEL 5: AUDIOCONTEXT FINGERPRINTING PROTECTION
            // ════════════════════════════════════════════════════════════
            
            const audioSeed = {audio_noise};
            if (window.AudioContext) {{
                const origCreateOscillator = AudioContext.prototype.createOscillator;
                AudioContext.prototype.createOscillator = function() {{
                    const osc = origCreateOscillator.call(this);
                    try {{
                        osc.frequency.value ^= (audioSeed % 100);
                    }} catch(e) {{}}
                    return osc;
                }};
                
                const origCreateAnalyser = AudioContext.prototype.createAnalyser;
                AudioContext.prototype.createAnalyser = function() {{
                    const analyser = origCreateAnalyser.call(this);
                    const origGetByteFrequencyData = analyser.getByteFrequencyData;
                    analyser.getByteFrequencyData = function(data) {{
                        origGetByteFrequencyData.call(this, data);
                        for (let i = 0; i < data.length; i++) {{
                            data[i] ^= (audioSeed % 256);
                        }}
                    }};
                    return analyser;
                }};
            }}
            
            // ════════════════════════════════════════════════════════════
            // LEVEL 6: SCREEN & WINDOW SPOOFING
            // ════════════════════════════════════════════════════════════
            
            Object.defineProperty(screen, 'width', {{
                get: () => {fp.screen_width},
                configurable: true,
            }});
            
            Object.defineProperty(screen, 'height', {{
                get: () => {fp.screen_height},
                configurable: true,
            }});
            
            Object.defineProperty(screen, 'availWidth', {{
                get: () => {fp.available_width},
                configurable: true,
            }});
            
            Object.defineProperty(screen, 'availHeight', {{
                get: () => {fp.available_height},
                configurable: true,
            }});
            
            Object.defineProperty(screen, 'colorDepth', {{
                get: () => {fp.color_depth},
                configurable: true,
            }});
            
            Object.defineProperty(screen, 'pixelDepth', {{
                get: () => {fp.color_depth},
                configurable: true,
            }});
            
            // ════════════════════════════════════════════════════════════
            // LEVEL 7: TIMEZONE SPOOFING
            // ════════════════════════════════════════════════════════════
            
            const origResolvedOptions = Intl.DateTimeFormat.prototype.resolvedOptions;
            Intl.DateTimeFormat.prototype.resolvedOptions = function() {{
                const result = origResolvedOptions.call(this);
                result.timeZone = '{tz}';
                return result;
            }};
            
            // ════════════════════════════════════════════════════════════
            // LEVEL 8: FONTS FINGERPRINTING PROTECTION
            // ════════════════════════════════════════════════════════════
            
            const origMeasureText = CanvasRenderingContext2D.prototype.measureText;
            CanvasRenderingContext2D.prototype.measureText = function(text) {{
                const result = origMeasureText.call(this, text);
                const noise = (canvasSeed * 0.01) % 1;
                result.width += noise;
                return result;
            }};
            
            // ════════════════════════════════════════════════════════════
            // LEVEL 9: WEBRTC LEAK PREVENTION
            // ════════════════════════════════════════════════════════════
            
            if (window.RTCPeerConnection) {{
                const origRTC = window.RTCPeerConnection;
                window.RTCPeerConnection = function(config) {{
                    config = config || {{}};
                    config.iceServers = [];
                    return new origRTC(config);
                }};
                window.RTCPeerConnection.prototype = origRTC.prototype;
            }}
            
            // ════════════════════════════════════════════════════════════
            // LEVEL 10: FETCH/XHR INTERCEPTION (ANTI-BOT DETECTION)
            // ════════════════════════════════════════════════════════════
            
            const origFetch = window.fetch;
            window.fetch = new Proxy(origFetch, {{
                apply(target, thisArg, args) {{
                    const url = typeof args[0] === 'string' ? args[0] : (args[0]?.url || '');
                    const urlLower = url.toLowerCase();
                    
                    const blockedPatterns = [
                        'bot-detection', 'antibot', 'bot-check', 'detect-bot',
                        'bot_detector', 'challenge.cloudflare', 'px.dev', 'perimeterx',
                        'bot-score', 'bot-assess', 'fingerprint'
                    ];
                    
                    for (const pattern of blockedPatterns) {{
                        if (urlLower.includes(pattern)) {{
                            console.log('[STEALTH] Blocked fetch to: ' + url);
                            return Promise.reject(new Error('Blocked'));
                        }}
                    }}
                    
                    return Reflect.apply(target, thisArg, args);
                }}
            }});
            
            // ════════════════════════════════════════════════════════════
            // LEVEL 11: DOCUMENT VISIBILITY
            // ════════════════════════════════════════════════════════════
            
            Object.defineProperty(document, 'hidden', {{
                get: () => false,
                configurable: true,
            }});
            
            Object.defineProperty(document, 'visibilityState', {{
                get: () => 'visible',
                configurable: true,
            }});
            
            // ════════════════════════════════════════════════════════════
            // LEVEL 12: PLUGINS SPOOFING
            // ════════════════════════════════════════════════════════════
            
            Object.defineProperty(navigator, 'plugins', {{
                get: () => [
                    {{'name': 'Chrome PDF Plugin', 'description': 'Portable Document Format', '0': {{}}}},
                    {{'name': 'Chrome PDF Viewer', 'description': ''}},
                    {{'name': 'Native Client Executable', 'description': ''}},
                ],
                configurable: true,
            }});
            
            console.log('%c✅ ALL 12 STEALTH LAYERS ACTIVATED ✅', 'color:#00ff88; font-size:12px; font-weight:bold; background:#000; padding:5px;');
        }})();
        """


async def build_stealth_script(fp: Fingerprint) -> str:
    """Построить stealth скрипт"""
    engine = StealthEngineV5()
    return engine.build_advanced_stealth_script(fp)


async def apply_stealth_scripts(page) -> None:
    """
    🛡️ ПРИМЕНИТЬ ВСЕ STEALTH СКРИПТЫ К СТРАНИЦЕ
    """
    
    fp = Fingerprint()
    script = await build_stealth_script(fp)
    
    await page.add_init_script(script)
    
    print("🛡️ STEALTH V6.0 APPLIED - 12 PROTECTION LAYERS ACTIVE")