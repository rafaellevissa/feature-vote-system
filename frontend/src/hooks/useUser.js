import React, { createContext, useContext, useState, useEffect } from 'react';
import { userStorage } from '../services';

const UserContext = createContext();

export const UserProvider = ({ children }) => {
  const [userId, setUserId] = useState(null);
  const [userVotes, setUserVotes] = useState([]);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    initializeUser();
  }, []);
  
  const initializeUser = async () => {
    try {
      const id = await userStorage.getUserId();
      const votes = await userStorage.getUserVotes();
      setUserId(id);
      setUserVotes(votes);
    } catch (error) {
      console.error('Error initializing user:', error);
    } finally {
      setLoading(false);
    }
  };
  
  const addVote = async (featureId) => {
    const newVotes = [...userVotes, featureId];
    setUserVotes(newVotes);
    await userStorage.setUserVotes(newVotes);
  };
  
  const removeVote = async (featureId) => {
    const newVotes = userVotes.filter(id => id !== featureId);
    setUserVotes(newVotes);
    await userStorage.setUserVotes(newVotes);
  };
  
  const hasVoted = (featureId) => {
    return userVotes.includes(featureId);
  };
  
  const clearUserData = async () => {
    await userStorage.clearUserData();
    setUserId(null);
    setUserVotes([]);
  };
  
  const value = {
    userId,
    userVotes,
    loading,
    addVote,
    removeVote,
    hasVoted,
    clearUserData,
    initializeUser,
  };
  
  return (
    <UserContext.Provider value={value}>
      {children}
    </UserContext.Provider>
  );
};

export const useUser = () => {
  const context = useContext(UserContext);
  if (!context) {
    throw new Error('useUser must be used within a UserProvider');
  }
  return context;
};