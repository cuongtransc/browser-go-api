from flask import Blueprint, request, jsonify, session
from models.User import User, user_schema, users_schema
from models.GameRoom import GameRoom, rooms_schema, room_schema
from models.Game import Game, game_schema
from database import db
from ..decorators import jwt_required
import jwt
import os
import json
from websockets.socket import new_game_notice, join_game_notice

api_games = Blueprint('api_games', __name__, url_prefix='/api/games')

@api_games.route('/<game_id>', methods=['GET'])
def get_room(game_id):
    print(game_id)
    game = Game.query.filter_by(id=game_id).first()
    response = game_schema.dumps(game)
    # TODO create decorator that returns user from header
    auth_header = request.headers.get('Authorization')
    user = jwt.decode(auth_header.split(" ")[1], os.environ.get('SECRET_KEY'))['user']
    print(user)
    join_game_notice(game_id, user)
    return jsonify(response)

@api_games.route('/', methods=['POST'])
@jwt_required()
def post_game():
    data = request.get_json()
    # TODO create decorator that returns user from header
    auth_header = request.headers.get('Authorization')
    user = jwt.decode(auth_header.split(" ")[1], os.environ.get('SECRET_KEY'))['user']
    user_id = json.loads(user)['id']
    try:
        game = Game(
            name = data['name'],
            description = data['description'],
            board_size = data['boardSize'],
            game_room = data['gameRoom'],
            player_white = user_id
        )
        db.session.add(game)
        db.session.commit()
        new_game_notice(room=game.game_room, game=game_schema.dumps(game))
        response = {
            'status': 'success',
            'message': 'Game created',
            'game': game.id
            }
        return jsonify(response), 201
    except Exception as e:
        print('error')
        print(e)
        print(e.__dict__)
        response = {
            'status': 'fail',
            'message': 'There was an error. Please try again.'
        }
        return jsonify(response), 401
