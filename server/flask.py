from flask import Flask, jsonify, request
from graphene import ObjectType, String, Field, List, Int, Boolean
from graphene import Boolean, InputObjectType, DateTime

app = Flask(__name__)

class TodoItem(ObjectType):
    title = String()
    description = String()
    time = DateTime()
    images = Boolean()

class Query(ObjectType):
    all_todos = List(TodoItem)

    def resolve_all_todos(root, info):
        # Implement logic to fetch all todos from database
        return []

class Mutation(ObjectType):
    add_todo = Field(TodoItem, title=String(), description=String(), time=DateTime(), images=Boolean())

    def resolve_add_todo(root, info, title, description, time, images):
        # Implement logic to add a new todo to the database
        # Return the newly created todo item
        return TodoItem(title=title, description=description, time=time, images=images)

# Create GraphQL endpoint
@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data)
    status_code = 200 if success else 400
    return jsonify(result.data), status_code

schema = Schema(query=Query, mutation=Mutation)

if __name__ == '__main__':
    app.run(debug=True)
