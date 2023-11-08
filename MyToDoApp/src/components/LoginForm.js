
import React, { useState } from 'react';
import { View, Text, TextInput, Button } from 'react-native';

const LoginForm = ({ onLogin, onRegister, isRegistering }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleAction = () => {
    if (isRegistering) {
      // Handle registration logic
      onRegister(email, password);
    } else {
      // Handle login logic
      onLogin(email, password);
    }
  };

  return (
    <View>
      <Text>{isRegistering ? 'Register' : 'Login'} Page</Text>
      <TextInput
        placeholder="Email"
        value={email}
        onChangeText={(text) => setEmail(text)}
      />
      <TextInput
        placeholder="Password"
        secureTextEntry
        value={password}
        onChangeText={(text) => setPassword(text)}
      />
      <Button title={isRegistering ? 'Register' : 'Login'} onPress={handleAction} />
      <Text onPress={() => onSwitchMode(!isRegistering)}>
        {isRegistering ? 'Switch to Login' : 'Switch to Register'}
      </Text>
    </View>
  );
};

export default LoginForm;