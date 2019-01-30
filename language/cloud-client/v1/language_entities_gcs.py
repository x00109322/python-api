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

# [START language_entities_gcs]
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import six

def analyze_entities(
    gcs_uri='gs://cloud-samples-data/language/california.txt'):
    """Analyze entities from a text file in Google Cloud Storage
    Args:
        gcs_uri: Path to file in GCS, e.g. gs://bucket/file.txt
    """

    client = language.LanguageServiceClient()

    if isinstance(gcs_uri, six.binary_type):
        gcs_uri = gcs_uri.decode('utf-8')

    document = types.Document(
        gcs_content_uri=gcs_uri,
        type=enums.Document.Type.PLAIN_TEXT)

    response = client.analyze_entities(document)

    entities = response.entities

    for entity in entities:
        entity_type = enums.Entity.Type(entity.type)
        print('Name: {}'.format(entity.name))
        print('Type: {}'.format(entity_type.name))
        print('Salience: {}'.format(entity.salience))
        print('Wikipedia URL: {}'.format(entity.metadata.get('wikipedia_url', '-')))
        print('Knowledge Graph MID: {}'.format(entity.metadata.get('mid', '-')))
# [END language_entities_gcs]

def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--gcs_uri',
        type=str,
        default='gs://cloud-samples-data/language/california.txt')
    args = parser.parse_args()

    analyze_entities(args.gcs_uri)

if __name__ == '__main__':
    main()