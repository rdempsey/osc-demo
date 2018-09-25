#!/usr/bin/env python

import redis
from time import sleep
from datetime import datetime
from random import choice
import json

WORD_FILE = "word_list.txt"
SEARCH_QUERIES = open(WORD_FILE).read().splitlines()

def create_redis_connection():
    '''
    Create a Redis connection.
    '''
    try:
        r = redis.StrictRedis(
            host='localhost',
            port=6379,
            db=0
        )
        return r
    except Exception as e:
        print("Unable to create Redis connection: {}".format(e))

def create_search_record(redis_conn):
    '''
    Create a search record in Redis.
    '''
    search_query = choice(SEARCH_QUERIES)
    redis_list = "search-log"
    record_value = {
        "search_date": "{}".format(datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S")),
        "search_url": 'http://duckduckgo.com/?q={}'.format(search_query.replace(" ", "+")),
        "search_query": search_query
    }

    try:
        redis_conn.lpush(redis_list, json.dumps(record_value, ensure_ascii=False))
    except Exception as e:
        print("Error when creating key in Redis: {}".format(e))

if __name__ == "__main__":
    r_conn = create_redis_connection()
    max_records = 500
    for i in range(1,max_records):
        print('%06.2f'%(i/max_records*100),'% complete', end="\r")
        create_search_record(r_conn)
        sleep(1)
    