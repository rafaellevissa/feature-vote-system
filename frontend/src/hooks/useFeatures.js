import { useState, useEffect, useCallback } from 'react';
import { featureApi } from '../services';
import { useUser } from './useUser';

export const useFeatures = () => {
  const [features, setFeatures] = useState([]);
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [error, setError] = useState(null);
  const { userId, addVote, removeVote } = useUser();
  
  const fetchFeatures = useCallback(async () => {
    try {
      setError(null);
      const data = await featureApi.getFeatures();
      setFeatures(data);
    } catch (err) {
      setError(err.message);
      console.error('Error fetching features:', err);
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  }, []);
  
  useEffect(() => {
    fetchFeatures();
  }, [fetchFeatures]);
  
  const refresh = useCallback(async () => {
    setRefreshing(true);
    await fetchFeatures();
  }, [fetchFeatures]);
  
  const createFeature = async (featureData) => {
    try {
      const newFeature = await featureApi.createFeature(featureData);
      setFeatures(prev => [newFeature, ...prev]);
      return newFeature;
    } catch (err) {
      throw new Error(err.message);
    }
  };
  
  const upvoteFeature = async (featureId) => {
    try {
      const updatedFeature = await featureApi.upvoteFeature(featureId, userId);
      setFeatures(prev => 
        prev.map(feature => 
          feature.id === featureId ? updatedFeature : feature
        )
      );
      await addVote(featureId);
      return updatedFeature;
    } catch (err) {
      throw new Error(err.message);
    }
  };
  
  const removeVoteFromFeature = async (featureId) => {
    try {
      const updatedFeature = await featureApi.removeVote(featureId, userId);
      setFeatures(prev => 
        prev.map(feature => 
          feature.id === featureId ? updatedFeature : feature
        )
      );
      await removeVote(featureId);
      return updatedFeature;
    } catch (err) {
      throw new Error(err.message);
    }
  };
  
  const deleteFeature = async (featureId) => {
    try {
      await featureApi.deleteFeature(featureId);
      setFeatures(prev => prev.filter(feature => feature.id !== featureId));
    } catch (err) {
      throw new Error(err.message);
    }
  };
  
  return {
    features,
    loading,
    refreshing,
    error,
    refresh,
    createFeature,
    upvoteFeature,
    removeVoteFromFeature,
    deleteFeature,
  };
};