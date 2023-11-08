import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import LoginScreen from '../screens/LoginScreen'; // Import your login screen
import HomeScreen from '../screens/HomeScreen'; // Import your home screen
import ProfileScreen from '../screens/ProfileScreen'; // Import your profile screen
import TaskCreationScreen from '../screens/TaskCreationScreen'; // Import your task creation screen
import TaskEditScreen from '../screens/TaskEditScreen'; // Import your task edit screen

const Stack = createStackNavigator();

const AppNavigator = () => {
  return (
    <Stack.Navigator initialRouteName="Login">
      <Stack.Screen name="Login" component={LoginScreen} /> /* Use "component" instead of "screens" */
      <Stack.Screen name="Home" component={HomeScreen} />
      <Stack.Screen name="Profile" component={ProfileScreen} />
      <Stack.Screen name="TaskCreation" component={TaskCreationScreen} />
      <Stack.Screen name="TaskEdit" component={TaskEditScreen} />
    </Stack.Navigator>
  );
};

export default AppNavigator;