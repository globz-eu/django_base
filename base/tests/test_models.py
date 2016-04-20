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
from base.models import Text

__author__ = 'Stefan Dieterle'


class TextModelTestCase(TestCase):
    """
    Tests Alignment model
    """

    def setUp(self):
        self.text = 'This is a test text'

    def test_alignment_basic(self):
        """
        Tests the basic functionality of Text
        :return:
        """
        text = Text.objects.create(text=self.text)
        self.assertEqual(text.text, 'This is a test text')

    def test_save_alignment_to_db(self):
        """
        Tests saving a text in Text model
        :return:
        """
        save = Text.objects.create(text=self.text)
        text = Text.objects.all()
        self.assertEqual(text[0].text, 'This is a test text', text[0].text)
        self.assertEqual(save.id, text[0].pk, save.id)

    def test_save_and_get_sanity_check(self):
        text_pk = Text.objects.create(text=self.text).id
        text = Text.objects.get(pk=text_pk)
        self.assertEqual(text.text, self.text)
