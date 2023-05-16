var input = document.getElementById("character");
let value = "";
let known = [];

input.addEventListener("keyup", function(event) {
    
    if (event.code === "Enter") {
        console.log('works');
        event.preventDefault();
        document.getElementById("btn").click();
  }
});

function setValue(){
    value = document.getElementById("input").value;
    document.getElementById("congrats").style.display= "none"
    known = []
    const field = document.getElementById("field");
    field.innerHTML = "";
    console.log(value);
    known.push(value[0]);
    updateValue();
}

function updateValue(){
    const field = document.getElementById("field");
    field.innerHTML = "";
    for(let i = 0; i < value.length; i++){
        let match_count = 0;
        for(const c of known){
            if(c === value[i]){
                match_count++;
                field.innerHTML += c;
            }
        }
        if(match_count === 0){
            field.innerHTML += " _ ";
        }
    }
}

function addBukva(){
    let char = document.getElementById("character").value
    if(char.length === 1){
        console.log("ok");
        if(! known.includes(char)){
            known.push(char);
        }
        updateValue();
        document.getElementById("character").value = "";

        if(field.innerHTML.includes("_")){
            console.log("vel jamin")
        }

        if(! field.innerHTML.includes("_")){
            document.getElementById("congrats").style.display= "inline"
        }
    }
    else{
        console.log("not ok")
    }
}