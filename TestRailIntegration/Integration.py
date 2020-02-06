from TestRailIntegration.testrail import *
from Config.ConfigReader import ConfigReader

class Integration():
    __result_flag = True
    __msg = ""
    __client = None

    def __init__(self):
        pass

    @classmethod
    def append_msg(cls, msg, result_flag):
        if cls.__client is None:
            cls.__client = cls.get_testrail_client()
        cls.__msg += msg
        if result_flag is False and cls.__result_flag is True:
            cls.__result_flag = False

        cls.__result_flag = result_flag

    @classmethod
    def send_msg(cls,case_id, run_id):
        if cls.__client is None:
            cls.__client = cls.get_testrail_client()
        if cls.__result_flag:
            cls.__msg += "Successfully updated the example form"
        else:
            cls.__msg += (" Failed to update the example form")

        cls.update_testrail(case_id, run_id, cls.__result_flag, cls.__msg)
        cls.__msg = ""
        cls.__result_flag = True

    @classmethod
    def get_testrail_client(cls):
        client = APIClient(ConfigReader.get_testratil_url())
        client.user = ConfigReader.get_testratil_name()
        client.password = ConfigReader.get_testratil_password()
        return client

    @classmethod
    def update_testrail(cls,case_id, run_id, result_flag, msg=""):
        if cls.__client is None:
            cls.__client = cls.get_testrail_client()
        update_flag = False
        #status_id is 1 for passed, 2 for blocked, 4 for retest amd 5 for failed
        status_id = 1 if result_flag is True else 5
        if run_id is not None:
            try:
                result = cls.__client.send_post(
                    'add_result_for_case/%s/%s'%(run_id,case_id),
                    {'status_id': status_id, 'comment':msg})
            except Exception as e:
                print('Exception in updat_testrail() updating TestRail.')
                print('Python says: ')
                print(e)
            else:
                print('Updated test result for case: %s in test run: %s with msg:%s'%(case_id,run_id,msg))

        return update_flag

    @classmethod
    def get_project_id(cls,project_name):
        if cls.__client is None:
            cls.__client = cls.get_testrail_client()
        project_id = None
        projects = cls.__client.send_get('get_projects')
        for project in projects:
            if project['name'] == project_name:
                project_id = project['id']
                break
        return project_id

    @classmethod
    def get_run_id(cls,test_run_name, project_name):
        run_id = None
        if cls.__client is None:
            cls.__client = cls.get_testrail_client()
        project_id = cls.get_project_id(project_name)
        try:
            test_runs = cls.__client.send_get('get_runs/%s'%(project_id))
        except Exception as e:
            print('Exception in update_testrail() updating TestRail.')
            print('PYTHON SAYS: ')
            print(e)
            return None
        else:
            for test_run in test_runs:
                if test_run['name'] == test_run_name:
                    run_id = test_run['id']
                    break
            return run_id



