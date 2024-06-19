#
# Copyright (C) 2024 by TheTeamVivek@Github, < https://github.com/TheTeamVivek >.
#
# This file is part of < https://github.com/TheTeamVivek/YukkiMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheTeamVivek/YukkiMusic/blob/master/LICENSE >
#
# All rights reserved.
#

import sys
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import BotCommand
import config

from ..logging import LOGGER


class YukkiBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Alem Müzik Başlıyor")
        super().__init__(
            "YukkiMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.mention = self.me.mention

        try:
            await self.send_message(
                config.LOG_GROUP_ID,
                text=f"<u><b>{self.mention} Alem Müzik Yayında :</b><u>\n\nɪᴅ : <code>{self.id}</code>\nɴᴀᴍᴇ : {self.name}\nᴜsᴇʀɴᴀᴍᴇ : @{self.username}",
            )
        except:
            LOGGER(__name__).error(
                "Bot has failed to access the log Group. Make sure that you have added your bot to your log channel and promoted as admin!"
            )
            sys.exit()
        if config.SET_CMDS:
            try:
                await self.set_bot_commands(
                    [
                        BotCommand("start", "Başlat"),
                        BotCommand("ping", "Bot Hız Ölçümü Yapar."),
                        BotCommand("play", "Müzik Oynatır."),
                        BotCommand("skip", "Sıradaki Parçayı Oynatır."),
                        BotCommand("pause", "Medya Yayınını Durdurur."),
                        BotCommand("resume", "Yayını Devam Ettirir."),
                        BotCommand("end", "Yayını Sonlandırır."),
                        BotCommand("shuffle", "Listeyi Karışık Oynatır."),
                        BotCommand(
                            "playmode",
                            "Oynatma Modunu Değiştirir",
                        ),
                        BotCommand(
                            "settings",
                            "Grup İçinde Bot Ayarını Açar.",
                        ),
                    ]
                )
            except:
                pass
        else:
            pass
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error("Log Grubunda Bota Yetki Ver")
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"Alem Müzik Yayında as {self.name}")
