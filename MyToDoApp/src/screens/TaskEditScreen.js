import React from 'react';
import TaskEditForm from './TaskEditForm';

const TaskEditScreen = ({ route, navigation, onEditTask }) => {
  const { taskId } = route.params;
  const task = {
    id: taskId, // Replace with actual task ID retrieval
    name: 'Sample Task', // Replace with actual task name retrieval
  };

  return (
    <TaskEditForm
      task={task}
      onEditTask={(taskId, taskName) => onEditTask(taskId, taskName)}
    />
  );
};

export default TaskEditScreen;