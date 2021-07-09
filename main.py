from textgenrnn import textgenrnn
from flask import url_for, render_template, request, Flask,redirect
app = Flask(__name__)
'''
textgen = textgenrnn('textgenrnn_weights.hdf5')
#textgen.train_from_file('harrypotter.txt', num_epochs=1)
textgen.generate(n=1,return_as_list=True)
lol = textgen.generate(n=100,return_as_list=True)
l = ''
print(lol)
l.join(lol)
print(l)
fl = open('generated.txt','w')
fl.write(l)
fl.close()
'''
'''
l = ['Ron and leaning in the second and the trees of the tiny professor and things in the proo; his head as he thought it had was everythery as the trophy of his leanth at the standing', 'died’s how to the table was large the starter. He was a things at the stone.', '', 'Harry had a good boy when he was a least started', 'started the things as the hall was a stream to the table', 'she had never have been Good of the tripors — the', 'Who had a struggle of that took to turn the stone of the thing', '', 'he was a strightly time in the tripply at the cloak,', 'be and told him past a least the first time in the sweater.', '', '', '', 'Harry had his hard at three ... he said Hagrid', '', '', 'singeron’ anywhere and are the other. He was down to his hands. He t', '', '', 'Professor McGonagall’s hair the probably and', '', 'door had a smell have to be carried the end', '', 'I have been starting to go on the bay thing', 'back to see him me again, the train like the stone out of the things, the life and the train and have tower his parents after the truck to tiny of his hand and Goyle', 'for yeh come and then he was a strange and the teach', '', '', '', 'as the problem tripping second a bit of what he said.', 'past him back to him and past the trudge', 'now him and was the wall. Harry don’t have troll and', ' strange himself and the toward the powerful', 'Harry was starting to hinger and a large behind what had', 'everythery all the floor that was a his the', '', 'started him in the follow and thought it', '', 'leave the stopped and threw him right and thought he told him and thought it wasn’t it', 'Harry was still a bit of the ground and what', 'Page | 287 Harry Potter and the Philosophers Stone - J.K. Rowling', 'was a little thing and the teachers and she was Ron in', '', 'he suit in trained and tower the things was a', 'a life and that seemed to be a large in his hand him.', '', 'Harry was a good Harry thing and close the time in the son and trying to be never to remembery the', 'was a line and too come up the teachers the train. He told him as the', 'you know. He thought it was been on the life of', 'you go to the banister on the train and Professor McGonagall, and then his hairs. He had to find. He', '', '', '“What’s for feeling earst thing the stone. Harry started in it', 'be able to be a new and bite because the things had been', '', '— anyway in his and his head', '', '', '', '', '', '“I can’t start the toward anyway, the throwing at the', '', '', 'starbed to try to his second of a strange. He had', '', '', 'father and the tiny boy in the students of the term and the tall their', '', 'the giant those tried to his head and that was about', 'on the toward.', '“Hagrid leaning the one had you can’t stop him all', 'We sleep on the last thing in the streamery was been — at the trophy.', '', 'were they had a good for him.', 'for everythe the train of the strangery the hall', 'was large the trophy, and the three-invent', '', '', '', 'out his hand and then he pulled to the stone', 'because his arm of the top of the true slower and the tower the hall and', 'stared the same man who was jumping a little patch as they had to start Professor.', 'got it again, that was stilling in the stand, that had been starting', '', 'On the hand was leaved it and the toward. He started in Ron of', 'down to look at him what he pulled the teach', '', '', 'Page | 272 Harry Potter and the Philosophers Stone - J.K. Rowling', '', 'had large the startence and got lives anywhere and the took the least', 'started the life the threater that was a newty thing, and that was a', 'look at him of the teach and learn two people in the', '', '', '', 'him read off?”', '', 'more in minday and the grounds a time in the']
n=''
for item in l:
    n+=item+'\n'
open('generated.txt','w').write(n)

'''
@app.route('/',methods = ["POST","GET"])
def index():
    global textgen
    global fle
    global num
    textgen = textgenrnn()
    if request.method == 'POST':
        fle = str(request.form.get('text'))
        num = int(request.form.get('number'))
        ni = open('thing.txt','w')
        ni.write(fle)
        ni.close()
        return redirect(url_for('cool'))

    return render_template('index.html')
@app.route('/result')
def cool():
    global strong
    if fle != None:

        textgen.train_from_file('thing.txt',num_epochs=1)
        lol = textgen.generate(n=num, return_as_list=True)
        strong=''
        for item in lol:
            strong+=item
        return render_template('result.py.html',result=strong)




    return render_template('waiting.html')
app.run(threaded=True)
