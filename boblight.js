exports.action = function(data, callback, config, SARAH){
config = config.modules.boblight;
if (!config.url){
		console.log("La variable url n'est pas configurée");
		return callback({'tts' : "La variable adresse n'est pas configurée"})};
switch(data.boblight){
			case "police":
				execprocess('kill');
				pause(200);
				execprocess(data.boblight);
				phrase='Haut-les-mains. Vous êtes cernés';
			break;
			case "rgb":
				execprocess('kill');
				pause(200);
				execprocess(data.boblight);
				phrase='Test en cours';
			break;
			case "rainbow":
				execprocess('kill');
				pause(200);
				execprocess(data.boblight);
				phrase='C\'est zooli';
			break;
			case "marseillaise":
				execprocess('kill');
				pause(200);
				execprocess(data.boblight);
				phrase='Allons zanfants de la patrie';
			break;
			case "strobe":
				execprocess('kill');
				pause(200);
				execprocess(data.boblight);
				phrase='Attention les yeux';
			break;
			case "k2000":
				execprocess('kill');
				pause(200);
				execprocess(data.boblight);
				phrase='Voilà';
			break;
			case "feu":
				execprocess('kill');
				pause(200);
				execprocess(data.boblight);
				phrase='Voilà';
			break;
			case "snake":
				execprocess('kill');
				pause(200);
				execprocess(data.boblight);
				phrase='Le serpent se mord la queue';
			break;
			case "orage":
				execprocess('kill');
				pause(200);
				execprocess(data.boblight);
				phrase='Il fait nuit';
			break;
			case "kill":
				execprocess('kill');
				phrase='J\'éteins boblight';
			break;
				}
	callback({ 'tts': phrase});
function execprocess(command){
	var exec = require('child_process').exec;
	if (command=='kill'){
		var process=__dirname+'\\lib\\killboblighteffect.bat';
		}
	else {
		var process = __dirname+'\\lib\\boblight.pyw '+command+' '+config.url+' '+ config.port;
		}
	console.log(process);
	var child = exec(process,
	function (error, stdout, stderr) {
	})};
function pause(millis){
	var date = new Date();
	var curDate = null;
	do { curDate = new Date(); }
	while(curDate-date < millis);
	};
};