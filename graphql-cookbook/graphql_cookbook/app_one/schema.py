import graphene
from graphene import relay, AbstractType, ObjectType, List
from graphene_django.types import DjangoObjectType
from .models import Message
from graphene_django.filter import DjangoFilterConnectionField


class MessageType(DjangoObjectType):
    class Meta:
        model = Message
        filter_fields = {'message': ['icontains']}   # If you need filtering.
        interfaces = (relay.Node, )      # if you need filter


class Query(ObjectType):
    # all_messages = graphene.List(MessageType)   # Normal Method
    message = relay.Node.Field(MessageType)
    all_messages = DjangoFilterConnectionField(MessageType)     # If you need filtering.

    # @graphene.resolve_only_args        # needed for normal method. not for fitler.
    # def resolve_all_messages(self):
    #     return Message.objects.all()


schema = graphene.Schema(query=Query)
