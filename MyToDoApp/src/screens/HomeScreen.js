import React, { useState, useEffect } from 'react';
import { View, Text, Button, ScrollView, TouchableOpacity } from 'react-native';
import TaskList from './TaskList'; // Import the TaskList component

const HomeScreen = ({ navigation }) => {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    // Fetch tasks from your data source or AsyncStorage
    const fetchedTasks = [
      { id: 1, name: 'Task 1', status: 'TO DO' },
      { id: 2, name: 'Task 2', status: 'IN PROGRESS' },
      { id: 3, name: 'Task 3', status: 'COMPLETED' },
    ];

    setTasks(fetchedTasks);
  }, []);

  const handleTaskClick = (taskId) => {
    // Navigate to the task details screen with the taskId
    navigation.navigate('TaskDetails', { taskId });
  };

  return (
    <View style={{ flex: 1, padding: 16 }}>
      <Text style={{ fontSize: 24, fontWeight: 'bold', marginBottom: 16 }}>
        To-Do List
      </Text>

      {/* Add the TaskList component here */}
      <TaskList tasks={tasks} onTaskClick={handleTaskClick} />

      <Button
        title="Add Task"
        onPress={() => navigation.navigate('TaskCreation')}
      />
    </View>
  );
};

export default HomeScreen;