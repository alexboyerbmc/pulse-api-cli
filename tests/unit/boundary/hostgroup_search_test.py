#!/usr/bin/env python
#
# Copyright 2015 BMC Software, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import json
from unittest import TestCase
from string import split

from boundary import HostgroupCreate
from boundary import HostgroupDelete
from boundary import HostgroupSearch
from cli_runner import CLIRunner
from cli_test import CLITest


class HostgroupSearchTest(TestCase):

    def setUp(self):
        self.cli = HostgroupSearch()

    def test_cli_description(self):
        CLITest.check_description(self, self.cli)

    def test_cli_help(self):
        CLITest.check_cli_help(self, self.cli)

    def test_create_curl(self):
        runner = CLIRunner(self.cli)

        filter_name = 'My-Filter'

        curl = runner.get_output(['-n', filter_name,
                                  '-z'])
        CLITest.check_curl(self, self.cli, curl)

    def test_search_filter(self):
        runner_create = CLIRunner(HostgroupCreate())
        filter_name = 'Filter' + CLITest.random_string(6)
        sources = 'foo,bar,red,green'

        create = runner_create.get_output(['-n', filter_name,
                                           '-s', sources])
        filter_create = json.loads(create)
        filter = filter_create['result']
        filter_id = filter['id']

        runner_search = CLIRunner(HostgroupSearch())
        search = runner_search.get_output(['-n', filter_name])
        filter_search = json.loads(search)
        filter = filter_search['result']

        self.assertEqual(filter_name, filter[0]['name'])
        self.assertItemsEqual(split(sources, ','), filter[0]['hostnames'])

        runner_delete = CLIRunner(HostgroupDelete())
        delete = runner_delete.get_output(['-i', str(filter_id)])
        delete_result = json.loads(delete)
        self.assertTrue(delete_result['result']['success'])
