from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .processing import process_audio
from spleeter.separator import Separator
from music21 import *
import os
from django.conf import settings
import json

def setup_ffmpeg():
    os.environ["PATH"] += os.pathsep + 'C:\\Users\\m-zso\\OneDrive\\Documents\\ffmpeg\\ffmpeg-2023-03-27-git-f7abe92bd7-full_build\\bin'

def index(request):
    return render(request, 'index.html')
# Create your views here.

def feldolgozas(request):
    if request.method == 'POST':
        zene_fajl = request.FILES['zene_fajl']
        # Feldolgozási logika (hangszerekre bontás, kotta generálás)

    return JsonResponse({'status': 'success'})



@csrf_exempt
def process_audio_view(request):
    setup_ffmpeg()
    if request.method == "POST":
        audio_file = request.FILES.get("audio-file")
        if not audio_file:
            return JsonResponse({"error": "Nincs fájl feltöltve."}, status=400)

         # Ide írd a zenefájl feldolgozásának kódját.
        # Hangszerenkénti szétválasztás a Spleeter segítségével
        separator = Separator('spleeter:2stems')
        audio_file_path = os.path.join(settings.MEDIA_ROOT, audio_file.name)
        
        os.makedirs(os.path.dirname(audio_file_path), exist_ok=True)
        
        with open(audio_file_path, 'wb+') as f:
            for chunk in audio_file.chunks():
                f.write(chunk)
        output_path = os.path.join(settings.MEDIA_ROOT, 'output')
        separator.separate_to_file(audio_file_path, output_path)

        # Kotta generálása a Music21 segítségével
        # Egyelőre csak egy példa kotta
        c_major_scale = scale.MajorScale('C4')
        stream1 = stream.Stream()
        for pitch in c_major_scale.getPitches('C4', 'C5'):
            n = note.Note(pitch)
            n.duration.type = 'quarter'
            n.quarterLength = 1
            stream1.append(n)
        musicxml_str = stream1.write('musicxml')

        # Visszaadja a fájl nevét és a generált kotta XML-t
        
        with open(musicxml_str, 'r', encoding='utf-8') as file:
             musicxml_content = file.read()
        
        response_data = {
            'file_name': str(audio_file.name),
            'sheet_music': musicxml_content,
        }

        return JsonResponse(response_data)
    else:
        return JsonResponse({"error": "Hibás kérés."}, status=400)