import math

from pyrogram.types import InlineKeyboardButton

from JioSavaan.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 10:
        ba = "⚪─────────"
    elif 10 < anon < 20:
        ba = "━⚪────────"
    elif 20 <= anon < 30:
        ba = "━━⚪───────"
    elif 30 <= anon < 40:
        ba = "━━━⚪──────"
    elif 40 <= anon < 50:
        ba = "━━━━⚪─────"
    elif 50 <= anon < 60:
        ba = "━━━━━⚪────"
    elif 60 <= anon < 70:
        ba = "━━━━━━⚪───"
    elif 70 <= anon < 80:
        ba = "━━━━━━━⚪──"
    elif 80 <= anon < 95:
        ba = "━━━━━━━━⚪─"
    else:
        ba = "━━━━━━━━━⚪"

##bar of wynk---------------------------------------

    if 0 < anon <= 5:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 5 <= anon < 10:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 10 <= anon < 15:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 15 <= anon < 20:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 20 <= anon < 25:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 25 <= anon < 30:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 30 <= anon < 35:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 35 <= anon < 40:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 40 <= anon < 45:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣"
    elif 45 <= anon < 50:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐒𝗍υᑯ𝗂ⱺ"
    elif 50 <= anon < 55:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ"
    elif 55 <= anon < 60:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 60 <= anon < 65:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐌υ𝗌𝗂𝖼"
    elif 65 <= anon < 70:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝑴𝒖𝒔𝒊𝒄"
    elif 70 <= anon < 75:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 80 <= anon < 80:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 80 <= anon < 85:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 85 <= anon < 90:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 90 <= anon < 95:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    else:
        bar = "𝐓ɦ𝖾 𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐎𝗏𝖾𝗋"

    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text=f"{bar}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {ba} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"), 
        ],
    ]
    return buttons

def stream_markup(_, chat_id):
    buttons = [
       [
            InlineKeyboardButton(text="ᴘᴀᴜsᴇ", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="ʀᴇsᴜᴍᴇ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="sᴋɪᴘ", callback_data=f"ADMIN Skip|{chat_id}")
        ],
        [
            InlineKeyboardButton(text="sᴛᴏᴘ", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="ʀᴇᴘʟᴀʏ", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
        [

            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
        ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AviaxPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AviaxPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
