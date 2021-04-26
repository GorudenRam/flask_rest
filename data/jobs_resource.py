from flask_restful import reqparse, abort, Resource
from flask import jsonify
from .jobs import Job
from . import db_session


def abort_if_job_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Job).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")


def abort_if_job_found(job_id):
    session = db_session.create_session()
    job = session.query(Job).get(job_id)
    if job:
        abort(404, message=f"Job {job_id} already exists")


parser = reqparse.RequestParser()
parser.add_argument('id', required=True, type=int)
parser.add_argument('team_leader', required=True, type=int)
parser.add_argument('job', required=True)
parser.add_argument('work_size', required=True, type=int)
parser.add_argument('collaborators', required=True)
parser.add_argument('is_finished', required=True, type=bool)


class JobResource(Resource):
    def get(self, job_id):
        abort_if_job_not_found(job_id)
        db_sess = db_session.create_session()
        job = db_sess.query(Job).get(job_id)
        return jsonify(
            {
                'job': job.to_dict(only=('id', 'team_leader', 'job', 'collaborators', 'is_finished', 'work_size'))
            }
        )

    def put(self, job_id):
        abort_if_job_not_found(job_id)
        args = parser.parse_args()
        session = db_session.create_session()
        job = session.query(Job).filter(Job.id == job_id).first()
        job.id = args['id']
        job.team_leader = args['team_leader']
        job.job = args['job']
        job.work_size = args['work_size']
        job.collaborators = args['collaborators']
        job.is_finished = args['is_finished']
        session.commit()
        return jsonify({'success': 'OK'})

    def delete(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Job).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})


class JobListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Job).all()
        return jsonify({'jobs': [item.to_dict(
            only=('id', 'team_leader', 'job', 'collaborators', 'is_finished', 'work_size')) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        abort_if_job_found(args['id'])
        job = Job(
            id=args['id'],
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            is_finished=args['is_finished']
        )
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})