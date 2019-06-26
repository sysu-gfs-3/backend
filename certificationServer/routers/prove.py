# -*- encoding:utf-8 -*-
import json
from flask import session, Flask, jsonify, request, send_from_directory
from flask_cors import CORS

from swagger_server.modules.userManagementSystem import ManagementSystem as UMS
from swagger_server.modules.taskManagementSystem import taskManagementSystem as TMS
from swagger_server.modules.AdminPlatform import AdminPlatform as AP
app = Flask(__name__)
app.secret_key = "nQnk2n8moN=GLNmE.wL6PTZD"

CORS(app, supports_credentials=True)


def ok(data=None):
    return jsonify({
        "status": "ok",
        "data": data
    })


def bad(msg=""):
    return jsonify({
        "status": "bad",
        "message": msg
    })

# Login Part:
@app.route("/api/v1/login", methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        print(json_data)

        account = json_data.get('account', None)
        password = json_data.get('password', None)

        admin = AP.get_admin(account) # search for admin by account
        if admin is None:
            return bad('wrong account')
        print(admin[0])

        if password == admin[0]['password']:
            session['account'] = account
            return ok(json.dumps(admin[0]))
        else:
            return bad('wrong password')

    return bad('please POST')


# Query Part:
@app.route('/api/v1/get_users', methods=['POST'])
def get_users():
    if request.method =='POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        print('data', json_data)

        page      = json_data.get('page', None)
        user_type = json_data.get('user_type', None)

        if page is None or user_type is None:
            return bad('key error')

        record_num = UMS.get_user_count(user_type)

        if page > record_num // 100 + 1:
            return bad('out of user size')

        data = UMS.get_users(user_type=user_type, page=page)
        print(data)

        return ok(json.dumps(data))
    return bad('error')

@app.route('/api/v1/get_user_count', methods=['POST'])
def get_user_count():
    if request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        print('data', json_data)

        user_type = json_data.get('user_type', None)
        if user_type is None:
            return bad('key error')

        record_num = UMS.get_user_count(user_type)

        print('record_num', record_num)

        return ok(json.dumps({'count': record_num}))
    return bad('please user POST!')

@app.route('/api/v1/specific_user_count', methods=['POST'])
def specific_user_count():
    if request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        print('data', json_data)

        gender = json_data.get('gender', None)
        identity = json_data.get('identity', None)

        if gender not in ['W', 'M'] or identity not in ['S', 'C']:
            return bad('bad gender/identity')

        record_num = UMS.specific_user_count(gender, identity)

        print('record_num', record_num)

        if record_num[0]:
            return ok(json.dumps({'count': record_num[1]}))
        else:
            return bad(json.dumps(record_num[1]))
    else:
        return bad('use POST')

@app.route('/api/v1/get_task', methods=['POST'])
def get_task():
    if request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        print('data', json_data)

        page      = json_data.get('page', None)
        task_type = json_data.get('task_type', None)

        if page is None or task_type is None:
            return bad('key error')

        record_num = TMS.get_task_count(task_type)
        if page > record_num // 100 + 1:
            return bad('out of user size')

        data = TMS.get_tasks(task_type=task_type, page=page)
        print(data)
        return ok(json.dumps(data))
    return bad('error')

@app.route('/api/v1/get_task_count', methods=['POST'])
def get_task_count():
    if request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        print('data', json_data)

        task_type = json_data.get('task_type', None)
        task_state = json_data.get('task_state', None)

        if task_type not in ['O', 'W', 'all'] or task_state not in ['all', 'waiting']:
            return bad('task type/state error')

        record_num = TMS.get_task_count(state=task_state, type=task_type)

        print('record_num', record_num)

        if record_num[0]:
            return ok(json.dumps({'count': record_num[1]}))
        else:
            return bad(json.dumps(record_num[1]))

    return bad('please user POST!')


@app.route('/api/v1/get_user_info', methods=['POST'])
def get_user_info():
    if request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        print('data', json_data)

        user_id      = json_data.get('user_id', None)
        if user_id is None:
            return bad('user id is None')
        user = UMS.get_user_info(user_id)
        identity = json_data.get('identity', None)

        if identity is not None:
            if identity != user['identity']:
                return bad('wrong identity')
        else:
            identity = user.identity

        data = UMS.get_indentity_info(user_id, identity)
        if data is None:
            return bad('nothing found')

        data.update(user.info_dict())
        print(data)
        return ok(json.dumps(data))
    return bad('error')


###################
## Auditing Part ##
###################

"""
N W F P
"""
@app.route('/api/v1/audit_user', methods=['POST'])
def audit_user():
    if request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        print('data', json_data)

        user_id = json_data.get('user_id', None)
        identity = json_data.get('identity', None)
        audit = json_data.get('audit', None)

        if not (user_id and identity and audit is not None):
            print(user_id, identity, audit)
            return bad('wrong data value')

        resutl = AP.audit_user(user_id, identity, audit)

        if isinstance(resutl, tuple) and resutl[0]:
            if resutl[0]:
                return ok(resutl[1])
            else:
                return bad('Unknown error: %s' % resutl[1])
        else:
            return bad(resutl)
    else:
        return bad('please use POST')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=60006, threaded=True)
