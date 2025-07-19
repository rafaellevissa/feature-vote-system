import React from 'react';
import { FlatList, View, Text, StyleSheet, RefreshControl } from 'react-native';
import { colors, typography, spacing } from '../../styles';
import FeatureCard from './FeatureCard';
import LoadingSpinner from '../common/LoadingSpinner';

const FeatureList = ({
  features,
  loading,
  refreshing,
  onRefresh,
  hasVoted,
  onVote,
  onRemoveVote,
  onFeaturePress,
  ListHeaderComponent,
  ListFooterComponent,
}) => {
  const renderFeature = ({ item }) => (
    <FeatureCard
      feature={item}
      hasVoted={hasVoted(item.id)}
      onVote={onVote}
      onRemoveVote={onRemoveVote}
      onPress={() => onFeaturePress?.(item)}
    />
  );
  
  const renderEmptyState = () => (
    <View style={styles.emptyState}>
      <Text style={styles.emptyTitle}>No features yet!</Text>
      <Text style={styles.emptySubtitle}>
        Be the first to suggest a feature
      </Text>
    </View>
  );
  
  if (loading && !refreshing) {
    return <LoadingSpinner text="Loading features..." />;
  }
  
  return (
    <FlatList
      data={features}
      renderItem={renderFeature}
      keyExtractor={(item) => item.id.toString()}
      refreshControl={
        <RefreshControl
          refreshing={refreshing}
          onRefresh={onRefresh}
          colors={[colors.primary]}
          tintColor={colors.primary}
        />
      }
      ListEmptyComponent={renderEmptyState}
      ListHeaderComponent={ListHeaderComponent}
      ListFooterComponent={ListFooterComponent}
      showsVerticalScrollIndicator={false}
      contentContainerStyle={styles.contentContainer}
    />
  );
};

const styles = StyleSheet.create({
  contentContainer: {
    paddingVertical: spacing.sm,
    flexGrow: 1,
  },
  emptyState: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.xl,
  },
  emptyTitle: {
    fontSize: typography.fontSize.xl,
    fontWeight: typography.fontWeight.semibold,
    color: colors.textSecondary,
    marginBottom: spacing.sm,
  },
  emptySubtitle: {
    fontSize: typography.fontSize.base,
    color: colors.textTertiary,
    textAlign: 'center',
  },
});

export default FeatureList;