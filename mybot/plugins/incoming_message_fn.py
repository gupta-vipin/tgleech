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
LOGGER = logging.getLogger(__name__)


import os

from mybot import (
    DOWNLOAD_LOCATION
)


import time
from mybot.helper_funcs.extract_link_from_message import extract_link
from mybot.helper_funcs.download_aria_p_n import call_apropriate_function, aria_start
from mybot.helper_funcs.download_from_link import request_download
from mybot.helper_funcs.display_progress import progress_for_pyrogram
from mybot.helper_funcs.youtube_dl_extractor import extract_youtube_dl_formats


async def incoming_message_f(client, message):
    """/upload command"""
    i_m_sefg = await message.reply_text("processing", quote=True)
    is_zip = False
    if len(message.command) > 1:
        if message.command[1] == "archive":
            is_zip = True
    # get link from the incoming message
    dl_url, cf_name = extract_link(message.reply_to_message)
    LOGGER.info(dl_url)
    LOGGER.info(cf_name)
    if dl_url is not None:
        await i_m_sefg.edit_text("extracting links")
        # start the aria2c daemon
        aria_i_p = await aria_start()
        LOGGER.info(aria_i_p)
        current_user_id = message.from_user.id
        # create download directory, if not exist
        if not os.path.isdir(new_download_location):
            os.makedirs(new_download_location)
        await i_m_sefg.edit_text("trying to download")
        # try to download the "link"
        sagtus, err_message = await call_apropriate_function(
            aria_i_p,
            dl_url,
            new_download_location,
            i_m_sefg,
            is_zip
        )
        if not sagtus:
            # if FAILED, display the error message
            await i_m_sefg.edit_text(err_message)
    else:
        await i_m_sefg.edit_text("**FCUK**! wat have you entered.")


async def incoming_youtube_dl_f(client, message):
    """ /ytdl command """
    i_m_sefg = await message.reply_text("processing", quote=True)
    # LOGGER.info(message)
    # extract link from message
    dl_url, cf_name = extract_link(message.reply_to_message)
    LOGGER.info(dl_url)
    LOGGER.info(cf_name)
    if dl_url is not None:
        await i_m_sefg.edit_text("extracting links")
        # list the formats, and display in button markup formats
        thumb_image, text_message, reply_markup = await extract_youtube_dl_formats(
            dl_url,
            ./,
        )
        if thumb_image is not None:
            await message.reply_photo(
                photo=thumb_image,
                quote=false,
            )
            await i_m_sefg.delete()
        else:
            await i_m_sefg.edit_text(
                text=text_message,
            )
    else:
        # if no links found, delete the "processing" message
        await i_m_sefg.delete()
