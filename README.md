# voice-analysis

* [praat](https://www.fon.hum.uva.nl/praat/)
* [my-voice-analysis](https://github.com/Shahabks/my-voice-analysis)
* [jdenticon](https://jdenticon.com/)

목소리의 특성을 반영한 [아이덴티콘](https://zetawiki.com/wiki/%EC%95%84%EC%9D%B4%EB%8D%B4%ED%8B%B0%EC%BD%98)을 생성해준다.
(목소리가 저음일수록 차가운 색으로 생성)

# 사용법

1. `pip install praat-parselmouth`
2. `node app.js`
3. 목소리.wav를 업로드
4. 짜잔

# 예시

## hello World! ①

설명: 파파고 TTS, 여성, 3번 반복

파일명: helloWorldx3.wav

결과물:

![image](https://raw.githubusercontent.com/hehehwang/voice-identicon-web/master/file/helloWorldx3.wav.svg)
`{"number_of_syllables":"11","number_of_pauses":"2","rate_of_speech":"3","articulation_rate":"4","speaking_duration":"2.9","original_duration":"3.8","balance":"0.8","f0_mean":"239.72","f0_std":"68.75","f0_median":"245.7","f0_min":"88","f0_max":"336","f0_quantile 25":"208","f0_quantile 75":"301","prob_pron":"0.8","gender_analysis":{"Success":true,"gender":"Female","mood of speech":"speaking passionately"}}`


## hello World! ②

설명: 파파고 TTS, 남성, 5번 반복

파일명: helloWorldx5.wav

결과물:

![image](https://raw.githubusercontent.com/hehehwang/voice-identicon-web/master/file/helloWorldx5.wav.svg)
`{"number_of_syllables":"19","number_of_pauses":"4","rate_of_speech":"3","articulation_rate":"4","speaking_duration":"4.7","original_duration":"6.6","balance":"0.7","f0_mean":"133.11","f0_std":"22.03","f0_median":"134.6","f0_min":"82","f0_max":"168","f0_quantile 25":"118","f0_quantile 75":"153","prob_pron":"0.8","gender_analysis":{"Success":true,"gender":"Male","mood of speech":"Reading"}}`

# further discussion
* 
