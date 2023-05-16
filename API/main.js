const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'f51be84b20msh28b0658f5161e7ep17c531jsnfc4024f1a1ca',
		'X-RapidAPI-Host': 'love-calculator.p.rapidapi.com'
	}
};

function calculate(){
	male = document.getElementById("male").value
	female = document.getElementById("female").value

	fetch('https://love-calculator.p.rapidapi.com/getPercentage?sname='+ male +'&fname='+ female, options)
	.then(response => response.json())
	.then(response => {
		console.log(response)
		document.getElementById('result').inenerHTML = response['percentage'] + '%'
		document.getElementById('recom').inenerHTML = response['result']
	})
	.catch(err => console.error(err));
}