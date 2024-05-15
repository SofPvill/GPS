const express = require('express');
const multer = require('multer');
const upload = multer({ dest: 'uploads/' });
const { PythonShell } = require('python-shell');
const app = express();
app.use(express.json());

app.post('/predict', upload.single('csv'), (req, res) => {
    let options = {
        mode: 'text',
        pythonOptions: ['-u'],
        scriptPath: './',
        args: [req.file.path]
    };

    PythonShell.run('prediction-script.py', options, function(err, result) {
        if (err) res.send(err);
        res.send(result);
    });
});

app.listen(3000, () => console.log('Servidor corriendo en el puerto 3000'));
