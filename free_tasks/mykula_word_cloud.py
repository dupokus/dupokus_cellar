class Solution:
    text = """  //wont won't won't"""
    def top_3_words(text):
        result = {}
        res = []
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        refined_text = ''
        for char in text:
            if char not in punctuations:
                refined_text += char
        sorted_text = refined_text.lower().split()
        for word in sorted_text:
            for letter in word:
                if letter in punctuations:
                    letter.replace(punctuations,"")
            if word not in result.keys():
                result[word]=0
            else:
                result[word]+=1
                
        for i in range(3):
            if result != {}:
                e = max(result, key=result.get)
                res.append(e)
                result.pop(e)
        return res
    print(top_3_words(text))
    