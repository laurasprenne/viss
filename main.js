const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'a6108fdc97msh60c32ab6027c096p1c6364jsn95a40d24770d',
		'X-RapidAPI-Host': 'free-nba.p.rapidapi.com'
	}
};

// divi globali masivi, kur katra tiks ieladeti dati
let teams = []
let players = []


// load data funkcija saņem api izsaukuma atgrieztos datus
function load_data(response_data){
	// ieliekam datus teams masīvā
	teams = response_data

	// atlasām dropdown elementu no HTML
	let dropdown = document.getElementById("players")

	// katrai komandai no datu masīva
	response_data.forEach(team => {
		// izveidojam HTML option elementu un ierakstām tajā komandas nosaukumu
		let option_element = document.createElement("option")
		option_element.innerHTML = team.full_name
		option_element.value = team.id
		
		// pievienojam option elementu dropdown sarakstam
		dropdown.append(option_element)
	});
}


// load data funkcija saņem api izsaukuma atgrieztos datus un konkrētās komandas id
function load_players(response_data, id){
	console.log(response_data)
	// visi speletaji tiek  ielikti players masiivaa
	players = response_data

	// tiek atlasīts un iztukšots ul elements, lai pie katras nākošās spēlētāju
	// ielādes tie tiek likti tukšā sarakstā 
	let list = document.getElementById("list")
	list.innerHTML = ""

	// ejam pāri katram playeram iekš masīva
	response_data.forEach(player => {
		// turpinām tikai ar tiem, kam atbilstošs id
		if(id == player.team.id){
			// izveidojam li elementu un ieliekam sarakstā
			list_item = document.createElement("li")
			list_item.innerHTML = player.first_name + " " + player.last_name
			list.append(list_item)
		}
	});
}

// ārpus funkciju konteksta veicam teams fetch, lai pie
// web lapas palaišanas uzreiz viss ielādējas dropdown sarakstā
fetch('https://free-nba.p.rapidapi.com/teams?page=0&per_page=100', options)
	.then(response => response.json())
	.then(response => load_data(response.data))
	.catch(err => console.error(err));
	

// select player palaizas pie button onclick notikuma
function select_player(){
	// iegustam indexu izvēlētajai komandai
	select = document.getElementById("players")
	i = select.selectedIndex

	// veicam players fetch un load_players funkcijai padodam arī izvēlētās komandas id
	fetch('https://free-nba.p.rapidapi.com/players?page=0&per_page=100', options)
		.then(response => response.json())
		.then(response => load_players(response.data, teams[i].id))
		.catch(err => console.error(err));
}
