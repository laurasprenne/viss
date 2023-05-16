const options = {
	method: 'GET',
	headers: {
		Accept: 'application/hal+json',
		'X-RapidAPI-Key': 'f51be84b20msh28b0658f5161e7ep17c531jsnfc4024f1a1ca',
		'X-RapidAPI-Host': 'matchilling-tronald-dump-v1.p.rapidapi.com'
	}
};

function display_quote(){
    fetch('https://matchilling-tronald-dump-v1.p.rapidapi.com/random/quote', options)
	.then(response => response.json())
	.then(response => {
    })
	.catch(err => console.error(err));
}