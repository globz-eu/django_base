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
from base.forms import TextForm

__author__ = 'Stefan Dieterle'


class NameFormTest(TestCase):
    def test_form_renders_seq_text_input_widget(self):
        """
        Tests correct rendering of form input text area
        :return:
        """
        form = TextForm()
        field = form['test_text_input']
        self.assertIn('<label for="id_test_text_input">Paste in your text:</label>', field.label_tag())
        self.assertIn('placeholder="Test Text"', form.as_p())
        self.assertIn('class="form-control"', form.as_p())

    def test_form_validation_for_blank_items(self):
        """
        Tests error on submission of empty form
        :return:
        """
        form = TextForm(data={'test_text_input': ''})
        # field = form['test_text_input']
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['test_text_input'][0],
            'Please submit a Test Text', format(form.errors['test_text_input'])
        )
