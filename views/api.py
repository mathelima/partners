from flask import Flask
from flask_restful import Api
from src.resources.partner_resource import PartnerResource

app = Flask(__name__)
api = Api(app)

api.add_resource(PartnerResource, '/api/partner', endpoint='partners')
api.add_resource(PartnerResource, '/api/partner/<int:id>', endpoint='partner')


@app.route('/')
def index():
    return "Welcome"


app.run(debug=True)