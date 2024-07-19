import sparknlp
from sparknlp.pretrained import PretrainedPipeline
import  os
spark = sparknlp.start()

root = os.path.dirname(os.path.realpath('cormac.py'))

# find all txt in /books/
os.chdir(root + '/books/')
all_txt = os.listdir()
print(all_txt)

# read the first book
# first =