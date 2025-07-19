import { View, StyleSheet, Alert } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { globalStyles } from '../styles';
import { FeatureList, LoadingSpinner } from '../components';
import { useFeatures } from '../hooks/useFeatures';
import { useUser } from '../hooks/useUser';
import Header from '../components/common/Header';

const HomeScreen = ({ navigation }) => {
  const { features, loading, refreshing, error, refresh, upvoteFeature, removeVoteFromFeature } = useFeatures();
  const { hasVoted, loading: userLoading } = useUser();
  
  const handleVote = async (featureId) => {
    try {
      await upvoteFeature(featureId);
    } catch (error) {
      Alert.alert('Error', error.message);
    }
  };
  
  const handleRemoveVote = async (featureId) => {
    try {
      await removeVoteFromFeature(featureId);
    } catch (error) {
      Alert.alert('Error', error.message);
    }
  };
  
  const handleFeaturePress = (feature) => {
    // Navigate to feature detail screen if implemented
    console.log('Feature pressed:', feature.title);
  };
  
  const navigateToAddFeature = () => {
    navigation.navigate('AddFeature');
  };
  
  if (userLoading) {
    return <LoadingSpinner text="Initializing..." />;
  }
  
  return (
    <SafeAreaView style={globalStyles.container}>
      <Header 
        title="Feature Voting" 
        showAddButton={true}
        onAddPress={navigateToAddFeature}
      />
      <FeatureList
        features={features}
        loading={loading}
        refreshing={refreshing}
        onRefresh={refresh}
        hasVoted={hasVoted}
        onVote={handleVote}
        onRemoveVote={handleRemoveVote}
        onFeaturePress={handleFeaturePress}
      />
    </SafeAreaView>
  );
};

export default HomeScreen;