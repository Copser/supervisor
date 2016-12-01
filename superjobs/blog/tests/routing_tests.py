import pytest

from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from django.shortcuts import render_to_response

from blog.views import jobs

class JobsPageTest(TestCase):
    """TODO: testing blog/ routing, we want to see if are pages are
    wired correctly
    return: TODO
    """
    def test_jobs_resolvers_to_jobs_view(self):
        """TODO: should return jobs page
        return: TODO
        """
        jobs_page = resolve('/blog/jobs')
        assert jobs_page.func, jobs
