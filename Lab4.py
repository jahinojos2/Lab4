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
        self.table = [None] * (table_size*2)

    def hash(self, key):
        ascii = 1
        for i in range(len(key)):
            ascii = (ascii + ord(key[i]))*ord(key[i])
        ascii =  ascii/len(key[i])
        hash_value = (ascii) % len(self.table)
        return int(hash_value)

    def hash2(self, key):
        ascii = 1
        for i in range(len(key)):
            ascii = (ascii*ord(key[i]))
        hash_value = ascii%len(self.table)
        return int(hash_value)

    def hash3(self, key):
        ascii = 0
        for i in range(len(key)):
            ascii += ord(key[i])
        hash_value = (ascii*26) % len(self.table)
        return int(hash_value)

    def insert(self, element, new_array, answer):
        index = 0
        if answer == 1:
            index = self.hash(element)
        elif answer == 2:
            index = self.hash2(element)
        else:
            index = self.hash3(element)

        self.table[index] = hashtablenode(element, new_array,self.table[index])

    def search(self, k, answer):
        index = 0
        count = 0
        if answer == 1:
            index = self.hash(k)
        elif answer == 2:
            index = self.hash2(k)
        else:
            index = self.hash3(k)

        temp = self.table[index]

        while temp is not None:
            count += 1
            if temp.key == k:
                return count

            temp = temp.next

        return count



def read_file(a):
    with open(a) as f:
        list = f.read().splitlines()
    return list

def get_load_factor(hash_table):
    num_keys = 0
    for i in range(len(hash_table.table)):
        temp_table = hash_table.table[i]
        while temp_table is not None:
            num_keys += 1
            temp_table = temp_table.next

    num = float((num_keys))/float(len(hash_table.table))
    print(num)



def average_number_of_comparisons(list, table, answer):
    number = 0
    for i in range(len(list)):
        tempArray = list[i].split(' ')
        testWord = tempArray[0]
        if testWord[0].isalpha():
            number += table.search(testWord, answer)
    print(number/len(list))


def create_hash_table(list, table, answer):

    for i in range(len(list)):

        tempArray = list[i].split(' ')
        testWord = tempArray[0]

        if testWord[0].isalpha():
            newarray = []

            for j in range(len(tempArray)-1):
                newarray.append(tempArray[j+1])
            table.insert(testWord, newarray,answer)

def main(list):
    table_hash = HashTable(len(list))
    print('Choose one of the following hash functions to run optimization')
    print('1. Multiplication of every ascii value of the characters inside word divided by the length of the word, remainder of the hash table size')
    print('2. Sum of every ascii value of the characters inside word, remainder of the hash table length')
    print('3. Sum of every ascii value of the characters inside word times 26, remainder of hash table length')
    answer = input(str('Please type in the number: '))
    answer_pop = False
    while answer_pop != True:
        if answer == 1 or answer == 2 or answer == 3:
            answer_pop = True

        else:
            print('Invalid answer Try Again')
            answer = input(str('Please type in the number: '))
    create_hash_table(list, table_hash, answer)
    print('Average Number of Comparisons Per Search using option '+str(answer)+':')
    average_number_of_comparisons(list, table_hash, answer)
    print('Load Factor of the Hash Table')
    get_load_factor(table_hash)

