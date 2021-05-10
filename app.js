const express = require('express')
const multer = require('multer')
const fs = require('fs')
const hash = require('object-hash')
const jdenticon = require('jdenticon')
const spawn = require('child_process').spawn
const app = express()
const port = 3000
var storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, 'file/') // cb 콜백함수를 통해 전송된 파일 저장 디렉토리 설정
    },
    filename: function (req, file, cb) {
        cb(null, file.originalname) // cb 콜백함수를 통해 전송된 파일 이름 설정
    }
})
var upload = multer({ storage: storage })

app.use(express.static('public'))
app.use(express.json())
app.use(express.urlencoded({
    extended: true
}));

app.get('/', (req, res) => {
    const content = `
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>Document</title>
        <style>
        </style>
    </head>
    <body>
        <form method="post" enctype="multipart/form-data" action="/upload">
            <label for="soundFile">Let me hear your voice</label>
            <br>
            <input type="file" name="wavFile" id="soundFile" accept=".wav" capture="microphone">
            <br>
            <div>
                <button>Submit</button>
            </div>
        </form>
    </body>
    </html>
    `
    res.send(content)
})

app.post('/upload', upload.single('wavFile'), (req, res) => {
    let result = spawn('python', ['voiceAnalyser.py', req.file.originalname, 'file'])
    result.stdout.on('data', (voiceData) => {
        voiceData = JSON.parse(voiceData.toString())
        let output = {};
        let hueValue = Math.max(Math.min(Math.round(voiceData.f0_median) + 100, 359), 0);
        console.log(req.file.originalname, voiceData.f0_mean, voiceData.f0_median, hueValue, `${hueValue}`)
        jdenticon.configure({
            hues: [hueValue]
        })
        let icon = jdenticon.toSvg(hash(voiceData), 200)
        output['data'] = voiceData
        output['identicon'] = icon.toString()
        fs.writeFileSync("file/" + req.file.originalname + ".svg", icon)
        // res.json(output)
        res.send(icon + '<br>' +
            req.file.originalname + '<br>' +
            JSON.stringify(voiceData))
    })
})

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})
