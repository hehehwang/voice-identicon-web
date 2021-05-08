# originate from https://github.com/Shahabks/my-voice-analysis
from parselmouth.praat import run_file


def setRoute(m, p):
    # sound = p+"/"+m+".wav"
    # sourceRun = p+"/myspsolution.praat"
    # path = p+"/"
    sound = m + ".wav"
    sourceRun = p + "\myspsolution.praat"
    path = ""
    return sound, sourceRun, path


def genderAnalysis(f0_mean, f0_std):
    z3 = f0_std
    z4 = f0_mean

    result = {}
    if z4 > 97 and z4 <= 114:
        result['Success'] = True
        result['gender'] = 'Male'
        result['mood of speech'] = 'Showing no emotion, normal'
    elif z4 > 114 and z4 <= 135:
        result['Success'] = True
        result['gender'] = 'Male'
        result['mood of speech'] = 'Reading'
    elif z4 > 135 and z4 <= 163:
        result['Success'] = True
        result['gender'] = 'Male'
        result['mood of speech'] = 'speaking passionately'
    elif z4 > 163 and z4 <= 197:
        result['Success'] = True
        result['gender'] = 'Female'
        result['mood of speech'] = 'Showing no emotion, normal'
    elif z4 > 197 and z4 <= 226:
        result['Success'] = True
        result['gender'] = 'Female'
        result['mood of speech'] = 'Reading'
    elif z4 > 226 and z4 <= 245:
        result['Success'] = True
        result['gender'] = 'Female'
        result['mood of speech'] = 'speaking passionately'
    else:
        result['Success'] = False

    return result


def analyse(wave_file_name, directory):
    sound, sourceRun, path = setRoute(wave_file_name, directory)
    try:
        praatResult = run_file(sourceRun, -20, 2, 0.3, "yes", sound, path, 80, 400, 0.01, capture_output=True)
    except Exception as err:
        print("Try again the sound of the audio was not clear")
        print(err)
        return
    dataLabel = ['number_of_syllables',  # 0
                 'number_of_pauses',  # 1
                 'rate_of_speech',  # 2
                 'articulation_rate',  # 3
                 'speaking_duration',  # 4
                 'original_duration',  # 5
                 'balance',  # 6
                 'f0_mean',  # 7
                 'f0_std',  # 8
                 'f0_median',
                 'f0_min',
                 'f0_max',
                 'f0_quantile 25',
                 'f0_quantile 75',
                 'prob_pron']
    data = {}
    # print(praatResult[0])
    for i, obj in enumerate(praatResult[1].split()):
        data[dataLabel[i]] = obj
    if data['f0_mean'] != 'No':
        data['gender_analysis'] = genderAnalysis(float(data['f0_mean']), float(data['f0_std']))
    return data

if __name__ == '__main__':
    from sys import argv
    import json
    if len(argv)<3 : raise NotImplementedError
    waveFileName, directory = argv[1:]
    result = analyse(waveFileName.split('.')[0], directory)
    print(json.dumps(result))