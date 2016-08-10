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
from django.core.urlresolvers import resolve

from base.views import index, text_display

__author__ = 'Stefan Dieterle'


class BaseURLsTestCase(TestCase):

    def test_root_url_uses_index_view(self):
        """
        Tests that the root of the site resolves to the correct view function
        :return:
        """
        root = resolve('/')
        self.assertEqual(root.func, index)

    def test_text_url_uses_seq_display_view(self):
        """
        Test that the /text-display/ URL resolves to the correct view function
        :return:
        """
        text_view = resolve('/text-display/1')
        self.assertEqual(text_view.func, text_display)
