import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { colors, typography, spacing, borderRadius } from '../../styles';
import { formatDate } from '../../utils/helpers';
import VoteButton from './VoteButton';

const FeatureCard = ({ 
  feature, 
  hasVoted, 
  onVote, 
  onRemoveVote, 
  onPress,
  disabled = false 
}) => {
  const handleVotePress = () => {
    if (hasVoted) {
      onRemoveVote(feature.id);
    } else {
      onVote(feature.id);
    }
  };
  
  return (
    <TouchableOpacity 
      style={styles.container} 
      onPress={onPress}
      activeOpacity={0.95}
      disabled={!onPress}
    >
      <View style={styles.header}>
        <View style={styles.titleContainer}>
          <Text style={styles.title} numberOfLines={2}>
            {feature.title}
          </Text>
        </View>
        <VoteButton
          upvotes={feature.upvotes}
          hasVoted={hasVoted}
          onPress={handleVotePress}
          disabled={disabled}
          size="medium"
        />
      </View>
      
      {feature.description && (
        <Text style={styles.description} numberOfLines={3}>
          {feature.description}
        </Text>
      )}
      
      <View style={styles.footer}>
        <Text style={styles.author}>by {feature.author}</Text>
        <Text style={styles.date}>
          {formatDate(feature.created_at)}
        </Text>
      </View>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: colors.white,
    marginHorizontal: spacing.md,
    marginVertical: spacing.sm,
    padding: spacing.md,
    borderRadius: borderRadius.lg,
    shadowColor: colors.black,
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.1,
    shadowRadius: 3.84,
    elevation: 5,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    marginBottom: spacing.sm,
  },
  titleContainer: {
    flex: 1,
    marginRight: spacing.md,
  },
  title: {
    fontSize: typography.fontSize.lg,
    fontWeight: typography.fontWeight.semibold,
    color: colors.textPrimary,
    lineHeight: typography.lineHeight.tight * typography.fontSize.lg,
  },
  description: {
    fontSize: typography.fontSize.base,
    color: colors.textSecondary,
    lineHeight: typography.lineHeight.normal * typography.fontSize.base,
    marginBottom: spacing.md,
  },
  footer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  author: {
    fontSize: typography.fontSize.sm,
    color: colors.textTertiary,
    fontStyle: 'italic',
  },
  date: {
    fontSize: typography.fontSize.sm,
    color: colors.textTertiary,
  },
});

export default FeatureCard;