import graphene
import Users.schema


class Query(Users.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
