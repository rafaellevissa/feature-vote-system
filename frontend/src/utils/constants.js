import { Platform } from 'react-native';

// API Configuration
export const API_CONFIG = {
  BASE_URL: Platform.select({
    android: 'http://10.0.2.2:5000',
    ios: 'http://localhost:5000',
    web: 'http://localhost:5000',
    default: 'http://localhost:5000',
  }),
  TIMEOUT: 10000,
  RETRY_ATTEMPTS: 3,
};

// Storage Keys
export const STORAGE_KEYS = {
  USER_ID: 'user_id',
  USER_VOTES: 'user_votes',
};

// Screen Names
export const SCREENS = {
  HOME: 'Home',
  ADD_FEATURE: 'AddFeature',
};

// Feature Status
export const FEATURE_STATUS = {
  PENDING: 'pending',
  IN_PROGRESS: 'in_progress',
  COMPLETED: 'completed',
};