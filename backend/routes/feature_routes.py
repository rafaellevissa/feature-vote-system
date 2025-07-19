from flask import Blueprint, request, jsonify
from services.feature_service import FeatureService
from services.vote_service import VoteService
from schemas.feature_schemas import CreateFeatureRequest, VoteRequest

feature_bp = Blueprint('features', __name__)
feature_service = FeatureService()
vote_service = VoteService()

@feature_bp.route('/features', methods=['GET'])
def get_features():
    """Get all features"""
    try:
        features = feature_service.get_all_features()
        return jsonify(features), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@feature_bp.route('/features', methods=['POST'])
def create_feature():
    """Create a new feature"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        request_obj = CreateFeatureRequest.from_dict(data)
        request_obj.validate()
        
        feature = feature_service.create_feature(
            title=request_obj.title,
            author=request_obj.author,
            description=request_obj.description
        )
        
        return jsonify(feature), 201
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@feature_bp.route('/features/<int:feature_id>', methods=['GET'])
def get_feature(feature_id):
    """Get a specific feature"""
    try:
        feature = feature_service.get_feature_by_id(feature_id)
        if not feature:
            return jsonify({'error': 'Feature not found'}), 404
        
        return jsonify(feature), 200
    
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@feature_bp.route('/features/<int:feature_id>', methods=['DELETE'])
def delete_feature(feature_id):
    """Delete a feature"""
    try:
        success = feature_service.delete_feature(feature_id)
        if not success:
            return jsonify({'error': 'Feature not found'}), 404
        
        return jsonify({'message': 'Feature deleted successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@feature_bp.route('/features/<int:feature_id>/upvote', methods=['POST'])
def upvote_feature(feature_id):
    """Upvote a feature"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        vote_request = VoteRequest.from_dict(data)
        vote_request.validate()
        
        feature = vote_service.upvote_feature(feature_id, vote_request.user_id)
        return jsonify(feature), 200
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@feature_bp.route('/features/<int:feature_id>/remove-vote', methods=['DELETE'])
def remove_vote(feature_id):
    """Remove vote from a feature"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        vote_request = VoteRequest.from_dict(data)
        vote_request.validate()
        
        feature = vote_service.remove_vote(feature_id, vote_request.user_id)
        return jsonify(feature), 200
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@feature_bp.route('/user/<user_id>/votes', methods=['GET'])
def get_user_votes(user_id):
    """Get user's votes"""
    try:
        votes = vote_service.get_user_votes(user_id)
        return jsonify(votes), 200
    
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500