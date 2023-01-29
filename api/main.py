import strawberry

from api.schema import Query

schema = strawberry.Schema(query=Query)

# Run to start the server
# strawberry server api.main