"""
=====================================================================
django_base minimal django project
Copyright (C) 2016 Stefan Dieterle
e-mail: golgoths@yahoo.fr

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
=====================================================================
"""

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import requests
from lxml import etree, html
from lxml.cssselect import CSSSelector
from io import StringIO
from pprint import pprint

__author__ = 'Stefan Dieterle'


class BasicUserTestCase(StaticLiveServerTestCase):
    """
    Tests basic user interaction with the app
    """
    def test_user_input(self):
        """
        Tests response on input of some text
        :return:
        """
        # user navigates to /
        client = requests.session()
        r = client.get(self.live_server_url)
        csrftoken = client.cookies['csrftoken']
        page = html.parse(StringIO(r.text)).getroot()
        form_textarea = page.cssselect('textarea[id="id_test_text_input"]')

        # page displays no error message
        self.assertEqual(r.status_code, 200, r.text)

        # user sees input test area with a placeholder saying "Test Text"
        self.assertEqual(form_textarea[0].attrib.get('placeholder'), 'Test Text')

        # user writes "Testing 1234" in text area and submits
        r = client.post(self.live_server_url, data={'csrfmiddlewaretoken': csrftoken, 'test_text_input': 'Testing 1234'})

        # page displays no error
        self.assertEqual(r.status_code, 200, r.text)

        # user sees the submitted text displayed on page
        self.assertTrue('Testing 1234' in r.text)
