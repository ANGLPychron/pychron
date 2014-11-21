# ===============================================================================
# Copyright 2013 Jake Ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.declarative import declarative_base

# ============= enthought library imports =======================

# ============= standard library imports ========================
# ============= local library imports  ==========================
Base = declarative_base()


def foreignkey(name):
    return Column(Integer, ForeignKey('{}.id'.format(name)))


def stringcolumn(size=40, *args, **kw):
    return Column(String(size), *args, **kw)

# ============= EOF =============================================
