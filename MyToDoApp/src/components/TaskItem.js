import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';

const TaskItem = ({ task, onEdit, onDelete, onComplete }) => {
  return (
    <View style={styles.container}>
      <Text>{task.name}</Text>
      {task.isCompleted ? <Text>Completed</Text> : null}
      <Button title="Edit" onPress={onEdit} />
      <Button title="Delete" onPress={onDelete} />
      <Button title="Complete" onPress={onComplete} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    borderWidth: 1,
    borderColor: '#ddd',
    padding: 10,
    marginBottom: 10,
  },
});

export default TaskItem;