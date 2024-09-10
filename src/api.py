from flask import Blueprint, jsonify
from src.models import Project, Task

api = Blueprint('api', __name__)


@api.route('/api/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    project_data = []
    for project in projects:
        tasks = Task.query.filter_by(project_id=project.id).all()
        task_count = len(tasks)
        project_data.append({
            'code': project.code,
            'task_count': task_count,
            'progress': project.progress,
            'time_start': project.time_start,
        })
    return jsonify(project_data)

