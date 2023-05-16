let drink = []

// fetch('https://www.thecocktaildb.com/api/json/v1/1/random.php')
// 	.then(response => response.json())
// 	.then(response => {
// 		console.log(response)
// 	})
// 	.catch(err => console.error(err));

function get_drink(){
    fetch('https://www.thecocktaildb.com/api/json/v1/1/random.php')
	.then(response => response.json())
	.then(response => {
		console.log(response)

        document.getElementById('drink').innerHTML = response.drinks[0].strDrink
        document.getElementById('image').src = response.drinks[0].strDrinkThumb
        document.getElementById('instructions').innerHTML = response.drinks[0].strInstructions
	})
	.catch(err => console.error(err));
}