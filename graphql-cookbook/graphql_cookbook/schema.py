import graphene
import graphql_cookbook.app_one.schema


class Query(graphql_cookbook.app_one.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
