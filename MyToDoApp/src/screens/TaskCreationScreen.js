import React, { useState } from 'react';
import LoginForm from './src/components/LoginForm';


const TaskCreationScreen = ({ navigation, onAddTask }) => {
  return (
    <NewTaskForm onAddTask={(taskName) => onAddTask(taskName)} />
  );
};

export default TaskCreationScreen;