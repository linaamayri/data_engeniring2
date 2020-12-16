import unittest
import os
import requests
import json
import time

 

 

class FlaskTests(unittest.TestCase):

 

    #def setUp(self):
        #self.sen_check = ((u'bombed', True),(u'people', True),(u'team', True),(u'staff', True),(u'support', True),(u'jenkinssssssssss', False),(u'dockerrrrr', False),(u'sadness', False),(u'difficulties', True))
        
    def test_a_index(self):
        responce = requests.get('http://localhost:5000')
        self.assertEqual(responce.status_code, 200)

 

    def test_time(self):
        dt = json.dumps({
            'text': 'bombed'
        })
        hd = {'Content-Type': 'application/json'}

 

        begin = time.time()
        i = 0

 

        while((i < 1000) & (begin - time.time() < 60)):
            requests.post('http://localhost:5000/', dt, headers=hd)
            i += 1
        finish = time.time()

 

        total_time = finish - begin

 

        self.assertLess(total_time, 60)

 

    #def test_phrase(self):

 

        #for check in self.sen_check:
            #self.assertEqual(tweet.isWordInSentence(check[0],tweet.phrase(check[0])), check[1])
            
            
if __name__ == '__main__':
    unittest.main()
