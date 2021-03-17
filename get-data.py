import apscheduler.schedulers.blocking
import fort
import logging
import os
import requests
import requests.auth
import signal
import sys

log = logging.getLogger('pudding_api.get_data')


class Database(fort.PostgresDatabase):
    def add_competitor(self, params: dict):
        sql = '''
            insert into pudding_competitors (
                id, name, created_at, updated_at
            ) values (
                %(id)s, %(name)s, %(created_at)s, %(updated_at)s
            ) on conflict (id, updated_at) do nothing
        '''
        self.u(sql, params)

    def add_contact(self, params: dict):
        sql = '''
            insert into pudding_contacts (
                id, name, email, initial, parent_type, parent_id, created_by_type,
                created_by_id, created_at, updated_by_type, updated_by_id, updated_at
            ) values (
                %(id)s, %(name)s, %(email)s, %(initial)s, %(parent_type)s, %(parent_id)s, %(created_by_type)s,
                %(created_by_id)s, %(created_at)s, %(updated_by_type)s, %(updated_by_id)s, %(updated_at)s
            ) on conflict (id, updated_at) do nothing
        '''
        self.u(sql, params)

    def add_customer(self, params: dict):
        sql = '''
            insert into pudding_customers (
                id, name, domain, created_by_type, created_by_id, created_at,
                updated_by_type, updated_by_id, updated_at
            ) values (
                %(id)s, %(name)s, %(domain)s, %(created_by_type)s, %(created_by_id)s, %(created_at)s,
                %(updated_by_type)s, %(updated_by_id)s, %(updated_at)s
            ) on conflict (id, updated_at) do nothing
        '''
        self.u(sql, params)

    def add_milestone(self, params: dict):
        sql = '''
            insert into pudding_milestones (
                id, code, title, start_date, due_date, visibility, milestone_order, project_id,
                created_by_type, created_by_id, created_at, updated_by_type, updated_by_id,
                updated_at, assignees
            ) values (
                %(id)s, %(code)s, %(title)s, %(start_date)s, %(due_date)s, %(visibility)s, %(order)s, %(project_id)s,
                %(created_by_type)s, %(created_by_id)s, %(created_at)s, %(updated_by_type)s, %(updated_by_id)s,
                %(updated_at)s, %(assignees)s
            ) on conflict (id, updated_at) do nothing
        '''
        self.u(sql, params)

    def add_partner(self, params: dict):
        sql = '''
            insert into pudding_partners (
                id, name, domain, created_by_type, created_by_id, created_at,
                updated_by_type, updated_by_id, updated_at
            ) values (
                %(id)s, %(name)s, %(domain)s, %(created_by_type)s, %(created_by_id)s, %(created_at)s,
                %(updated_by_type)s, %(updated_by_id)s, %(updated_at)s
            ) on conflict (id, updated_at) do nothing
        '''
        self.u(sql, params)

    def add_project(self, params: dict):
        sql = '''
            insert into pudding_projects (
                id, title, description, next_step, deal_amount, start_date, due_date,
                estimated_start_date, estimated_end_date, status, health_color, customer_id,
                partner_id, stage_id, workspace_id, result_id, project_order, code, serial_number,
                archived_at, created_by_type, created_by_id, created_at, updated_by_type,
                updated_by_id, updated_at, competitors, tags, territories
            ) values (
                %(id)s, %(title)s, %(description)s, %(next_step)s, %(deal_amount)s, %(start_date)s, %(due_date)s,
                %(estimated_start_date)s, %(estimated_end_date)s, %(status)s, %(health_color)s, %(customer_id)s,
                %(partner_id)s, %(stage_id)s, %(workspace_id)s, %(result_id)s, %(order)s, %(code)s, %(serial_number)s,
                %(archived_at)s, %(created_by_type)s, %(created_by_id)s, %(created_at)s, %(updated_by_type)s,
                %(updated_by_id)s, %(updated_at)s, %(competitors)s, %(tags)s, %(territories)s
            ) on conflict (id, updated_at) do nothing
        '''
        self.u(sql, params)

    def add_result(self, params: dict):
        sql = '''
            insert into pudding_results (
                id, value, created_at, updated_at
            ) values (
                %(id)s, %(value)s, %(created_at)s, %(updated_at)s
            ) on conflict (id, updated_at) do nothing
        '''
        self.u(sql, params)

    def add_stage(self, params: dict):
        sql = '''
            insert into pudding_stages (
                id, name, created_at, updated_at
            ) values (
                %(id)s, %(name)s, %(created_at)s, %(updated_at)s
            ) on conflict (id, updated_at) do nothing
        '''
        self.u(sql, params)

    def add_status(self, params: dict):
        sql = '''
            insert into pudding_status (
                id, type, value, status, is_active, status_order, is_starred, created_by_type,
                created_by_id, created_at, updated_by_type, updated_by_id, updated_at
            ) values (
                %(id)s, %(type)s, %(value)s, %(status)s, %(is_active)s, %(order)s, %(is_starred)s, %(created_by_type)s,
                %(created_by_id)s, %(created_at)s, %(updated_by_type)s, %(updated_by_id)s, %(updated_at)s
            ) on conflict (id, updated_at) do nothing
        '''
        self.u(sql, params)

    def add_success_criteria(self, params: dict):
        sql = '''
            insert into pudding_success_criteria (
                id, code, title, description, status_id, success_criteria_order, usecase_id,
                created_by_type, created_by_id, created_at, updated_by_type, updated_by_id,
                updated_at, assignees
            ) values (
                %(id)s, %(code)s, %(title)s, %(description)s, %(status_id)s, %(order)s, %(usecase_id)s,
                %(created_by_type)s, %(created_by_id)s, %(created_at)s, %(updated_by_type)s, %(updated_by_id)s,
                %(updated_at)s, %(assignees)s
            ) on conflict (id, updated_at) do nothing
        '''
        self.u(sql, params)

    def add_tag(self, params: dict):
        sql = '''
            insert into pudding_tags (
                id, label, color, type, created_at, updated_at
            ) values (
                %(id)s, %(label)s, %(color)s, %(type)s, %(created_at)s, %(updated_at)s
            ) on conflict (id, updated_at) do nothing
        '''
        self.u(sql, params)

    def add_task(self, params: dict):
        sql = '''
            insert into pudding_tasks (
                id, code, title, description, priority, due_date, visibility, task_order,
                milestone_id, project_id, completed_by_type, completed_by_id, completed_at,
                created_by_type, created_by_id, created_at, updated_by_type, updated_by_id,
                updated_at, assignees
            ) values (
                %(id)s, %(code)s, %(title)s, %(description)s, %(priority)s, %(due_date)s, %(visibility)s, %(order)s,
                %(milestone_id)s, %(project_id)s, %(completed_by_type)s, %(completed_by_id)s, %(completed_at)s,
                %(created_by_type)s, %(created_by_id)s, %(created_at)s, %(updated_by_type)s, %(updated_by_id)s,
                %(updated_at)s, %(assignees)s
            ) on conflict (id, updated_at) do nothing
        '''
        self.u(sql, params)

    def add_territory(self, params: dict):
        sql = '''
            insert into pudding_territories (
                id, name, color, created_at, updated_at
            ) values (
                %(id)s, %(name)s, %(color)s, %(created_at)s, %(updated_at)s
            ) on conflict (id, updated_at) do nothing
        '''
        self.u(sql, params)

    def add_testcase(self, params: dict):
        sql = '''
            insert into pudding_testcases (
                id, code, title, description, status_id, testcase_order, usecase_id,
                created_by_type, created_by_id, created_at, updated_by_type, updated_by_id,
                updated_at, assignees
            ) values (
                %(id)s, %(code)s, %(title)s, %(description)s, %(status_id)s, %(order)s, %(usecase_id)s,
                %(created_by_type)s, %(created_by_id)s, %(created_at)s, %(updated_by_type)s, %(updated_by_id)s,
                %(updated_at)s, %(assignees)s
            ) on conflict (id, updated_at) do nothing
        '''
        self.u(sql, params)

    def add_usecase(self, params: dict):
        sql = '''
            insert into pudding_usecases (
                id, code, title, description, visibility, status, usecase_order, project_id,
                created_by_type, created_by_id, created_at, updated_by_type, updated_by_id,
                updated_at, assignees
            ) values (
                %(id)s, %(code)s, %(title)s, %(description)s, %(visibility)s, %(status)s, %(order)s, %(project_id)s,
                %(created_by_type)s, %(created_by_id)s, %(created_at)s, %(updated_by_type)s, %(updated_by_id)s,
                %(updated_at)s, %(assignees)s
            ) on conflict (id, updated_at) do nothing
        '''
        self.u(sql, params)

    def add_user(self, params: dict):
        sql = '''
            insert into pudding_users (
                id, name, email, created_at, updated_at
            ) values (
                %(id)s, %(name)s, %(email)s, %(created_at)s, %(updated_at)s
            ) on conflict (id, updated_at) do nothing
        '''
        self.u(sql, params)

    def add_workspace(self, params: dict):
        sql = '''
            insert into pudding_workspaces (
                id, title, is_default, is_global, is_active, workspace_order, created_by_type,
                created_by_id, created_at, updated_by_type, updated_by_id, updated_at
            ) values (
                %(id)s, %(title)s, %(is_default)s, %(is_global)s, %(is_active)s, %(order)s, %(created_by_type)s,
                %(created_by_id)s, %(created_at)s, %(updated_by_type)s, %(updated_by_id)s, %(updated_at)s
            ) on conflict (id, updated_at) do nothing
        '''
        self.u(sql, params)


def get_data(s: requests.Session, data_type: str, params: dict = None):
    domain = os.getenv('PUDDING_DOMAIN')
    url = f'https://pra01-api.pudding.app/v1/{domain}/public/{data_type}'
    while True:
        response = s.get(url, params=params)
        response.raise_for_status()
        rate_limit_remaining = response.headers.get('x-ratelimit-remaining')
        log.debug(f'Remaining API calls: {rate_limit_remaining}')
        yield from response.json().get('data', [])
        url = response.json().get('links', {}).get('next')
        if url is None:
            break


def get_competitors(s: requests.Session):
    yield from get_data(s, 'competitors')


def get_contacts(s: requests.Session, parent_type: str, parent_id: str):
    # parent_type should be 'Customer' or 'Partner'
    params = {
        'filter[parent_type]': parent_type,
        'filter[parent_id]': parent_id
    }
    yield from get_data(s, 'contacts', params)


def get_customers(s: requests.Session):
    yield from get_data(s, 'customers')


def get_partners(s: requests.Session):
    yield from get_data(s, 'partners')


def get_projects(s: requests.Session, workspace_id: str):
    params = {
        'filter[workspace_id]': workspace_id,
        'include': 'competitors,tags,territories'
    }
    yield from get_data(s, 'projects', params)


def get_results(s: requests.Session):
    yield from get_data(s, 'results')


def get_stages(s: requests.Session, workspace_id: str):
    params = {
        'filter[workspace_id]': workspace_id
    }
    yield from get_data(s, 'stages', params)


def get_tags_for_type(s: requests.Session, tag_type: str):
    # type should be 'label' or 'product' or 'platform'
    params = {
        'filter[type]': tag_type
    }
    yield from get_data(s, 'tags', params)


def get_tags(s: requests.Session):
    for tag_type in ('label', 'product', 'platform'):
        for t in get_tags_for_type(s, tag_type):
            t.update({'type': tag_type})
            yield t


def get_tasks_for_project(s: requests.Session, project_id: str):
    params = {
        'filter[project_id]': project_id,
        'include': 'assignees,milestone.assignees'
    }
    yield from get_data(s, 'tasks', params)


def get_territories(s: requests.Session):
    yield from get_data(s, 'territories')


def get_usecases_for_project(s: requests.Session, project_id: str):
    params = {
        'filter[project_id]': project_id,
        'include': 'assignees,success_criteria.assignees,success_criteria.status,testcases.assignees,testcases.status'
    }
    yield from get_data(s, 'usecases', params)


def get_users(s: requests.Session):
    yield from get_data(s, 'users')


def get_workspaces(s: requests.Session):
    yield from get_data(s, 'workspaces')


def main_job():
    log.info('Getting all data from Pudding')
    db = Database(os.getenv('DB'))
    s = requests.Session()
    token = os.getenv('PUDDING_TOKEN')
    s.headers.update({
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    })
    for c in get_competitors(s):
        db.add_competitor(c)
    for c in get_customers(s):
        db.add_customer(c)
        for co in get_contacts(s, 'Customer', c.get('id')):
            db.add_contact(co)
    for p in get_partners(s):
        db.add_partner(p)
        for co in get_contacts(s, 'Partner', p.get('id')):
            db.add_contact(co)
    for r in get_results(s):
        db.add_result(r)
    for t in get_tags(s):
        db.add_tag(t)
    for t in get_territories(s):
        db.add_territory(t)
    for u in get_users(s):
        db.add_user(u)
    for ws in get_workspaces(s):
        db.add_workspace(ws)
        workspace_id = ws.get('id')
        for st in get_stages(s, workspace_id):
            db.add_stage(st)
        for p in get_projects(s, workspace_id):
            p.update({
                'competitors': ' '.join([c.get('id') for c in p.get('competitors')]),
                'tags': ' '.join([t.get('id') for t in p.get('tags')]),
                'territories': ' '.join([t.get('id') for t in p.get('territories')])
            })
            db.add_project(p)
            project_id = p.get('id')
            for ta in get_tasks_for_project(s, project_id):
                ta.update({'assignees': ' '.join([a.get('id') for a in ta.get('assignees')])})
                db.add_task(ta)
                m = ta.get('milestone')
                if m is not None:
                    m.update({'assignees': ' '.join([a.get('id') for a in m.get('assignees')])})
                    db.add_milestone(ta.get('milestone'))
            for u in get_usecases_for_project(s, project_id):
                u.update({'assignees': ' '.join([a.get('id') for a in u.get('assignees')])})
                db.add_usecase(u)
                for t in u.get('testcases', []):
                    t.update({'assignees': ' '.join([a.get('id') for a in t.get('assignees')])})
                    db.add_testcase(t)
                    db.add_status(t.get('status'))
                for c in u.get('success_criteria', []):
                    c.update({'assignees': ' '.join([a.get('id') for a in c.get('assignees')])})
                    db.add_success_criteria(c)
                    db.add_status(c.get('status'))
    log.info('Done getting all data from Pudding')


def main():
    log_format = os.getenv('LOG_FORMAT', '%(levelname)s [%(name)s] %(message)s')
    logging.basicConfig(format=log_format, level='DEBUG', stream=sys.stdout)
    version = os.getenv('APP_VERSION', 'unknown')
    log.debug(f'pudding_api.get_data {version}')
    log_level = os.getenv('LOG_LEVEL', 'INFO')
    if not log_level == 'DEBUG':
        log.debug(f'Setting log level to {log_level}')
    logging.getLogger().setLevel(log_level)

    for log_spec in os.getenv('OTHER_LOG_LEVELS', '').split():
        logger, level = log_spec.split(':', maxsplit=1)
        log.debug(f'Setting log level for {logger} to {level}')
        logging.getLogger(logger).setLevel(level)

    if os.getenv('RUN_AND_EXIT'):
        main_job()
    else:
        scheduler = apscheduler.schedulers.blocking.BlockingScheduler()
        scheduler.add_job(main_job)
        scheduler.add_job(main_job, 'interval', minutes=int(os.getenv('SYNC_INTERVAL', 60 * 24)))
        scheduler.start()


def handle_sigterm(_signal, _frame):
    sys.exit()


if __name__ == '__main__':
    signal.signal(signal.SIGTERM, handle_sigterm)
    main()
