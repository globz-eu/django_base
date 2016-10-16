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

from behave import given, then
from lxml import html
from io import StringIO

__author__ = 'Stefan Dieterle'


@given(r'a user visits the URL "(?P<url>[^"]*)"')
def visit_url(context, url):
    context.home_url = context.base_url
    context.r = context.client.get(context.home_url + url)
    context.display = html.parse(StringIO(context.r.text)).getroot()


@then(r'the server\'s response status code is (?P<expected_code>\d+)')
def check_status_code(context, expected_code):
    assert context.r.status_code == int(expected_code), 'Got %d' % context.r.status_code


@then(r'the url is the home url')
def check_page_url(context):
    assert context.r.url == context.home_url + '/', 'Got %s' % context.r.url


@then(r'the page title is "(?P<expected_title>[^"]*)"')
def check_page_title(context, expected_title):
    title = context.display.cssselect('title')[0].text_content()
    assert expected_title == title, 'Got %s' % title
