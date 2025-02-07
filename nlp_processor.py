import time

NLP_RESPONSES = {
    "halo": "halo! Ada yang bisa saya bantu ?",
    "hai": "halo! Ada yang bisa saya bantu ?",
    "selamat pagi": "selamat pagi! Ada yang bisa saya bantu ?",
    "selamat siang": "selamat siang! Ada yang bisa saya bantu ?",
    "selamat sore": "selamat sore! Ada yang bisa saya bantu ?",
    "selamat malam": "selamat malam! Ada yang bisa saya bantu ?",
    "terima kasih": "Sama-sama! Senang bisa membantu anda 😊",
    "waktu sekarang": "Saat ini adalah waktu lokal Anda.",
    "siapa": "Saya adalah Avatar AI dari PT Trikod, saya siap membantu anda kapan pun dimanapun",
    "siapa kamu": "Saya adalah Avatar AI dari PT Trikod, saya siap membantu anda kapan pun dimanapun",
    "nama kamu": "Saya adalah Avatar AI dari PT Trikod, saya siap membantu anda kapan pun dimanapun",
    "cuaca": "Maaf, saya tidak bisa melihat cuaca saat ini, tetapi Anda bisa mengeceknya di Google 🌤️."
}

def process_nlp(user_input):
    """Cek apakah ada kata kunci dalam input pengguna."""
    for keyword, response in NLP_RESPONSES.items():
        if keyword.lower() in user_input.lower():
            return response
    return None  

def execute_nlp(user_input):
    """Eksekusi NLP dan beri delay sebelum lanjut ke AI."""
    nlp_response = process_nlp(user_input)
    if nlp_response:
        print(f"NLP Response: {nlp_response}")  
        time.sleep(2)  
    return nlp_response
