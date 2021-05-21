# Copyright (C) 2015 Bahtiar `kalkin-` Gadimov <bahtiar@gadimov.de>
#
# This file is part of OMEMO Gajim Plugin.
#
# OMEMO Gajim Plugin is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation; version 3 only.
#
# OMEMO Gajim Plugin is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with OMEMO Gajim Plugin. If not, see <http://www.gnu.org/licenses/>.

import pickle
from pathlib import Path
from gajim.common import configpaths

import binascii
import textwrap
from logging import LoggerAdapter
from enum import IntEnum

from axolotl.identitykey import IdentityKey

DEFAULT_PREKEY_AMOUNT = 100
MIN_PREKEY_AMOUNT = 80
SPK_ARCHIVE_TIME = 86400 * 15  # 15 Days
SPK_CYCLE_TIME = 86400         # 24 Hours


class Manage_Constants():

    def __init__(self):
        conf_dir = Path(configpaths.get('PLUGINS_CONFIG_DIR'))
        self.conf_file = conf_dir / 'omemo_mod.pickle'
        if not Path(self.conf_file).is_file():
            self.var = 300
            with open(self.conf_file, 'wb') as f:
                pickle.dump(self.var, f)
        else:
            with open(self.conf_file, 'rb') as f:
                self.var = pickle.load(f)

    def set_constants(self):
        with open(self.conf_file, 'wb') as f:
            pickle.dump(self.var, f)


UNACKNOWLEDGED_COUNT = Manage_Constants()


class Trust(IntEnum):
    UNTRUSTED = 0
    VERIFIED = 1
    UNDECIDED = 2
    BLIND = 3


def get_fingerprint(identity_key, formatted=False):
    public_key = identity_key.getPublicKey().serialize()
    fingerprint = binascii.hexlify(public_key).decode()[2:]
    if not formatted:
        return fingerprint
    fplen = len(fingerprint)
    wordsize = fplen // 8
    buf = ''
    for w in range(0, fplen, wordsize):
        buf += '{0} '.format(fingerprint[w:w + wordsize])
    buf = textwrap.fill(buf, width=36)
    return buf.rstrip().upper()


class IdentityKeyExtended(IdentityKey):
    def __hash__(self):
        return hash(self.publicKey.serialize())

    def get_fingerprint(self, formatted=False):
        return get_fingerprint(self, formatted=formatted)
