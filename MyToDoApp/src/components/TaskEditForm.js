import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

const TaskEditForm = ({ task, onEditTask }) => {
  const [taskName, setTaskName] = useState(task.name);

  const handleEditTask = () => {
    if (taskName) {
      onEditTask(task.id, taskName);
    }
  };

  return (
    <View style={styles.container}>
      <Text>Edit Task</Text>
      <TextInput
        style={styles.input}
        value={taskName}
        onChangeText={(text) => setTaskName(text)}
      />
      <Button title="Save" onPress={handleEditTask} />
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

export default TaskEditForm;