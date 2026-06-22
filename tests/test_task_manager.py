import pytest
from task_manager.task_manager import Task_manager
from task_manager.task import Task


def test_add_task():
    # Arrange
    title = "Faire à manger"
    tm = Task_manager()

    # Act
    newTask = tm.add_task(title)

    # Assert
    assert newTask.title == title
    assert newTask in tm.task_list


def test_delete_task():
    # Arrange
    title = "Faire la sieste"
    tm = Task_manager()
    newTask = tm.add_task(title)

    # Act
    tm.delete_task(newTask.id)

    # Assert
    assert newTask not in tm.task_list


def test_show_tasks():
    # Arrange
    title = "Laver les vitres"
    tm = Task_manager()
    newTask = tm.add_task(title)

    # Act
    result = tm.show_tasks()

    # Assert
    assert newTask in result


def test_search_by_id():
    # Arrange
    title = "Gonfler les pneus"
    tm = Task_manager()
    newTask = tm.add_task(title)

    # Act
    result = tm.search_by_id(newTask.id)

    # Assert
    assert newTask.id == result.id


def test_search_by_id_not_found():
    # Arrange
    title = "Ranger les livres"
    tm = Task_manager()
    newTask = tm.add_task(title)

    # Act
    result = tm.search_by_id("40")

    # Assert
    assert result is None
