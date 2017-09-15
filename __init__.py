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
    def init(self, settings, q):
        self.terminal = 'xterm' if ('terminal' not in settings) else settings['terminal']

        self.q = q

        self._get_entries()

    def _get_entries(self):
        with open(expanduser('~') + '/.ssh/config', 'r') as f:
            for line in f:
                if line.lower().startswith("host "):
                    hostname = line[5:].strip()
                    if hostname != "*":
                        self.q.put([Action.add_entry, hostname])

    def stop(self):
        pass

    def selection_made(self, selection):
        if len(selection) == 1:
            try:
                Popen([self.terminal, "-e", "ssh", selection[0]["value"]])
            except FileNotFoundError:
                self.q.put([Action.critical_error, "Could not open {}".format(self.terminal)])
                return

            self.q.put([Action.close])

    def process_response(self, response):
        pass
