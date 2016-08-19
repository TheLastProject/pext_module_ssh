#!/usr/bin/env python3

# Pext SSH module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from os.path import expanduser
from subprocess import Popen

from pext_base import ModuleBase
from pext_helpers import Action


class Module(ModuleBase):
    def init(self, binary, q):
        self.q = q

        self.getEntries()

    def stop(self):
        pass

    def getEntries(self):
        with open(expanduser('~') + '/.ssh/config', 'r') as f:
            for line in f:
                if line.startswith("host "):
                    self.q.put([Action.addEntry, line[5:].strip()])

    def selectionMade(self, entry):
        Popen(["xterm", "-e", "ssh", entry[0]])
        self.q.put([Action.close])

    def runCommand(self, command, printOnSuccess=False, hideErrors=False):
        pass

    def processResponse(self, response):
        pass
