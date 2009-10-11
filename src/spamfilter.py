from reverend.thomas import Bayes
guesser = Bayes()

f = open("spam.log",'r')
for line in f:
  guesser.train('spam', line.strip())

f = open("notspam.log",'r')
for line in f:
  guesser.train('notspam', line.strip())

guesser.save('my_guesser.bay')