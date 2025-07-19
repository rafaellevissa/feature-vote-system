import { createStackNavigator } from '@react-navigation/stack';
import { SCREENS } from '../utils/constants';
import HomeScreen from '../screens/HomeScreen';
import AddFeatureScreen from '../screens/AddFeatureScreen';

const Stack = createStackNavigator();

const AppNavigator = () => {
  return (
    <Stack.Navigator
      initialRouteName={SCREENS.HOME}
      screenOptions={{
        headerShown: false,
      }}
    >
      <Stack.Screen name={SCREENS.HOME} component={HomeScreen} />
      <Stack.Screen 
        name={SCREENS.ADD_FEATURE} 
        component={AddFeatureScreen}
        options={{
          presentation: 'modal',
        }}
      />
    </Stack.Navigator>
  );
};

export default AppNavigator;