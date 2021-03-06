"""
ReconStruct

Reconstruct is a application which helps easily reverse engineer binary file
formats.  It is tested to run on Python 2.7, 3.3, 3.4 and pypy.

Copyright (c) 2014 Sandy Carter
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

try:
    from ReconStruct.ManifestInt import ManifestInt, ParsedInt
except ImportError:
    from ManifestInt import ManifestInt, ParsedInt


class ManifestBool(ManifestInt):
    """Descriptor manifest which represents Booleans"""

    def __init__(self, label, size, type_name='bool', parent=None):
        super(ManifestBool, self).__init__(label, size, type_name, parent)

    def __call__(self, data, start=0):
        return super(ManifestBool, self).__call__(data, start)

    @classmethod
    def type(cls):
        return 'bool'

    @classmethod
    def parser(cls):
        return ParsedBool


class ParsedBool(ParsedInt):
    def __init__(self, manifest, data, index, size):
        super(ParsedBool, self).__init__(manifest, bool(data), index, size)
