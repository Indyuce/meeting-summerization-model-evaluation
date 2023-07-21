from huggingface_hub import login

def perform_login():

    atoken_file = open('../../archive/huggingface_atoken.txt', 'r', encoding='utf-8')
    atoken = atoken_file.read()
    atoken_file.close()

    print('Logging in to HuggingFace')
    login(atoken, add_to_git_credential=False)


