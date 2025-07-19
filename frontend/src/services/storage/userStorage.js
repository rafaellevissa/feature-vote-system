import AsyncStorage from '@react-native-async-storage/async-storage';
import { STORAGE_KEYS } from '../../utils/constants';
import { generateUserId } from '../../utils/helpers';

class UserStorageService {
  async getUserId() {
    try {
      let userId = await AsyncStorage.getItem(STORAGE_KEYS.USER_ID);
      if (!userId) {
        userId = generateUserId();
        await AsyncStorage.setItem(STORAGE_KEYS.USER_ID, userId);
      }
      return userId;
    } catch (error) {
      console.error('Error getting user ID:', error);
      return generateUserId(); // Fallback to memory-only ID
    }
  }
  
  async clearUserData() {
    try {
      await AsyncStorage.multiRemove([
        STORAGE_KEYS.USER_ID,
        STORAGE_KEYS.USER_VOTES,
      ]);
    } catch (error) {
      console.error('Error clearing user data:', error);
    }
  }
  
  async setUserVotes(votes) {
    try {
      await AsyncStorage.setItem(STORAGE_KEYS.USER_VOTES, JSON.stringify(votes));
    } catch (error) {
      console.error('Error saving user votes:', error);
    }
  }
  
  async getUserVotes() {
    try {
      const votes = await AsyncStorage.getItem(STORAGE_KEYS.USER_VOTES);
      return votes ? JSON.parse(votes) : [];
    } catch (error) {
      console.error('Error getting user votes:', error);
      return [];
    }
  }
}

export default new UserStorageService();