import unittest
import os
from task_manager import Task, TaskManager

class TestTask(unittest.TestCase):
    """Pruebas para la clase Task."""
    def test_mark_complete(self):
        """Verifica que el estado cambie a Completada."""
        task = Task(1, "Estudiar Python", "Completar lecciones", "Estudio")
        self.assertEqual(task.status, "Pendiente")
        task.mark_complete()
        self.assertEqual(task.status, "Completada")

class TestTaskManager(unittest.TestCase):
    """Pruebas para la clase TaskManager."""
    def setUp(self):
        self.filename = 'test_tasks.json'
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass
        self.manager = TaskManager(filename=self.filename)
        self.task1 = Task(1, "Tarea 1", "Desc 1", "Cat 1")
        self.task2 = Task(2, "Tarea 2", "Desc 2", "Cat 2")
        self.manager.add_task(self.task1)
        self.manager.add_task(self.task2)

    def tearDown(self):
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass

    def test_add_task(self):
        """Prueba la adición de tareas."""
        self.assertEqual(len(self.manager.tasks), 2)
        new_task = Task(3, "Tarea 3", "Desc 3", "Cat 3")
        self.manager.add_task(new_task)
        self.assertEqual(len(self.manager.tasks), 3)

    def test_edit_task(self):
        """Prueba la edición de una tarea."""
        self.manager.edit_task(2, new_title="Tarea editada")
        edited_task = next(t for t in self.manager.tasks if t.task_id == 2)
        self.assertEqual(edited_task.title, "Tarea editada")

    def test_delete_task(self):
        """Prueba la eliminación de una tarea."""
        self.manager.delete_task(1)
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertNotIn(1, [t.task_id for t in self.manager.tasks])

    def test_list_tasks(self):
        """Prueba el listado de tareas."""
        self.assertIn(self.task1, self.manager.tasks)
        self.assertIn(self.task2, self.manager.tasks)

if __name__ == "__main__":
    unittest.main()
