#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import os

from mybot import (
    DOWNLOAD_LOCATION,
    TG_BOT_TOKEN,
    APP_ID,
    API_HASH,
)

from pyrogram import Client, Filters, MessageHandler, CallbackQueryHandler

from mybot.plugins.incoming_message_fn import incoming_message_f, incoming_youtube_dl_f
from mybot.plugins.call_back_button_handler import button
from mybot.plugins.custom_thumbnail import (
    save_thumb_nail,
    clear_thumb_nail
)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    #
    app = Client(
        "PublicBot",
        bot_token=TG_BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        workers=128
    )
    #
    incoming_message_handler = MessageHandler(
        incoming_message_f,
        filters=Filters.command(["upload"]) 
    )
    app.add_handler(incoming_message_handler)
    #
    incoming_youtube_dl_handler = MessageHandler(
        incoming_youtube_dl_f,
        filters=Filters.command(["ytdl"])
    )
    app.add_handler(incoming_youtube_dl_handler)
    #
    save_thumb_nail_handler = MessageHandler(
        save_thumb_nail,
        filters=Filters.command(["savethumbnail"]) 
    )
    app.add_handler(save_thumb_nail_handler)
    #
    clear_thumb_nail_handler = MessageHandler(
        clear_thumb_nail,
        filters=Filters.command(["clearthumbnail"]) 
    )
    app.add_handler(clear_thumb_nail_handler)
    #
    app.run()
