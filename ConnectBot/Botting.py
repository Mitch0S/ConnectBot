import base64
import time
import traceback

import requests
import random

class Botting:
    class Auth:
        def get_oauth(self, **kwargs):
            required_kwargs = ['username', 'password']
            missing_required_kwargs = []
            for required_kwarg in required_kwargs:
                try:
                    kwargs[required_kwarg]
                except:
                    missing_required_kwargs.append(required_kwarg)
            if len(missing_required_kwargs) > 0:
                return {'status': 'error', 'reason': 'missing required kwargs',
                        'data': {'missing_kwargs': missing_required_kwargs}, 'required_kwargs': required_kwargs}

            url = "https://connect.det.wa.edu.au/mobile/oauth/token"
            headers = {
                "Authorization": f"Basic {base64.b64encode(b'connect-mobile:7df5336c-3634-4a64-bd0d-7f0d504d7eaf').decode()}"
            }
            url_data = f"?username={kwargs['username']}&password={kwargs['password']}&grant_type=password&scope=connectNow"
            data = {}
            response = requests.post(url + url_data, headers=headers, data=data).json()
            if "error" in response:
                return {'status': "error", 'reason': 'error whilst signing in', 'data': response}
            return {'status': 'ok', 'reason': 'successfully signed in', 'token': response['access_token']}

    class ViewBot:

        total_do_item_event_thread_views = 0
        def do_item_event(self, **kwargs):
            global total_views
            total_views = 0

            required_kwargs = ['item_event', 'access_token', 'views']
            missing_required_kwargs = []
            for required_kwarg in required_kwargs:
                try:
                    kwargs[required_kwarg]
                except:
                    missing_required_kwargs.append(required_kwarg)
            if len(missing_required_kwargs) > 0:
                return {'status': 'error', 'reason': 'you are missing required kwargs', 'data': {'missing_kwargs': missing_required_kwargs, 'required_kwargs': required_kwargs}}

            # TODO:
            #   Add filtering to item_event
            #   Add filtering to access_token
            #   Add filtering to views

            access_token = kwargs['access_token']
            ItemEvent = kwargs['item_event'].replace(":", "%3A")

            views_added = 0
            while views_added != int(kwargs['views']):
                try:
                    start_time = time.time()
                    url = f"https://connect.det.wa.edu.au/mobile/api/v1/stream/card/{ItemEvent}?_dc={random.randint(1000000000000, 9999999999999)}"
                    headers = {
                        "Authorization": f"bearer {access_token}"
                    }
                    try:
                        response = requests.get(url, headers=headers, timeout=5)
                        if response.status_code == 200:
                            views_added += 1

                    except:
                        time.sleep(10)
                except:
                    pass
            return None


    class Feed:
        def get_feed(self, **kwargs):
            required_kwargs = ['access_token', 'quantity']
            missing_required_kwargs = []
            for required_kwarg in required_kwargs:
                try:
                    kwargs[required_kwarg]
                except:
                    missing_required_kwargs.append(required_kwarg)
            if len(missing_required_kwargs) > 0:
                return {'status': 'error', 'reason': 'you are missing required kwargs', 'data': {'missing_kwargs': missing_required_kwargs, 'required_kwargs': required_kwargs}}

            # TODO:
            #   Add filtering to item_event
            #   Add filtering to access_token
            #   Add filtering to quantity

            access_token = kwargs['access_token']
            url = f"https://connect.det.wa.edu.au/mobile/api/v1/stream/card?_dc={random.randint(1000000000000, 9999999999999)}&page=1&size={int(kwargs['quantity'])}"
            headers = {
                "Authorization": f"bearer {access_token}"
            }
            try:
                response = requests.get(url, headers=headers)
                notices = response.json()['data']
                notices = {}
                for notice in notices:
                    print(f"""    Title: {notice['data']['title']}\n    Class: {notice['data']['owner']['name']}\nItemEvent: {notice['id']}\n""")
            except Exception as error:
                return {'status': 'error', 'reason': 'not signed in'}
            return {'status': 'ok', 'reason': 'retrieved notice feed successfully', 'data': {'response': response}}

        def get_feed_json(self, **kwargs):
            required_kwargs = ['access_token', 'quantity']
            missing_required_kwargs = []
            for required_kwarg in required_kwargs:
                try:
                    kwargs[required_kwarg]
                except:
                    missing_required_kwargs.append(required_kwarg)
            if len(missing_required_kwargs) > 0:
                return {'status': 'error', 'reason': 'you are missing required kwargs', 'data': {'missing_kwargs': missing_required_kwargs, 'required_kwargs': required_kwargs}}

            # TODO:
            #   Add filtering to item_event
            #   Add filtering to access_token
            #   Add filtering to quantity

            access_token = kwargs['access_token']
            url = f"https://connect.det.wa.edu.au/mobile/api/v1/stream/card?_dc={random.randint(1000000000000, 9999999999999)}&page=1&size={int(kwargs['quantity'])}"
            headers = {
                "Authorization": f"bearer {access_token}"
            }
            try:
                response = requests.get(url, headers=headers)
                notices = response.json()['data']
                notices_dict = {}
                notice_select_number = 0
                for notice in notices:
                    notices_dict[notice_select_number] = {'title': notice['data']['title'], 'class': notice['data']['owner']['name'], 'item_event': notice['id']}
                    notice_select_number += 1

            except Exception as error:
                return {'status': 'error', 'reason': 'not signed in'}
            return {'status': 'ok', 'reason': 'retrieved notice feed successfully', 'data': {'notices': notices_dict}}