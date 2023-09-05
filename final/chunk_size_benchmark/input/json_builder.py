import json

def to_json(transcript, summary):

    json_dict = {
        'transcript': transcript,
        'summary': summary
    }

    # Important for non ascii characters!!!
    return json.dumps(json_dict, ensure_ascii=False)