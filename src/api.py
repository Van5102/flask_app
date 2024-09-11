from flask import Blueprint, jsonify
from src.models import Project, Task
import subprocess

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

@api.route('/api/check_deadlines', methods=['GET'])
def run_task():
    # Khi nhận được tín hiệu từ GitHub, chạy script trên máy nội bộ
    subprocess.run(["D:/code/Back_end_test/flask_app/check_deadlines.py"])
    return 'Task started', 200

