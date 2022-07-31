import { NavigationContainer } from '@react-navigation/native';
import React, { useEffect } from 'react';
import { Text } from 'react-native';
import HomeScreen from './screens/Home';
import SearchScreen from './screens/Search';
import ArticleScreen from './screens/Article';
import SectionScreen from './screens/Section';
import FeedScreen from './screens/Feed';
import SettingsScreen from './screens/Settings';
import LoginScreen from './screens/Login';
import RegisterScreen from './assets/register';

import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

const Stack = createNativeStackNavigator();

const Tab = createBottomTabNavigator();

const TabNav = navigation => {
  return (
    <Tab.Navigator
      initialRouteName="Home"
      screenOptions={{ headerShown: false }}>
      <Tab.Screen name="Feed" component={FeedScreen} />
      <Tab.Screen name="Home" component={HomeScreen} />
      <Tab.Screen name="Settings" component={SettingsScreen} />
    </Tab.Navigator>
  );
};

const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator screenOptions={{ headerShown: false }}>
        <Stack.Screen name="HomeTab" component={TabNav} />
        <Stack.Screen
          name="Article"
          component={ArticleScreen}
          options={{ headerShown: true }}
        />
        <Stack.Screen name="Search" component={SearchScreen} />
        <Stack.Screen
          name="Section"
          component={SectionScreen}
          options={{ headerShown: true }}
        />
        <Stack.Screen
          name="Login"
          component={LoginScreen}
          options={{ headerShown: true }}
        />
        <Stack.Screen
          name="Register"
          component={RegisterScreen}
          options={{ headerShown: true }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;
