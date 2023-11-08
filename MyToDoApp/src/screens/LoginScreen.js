import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

const LoginScreen = ({ navigation }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isRegistering, setIsRegistering] = useState(false);

  const handleLogin = () => {
    // Implement the logic to handle login here
    // You can send the email and password to your authentication API
  };

  const handleSwitchMode = () => {
    setIsRegistering(!isRegistering);
  };

  return (
    <View style={styles.container}>
      <View style={styles.formContainer}>
        <Text style={styles.title}>{isRegistering ? 'Register' : 'Login'} Page</Text>
        <TextInput
          style={styles.input}
          placeholder="Email"
          value={email}
          onChangeText={(text) => setEmail(text)}
        />
        <TextInput
          style={styles.input}
          placeholder="Password"
          secureTextEntry
          value={password}
          onChangeText={(text) => setPassword(text)}
        />
        <Button title={isRegistering ? 'Register' : 'Login'} onPress={handleLogin} />
        <Text style={styles.switchText} onPress={handleSwitchMode}>
          {isRegistering ? 'Switch to Login' : 'Switch to Register'}
        </Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'gray',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
  },
  formContainer: {
    backgroundColor: 'white',
    padding: 16,
    borderRadius: 8,
    width: '100%',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 16,
  },
  input: {
    width: '100%',
    height: 40,
    borderColor: 'black',
    borderWidth: 1,
    borderRadius: 8,
    marginBottom: 12,
    paddingHorizontal: 12,
  },
  switchText: {
    textAlign: 'center',
    marginTop: 8,
    color: 'blue', // You can customize the color
    textDecorationLine: 'underline',
  },
});

export default LoginScreen;