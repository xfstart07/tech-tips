#!/usr/bin/python
# -*- coding: UTF-8 -*-

import redis
import json
from pprint import pprint

class FabricRedis:
    def __init__(self):
        self.redis = redis.Redis(host='localhost',port=6379,db=0) 
    
    def keys(self):
        return self.redis.keys('fabricStyleFabricId*') 
    
    def empty(self):
        keys = self.redis.keys('fabricStyleFabricId*') 
        for item in keys:
            self.redis.empty(item)

    def delete(self):
        keys = self.redis.keys('fabricStyleFabricId*') 
        for item in keys:
            self.redis.delete(item)
    
    def input(self):
        with open('data.json') as data_file:    
            data = json.load(data_file)
        for item in data:
            self.redis.set(item['key'], item['value'])
    
    def output(self):
        result = [] 
        for item in keys:
            value = redis.get(item)
            temp = {}
            temp['key'] = item
            temp['value'] = value
            result.append(temp)

        json.dump(result, open('data.json', 'wb'))

fabric = FabricRedis()
fabric.delete()
