const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'f51be84b20msh28b0658f5161e7ep17c531jsnfc4024f1a1ca',
		'X-RapidAPI-Host': 'free-nba.p.rapidapi.com'
	}
};

let teams = []
let players = []

function load_teams(response_data){
	teams = response_data
	let dropdown = document.getElementById("players")
	console.log(response_data)
	response_data.forEach(team => {
		let option_element = document.createElement("option")
		option_element.innerHTML = team.full_name
		option_element.value = team.id 
		dropdown.append(option_element)
	});
}


function load_players(response_players, id){
	players = response_players
	let list = document.getElementById("list")
	list.innerHTML = ""
	console.log(response_players)
	response_players.forEach(player => {
		if(id == player.team.id){
			list_item = document.createElement("li")
			list_item.innerHTML = player.first_name + " " + player.last_name
			list.append(list_item)
		}
	});
}

fetch('https://free-nba.p.rapidapi.com/teams?page=0&per_page=100', options)
	.then(response => response.json())
	.then(response => load_teams(response.data))
	.catch(err => console.error(err));


function select_player(){
	select = document.getElementById("players")
	i = select.selectedIndex

	name_element = document.getElementById("name")
	name_element = document.getElementById("team")
	name_element.innerHTML = teams[i].id
	fetch('https://free-nba.p.rapidapi.com/players?page=0&per_page=100', options)
	.then(response => response.json())
	.then(response => load_players(response.data, teams[i].id))
	.catch(err => console.error(err));
}