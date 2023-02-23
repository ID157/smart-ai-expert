from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader, Document, QueryMode, QueryConfig, IndexStructType
from sys import argv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from time import sleep

def strip_short_line(raw):
  texts = raw.split("\n")
  result = []
  for text in texts:
    if len(text) > 200:
      result.append(text)
  return '\n'.join(result)

def chunk_paper(name):
  with open(f'{name}/data.txt') as f:
    txt = strip_short_line(f.read())
    print(txt)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    texts = text_splitter.split_text(txt)
    doc_chunks = []
    for i, text in enumerate(texts):
      doc = Document(text, doc_id=f"doc_id_{name}_{i}")
      doc_chunks.append(doc)
    return doc_chunks

# add index
if argv[1] == 'add':
  progress = 0
  documents_length = 0
  # try:
  index = GPTSimpleVectorIndex.load_from_disk('index.json')
  documents = chunk_paper(argv[2])
  documents_length = documents
  for doc in documents:
    progress += 1
    print(f"progress:{progress}/{len(documents)}")
    index.insert(doc)
    # rate limitもあるので...
    sleep(1)
    index.save_to_disk('index.json')
  # except:
  #   index.save_to_disk('index_tmp.json')
  #   print(f"Error! progress:{progress}/{documents_length}")


# init index
if argv[1] == 'init':
  documents = SimpleDirectoryReader(argv[2]).load_data()
  index = GPTSimpleVectorIndex(documents)
  print('index was created')
  index.save_to_disk('./index.json') 

# query
if argv[1] == 'query':
  index = GPTSimpleVectorIndex.load_from_disk('index.json')

  response = index.query(
    argv[2],
    mode=QueryMode.DEFAULT,
  )
  print(response)
  print(response.get_formatted_sources(100))

