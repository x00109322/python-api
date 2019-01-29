#!/usr/bin/env python

# Copyright 2019 Google, LLC.
#
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

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-language

# [START language_sentiment_text]
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import six

def analyze_sentiment(text_content='Hello, world!'):
    """Analyze sentiment of text
    Args:
        text: Text to analyze, e.g. 'Hello, world!'
    """

    client = language.LanguageServiceClient()

    if isinstance(text_content, six.binary_type):
        text_content = text_content.decode('utf-8')

    document = types.Document(
        content=text_content,
        type=enums.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document)

    sentiment = response.document_sentiment
    print('Score: {}'.format(sentiment.score))
    print('Magnitude: {}'.format(sentiment.magnitude))
# [END language_sentiment_text]

def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--text_content',
        type=str,
        default='Hello, world!')
    args = parser.parse_args()

    analyze_sentiment(args.text_content)

if __name__ == '__main__':
    main()