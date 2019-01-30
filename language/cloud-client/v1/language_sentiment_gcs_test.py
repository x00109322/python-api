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

from language_sentiment_gcs import analyze_sentiment

def test_language_sentiment_gcs_positive_sentiment(capsys):
    analyze_sentiment(
        gcs_uri='gs://cloud-samples-data/language/positive.txt')
    out, _ = capsys.readouterr()

    assert 'Score: 0.' in out
    assert 'Magnitude: 0.' in out

def test_language_sentiment_gcs_negative_sentiment(capsys):
    analyze_sentiment(
        gcs_uri='gs://cloud-samples-data/language/negative.txt')
    out, _ = capsys.readouterr()

    assert 'Score: -0.' in out
    assert 'Magnitude: 0.' in out