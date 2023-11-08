import React, { useState, useEffect } from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import { getUserDetails, clearUserData } from './api'; // Replace with your actual API functions

const ProfileScreen = ({ navigation }) => {
  const [userDetails, setUserDetails] = useState(null);

  const fetchUserDetails = async () => {
    try {
      // Replace with your API function to fetch user details using the access token
      const response = await getUserDetails();
      setUserDetails(response.data); // Assuming your API returns user details in the 'data' field
    } catch (error) {
      console.error('Error fetching user details:', error);
    }
  };

  const handleLogout = () => {
    // Implement your logout logic here, including clearing user data and navigating to the login screen
    clearUserData(); // Replace with the function to clear user data
    navigation.navigate('Login');
  };

  useEffect(() => {
    fetchUserDetails();
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Profile Page</Text>
      {userDetails ? (
        <View>
          <Text>Name: {userDetails.name}</Text>
          <Text>Email: {userDetails.email}</Text>
          {/* Display other user details as needed */}
        </View>
      ) : (
        <Text>Loading user details...</Text>
      )}
      <Button title="Logout" onPress={handleLogout} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 16,
  },
});

export default ProfileScreen;