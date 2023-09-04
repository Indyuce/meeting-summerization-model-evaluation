import json

def to_json(transcript, summary):

    json_dict = {
        'transcript': transcript,
        'summary': summary
    }

    return json.dumps(json_dict)