const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'f51be84b20msh28b0658f5161e7ep17c531jsnfc4024f1a1ca',
		'X-RapidAPI-Host': 'instagram-profile1.p.rapidapi.com'
	}
};

function setImage(image_url){
    document.getElementById("image").src = image.url
}

function getUserData(){
    username = document.getElementById("name").value

    fetch('https://instagram-profile1.p.rapidapi.com/getprofile/' + username, options)
	.then(response => response.json())
	.then(response => {
        console.log(response)
        setImage(response["profile_pic_url_hd"])
    })
	.catch(err => console.error(err));
}