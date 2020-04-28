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
import re


MAGNETIC_LINK_REGEX = r"magnet\:\?xt\=urn\:btih\:([A-Z])"
# magnet:\?xt=urn:[a-z0-9]+:[a-z0-9]{32,40}&dn=.+&tr=.+/gi
# magnet:\?xt=urn:[a-z0-9]+:[a-z0-9]{32,40}&dn=.+&tr=.+/gi
# magnet:?xt=urn:btih:B05E84BA2455A85DE9F1A3CAC01A2B36E14CBFF1



def extract_info_hash_from_ml(magnetic_link):
    ml_re_match = re.search(MAGNETIC_LINK_REGEX, magnetic_link)
    if ml_re_match is not None:
        return ml_re_match.group(1)
