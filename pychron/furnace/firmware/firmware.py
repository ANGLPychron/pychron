# ===============================================================================
# Copyright 2016 Jake Ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================

# ============= enthought library imports =======================

from traits.api import HasTraits, Str, Int, Bool, Any, Float, Property, on_trait_change
from traitsui.api import View, UItem, Item, HGroup, VGroup
# ============= standard library imports ========================
# ============= local library imports  ==========================
from pychron.furnace.firmware.manager import FirmwareManager
from pychron.furnace.firmware.server import FirmwareServer
from pychron.loggable import Loggable


class Firmware(Loggable):
    manager = None
    server = None

    def bootstrap(self, **kw):
        self.manager = FirmwareManager()
        self.manager.bootstrap(**kw)
        self.server = FirmwareServer(manager=self.manager)
        self.server.bootstrap(**kw)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Run NMGRL Furnace Firmware')

    # parser.add_argument('--host',
    #                     type=str,
    #                     default='127.0.0.1',
    #                     help='host')

    parser.add_argument('--port',
                        type=int,
                        default=4567,
                        help='TCP port to listen')

    # parser.add_argument('--debug',
    #                     action='store_true',
    #                     default=False,
    #                     help='run in debug mode')

    fm = Firmware()
    fm.bootstrap(**parser.parse_args())


# ============= EOF =============================================
