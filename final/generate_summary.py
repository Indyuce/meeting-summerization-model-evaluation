from chunking_algorithm import chunkize

# Load tokenizer using the transformers library
TOKENIZER = None
MODEL = None

# Generation config used in our benchmarks
DO_SAMPLE = True
MAX_NEW_TOKENS = 1024
TEMPERATURE = .3
TOP_K = 100

# Prompt template for LLaMA-2 Chat available on HuggingFace
# Prompt template is different for every LLM
PROMPT_TEMPLATE = """<s>[INST] <<SYS>>
You are an artificial intelligence assistant. You must give helpful, detailed, and polite answers to the instructed provided.
<</SYS>>

Summarize the following text. Provide only one paragraph. Avoid vague or uninformative phrasing. Do not provide a list of keypoints.

{text}[/INST]"""

def result_from_output_sequence(output, n_shot = 0):
    """
    This transformers the output sequence (input sequence + generated summary) into a string that contains only the generated summary.
    This method extracts the generated summary from the string returned by the LLM.
    This method is highly-model dependent, this implementation is for LLaMA-2-Chat-HF
    """
    
    # Un-prompt output
    delimiter = '[/INST]'
    output = delimiter.join(output.split(delimiter)[1 + n_shot:])
    
    # Remove white spaces in front of summary
    while len(output) > 0 and output[0] == ' ':
        output = output[1:]
    
    # Remove <|endoftext|> token
    eos_token = '</s>'
    output = output[:-len(eos_token)]
    
    return output

def generate_output(prompt):
    input_ids = TOKENIZER(prompt, return_tensors="pt").to('cuda')
    output_ids = MODEL.generate(**input_ids, do_sample=DO_SAMPLE, max_new_tokens=MAX_NEW_TOKENS, temperature=TEMPERATURE, top_k=TOP_K)
    return TOKENIZER.decode(output_ids[0]).strip()

def inference_sample(sample):
    
    # Current summary is the concatenation of all the chunk sub-summaries 
    current_summary = ''
    chunks = chunkize(sample)

    # Split into chunks
    for chunk in chunks:

        prompt = PROMPT_TEMPLATE.format(text=chunk)
            
        # Sample one sub-input
        output = generate_output(prompt)
        subsummary = result_from_output_sequence(output)

        # Add to summary
        if len(current_summary) > 0:
            current_summary += '\n\n'
        current_summary += subsummary
    
    return current_summary