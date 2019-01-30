# Copyright 2019, Google LLC
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

import os
import re

from language_entities_text import analyze_entities

def test_language_entities_text(capsys):
    analyze_entities(
        text_content='California is a state.')
    out, _ = capsys.readouterr()

    assert 'Name: California' in out
    assert 'Type: LOCATION' in out
    assert re.search('Salience: \d\.\d', out)
    assert 'Wikipedia URL: https://en.wikipedia.org/wiki/California' in out
    assert 'Knowledge Graph MID: /m/' in out