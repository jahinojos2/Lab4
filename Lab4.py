#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 19:27:26 2018
@author: jaimeahinojos
"""

class hashtablenode:

    def __init__(self, k, l, next):
        self.key = k
        self.vect = l
        self.next = next
class HashTable:
    def __init__(self, table_size):
        self.table = [None] * table_size

def hash(key):
    hash_value = (key*5)%26415
    return hash_value
def read_file(a):
    with open(a) as f:
        list = f.read().splitlines()
    return list
def get_load_factor():
    return None
def average_number_of_comparisons():

def get_max(list):
    max_num = 0
    for i in range(len(list)):
        tempArray = list[i].split(' ')
        testWord = tempArray[0]
        if testWord[0].isalpha():
            new_num = 0
            for j in range(len(testWord)):
                new_num = new_num + ord(testWord[j])
            if new_num > max_num:
                max_num = new_num
    print (max_num)
def main():
    table_hash = HashTable(26415)

text1 = 'glove.6B.50d.txt'
list = read_file(text1)
get_max(list)


