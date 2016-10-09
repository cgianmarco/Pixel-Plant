var multiparty = require('multiparty');
var http = require('http');
var util = require('util');
var fs = require('fs');
var watson = require('watson-developer-cloud');
var st = require('st');

var visual_recognition = watson.visual_recognition({
    api_key: '946c5bc6913a2abad3d285c1312e6281b2ff94f2',
    version: 'v3',
    version_date: '2016-05-20'
});

http.createServer(function(req, responseAjax) {
    if (req.url === '/classify' && req.method === 'POST') {
        // parse a file upload
        var form = new multiparty.Form();

        form.parse(req, function(err, fields, files) {
            var fileName = 'shot.png';
            
            var imageFile = fields['images_file'][0];
            var buf = Buffer.from(imageFile.substr(22), 'base64');
            fs.writeFileSync(fileName, buf);

            var params = {
                images_file: fs.createReadStream(fileName),
                classifier_ids: 'leave_vs_tomato',
                threshold: 0
            };
            visual_recognition.classify(params, function(err, res) {
                console.log("res");
                responseAjax.setHeader('Access-Control-Allow-Origin', '*');
                responseAjax.writeHead(200, {'content-type': 'application/json'});
                responseAjax.write(JSON.stringify(res, null, 2));
                responseAjax.end();
                fs.unlink(fileName);

                if (err)
                    console.log(err);
                else
                    console.log(JSON.stringify(res, null, 2));
            });
        });

    }

}).listen(8085);


http.createServer(
    st({ path: __dirname+"/../web", index: 'index.html', cache: false })
).listen(80);

console.log("running on http://127.0.0.1/");
