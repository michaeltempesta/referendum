# backend/app/resources/PollResource.py


from flask_restful import Resource

class PollResource(Resource):
    def get(self, poll_id):
        return {'poll_id': poll_id, 'message': 'Hello from PollResource GET'}

    def post(self):
        return {'message': 'Hello from PollResource POST'}

    def put(self, poll_id):
        return {'poll_id': poll_id, 'message': 'Hello from PollResource PUT'}

    def delete(self, poll_id):
        return {'poll_id': poll_id, 'message': 'Hello from PollResource DELETE'}
