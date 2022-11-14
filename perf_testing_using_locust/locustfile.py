# -*- coding: utf-8 -*-
# Built-in/Generic Imports

import logging, json, time
import random

from locust import task, between, HttpUser

__author__ = "Gaurav Mishra"
log = logging.getLogger("rest-api-perf-test")

def get_headers():
    """ It generated the api headers."""
    headers = {'Content-type': 'application/json',
               'Accept': 'application/json'}
    return headers

def get_api_payload(added_fields=None):
    """ It generated the payload of request."""
    payload = {}
    if added_fields:
      payload.update(added_fields)
    return payload

def randome_delay():
    return random.randint(2, 10)

class StartUser(HttpUser):
    # the simulated users wait between 1 and 5 seconds after each task
    wait_time = between(5, 10)
    host = "https://fakerestapi.azurewebsites.net/api/v1/"

    def __init__(self, environment):
        """ Class constructor."""
        super().__init__(environment)

    #base functions/library
    def get_author_details(self):
        # --------------------- get author details -----------
        get_author_url = self.host + "Authors"
        print(get_author_url)
        try:
            with self.client.get(get_author_url,
                                 headers=get_headers(),
                                 catch_response=True) as resp_of_api:

                if resp_of_api.status_code == 200:
                    resp_of_api.success()
                    log.info("API call resulted in success.")
                else:
                    resp_of_api.failure(resp_of_api.text)
                    log.error("API call resulted in failed.")

        except Exception as e:
            log.error(f"Exception occurred! details are {e}")

    def get_book_by_id(self, book_id):
        # -------------------- get book by id ------------------
        get_author_book_by_id_url = self.host + "Authors/authors/books/{}".format(book_id)
        print(get_author_book_by_id_url)
        try:
            with self.client.get(get_author_book_by_id_url,
                                 headers=get_headers(),
                                 catch_response=True) as resp_of_api:

                if resp_of_api.status_code == 200:
                    resp_of_api.success()
                    log.info("API call resulted in success.")
                else:
                    resp_of_api.failure(resp_of_api.text)
                    log.error("API call resulted in failed.")

        except Exception as e:
            log.error(f"Exception occurred! details are {e}")

    def get_author_by_id(self, author_id):
        # ---------------------- get author by id ---------------------
        get_author_by_id_url = self.host + "Authors/{}".format(author_id)
        try:
            with self.client.get(get_author_by_id_url,
                                 headers=get_headers(),
                                 catch_response=True) as resp_of_api:
                if resp_of_api.status_code == 200:
                    resp_of_api.success()
                    log.info("API call resulted in success.")
                else:
                    resp_of_api.failure(resp_of_api.text)
                    log.error("API call resulted in failed.")

        except Exception as e:
            log.error(f"Exception occurred! details are {e}")

    def create_author(self, author_id):
        # ---------------------- create author ---------------------
        create_author_by_id_url = self.host + "Authors"
        try:
            payload = {"id": author_id,
                       "idBook": author_id,
                       "firstName": "abc",
                       "lastName": "xyz"}
            with self.client.post(create_author_by_id_url,
                                  headers=get_headers(),
                                  data=json.dumps(payload),
                                  catch_response=True) as resp_of_api:
                if resp_of_api.status_code == 200:
                    resp_of_api.success()
                    log.info("create_author_by_id API call resulted in success.")
                else:
                    resp_of_api.failure(resp_of_api.text)
                    print(resp_of_api.status_code)
                    log.error("create_author_by_id API call resulted in failed.")

        except Exception as e:
            log.error(f"Exception occurred! details are {e}")

    def modify_author_details(self, author_id):
        # ---------------------- modify author details ----------------
        modify_author_by_id_url = self.host + "Authors/{}".format(author_id)
        try:
            payload = {"id": author_id,
                       "idBook": author_id,
                       "firstName": "abc1",
                       "lastName": "xyz1"}
            with self.client.put(modify_author_by_id_url,
                                 headers=get_headers(),
                                 data=json.dumps(payload),
                                 catch_response=True) as resp_of_api:
                if resp_of_api.status_code == 200:
                    resp_of_api.success()
                    log.info("modify_author_by_id API call resulted in success.")
                else:
                    resp_of_api.failure(resp_of_api.text)
                    log.error("modify_author_by_id API call resulted in failed.")

        except Exception as e:
            log.error(f"Exception occurred! details are {e}")

    def delete_author(self, author_id):
        # ---------------------- delete author ------------------------
        delete_author_url = self.host + "Authors/{}".format(author_id)
        try:
            with self.client.delete(delete_author_url,
                                    headers=get_headers(),
                                    catch_response=True) as resp_of_api:
                if resp_of_api.status_code == 200:
                    resp_of_api.success()
                    log.info("delete_author API call resulted in success.")
                else:
                    resp_of_api.failure(resp_of_api.text)
                    log.error("delete_author API call resulted in failed.")

        except Exception as e:
            log.error(f"Exception occurred! details are {e}")

    # single event tasks
    @task(6)
    def load_rest_api_get_author(self):
        self.get_author_details()
        randome_delay()

    @task(6)
    def load_rest_api_get_author_book_by_id(self):
        self.get_book_by_id(1)
        randome_delay()

    @task(6)
    def load_rest_api_get_author_by_id(self):
        for item_id in range(10):
            self.get_author_by_id(item_id)
            time.sleep(1)
        randome_delay()

    # multi event tasks
    @task(8)
    def load_rest_api_get_author_and_book(self):
        self.get_author_details()
        self.get_author_by_id(22)
        self.get_book_by_id(1)
        randome_delay()

    @task(8)
    def load_rest_api_get_author_and_book(self):
        self.get_author_details()
        self.get_book_by_id(1)
        randome_delay()

    @task(4)
    def load_rest_api_post_author_create_delete(self):
        author_id = 22
        self.create_author(author_id)
        self.get_author_by_id(author_id)
        self.delete_author(author_id)
        randome_delay()

    @task(10)
    def load_rest_api_post_author_create_update(self):
        author_id = 22
        self.create_author(author_id)
        self.get_author_by_id(author_id)
        for _ in range(3):
            self.modify_author_details(author_id)
            self.get_author_by_id(author_id)
        randome_delay()

    @task(10)
    def load_rest_api_post_author_create_update_delete(self):
        author_id = 22
        self.create_author(author_id)
        self.get_author_by_id(author_id)
        for _ in range(5):
            self.modify_author_details(author_id)
            self.get_author_by_id(author_id)
        self.delete_author(author_id)
        randome_delay()



