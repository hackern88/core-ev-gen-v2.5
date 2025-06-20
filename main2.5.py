global tokens_generated  # inserted
global discord_id  # inserted
global config  # inserted
import asyncio
import random
import string
import requests
import re
import time
import json
import os
from datetime import datetime
from colorama import Fore, Style, init
from pystyle import *
init(autoreset=True)
API_ENDPOINT = 'http://dv-n6.divahost.net:6094/api/client'
API_KEY = 'workerevesgenhere'
PRODUCT = 'EVS-GEN'
VERSION = '1.0.0'
EMAIL_API_URL = 'https://leveragers.xyz/api/email'
RESULT_API_URL = 'https://leveragers.xyz/api/result'
EMAIL_API_KEY = '3PY5ACVKX5YA8QV3U45SG9WAEL0XLWDT'
EMAIL_HEADERS = {'Authorization': f'Bearer {EMAIL_API_KEY}', 'Content-Type': 'application/json'}
DATABASE_URL = 'http://dv-n1.divahost.net:50345'
DATABASE_API_ENDPOINT = f'{DATABASE_URL}/api/add_token'
SERVER_INVITES = ['https://discord.gg/coregen']
config = {}
discord_id = ''
tokens_generated = 0
BANNER = f'{Fore.CYAN}{Style.BRIGHT}\n ██████╗ ██████╗ ██████╗ ███████╗     ██████╗ ███████╗███╗   ██╗\n██╔════╝██╔═══██╗██╔══██╗██╔════╝    ██╔════╝ ██╔════╝████╗  ██║\n██║     ██║   ██║██████╔╝█████╗      ██║  ███╗█████╗  ██╔██╗ ██║\n██║     ██║   ██║██╔══██╗██╔══╝      ██║   ██║██╔══╝  ██║╚██╗██║\n╚██████╗╚██████╔╝██║  ██║███████╗    ╚██████╔╝███████╗██║ ╚████║\n ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝\n{Style.RESET_ALL}'
BANNER1 = f'{Fore.CYAN}{Style.BRIGHT}\n[+] Discord Token Generator [+]\n [+] Programmed By CoreGen [+]\n{Style.RESET_ALL}'
PRONOUNS_LIST = ['he/him', 'she/her', 'they/them', 'he/they', 'she/they', 'any pronouns', 'ask me', 'ze/zir', 'xe/xem', 'it/its', 'fae/faer', 'ey/em', 've/ver', 'ne/nem', 'co/cos']
BIO_LIST = ['Just vibing and gaming 🎮', 'Coffee addict ☕ | Code enthusiast 💻', 'Gamer | Streamer | Dreamer ✨', 'Living life one pixel at a time 🎨', 'Music lover 🎵 | Night owl 🦉', 'Aspiring developer | Learning everyday 📚', 'Anime fan | Manga reader 📖', 'Always down for a good conversation 💬', 'Tech enthusiast | Future innovator 🚀', 'Artist at heart | Creator by choice 🎭', 'Foodie | Traveler | Adventure seeker 🌍', 'Minimalist | Productivity nerd ⚡', 'Plant parent 🌱 | Book worm 📚', 'Fitness enthusiast | Health conscious 💪', 'Photographer | Capturing moments 📸', 'Love is all you need 💕', 'Making memories one day at a time', 'Exploring the world through pixels', 'Digital nomad | Creative soul', 'Building dreams in code', 'Gaming is my therapy 🎯', 'Collecting moments, not things', 'Living in a world of possibilities']

def load_config():
    """Load license key from config.json"""  # inserted
    global config  # inserted
    try:
        if not os.path.exists('config.json'):
            log('Configuration file not found!', Fore.RED, 'ERROR')
            print(f'{Fore.YELLOW}Please create config.json with your license key.{Style.RESET_ALL}')
            input('Press Enter to exit...')
            exit()
        with open('config.json', 'r') as f:
            config = json.load(f)
            if 'license_key' not in config or not config['license_key'] or config['license_key'] == 'YOUR_LICENSE_KEY_HERE':
                    log('Missing or invalid license key in config.json!', Fore.RED, 'ERROR')
                    print(f'{Fore.YELLOW}Please update config.json with a valid license key.{Style.RESET_ALL}')
                    input('Press Enter to exit...')
                    exit()
            log('Configuration loaded successfully', Fore.GREEN, 'CONFIG')
            return True
    except Exception as e:
        log(f'Failed to load configuration: {e}', Fore.RED, 'ERROR')
        input('Press Enter to exit...')
        exit()

def verify_license():
    """Verify license key with the server"""  # inserted
    global discord_id  # inserted
    try:
        log('Verifying license key...', Fore.CYAN, 'LICENSE')
        headers = {'Authorization': API_KEY}
        data = {'license': config['license_key'], 'product': PRODUCT, 'version': VERSION}

        response = requests.post(API_ENDPOINT, headers=headers, json=data, timeout=10)
        status = response.json()
        if status.get('status_overview') == 'success':
            discord_id = status.get('discord_id', 'Unknown')
            log('License key is valid!', Fore.GREEN, 'LICENSE')
            log(f'Discord ID: {discord_id}', Fore.CYAN, 'USER')
        return True
    except Exception as e:
        log(f'License verification failed: {e}', Fore.RED, 'ERROR')
        log('Please check your internet connection and API endpoint.', Fore.YELLOW, 'NETWORK')
        input('Press Enter to exit...')
        exit()

def check_dashboard_status():
    """Check if dashboard is online and accessible"""  # inserted
    try:
        response = requests.get(f'{DATABASE_URL}/api/status', timeout=5)
        if response.status_code == 200:
            status = response.json()
            log(f"DataBase Status: {status['status']}", Fore.GREEN, 'DATABASE')
        return True
    except Exception as e:
        log('DataBase Is Offline Wait Until It ComeBack: Report On CoreGen', Fore.YELLOW, 'DATABASE')
        input('Press Enter to exit...')
        exit()

def send_token_to_dashboard(email, password, token, humanized=False, servers_joined=0):
    """Send generated token data to the dashboard"""  # inserted
    try:
        data = {'discord_id': discord_id, 'email': email, 'password': password, 'token': token, 'license_key': config['license_key'], 'humanized': humanized, 'servers_joined': servers_joined}
        response = requests.post(DATABASE_API_ENDPOINT, json=data, timeout=10)
        if response.status_code == 200:
            result = response.json()
            log('Token data saved successfully', Fore.GREEN, 'DATABASE')
        return True
    except Exception as e:
        log(f'Failed to send to database: {e}', Fore.RED, 'DATABASE')
        return False

def log(msg, color=Fore.WHITE, prefix='INFO', timestamp=True):
    """Enhanced logging function with professional styling"""  # inserted
    if timestamp:
        time_str = datetime.now().strftime('%H:%M:%S')
        print(f'{Fore.CYAN}[{time_str}]{Style.RESET_ALL} {color}[{prefix}]{Style.RESET_ALL} {msg}')
    return None

def get_discord_api_headers(token=None):
    """Generate Discord API headers that match Chrome browser"""  # inserted
    headers = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Content-Type': 'application/json', 'DNT': '1', 'Origin': 'https://discord.com', 'Referer': 'https://discord.com/', 'Sec-Ch-Ua': '\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"', 'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Platform': '\"Windows\"', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', 'X-Debug-Options': 'bugReporterEnabled', 'X-Discord-Locale': 'en-US', 'X-Discord-Timezone': 'America/New_York', 'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExOS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE5LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyNTU5NzEsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGwsImRlc2lnbl9pZCI6MH0='}
    if token:
        headers['Authorization'] = token
    return headers

def get_discord_cookies():
    """Get Discord cookies for requests"""  # inserted
    try:
        session = requests.Session()
        response = session.get('https://discord.com')
        cookies = {}
        for cookie in response.cookies:
            if cookie.name.startswith('__') and cookie.name.endswith('uid'):
                pass  # postinserted
            else:  # inserted
                cookies[cookie.name] = cookie.value
        else:  # inserted
            return '; '.join([f'{k}={v}' for k, v in cookies.items()]) + '; locale=en-US'
    except:
        pass  # postinserted
    return '__dcfduid=4e0a8d504a4411eeb88f7f88fbb5d20a; __sdcfduid=4e0a8d514a4411eeb88f7f88fbb5d20ac488cd4896dae6574aaa7fbfb35f5b22b405bbd931fdcb72c21f85b263f61400; __cfruid=f6965e2d30c244553ff3d4203a1bfdabfcf351bd-1699536665; _cfuvid=rNaPQ7x_qcBwEhO_jNgXapOMoUIV2N8FA_8lzPV89oM-1699536665234-0-604800000; locale=en-US'

def get_email_from_api():
    """Generate temporary email using API"""  # inserted
    log('Generating temporary email...', Fore.CYAN, 'EMAIL')
    try:
        res = requests.post(EMAIL_API_URL, headers=EMAIL_HEADERS, timeout=10)
        if res.status_code == 200:
            email = res.json().get('email')
            if email:
                log(f'Email generated: {email}', Fore.GREEN, 'EMAIL')
                return email
        return
    except Exception as e:
        log(f'Email API Exception: {e}', Fore.RED, 'EMAIL')

def get_token(email, password):
    """Get Discord token using login API with undetectable headers"""  # inserted
    try:
        payload = {'login': email, 'password': password}
        headers = get_discord_api_headers()
        headers.update({'Referer': 'https://discord.com/login', 'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkxvZ2luIn0=', 'Cookie': get_discord_cookies()})
        session = requests.Session()
        session.get('https://discord.com/login', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'})
        res = session.post('https://discord.com/api/v9/auth/login', json=payload, headers=headers, timeout=10)
        if res.status_code == 200 and 'token' in res.json():
            token = res.json()['token']
            log(f'Token retrieved: {token[:25]}...', Fore.GREEN, 'TOKEN')
            return token
    except Exception as e:
        log(f'Token error: {e}', Fore.RED, 'TOKEN')

async def detect_captcha_on_page(page):
    """Enhanced CAPTCHA detection for any page"""  # inserted
    captcha_selectors = ['iframe[src*=\"captcha\"]', 'iframe[src*=\"recaptcha\"]', 'iframe[src*=\"hcaptcha\"]', 'div[class*=\"captcha\"]', 'div[class*=\"recaptcha\"]', 'div[class*=\"hcaptcha\"]', '[data-sitekey]', '.h-captcha', '.g-recaptcha', '#captcha', '[id*=\"captcha\"]', 'div[data-testid*=\"captcha\"]', 'div[aria-label*=\"captcha\"]']
    for selector in captcha_selectors:
        element = await page.query_selector(selector)
        if element:
            pass  # postinserted
        else:  # inserted
            return True
    else:  # inserted
        page_content = await page.get_content()
        captcha_indicators = ['captcha', 'recaptcha', 'hcaptcha', 'challenge', 'verify you are human', 'prove you\'re not a robot', 'security check']
        for indicator in captcha_indicators:
            if indicator.lower() in page_content.lower():
                pass  # postinserted
            else:  # inserted
                return True
        else:  # inserted
            return False

async def wait_for_user_input(message):
    """Wait for user to press Enter in console"""  # inserted
    return await asyncio.to_thread(input, message)

async def join_discord_servers(page, servers_to_join=1):
    """Join Discord servers using direct invite links - Simplified and more reliable"""  # inserted
    log('🚀 Starting direct server joining process...', Fore.CYAN, 'NON-CAP')
    servers_joined = 0
    try:
        selected_invite = random.choice(SERVER_INVITES)
        try:
            log(f" Joining server via direct invite: {selected_invite.split('/')[(-1)]}", Fore.CYAN, 'NON-CAP')
            await page.get(selected_invite)
            await asyncio.sleep(6)
            log(f' Direct server joining completed: {servers_joined}/1 server joined', Fore.GREEN if servers_joined == 1 else Fore.RED, 'NON-CAP')
            return servers_joined
        except Exception as e:
            log(f' Error during direct server join: {str(e)[:50]}...', Fore.RED, 'NON-CAP')
    except Exception as e:
        log(f' Direct server joining process failed: {str(e)[:50]}...', Fore.RED, 'NON-CAP')
        return servers_joined

def humanize_token(token):
    """Enhanced token humanization with proper Discord API usage"""  # inserted
    log('Starting token humanization...', Fore.CYAN, 'HUMANIZE')
    headers = get_discord_api_headers(token)
    headers['Cookie'] = get_discord_cookies()
    success_count = 0
    session = requests.Session()
    try:
        pronouns = random.choice(PRONOUNS_LIST)
        pronouns_payload = {'pronouns': pronouns}
        pronouns_headers = headers.copy()
        pronouns_headers['Referer'] = 'https://discord.com/channels/@me'
        res = session.patch('https://discord.com/api/v9/users/@me/profile', json=pronouns_payload, headers=pronouns_headers, timeout=10)
        if res.status_code == 200:
            log(f'Pronouns set: {pronouns}', Fore.GREEN, 'PRONOUNS')
            success_count += 1
            await_time = random.uniform(2, 4)
            time.sleep(await_time)
            try:
                bio = random.choice(BIO_LIST)
                bio_payload = {'bio': bio}
                bio_headers = headers.copy()
                bio_headers['Referer'] = 'https://discord.com/channels/@me'
                res = session.patch('https://discord.com/api/v9/users/@me/profile', json=bio_payload, headers=bio_headers, timeout=10)
                if res.status_code == 200:
                    log(f'Bio set: {bio[:30]}...', Fore.GREEN, 'BIO')
                    success_count += 1
                    await_time = random.uniform(2, 4)
                    time.sleep(await_time)
                    hypersquad_houses = [{'house_id': 1, 'name': 'Bravery'}, {'house_id': 2, 'name': 'Brilliance'}, {'house_id': 3, 'name': 'Balance'}]
                    selected_house = random.choice(hypersquad_houses)
                    try:
                        hypersquad_payload = {'house_id': selected_house['house_id']}
                        hypersquad_headers = headers.copy()
                        hypersquad_headers['Referer'] = 'https://discord.com/settings/hypesquad'
                        hypersquad_headers['X-Context-Properties'] = 'eyJsb2NhdGlvbiI6IkpvaW4gSHlwZXJTcXVhZCJ9'
                        res = session.post('https://discord.com/api/v9/hypesquad/online', json=hypersquad_payload, headers=hypersquad_headers, timeout=10)
                        if res.status_code in [204, 200]:
                            log(f"Joined HyperSquad {selected_house['name']}", Fore.GREEN, 'HYPERSQUAD')
                            success_count += 1
                            await_time = random.uniform(2, 4)
                            time.sleep(await_time)
                            try:
                                settings_payload = {'show_current_game': True, 'default_guilds_restricted': False, 'inline_attachment_media': True, 'inline_embed_media': True, 'gif_auto_play': True, 'render_embeds': True, 'render_reactions': True, 'animate_emoji': True, 'enable_tts_command': True, 'message_display_compact': False, 'convert_emoticons': True, 'explicit_content_filter': 1, 'disable_games_tab': False, 'timezone_offset': (-300), 'theme': random.choice(['dark', 'light']), 'developer_mode': False, 'afk_timeout': 600, 'locale': 'en-US'}
                                settings_headers = headers.copy()
                                settings_headers['Referer'] = 'https://discord.com/channels/@me'
                                res = session.patch('https://discord.com/api/v9/users/@me/settings', json=settings_payload, headers=settings_headers, timeout=10)
                                if res.status_code == 200:
                                    log('User settings optimized', Fore.GREEN, 'SETTINGS')
                                    success_count += 1
                                    if success_count == 4:
                                        log('Humanization completed successfully! (4/4 features)', Fore.GREEN, 'HUMANIZE')
                                    return True
                            except Exception as e:
                                log(f'Error updating settings: {e}', Fore.YELLOW, 'SETTINGS')
                    except Exception as e:
                        log(f'Error setting pronouns: {e}', Fore.RED, 'PRONOUNS')
            except Exception as e:
                    log(f'Error setting bio: {e}', Fore.RED, 'BIO')
            except Exception as e:
                log(f'Error joining HyperSquad: {e}', Fore.RED, 'HYPERSQUAD')
            except Exception as e:
                log(f'Error updating settings: {e}', Fore.YELLOW, 'SETTINGS')

def extract_verification_link_from_content(content, email_type='text'):
    """Extract verification link from email content using multiple methods"""  # inserted
    if not content:
        pass  # postinserted
    url_patterns = None + ['https?://(?:discord\\.com|discordapp\\.com)/verify[^\\s<>\"\\\']+', 'https?://(?:discord\\.com|discordapp\\.com)/api/auth/verify[^\\s<>\"\\\']+', 'https?://click\\.discord\\.com/[^\\s<>\"\\\']+', 'https?://[^\\s<>\"\\\']*discord[^\\s<>\"\\\']*[?&]token=[^\\s<>\"\\\'&]+', 'https?://[^\\s<>\"\\\']*discord[^\\s<>\"\\\']*[^\\s<>\"\\\']*(?:verify|confirm|activate)[^\\s<>\"\\\']*', 'https?://[^\\s<>\"\\\']*(?:discord\\.com|discordapp\\.com)[^\\s<>\"\\\']*[a-zA-Z0-9_-]{20,}[^\\s<>\"\\\']*']

def validate_discord_verification_url(url):
    """Validate if a URL is likely a Discord verification link"""  # inserted
    if not url:
        pass  # postinserted
    return (False, 'Empty URL')

def is_verification_email(subject, text, html, sender):
    """Enhanced function to specifically identify Discord verification emails"""  # inserted
    subject_lower = subject.lower()
    text_lower = text.lower() if text else ''
    html_lower = html.lower() if html else ''
    sender_lower = sender.lower()
    discord_senders = ['discord.com', 'discordapp.com', 'noreply@discord.com', '@discord.com', '@discordapp.com', 'discord']
    is_from_discord = any((discord_sender in sender_lower for discord_sender in discord_senders))
    if not is_from_discord:
        pass  # postinserted
    return False

def get_verification_link(email):
    """Get verification link from email with enhanced filtering for verification emails only"""  # inserted
    log('Waiting for verification email...', Fore.CYAN, 'VERIFY')
    processed_email_ids = set()
    for i in range(150):
        try:
            check_interval = random.uniform(2.5, 3.5)
            res = requests.post(RESULT_API_URL, headers=EMAIL_HEADERS, json={'email': email, 'parse_links': True}, timeout=15)
            if res.status_code == 200:
                data = res.json().get('data', [])
                if not data:
                    log(f'Checking inbox... ({i + 1}/30)', Fore.YELLOW, 'VERIFY') if i % 10 == 0 else log(f'Checking inbox... ({i + 1}/30)', Fore.YELLOW, 'VERIFY')
            else:  # inserted
                break
            time.sleep(check_interval)
        except requests.exceptions.Timeout:
            if i % 15 == 0:
                log('Email API timeout, retrying...', Fore.YELLOW, 'VERIFY')
        except Exception as e:
            log(f'Error while checking verification email: {e}', Fore.RED, 'VERIFY')
    log('Verification email not received in time', Fore.RED, 'VERIFY')

def random_username():
    """Generate random username"""  # inserted
    Midnight_Rider = ['stylish_dude_88', 'the_desi_dude', 'boy_with_swag', 'the_urban_dude', 'the_boy_in_black', 'the_cool_guy_next_door', 'the_funky_boy', 'the_boy_with_the_swag', 'the_boy_with_the_style', 'the_boy_with_the_attitude', 'Mr_cool_personality', 'the_boy_with_the_smile', 'the_boy_with_the_edge', 'Mr_cool_king', 'The_Geek_Genius', 'The_Nerd_Whiz', 'The_Guru_of_Gadgets', 'The_Game_Master', 'Mr_Futuristic', 'Midnight_Rider', 'Shark_Slayer', 'The_Inventor_King', 'Adrenaline_Junkie', 'Danger_Zone_Dude', 'Fast_Furious', 'Stylish_stud', 'Fearless_Fighter_26', 'Daring_Dude_28', 'Resourceful_Racer_12', 'Rebellious_Rocker_13', 'Sharp_Shooter_8', 'Crazy_Carpenter_22', 'Jaunty_Juggler_12', 'Wild_Wanderer_2', 'Hyper_Hipster_73', 'Ambitious_Athlete_38', 'Crazy_dude_19', 'Unique_Urbanite_32', 'Irreverent_Innovator_47', 'Brazen_Biker_95', 'Unruly_Urbanite_02', 'Impetuous_Illusionist_90', 'NutsNerd', 'WildChildGuy', 'FreakyFella', 'CrazyCobraKid', 'WildWonderBoy', 'DarindDude7', 'LoopyLad', 'ManiacMuscleMan', 'FierceFighterDude', '
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return random.choice(prefixes) + suffix

def random_disname():
    """Generate random displayname"""  # inserted
    LOAD_CONST = ['ntk13', 'Glory', 'Lil_Drippzz', 'TheGlizzyGladiator', 'Ooga Booga', 'nicojustnico', 'Nado', 'Duck life 4 (IGN)', 'OilyBuht', 'pure', 'villa', 'EH', 'ŠtârÄłêx', '𝕮𝖍𝖎𝖕𝖘𝖆𝖓𝖉𝕼𝖚𝖊𝖘𝖔', 'Smurda', 'Ipoketurtles', 'A10WILDFIRE', 'Athena The Doe', 'Fwooji', 'bnicccck', 'Mr_Biggerz', 'reapz', 'Gene10101', 'Boggers', 'ungawdly', 'ToHighToday', 'sadTV', 'Arvin', 'AmITrippingOrWhatBro?', 'Wokeie', 'Dylaniz', 'SANGOKU', 'i_no_caleb', 'Prodigy', 'Rose Nynx', 'nydasa', 'beysu', 'DigitalProtocol', 'SlippIsTrash', 'Wizzy', 'W4vewalker', 'Zarrx', 'Nomiton', 'Zenith', 'xiffy', '! woc', 'MasonGamerTV', 'BlazinChill', 'dboss', 'FastBands', 'Lxllo', '
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return random.choice(display_names) + suffix

def random_password():
    """Generate secure random password"""  # inserted
    chars = string.ascii_letters + string.digits + '!@#$%'
    return ''.join(random.choices(chars, k=12))

async def wait_for_multiple_selectors(page, selectors, timeout=30):
    """Wait for any of the provided selectors and return the first found element"""  # inserted
    for _ in range(timeout * 2):
        for selector in selectors:
            el = await page.query_selector(selector)
            if el:
                pass  # postinserted
            else:  # inserted
                return (el, selector)
        else:  # inserted
            await asyncio.sleep(0.5)
    else:  # inserted
        raise Exception('Timeout waiting for selectors')

async def fill_form_field(page, field_name, value, selectors_list):
    """Try multiple selectors to fill a form field"""  # inserted
    try:
        element, used_selector = await wait_for_multiple_selectors(page, selectors_list, 15)
            await element.send_keys(value)
                log(f'{field_name} filled successfully', Fore.GREEN, 'FORM')
                return True
    except Exception as e:
        log(f'Failed to fill {field_name}', Fore.RED, 'FORM')
        return False

async def click_dropdown_item_with_js(page, label):
    """Click dropdown item using JavaScript"""  # inserted
    try:
        await asyncio.sleep(1)
            js = f'(function() {\n            const elements = document.querySelectorAll(\'div, span, button\');\n            for (let element of elements) {\n                if (element.innerText && element.innerText.trim() === \"{label}\") {\n                    element.click();\n                    return true;\n                }\n            }\n            return false;\n        })();'
            result = await page.evaluate(js)
                if result:
                    log(f'Selected: {label}', Fore.GREEN, 'FORM')
                await asyncio.sleep(1)
    except Exception as e:
        log(f'Failed to select {label}', Fore.RED, 'FORM')

async def detect_captcha(page):
    """Detect if CAPTCHA is present on the page"""  # inserted
    captcha_selectors = ['iframe[src*=\"captcha\"]', 'iframe[src*=\"recaptcha\"]', 'iframe[src*=\"hcaptcha\"]', 'div[class*=\"captcha\"]', 'div[class*=\"recaptcha\"]', 'div[class*=\"hcaptcha\"]', '[data-sitekey]', '.h-captcha', '.g-recaptcha', '#captcha', '[id*=\"captcha\"]']
    for selector in captcha_selectors:
        element = await page.query_selector(selector)
        if element:
            pass  # postinserted
        else:  # inserted
            return True
    else:  # inserted
        page_content = await page.get_content()
        captcha_indicators = ['captcha', 'recaptcha', 'hcaptcha', 'challenge', 'verify you are human', 'prove you\'re not a robot']
        for indicator in captcha_indicators:
            if indicator.lower() in page_content.lower():
                pass  # postinserted
            else:  # inserted
                return True
        else:  # inserted
            return False

async def wait_for_complete_form(page, timeout=60):
    """Wait for ALL registration form fields to be available"""  # inserted
    try:
        log(' Waiting for complete registration form...', Fore.CYAN, 'FORM')
        required_selectors = ['input[name=\"email\"], input[type=\"email\"]', 'input[name=\"username\"]', 'input[name=\"password\"], input[type=\"password\"]']
        for i in range(timeout):
            all_ready = True
            for selector_group in required_selectors:
                selectors = [s.strip() for s in selector_group.split(',')]
                    found = False
                    for selector in selectors:
                        element = await page.query_selector(selector)
                            if element:
                                pass  # postinserted
                            else:  # inserted
                                found = True
                                break
                    if not found:
                        pass  # postinserted
                    else:  # inserted
                        all_ready = False
                        break
            if all_ready:
                log(' Complete registration form ready!', Fore.GREEN, 'FORM')
                await asyncio.sleep(1)
                except:
                    pass  # postinserted
            else:  # inserted
                return True
        else:  # inserted
            log(' Complete form not ready within timeout', Fore.RED, 'FORM')
            return False
    except Exception as e:
        log(f' Error waiting for complete form: {e}', Fore.RED, 'FORM')
        return False

async def create_discord_account():
    """Create a single Discord account with undetectable Chrome usage"""  # inserted
    global tokens_generated  # inserted
    email = get_email_from_api()
    if not email:
        pass  # postinserted
    return False

def display_stats():
    """Display current statistics"""  # inserted
    print(f"\n{Fore.CYAN}{'======================================================================'}{Style.RESET_ALL}")
    print(f'{Fore.CYAN} Tokens Generated: {tokens_generated}{Style.RESET_ALL}')
    print(f'{Fore.CYAN} Next Generation: 5 seconds{Style.RESET_ALL}')
    print(f"{Fore.CYAN}{'======================================================================'}{Style.RESET_ALL}\n")

async def main():
    """Main function - continuous token generation with server joining (1 server)"""  # inserted
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(BANNER)))
    print(Colorate.Vertical(Colors.green_to_blue, Center.XCenter(BANNER1)))
    load_config()
    verify_license()
    dashboard_online = check_dashboard_status()
    if not dashboard_online:
        log('Dashboard is offline', Fore.RED, 'DATABASE')
        input('Press Enter to exit...')
        exit()
    log(' Starting continuous token generation...', Fore.GREEN, 'SYSTEM')
    log(f' Licensed to: {discord_id}', Fore.CYAN, 'LICENSE')
    pass
    try:
        log(f' Starting account creation cycle #{tokens_generated + 1}...', Fore.CYAN, 'CYCLE')
        success = await create_discord_account()
            if success:
                display_stats()
                log(' Waiting 5 seconds before next generation...', Fore.CYAN, 'CYCLE')
                for i in range(5, 0, (-1)):
                    dots = '.' * (4 - i % 4)
                    spaces = ' ' * (i % 4)
                    print(f'\r{Fore.YELLOW} Next generation in: {i:2d} seconds {dots}{spaces}{Style.RESET_ALL}', end='', flush=True)
                    time.sleep(1)
                print()
    except KeyboardInterrupt:
        log(' Stopping token generation by user request...', Fore.YELLOW, 'SYSTEM')
    print(f"\n{Fore.CYAN}{'======================================================================'}{Style.RESET_ALL}")
    print(f'{Fore.CYAN} Total Tokens Generated: {tokens_generated}{Style.RESET_ALL}')
    print(f"{Fore.CYAN}{'======================================================================'}{Style.RESET_ALL}")
    log(' Token generator stopped successfully', Fore.CYAN, 'SYSTEM')
    input('\nPress Enter to exit...')
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f'\n{Fore.YELLOW} Program interrupted by user{Style.RESET_ALL}')
