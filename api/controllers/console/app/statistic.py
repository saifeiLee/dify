# -*- coding:utf-8 -*-
from datetime import datetime
import pytz
from flask import jsonify
from models.model import Message
from sqlalchemy import func
from flask_login import login_required, current_user
from flask_restful import Resource, reqparse
from controllers.console import api
from controllers.console.app import _get_app
from controllers.console.setup import setup_required
from controllers.console.wraps import account_initialization_required
from libs.helper import datetime_string
from extensions.ext_database import db


class DailyConversationStatistic(Resource):

    @setup_required
    @login_required
    @account_initialization_required
    def get(self, app_id):
        account = current_user
        app_id = str(app_id)
        app_model = _get_app(app_id)

        parser = reqparse.RequestParser()
        parser.add_argument('start', type=datetime_string('%Y-%m-%d %H:%M'), location='args')
        parser.add_argument('end', type=datetime_string('%Y-%m-%d %H:%M'), location='args')
        args = parser.parse_args()

        # sql_query = '''
        # SELECT date(DATE_TRUNC('day', created_at AT TIME ZONE 'UTC' AT TIME ZONE :tz )) AS date, count(distinct messages.conversation_id) AS conversation_count
        #     FROM messages where app_id = :app_id
        # '''
        # arg_dict = {'tz': account.timezone, 'app_id': app_model.id}
        #
        # timezone = pytz.timezone(account.timezone)
        utc_timezone = pytz.utc

        # CVTE SQLAlchemy兼容性调整
        query = db.session.query(
            func.date(func.DATE_TRUNC('day', func.timezone(account.timezone, Message.created_at))).label('date'),
            func.count(func.distinct(Message.conversation_id)).label('conversation_count')
        ).filter(
            Message.app_id == app_model.id
        )

        if args['start']:
            start_datetime = datetime.strptime(args['start'], '%Y-%m-%d %H:%M')
            start_datetime = start_datetime.replace(second=0)

            # start_datetime_timezone = timezone.localize(start_datetime)
            # start_datetime_utc = start_datetime_timezone.astimezone(utc_timezone)

            start_datetime_utc = utc_timezone.localize(start_datetime)
            start_datetime_timezone = start_datetime_utc.astimezone(pytz.timezone(account.timezone))

            # sql_query += ' and created_at >= :start'
            # arg_dict['start'] = start_datetime_utc
            # CVTE SQLAlchemy兼容性调整
            query = query.filter(Message.created_at >= start_datetime_timezone)

        if args['end']:
            end_datetime = datetime.strptime(args['end'], '%Y-%m-%d %H:%M')
            end_datetime = end_datetime.replace(second=0)

            # end_datetime_timezone = timezone.localize(end_datetime)
            # end_datetime_utc = end_datetime_timezone.astimezone(utc_timezone)
            end_datetime_utc = utc_timezone.localize(end_datetime)
            end_datetime_timezone = end_datetime_utc.astimezone(pytz.timezone(account.timezone))

            # sql_query += ' and created_at < :end'
            # arg_dict['end'] = end_datetime_utc
            # CVTE SQLAlchemy兼容性调整
            query = query.filter(Message.created_at < end_datetime_timezone)

        # sql_query += ' GROUP BY date order by date'
        # rs = db.session.execute(sql_query, arg_dict)
        query = query.group_by(func.date(func.DATE_TRUNC('day', func.timezone(account.timezone, Message.created_at))))
        query = query.order_by(func.date(func.DATE_TRUNC('day', func.timezone(account.timezone, Message.created_at))))
        results = query.all()

        response_data = []

        # CVTE SQLAlchemy兼容性调整
        if len(results) > 0:
            for result in results:
                response_data.append({
                    'date': str(result.date),
                    'conversation_count': result.conversation_count
                })

        return jsonify({
            'data': response_data
        })

        # for i in rs:
        #     response_date.append({
        #         'date': str(i.date),
        #         'conversation_count': i.conversation_count
        #     })
        #
        # return jsonify({
        #     'data': response_date
        # })


class DailyTerminalsStatistic(Resource):

    @setup_required
    @login_required
    @account_initialization_required
    def get(self, app_id):
        account = current_user
        app_id = str(app_id)
        app_model = _get_app(app_id)

        parser = reqparse.RequestParser()
        parser.add_argument('start', type=datetime_string('%Y-%m-%d %H:%M'), location='args')
        parser.add_argument('end', type=datetime_string('%Y-%m-%d %H:%M'), location='args')
        args = parser.parse_args()

        # sql_query = '''
        #         SELECT date(DATE_TRUNC('day', created_at AT TIME ZONE 'UTC' AT TIME ZONE :tz )) AS date, count(distinct messages.from_end_user_id) AS terminal_count
        #             FROM messages where app_id = :app_id
        #         '''
        # arg_dict = {'tz': account.timezone, 'app_id': app_model.id}
        #
        # timezone = pytz.timezone(account.timezone)
        utc_timezone = pytz.utc

        # CVTE SQLAlchemy兼容性调整
        query = db.session.query(
            func.date(func.DATE_TRUNC('day', func.timezone(account.timezone, Message.created_at))).label('date'),
            func.count(func.distinct(Message.from_end_user_id)).label('terminal_count')
        ).filter(
            Message.app_id == app_model.id
        )

        if args['start']:
            start_datetime = datetime.strptime(args['start'], '%Y-%m-%d %H:%M')
            start_datetime = start_datetime.replace(second=0)

            # start_datetime_timezone = timezone.localize(start_datetime)
            # start_datetime_utc = start_datetime_timezone.astimezone(utc_timezone)

            start_datetime_utc = utc_timezone.localize(start_datetime)
            start_datetime_timezone = start_datetime_utc.astimezone(pytz.timezone(account.timezone))

            # sql_query += ' and created_at >= :start'
            # arg_dict['start'] = start_datetime_utc
            # CVTE SQLAlchemy兼容性调整
            query = query.filter(Message.created_at >= start_datetime_timezone)

        if args['end']:
            end_datetime = datetime.strptime(args['end'], '%Y-%m-%d %H:%M')
            end_datetime = end_datetime.replace(second=0)

            # end_datetime_timezone = timezone.localize(end_datetime)
            # end_datetime_utc = end_datetime_timezone.astimezone(utc_timezone)
            end_datetime_utc = utc_timezone.localize(end_datetime)
            end_datetime_timezone = end_datetime_utc.astimezone(pytz.timezone(account.timezone))

            # sql_query += ' and created_at < :end'
            # arg_dict['end'] = end_datetime_utc

            # CVTE SQLAlchemy兼容性调整
            query = query.filter(Message.created_at < end_datetime_timezone)

        # sql_query += ' GROUP BY date order by date'
        # rs = db.session.execute(sql_query, arg_dict)
        query = query.group_by(func.date(func.DATE_TRUNC('day', func.timezone(account.timezone, Message.created_at))))
        query = query.order_by(func.date(func.DATE_TRUNC('day', func.timezone(account.timezone, Message.created_at))))

        results = query.all()

        response_data = []

        # CVTE SQLAlchemy兼容性调整
        if len(results) > 0:
            for result in results:
                response_data.append({
                    'date': str(result.date),
                    'terminal_count': result.terminal_count
                })

        return jsonify({
            'data': response_data
        })
        # for i in rs:
        #     response_date.append({
        #         'date': str(i.date),
        #         'terminal_count': i.terminal_count
        #     })
        #
        # return jsonify({
        #     'data': response_date
        # })


class DailyTokenCostStatistic(Resource):
    @setup_required
    @login_required
    @account_initialization_required
    def get(self, app_id):
        account = current_user
        app_id = str(app_id)
        app_model = _get_app(app_id)

        parser = reqparse.RequestParser()
        parser.add_argument('start', type=datetime_string('%Y-%m-%d %H:%M'), location='args')
        parser.add_argument('end', type=datetime_string('%Y-%m-%d %H:%M'), location='args')
        args = parser.parse_args()

        # CVTE SQLAlchemy兼容性调整
        query = db.session.query(
            func.date(func.DATE_TRUNC('day', func.timezone(account.timezone, Message.created_at))).label('date'),
            func.sum(Message.message_tokens + Message.answer_tokens).label('token_count'),
            func.sum(Message.total_price).label('total_price')
        ).filter(
            Message.app_id == app_model.id
        )

        # sql_query = '''
        #         SELECT date(DATE_TRUNC('day', created_at AT TIME ZONE 'UTC' AT TIME ZONE :tz )) AS date,
        #             (sum(messages.message_tokens) + sum(messages.answer_tokens)) as token_count,
        #             sum(total_price) as total_price
        #             FROM messages where app_id = :app_id
        #         '''
        # arg_dict = {'tz': account.timezone, 'app_id': app_model.id}
        #
        # timezone = pytz.timezone(account.timezone)
        utc_timezone = pytz.utc

        if args['start']:
            start_datetime = datetime.strptime(args['start'], '%Y-%m-%d %H:%M')
            start_datetime = start_datetime.replace(second=0)

            start_datetime_utc = utc_timezone.localize(start_datetime)
            start_datetime_timezone = start_datetime_utc.astimezone(pytz.timezone(account.timezone))

            # start_datetime_timezone = timezone.localize(start_datetime)
            # start_datetime_utc = start_datetime_timezone.astimezone(utc_timezone)

            # sql_query += ' and created_at >= :start'
            # arg_dict['start'] = start_datetime_utc
            # CVTE SQLAlchemy兼容性调整
            query = query.filter(Message.created_at >= start_datetime_timezone)

        if args['end']:
            end_datetime = datetime.strptime(args['end'], '%Y-%m-%d %H:%M')
            end_datetime = end_datetime.replace(second=0)

            # end_datetime_timezone = timezone.localize(end_datetime)
            # end_datetime_utc = end_datetime_timezone.astimezone(utc_timezone)
            end_datetime_utc = utc_timezone.localize(end_datetime)
            end_datetime_timezone = end_datetime_utc.astimezone(pytz.timezone(account.timezone))

            # sql_query += ' and created_at < :end'
            # arg_dict['end'] = end_datetime_utc
            # CVTE SQLAlchemy兼容性调整
            query = query.filter(Message.created_at < end_datetime_timezone)

        # sql_query += ' GROUP BY date order by date'
        # rs = db.session.execute(sql_query, arg_dict)
        query = query.group_by(func.date(func.DATE_TRUNC('day', func.timezone(account.timezone, Message.created_at))))
        query = query.order_by(func.date(func.DATE_TRUNC('day', func.timezone(account.timezone, Message.created_at))))
        results = query.all()

        response_data = []

        # CVTE SQLAlchemy兼容性调整
        if len(results) > 0:
            for result in results:
                response_data.append({
                    'date': str(result.date),
                    'token_count': result.token_count,
                    'total_price': result.total_price
                })

        return jsonify({
            'data': response_data
        })


# CVTE 会话延迟统计
class DailyResponseLatencyStatistic(Resource):
    @setup_required
    @login_required
    @account_initialization_required
    def get(self, app_id):
        account = current_user
        app_id = str(app_id)
        app_model = _get_app(app_id)

        parser = reqparse.RequestParser()
        parser.add_argument('start', type=datetime_string('%Y-%m-%d %H:%M'), location='args')
        parser.add_argument('end', type=datetime_string('%Y-%m-%d %H:%M'), location='args')
        args = parser.parse_args()
        utc_timezone = pytz.utc

        query = db.session.query(
            func.date(func.DATE_TRUNC('day', func.timezone(account.timezone, Message.created_at))).label('date'),
            func.max(Message.provider_response_latency).label('max_latency'),
            func.avg(Message.provider_response_latency).label('avg_latency'),
            func.min(Message.provider_response_latency).label('min_latency')
        ).filter(
            Message.app_id == app_model.id
        )

        if args['start']:
            start_datetime = datetime.strptime(args['start'], '%Y-%m-%d %H:%M')
            start_datetime = start_datetime.replace(second=0)

            # start_datetime_timezone = timezone.localize(start_datetime)
            # start_datetime_utc = start_datetime_timezone.astimezone(utc_timezone)

            start_datetime_utc = utc_timezone.localize(start_datetime)
            start_datetime_timezone = start_datetime_utc.astimezone(pytz.timezone(account.timezone))

            # sql_query += ' and created_at >= :start'
            # arg_dict['start'] = start_datetime_utc
            # CVTE SQLAlchemy兼容性调整
            query = query.filter(Message.created_at >= start_datetime_timezone)

        if args['end']:
            end_datetime = datetime.strptime(args['end'], '%Y-%m-%d %H:%M')
            end_datetime = end_datetime.replace(second=0)

            # end_datetime_timezone = timezone.localize(end_datetime)
            # end_datetime_utc = end_datetime_timezone.astimezone(utc_timezone)
            end_datetime_utc = utc_timezone.localize(end_datetime)
            end_datetime_timezone = end_datetime_utc.astimezone(pytz.timezone(account.timezone))

            # sql_query += ' and created_at < :end'
            # arg_dict['end'] = end_datetime_utc

            # CVTE SQLAlchemy兼容性调整
            query = query.filter(Message.created_at < end_datetime_timezone)

        # sql_query += ' GROUP BY date order by date'
        # rs = db.session.execute(sql_query, arg_dict)
        query = query.group_by(func.date(func.DATE_TRUNC('day', func.timezone(account.timezone, Message.created_at))))
        query = query.order_by(func.date(func.DATE_TRUNC('day', func.timezone(account.timezone, Message.created_at))))

        results = query.all()

        response_data = []

        # CVTE SQLAlchemy兼容性调整
        if len(results) > 0:
            for result in results:
                response_data.append({
                    'date': str(result.date),
                    'max_latency': result.max_latency,
                    'avg_latency': result.avg_latency,
                    'min_latency': result.min_latency
                })

        return jsonify({
            'data': response_data
        })


api.add_resource(DailyConversationStatistic, '/apps/<uuid:app_id>/statistics/daily-conversations')
api.add_resource(DailyTerminalsStatistic, '/apps/<uuid:app_id>/statistics/daily-end-users')
api.add_resource(DailyTokenCostStatistic, '/apps/<uuid:app_id>/statistics/token-costs')
api.add_resource(DailyResponseLatencyStatistic, '/apps/<uuid:app_id>/statistics/response-latency')
