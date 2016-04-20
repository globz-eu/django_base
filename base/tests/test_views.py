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

from django.test import TestCase
from with_asserts.mixin import AssertHTMLMixin

import re

from base.models import Text


class IndexTestCase (TestCase):
    """
    Tests for index view
    """
    def test_index_view_basic(self):
        """
        Tests that index view returns a 200 response on GET, contains the form and uses the correct template
        :return:
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Paste in your text:')
        self.assertTemplateUsed(response, 'base/index.html')

    def test_text_display_view_basic(self):
        """
        Tests that index view returns a 302 response on POST
        :return:
        """
        response = self.client.post('/', {'test_text_input': 'Test text'})

        self.assertEqual(response.status_code, 302)

    def test_redirect_to_display_on_post(self):
        """
        Tests that valid POST request on index page redirects to /text-display/
        :return:
        """
        input_text = 'This is a test'
        response = self.client.post('/', {'test_text_input': input_text})
        self.assertTrue('/text-display/' in response.url)

    def test_text_is_saved_on_post(self):
        """
        Tests that text is saved on valid POST request to index
        :return:
        """
        input_text = 'This is a test'
        response = self.client.post('/', {'test_text_input': input_text})
        pk = re.match(r'^/text-display/(?P<text_id>\d+)/', response.url).group('text_id')
        text = Text.objects.get(pk=pk)
        self.assertEqual(text.text, 'This is a test')


class TextDisplayTestCase(TestCase, AssertHTMLMixin):
    """
    Tests for text_display view
    """
    def setUp(self):
        self.text = 'Test text'
        self.pk = Text.objects.create(text=self.text).pk

    def test_text_display_shows_saved_text(self):
        """
        Tests that text is displayed by text_display on GET
        :return:
        """
        response = self.client.get('/text-display/' + str(self.pk) + '/')
        self.assertTemplateUsed(response, 'base/text_display.html')
        self.assertContains(response, self.text)
