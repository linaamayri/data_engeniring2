import unittest

import tweet



class FlaskTests(unittest.TestCase):

    def setUp(self):
        self.sen_check = ((u'bombed', True),(u'people', True),(u'team', True),(u'staff', True),(u'support', True),(u'jenkinssssssssss', False),(u'dockerrrrr', False),(u'sadness', False),(u'difficulties', True))
        
    def test_a_index(self):
        responce = requests.get('http://localhost:5000')
        self.assertEqual(responce.status_code, 200)

    
    def test_phrase(self):

        for check in self.sen_check:
            self.assertEqual(tweet.isWordInSentence(check[0],tweet.phrase(check[0])), check[1])
            
            
if __name__ == 'main':
    unittest.main()