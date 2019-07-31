import graphene
from graphene_django.types import DjangoObjectType
from .models import UserProfile


class UserProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile


class Query(object):
    all_userprofile = graphene.List(UserProfileType)

    def resolve_all_userprofile(self, info, **kwargs):
        return UserProfile.objects.all()
