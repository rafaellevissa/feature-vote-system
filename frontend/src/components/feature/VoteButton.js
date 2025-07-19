import { TouchableOpacity, Text, StyleSheet } from 'react-native';
import { colors, typography, spacing, borderRadius } from '../../styles';

const VoteButton = ({ 
  upvotes, 
  hasVoted, 
  onPress, 
  disabled = false,
  size = 'medium' 
}) => {
  const buttonStyle = [
    styles.button,
    styles[size],
    hasVoted && styles.buttonActive,
    disabled && styles.buttonDisabled,
  ];
  
  const textStyle = [
    styles.text,
    styles[`${size}Text`],
    hasVoted && styles.textActive,
    disabled && styles.textDisabled,
  ];
  
  return (
    <TouchableOpacity
      style={buttonStyle}
      onPress={onPress}
      disabled={disabled}
      activeOpacity={0.7}
    >
      <Text style={textStyle}>
        ↑ {upvotes}
      </Text>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  button: {
    backgroundColor: colors.gray100,
    borderWidth: 1,
    borderColor: colors.border,
    borderRadius: borderRadius.lg,
    alignItems: 'center',
    justifyContent: 'center',
  },
  
  // Sizes
  small: {
    paddingHorizontal: spacing.sm,
    paddingVertical: spacing.xs,
    minWidth: 50,
  },
  medium: {
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.sm,
    minWidth: 60,
  },
  large: {
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.md,
    minWidth: 70,
  },
  
  // States
  buttonActive: {
    backgroundColor: colors.primary,
    borderColor: colors.primary,
  },
  buttonDisabled: {
    opacity: 0.6,
  },
  
  // Text styles
  text: {
    fontWeight: typography.fontWeight.semibold,
    color: colors.textSecondary,
  },
  smallText: {
    fontSize: typography.fontSize.xs,
  },
  mediumText: {
    fontSize: typography.fontSize.sm,
  },
  largeText: {
    fontSize: typography.fontSize.base,
  },
  textActive: {
    color: colors.white,
  },
  textDisabled: {
    opacity: 0.6,
  },
});

export default VoteButton;