import openai
from openai.embeddings_utils import cosine_similarity

openai.api_key = "<your-apikey-here>"

def get_embedding(txt):
    """
    Fetches OpenAI embedding for **txt**.
    """
    response = openai.Embedding.create(input=txt, model="text-embedding-ada-002")
    return response['data'][0]['embedding']

def similarity(request, data):
    '''
    Gets OpenAI embeddings for both the request object and the event data object, and returns how similar they are via cosine similarity.
    '''
    request_embedding = get_embedding(request)
    event_embedding = get_embedding(data)
    return cosine_similarity(request_embedding, event_embedding)

def find_top_10_events(request, list):
    '''
    Scores each event in **list** according to adherence to specifications in **request**.

    Args:
        - request (pd.DataFrame)    :   request text object from input JSON
        - list (pd.DataFrame)       :   df with rows corresponding to events and columns ['data', 'url']

    Returns:
        - scored (list)             :   list in order of ascending rank of top 10 events
    '''

    scored = []

    for row in list.itertuples():
        e = row.data
        url = row.url
        score = similarity(request, e)
        scored.append({
            "Event Name": e.split('\n')[1],
            "Event URL": url,
            "Description": e,
            "Score": score
        })
    
    top_10 = sorted(scored, key=lambda x: x["Score"], reverse=True)[:10]
    return top_10