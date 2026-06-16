from task_manager.task import Task
import pytest
from datetime import datetime

def test_task_creation():
    #Arrange
    task = Task(title="Faire les courses")

    #Act

    #Assert
    assert task.title == "Faire les courses"
    assert task.id is not None
    assert task.done == False
    assert task.created_at is not None


def test_mark_as_done():
    #Arrange
    task = Task("Tondre l'herbe")

    #Act
    assert task.done == False
    task.mark_as_done()

    #Assert
    assert task.done == True

def test_to_dict():
    #Arrange
    task = Task(title="Nourir le chien")

    #Act
    save = task.to_dict()

    #Assert
    assert save["title"] == task.title
    assert save["id"] == task.id
    assert save["status"] == task.done
    assert save["date"] == task.created_at.isoformat()
