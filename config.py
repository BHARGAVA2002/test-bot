#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "ecd8d9ff-4391-46c4-8a77-69b1d49dfbfc")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "6Y18Q~HH9f8hElafTCuuh7~L_QCv~qvCo8~Moa6V")
