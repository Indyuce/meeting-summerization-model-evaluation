# Load tokenizer using the transformers library
TOKENIZER = None

# Maximum chunk size in tokens for chunks
# This value is close to optimal for LLaMA-2 in 0SL
MAX_CHUNK_SIZE = 3500

def token_len(text):
    return len(TOKENIZER(text, return_tensors="pt")['input_ids'][0])

def append_to_chunk(current_chunk, utterance):
    if len(current_chunk) > 0:
        current_chunk += '\n'
    current_chunk += utterance
    return current_chunk

def chunkize(text):
    """
    Greedy implementation of a dialogue transcript chunking algorithm. This method returns a list of transcript chunks.
    - It priorities stability over performance. There is a set maximum chunk size for LLM inference stability. Really long utterances bypass this limit.
    - It guarantees the cuts are made at utterance ends (\n).
    - It counts everything in MODEL TOKENS and not characters for more exact experiments.
    """
    
    chunks = [] # Final list of transcript chunks. This makes up the loop invariant
    utterances = text.split('\n') # Transcript is split into sentences
    utterances.reverse() # Reverse everything!!
    current_chunk = ''

    # While there is still an utterance to process
    while len(utterances) > 0:
        utterance = utterances.pop()

        # Add to current chunk and proceed to next
        new_current_chunk = append_to_chunk(current_chunk, utterance)
        if token_len(new_current_chunk) <= MAX_CHUNK_SIZE:
            current_chunk = new_current_chunk
        
        # Utterance is larger than maximum chunk size
        elif len(current_chunk) == 0:
            chunks.append(current_chunk)
            chunks.append(utterance)
            current_chunk = ''

        # Current chunk is big enough, append to list and create new one
        else:
            chunks.append(current_chunk)
            current_chunk = utterance

    if len(current_chunk) > 0:
        chunks.append(current_chunk)

    return chunks