#   BAREOS - Backup Archiving REcovery Open Sourced
#
#   Copyright (C) 2020-2020 Bareos GmbH & Co. KG
#
#   This program is Free Software; you can redistribute it and/or
#   modify it under the terms of version three of the GNU Affero General Public
#   License as published by the Free Software Foundation and included
#   in the file LICENSE.
#
#   This program is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#   Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
#   02110-1301, USA.

import bareosfd


def load_bareos_plugin(plugindef):
    print("Hello from load_bareos_plugin")
    print(plugindef)
    print(bareosfd)
    bareosfd.DebugMessage(100, str(dir(bareosfd)))
    bareosfd.DebugMessage(100, "Kuckuck")
    bareosfd.DebugMessage(100, 'Kückuck->C\udcc3N')
    bareosfd.JobMessage(100, "Kuckuck")
    bareosfd.JobMessage(100, 'Kückuck->C\udcc3N')

    test_SavePacket = bareosfd.SavePacket(fname='Kückuck->C\udcc3N')

    bareosfd.DebugMessage(100, str(test_SavePacket))
