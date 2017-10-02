from graphene_django import DjangoObjectType
import graphene

from schema.models import UserModel


class User(DjangoObjectType):
    class Meta:
        model = UserModel

class Query(graphene.ObjectType):
    user = graphene.Field(User,
                                id=graphene.Int(),
                                name=graphene.String(),
                                lastName=graphene.String())
    users = graphene.List(User)

    @graphene.resolve_only_args
    def resolve_users(self, **kwargs):
        return UserModel.objects.all()

    @graphene.resolve_only_args
    def resolve_user(self, **kargs):
        id = kargs.get('id')
        name = kargs.get('name')

        if id is not None:
            return UserModel.objects.get(pk=id)

        if name is not None:
            return UserModel.objects.get(name=name)

        return None



schema = graphene.Schema(query=Query)