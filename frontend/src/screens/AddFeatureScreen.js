import React, { useState } from 'react';
import { View, StyleSheet, Alert, KeyboardAvoidingView, Platform, ScrollView } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { globalStyles, spacing } from '../styles';
import { Input, Button } from '../components';
import { useFeatures } from '../hooks/useFeatures';
import { validateFeature } from '../utils/validation';
import Header from '../components/common/Header';

const AddFeatureScreen = ({ navigation }) => {
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    author: '',
  });
  const [errors, setErrors] = useState({});
  const [loading, setLoading] = useState(false);
  
  const { createFeature } = useFeatures();
  
  const updateField = (field, value) => {
    setFormData(prev => ({ ...prev, [field]: value }));
    // Clear error when user starts typing
    if (errors[field]) {
      setErrors(prev => ({ ...prev, [field]: null }));
    }
  };
  
  const handleSubmit = async () => {
    const validation = validateFeature(formData);
    
    if (!validation.isValid) {
      setErrors(validation.errors);
      return;
    }
    
    setLoading(true);
    
    try {
      await createFeature(formData);
      Alert.alert(
        'Success',
        'Feature suggestion submitted successfully!',
        [
          {
            text: 'OK',
            onPress: () => navigation.goBack(),
          },
        ]
      );
    } catch (error) {
      Alert.alert('Error', error.message);
    } finally {
      setLoading(false);
    }
  };
  
  const handleCancel = () => {
    navigation.goBack();
  };
  
  return (
    <SafeAreaView style={globalStyles.container}>
      <Header 
        title="Suggest Feature"
        leftComponent={
          <Button
            title="Cancel"
            variant="outline"
            size="small"
            onPress={handleCancel}
          />
        }
      />
      
      <KeyboardAvoidingView
        style={styles.keyboardView}
        behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
      >
        <ScrollView style={styles.scrollView} showsVerticalScrollIndicator={false}>
          <View style={styles.form}>
            <Input
              label="Feature Title"
              value={formData.title}
              onChangeText={(value) => updateField('title', value)}
              placeholder="What feature would you like to see?"
              error={errors.title}
              maxLength={200}
            />
            
            <Input
              label="Description (Optional)"
              value={formData.description}
              onChangeText={(value) => updateField('description', value)}
              placeholder="Describe the feature in more detail..."
              multiline={true}
              numberOfLines={4}
              error={errors.description}
              maxLength={1000}
            />
            
            <Input
              label="Your Name"
              value={formData.author}
              onChangeText={(value) => updateField('author', value)}
              placeholder="Enter your name"
              error={errors.author}
              maxLength={100}
            />
            
            <View style={styles.buttonContainer}>
              <Button
                title="Submit Feature"
                onPress={handleSubmit}
                loading={loading}
                disabled={loading}
                style={styles.submitButton}
              />
            </View>
          </View>
        </ScrollView>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  keyboardView: {
    flex: 1,
  },
  scrollView: {
    flex: 1,
  },
  form: {
    padding: spacing.lg,
  },
  buttonContainer: {
    marginTop: spacing.lg,
  },
  submitButton: {
    width: '100%',
  },
});

export default AddFeatureScreen;