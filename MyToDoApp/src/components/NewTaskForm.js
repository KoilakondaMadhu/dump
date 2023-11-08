import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

const NewTaskForm = ({ onAddTask }) => {
  const [taskName, setTaskName] = useState('');

  const handleAddTask = () => {
    if (taskName) {
      onAddTask(taskName);
      setTaskName('');
    }
  };

  return (
    <View style={styles.container}>
      <Text>New Task</Text>
      <TextInput
        style={styles.input}
        placeholder="Task Name"
        value={taskName}
        onChangeText={(text) => setTaskName(text)}
      />
      <Button title="Add Task" onPress={handleAddTask} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 16,
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 10,
    paddingHorizontal: 10,
  },
});

export default NewTaskForm;