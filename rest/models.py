from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_fsm import FSMField, transition
from rest_framework.exceptions import PermissionDenied
from rest_framework.authtoken.models import Token
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance=None, created=False, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    manager = models.ForeignKey(User, related_name='subordinates', null=True)


class Project(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    notes = models.TextField()

    def __str__(self):
        return self.title


class Status(object):
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    WAITING = 'waiting'
    FINISHED = 'finished'


class Transition(object):
    APPROVE = 'approve'
    REJECT = 'reject'
    REQUEST = 'request'
    PROVIDE = 'provide'
    FINISH = 'finish'
    REOPEN = 'reopen'


class PersonRequest(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    notes = models.TextField()
    project = models.ForeignKey(Project, related_name="requests")
    requester = models.ForeignKey(User, related_name='requester_requests')
    requestee = models.ForeignKey(User, related_name='requestee_requests')
    status = FSMField(default=Status.PENDING)

    @transition(field=status, source=Status.PENDING, target=Status.APPROVED)
    def approve(self, by):
        pass

    @transition(field=status, source=Status.PENDING, target=Status.REJECTED)
    def reject(self, by):
        pass

    @transition(field=status, source=Status.PENDING, target=Status.WAITING)
    def request(self, by):
        pass

    @transition(field=status, source=Status.WAITING, target=Status.PENDING)
    def provide(self, by):
        pass

    @transition(field=status, source=(Status.APPROVED), target=Status.FINISHED)
    def finish(self, by):
        pass

    @transition(field=status, source=(Status.REJECTED, Status.FINISHED), target=Status.PENDING)
    def reopen(self, by):
        pass


    def can_transition(self, user, transition_method):
        transition_name = transition_method.__name__
        if transition_name == Transition.APPROVE or transition_name == Transition.REJECT or transition_name == Transition.REQUEST:
            return user == self.requestee.profile.manager

        if transition_name == Transition.PROVIDE or transition_name == Transition.REOPEN or transition_name == Transition.FINISH:
            return user == self.requester or user == self.requestee

        return False

    def possible_actions(self, user):
        return self.get_available_status_transitions()

    def allowed_actions(self, user):
        available_user_status_transitions = self.get_available_user_status_transitions(user)
        return (each for each in available_user_status_transitions if self.can_transition(user, each.method))



