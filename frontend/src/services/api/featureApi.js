import apiClient from './apiClient';
import { endpoints } from './endpoints';

class FeatureApiService {
  async getFeatures() {
    try {
      return await apiClient.get(endpoints.features.list);
    } catch (error) {
      console.error('Error fetching features:', error);
      throw new Error('Failed to fetch features. Please try again.');
    }
  }
  
  async createFeature(featureData) {
    try {
      return await apiClient.post(endpoints.features.create, featureData);
    } catch (error) {
      console.error('Error creating feature:', error);
      throw new Error('Failed to create feature. Please try again.');
    }
  }
  
  async getFeature(id) {
    try {
      return await apiClient.get(endpoints.features.get(id));
    } catch (error) {
      console.error('Error fetching feature:', error);
      throw new Error('Failed to fetch feature. Please try again.');
    }
  }
  
  async deleteFeature(id) {
    try {
      return await apiClient.delete(endpoints.features.delete(id));
    } catch (error) {
      console.error('Error deleting feature:', error);
      throw new Error('Failed to delete feature. Please try again.');
    }
  }
  
  async upvoteFeature(id, userId) {
    try {
      return await apiClient.post(endpoints.features.upvote(id), { user_id: userId });
    } catch (error) {
      console.error('Error upvoting feature:', error);
      throw new Error('Failed to upvote feature. Please try again.');
    }
  }
  
  async removeVote(id, userId) {
    try {
      return await apiClient.delete(endpoints.features.removeVote(id), { user_id: userId });
    } catch (error) {
      console.error('Error removing vote:', error);
      throw new Error('Failed to remove vote. Please try again.');
    }
  }
  
  async getUserVotes(userId) {
    try {
      return await apiClient.get(endpoints.user.votes(userId));
    } catch (error) {
      console.error('Error fetching user votes:', error);
      throw new Error('Failed to fetch user votes. Please try again.');
    }
  }
  
  async checkHealth() {
    try {
      return await apiClient.get(endpoints.health);
    } catch (error) {
      console.error('Error checking API health:', error);
      throw new Error('API is not available. Please try again later.');
    }
  }
}

export default new FeatureApiService();