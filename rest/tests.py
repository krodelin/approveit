from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from rest_framework.exceptions import PermissionDenied
from rest.models import PersonRequest, Project


class UserTestCase(TestCase):
    def test_profile(self):
        user = User.objects.create(username="User")
        self.assertIsNotNone(user.profile)
        self.assertIsNone(user.profile.manager)


class PersonRequestTestCase(TestCase):
    def setUp(self):
        self.manager = User.objects.create(username='Manager')
        self.sales_rep = User.objects.create(username='Sales Rep')
        self.sales_engineer = User.objects.create(username='SE')

        self.sales_engineer.profile.manager = self.manager
        self.sales_engineer.save()

        self.project = Project.objects.create(title='Project')
        self.request = PersonRequest.objects.create(title='Request', project=self.project, requester=self.sales_rep,
                                                    requestee=self.sales_engineer)

    def test_manager_approve_permission(self):
        self.request.approve(self.manager)

    def test_requester_approve_permission(self):
        self.assertRaises(PermissionDenied, self.request.approve, self.sales_rep)

    def test_requestee_approve_permission(self):
        self.assertRaises(PermissionDenied, self.request.approve, self.sales_engineer)

    def test_manager_reject_permission(self):
        self.request.reject(self.manager)

    def test_requester_reject_permission(self):
        self.assertRaises(PermissionDenied, self.request.reject, self.sales_rep)

    def test_requestee_reject_permission(self):
        self.assertRaises(PermissionDenied, self.request.reject, self.sales_engineer)

    def test_manager_request_permission(self):
        self.request.request(self.manager)

    def test_requester_request_permission(self):
        self.assertRaises(PermissionDenied, self.request.request, self.sales_rep)

    def test_requestee_request_permission(self):
        self.assertRaises(PermissionDenied, self.request.request, self.sales_engineer)

    def test_manager_provide_permission(self):
        self.request.request(self.manager)
        self.assertRaises(PermissionDenied, self.request.provide, self.manager)

    def test_requester_request_permission(self):
        self.request.request(self.manager)
        self.request.provide(self.sales_rep)

    def test_requestee_request_permission(self):
        self.request.request(self.manager)
        self.request.provide(self.sales_engineer)

    def test_manager_finish_permission(self):
        self.request.approve(self.manager)
        self.assertRaises(PermissionDenied, self.request.finish, self.manager)

    def test_requester_request_permission(self):
        self.request.approve(self.manager)
        self.request.finish(self.sales_rep)

    def test_requestee_request_permission(self):
        self.request.approve(self.manager)
        self.request.finish(self.sales_engineer)

    def test_manager_reopen_permission(self):
        self.request.approve(self.manager)
        self.request.finish(self.sales_engineer)
        self.assertRaises(PermissionDenied, self.request.reopen, self.manager)

    def test_requester_request_permission(self):
        self.request.approve(self.manager)
        self.request.finish(self.sales_engineer)
        self.request.reopen(self.sales_rep)


    def test_requestee_request_permission(self):
        self.request.approve(self.manager)
        self.request.finish(self.sales_engineer)
        self.request.reopen(self.sales_engineer)
        
